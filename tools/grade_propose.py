"""Propose a fixed head word for every non-standard grade_th; write docs/grades_review.md.

Heads: ศ่อฮีห์ · หะซัน · ฎออีฟ · ฎออีฟมาก · เมาฎูอ์ · เมากูฟ · มุรสัล · มีข้อขัดแย้ง
Proposal = head + " (" + current text + ")". The text in brackets is shortened later, bab by bab.
Confidence: A = the author's own words or an explicit grade word; B = inferred from the isnad
description; C = unclear, needs a decision.
Run with --apply to write the proposals (only A and B rows, and C rows listed in an override file).
"""
import glob, json, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import jsonio

root = pathlib.Path(__file__).resolve().parent.parent
HEADS = "ศ่อฮีห์|หะซัน|ฎออีฟมาก|ฎออีฟ|เมาฎูอ์|เมากูฟ|มุรสัล|มีข้อขัดแย้ง"
STD = re.compile(rf"^({HEADS})(?=$|\s*\()")

RULES = [  # (regex, head, confidence) — first match wins
    (r"^(?:ฎออีฟญิดดัน|อ่อนมาก|ฎออีฟมาก)", "ฎออีฟมาก", "A"),
    (r"^(?:มุงกัร|มุนกัร)(?=\s|$|\()", "ฎออีฟมาก", "A"),
    (r"^(?:เมาฎูอ์|โมฆะ)", "เมาฎูอ์", "A"),
    (r"^ฎออีฟ(?=\s|$|\(|—|;|,)", "ฎออีฟ", "A"),
    (r"^ศ่อฮีห์(?=\s|$|\(|—|;|,)", "ศ่อฮีห์", "A"),
    (r"^หะซัน(?=\s|$|\(|—|;|,)", "หะซัน", "A"),
    (r"ผู้แต่ง[^()]{0,20}(?:ฎออีฟมาก|อ่อนมาก)", "ฎออีฟมาก", "A"),
    (r"ผู้แต่ง[^()]{0,40}(?:เมาฎูอ์)", "เมาฎูอ์", "A"),
    (r"ผู้แต่ง[^()]{0,40}(?:อ่อน|ฎออีฟ|ไม่ได้รับการยอมรับ|ใช้เป็นหลักฐานไม่ได้|ไม่พ้นความอ่อน)", "ฎออีฟ", "A"),
    (r"ผู้แต่ง[^()]{0,30}หะซัน", "หะซัน", "A"),
    (r"ผู้แต่ง[^()]{0,30}ศ่อฮีห์", "ศ่อฮีห์", "A"),
    (r"ผู้แต่ง[^()]{0,40}มุรสัล", "มุรสัล", "A"),
    (r"ผู้แต่ง[^()]{0,40}เมากูฟ", "เมากูฟ", "A"),
    (r"^(?:อ่อนมาก|ฎออีฟญิดดัน|ฎออีฟมาก)", "ฎออีฟมาก", "A"),
    (r"^เมาฎูอ์|^โมฆะ", "เมาฎูอ์", "A"),
    (r"^(?:ฎออีฟ|ฎออีฟแบบ|ฎออีฟใน)", "ฎออีฟ", "A"),
    (r"^ศ่อฮีห์", "ศ่อฮีห์", "A"),
    (r"^หะซัน", "หะซัน", "A"),
    (r"^(?:เมากูฟ|ศ่อฮีห์เมากูฟ)", "เมากูฟ", "A"),
    (r"^มุรสัล", "มุรสัล", "A"),
    (r"(?:ที่ถูก(?:ต้อง)?(?:กว่า)?|ที่มีน้ำหนัก|ที่จำได้)(?:คือ|เป็น)?(?:แบบ)?เมากูฟ|เมากูฟถูกต้อง|เมากูฟที่", "เมากูฟ", "A"),
    (r"(?:ที่ถูก(?:ต้อง)?(?:กว่า)?|ที่จำได้|ที่มีน้ำหนัก)(?:คือ|เป็น)?(?:แบบ)?มุรสัล|มุรสัลถูกต้องกว่า", "มุรสัล", "A"),
    (r"มีความขัดแย้ง|มีข้อขัดแย้ง|^ขัดแย้ง|มีความเห็นต่าง|ขัดแย้งว่า", "มีข้อขัดแย้ง", "B"),
    (r"อ่อนมาก|มุงกัร|มุนกัร|มัตรูก|ถูกทิ้ง|ถูกกล่าวหาว่าโกหก", "ฎออีฟมาก", "B"),
    (r"^(?:อยู่ใน(?:อัล)?บุคอรีย์|ในมุสลิม|มุสลิมรายงาน|ต้น(?:เรื่อง|หะดีษ)ศ่อฮีห์|ตอนต้นศ่อฮีห์|ตัวหะดีษ.*ถูกต้อง)", "ศ่อฮีห์", "B"),
    (r"^สาย(?:รายงาน)?(?:ภายนอก)?(?:ศ่อฮีห์|แข็ง)|^สายตามเงื่อนไข|^สายหะซัน|^สาย(?:รายงาน)?ไม่เป็นไร|^สายรายงานพอใช้ได้", "ศ่อฮีห์|หะซัน", "C"),
    (r"มะอ์ลูล|มีข้อบกพร่อง|ชาซ|มุนเกาะฏิอ์|มักฏูอ์|ขาดตอน|สาย(?:สืบ)?ตก|สาย(?:รายงาน)?(?:นี้)?(?:อ่อน|ฎออีฟ|มีความอ่อน)|ไม่มั่นคง|เฆาะรีบ|แบบมัรฟูอ์ผิด", "ฎออีฟ", "B"),
]

rows = []
for f in sorted(glob.glob(str(root / "vol*/entries/*.json")), key=lambda p: (int(re.search(r"vol(\d+)", p).group(1)), p)):
    e = json.load(open(f, encoding="utf-8"))
    for h in e["hadith"]:
        g = h["grade_th"].strip()
        if STD.match(g):
            continue
        head, conf = "?", "C"
        for pat, hd, cf in RULES:
            if re.search(pat, g):
                head, conf = hd, cf
                break
        rows.append(dict(vol=e["volume"], file=str(pathlib.Path(f).relative_to(root)), no=h["no"],
                         topic=e["topic_th"], cur=g, head=head, conf=conf))

if "--apply" in sys.argv:
    over = {}
    p = root / "docs/grades_overrides.json"
    if p.exists():
        over = {int(k): v for k, v in json.load(open(p, encoding="utf-8")).items()}
    n = 0
    for r in rows:
        head = over.get(r["no"], r["head"] if r["conf"] in "AB" and "|" not in r["head"] else None)
        if not head:
            continue
        e, fmt = jsonio.load(root / r["file"])
        for h in e["hadith"]:
            if h["no"] == r["no"]:
                h["grade_th"] = f"{head} ({r['cur']})"
                n += 1
        jsonio.save(root / r["file"], e, fmt)
    print("applied", n)
    sys.exit()

c = {k: sum(1 for r in rows if r["conf"] == k) for k in "ABC"}
out = ["# ตารางระดับหะดีษ (รอตรวจ)", "",
       f"หะดีษที่ grade_th ยังไม่ขึ้นต้นด้วยคำหลัก: **{len(rows)}** จาก ~1,262 "
       f"(A = ชัดจากถ้อยคำเดิม {c['A']} · B = อนุมานจากคำบรรยายสาย {c['B']} · C = ต้องตัดสิน {c['C']})", "",
       "รูปแบบใหม่: `คำหลัก (ข้อความเดิม)` — ข้อความในวงเล็บจะย่อให้สั้นในรอบเกลาทีละบท",
       "ตรวจเฉพาะคอลัมน์ **คำหลักที่เสนอ** ถ้าไม่เห็นด้วย ให้บอกเลขหะดีษกับคำหลักที่ถูก (เช่น `h70 = มีข้อขัดแย้ง`)", ""]
for conf, title in (("C", "C — ต้องตัดสิน"), ("B", "B — อนุมาน (ตรวจผ่าน ๆ)"), ("A", "A — ชัดเจน (ดูเผื่อ)")):
    out += [f"## {title}", "", "| h | เล่ม | คำหลักที่เสนอ | ข้อความเดิม |", "|---|---|---|---|"]
    for r in rows:
        if r["conf"] == conf:
            cur = r["cur"].replace("|", "/")
            out.append(f"| {r['no']} | {r['vol']} | **{r['head']}** | {cur} |")
    out.append("")
(root / "docs/grades_review.md").write_text("\n".join(out), encoding="utf-8")
print(len(rows), c)
