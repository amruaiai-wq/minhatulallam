"""Apply the approved style guide (docs/style_guide.md) to every Thai text field.

Usage: python tools/style_fix.py <group> [--dry]
Groups: terms, bin, quotes, saw  (run in this order; each is its own commit)
Only Thai fields are touched: topic_th, translation_th, grade_th, key_rulings_th, vocab.th,
section heading_th/points_th, tags_th, and in toc.json: kitab/bab/topic "th" and intro_th.
"""
import sys, re, glob, collections, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import jsonio

root = pathlib.Path(__file__).resolve().parent.parent
GROUP = sys.argv[1]
DRY = "--dry" in sys.argv
stats = collections.Counter()

def sub(pat, rep, s, key):
    n = len(re.findall(pat, s))
    if n:
        stats[key] += n
        s = re.sub(pat, rep, s)
    return s

# ---------------------------------------------------------------- terms
BOOK = r"(?=ทั้งสอง|บุคอรีย์|อัลบุคอรีย์|มุสลิม|อิบนุ|อัล|ของ|\s*[»\"]|\")"
def terms(s, field):
    # 1 เราะซูล
    s = sub(r"รสูลุลลอฮ์|เราะสูลุลลอฮ์", "เราะซูลุลลอฮ์", s, "1 เราะซูลุลลอฮ์")
    s = sub(r"(?<!เ)(?<!เรา)(?<!ะ)รสูล(?!ุ)", "เราะซูล", s, "1 รสูล→เราะซูล")
    s = sub(r"เราะสูล(?!ุ)", "เราะซูล", s, "1 เราะสูล→เราะซูล")
    s = sub(r"ศาสนทูต", "เราะซูล", s, "16 ศาสนทูต")
    # 2 สุนนะฮ์
    s = sub(r"ซุนนะฮ์", "สุนนะฮ์", s, "2 ซุนนะฮ์")
    # 3 ศ่อฮีห์ = grade, เศาะฮีห์ = book title
    s = sub(r"ศ่อฮีห์(?=ทั้งสอง|บุคอรีย์|อัลบุคอรีย์|มุสลิม|อิบนุ(?:หิบบาน|คุซัยมะฮ์)|ของ(?:บุคอรีย์|มุสลิม|อัลบุคอรีย์))", "เศาะฮีห์", s, "3 ศ่อฮีห์(ชื่อหนังสือ)→เศาะฮีห์")
    if field == "grade_th":
        s = sub(r"เศาะฮีห์(?!ทั้งสอง|บุคอรีย์|อัลบุคอรีย์|มุสลิม|อิบนุ|ของ)", "ศ่อฮีห์", s, "3 เศาะฮีห์(ระดับ, grade_th)→ศ่อฮีห์")
    s = sub(r"(?:(?<=ว่า)|(?<=สาย)|(?<=เป็น)|(?<=ระดับ)|(?<=หะซัน)|(?<=หะสัน)|(?<=ว่า )|(?<=หะซัน ))เศาะฮีห์(?!ทั้งสอง|บุคอรีย์|อัลบุคอรีย์|มุสลิม|อิบนุ|ของ)", "ศ่อฮีห์", s, "3 เศาะฮีห์(ระดับ)→ศ่อฮีห์")
    # 4 หะซัน (grade); names keep หะสัน
    if field == "grade_th":
        s = sub(r"หะสัน", "หะซัน", s, "4 หะสัน→หะซัน (grade_th)")
    s = sub(r"(?:(?<=ว่า)|(?<=สาย)|(?<=เป็น)|(?<=ระดับ))หะสัน(?!\s*บิน|\s*อัล)", "หะซัน", s, "4 หะสัน→หะซัน (ระดับในเนื้อความ)")
    s = sub(r"หะสัน(?=ศ่อฮีห์|\s*ศ่อฮีห์|ด้วยหลักฐาน|ลิฆ็อยริฮี|ลิฆอยริฮี)", "หะซัน", s, "4 หะสันศ่อฮีห์→หะซันศ่อฮีห์")
    # 5 อุละมาอ์
    s = sub(r"นักวิชาการหะดีษ", "นักหะดีษ", s, "5 นักวิชาการหะดีษ→นักหะดีษ")
    s = sub(r"นักวิชาการ(?:ด้าน)?ภาษา", "นักภาษา", s, "5 นักวิชาการภาษา→นักภาษา")
    s = sub(r"นักวิชาการ", "อุละมาอ์", s, "5 นักวิชาการ→อุละมาอ์")
    # 6 ฟุเกาะฮาอ์
    s = sub(r"ฟุกอฮาอ์|ฟุก็อฮาอ์", "ฟุเกาะฮาอ์", s, "6 ฟุกอฮาอ์")
    s = sub(r"นักนิติศาสตร์(?:อิสลาม)?", "ฟุเกาะฮาอ์", s, "6 นักนิติศาสตร์")
    # 7 อิจญ์มาอ์ (not สมมติ, ห้ามติด, ลงมติ, สภา…มติ)
    s = sub(r"อิจญ์มาอ์\s*\(มติเอกฉันท์\)", "อิจญ์มาอ์", s, "7 อิจญ์มาอ์ (มติเอกฉันท์)")
    s = sub(r"มติเอกฉันท์|มติเห็นพ้อง", "อิจญ์มาอ์", s, "7 มติเอกฉันท์→อิจญ์มาอ์")
    s = sub(r"(?<!สม)(?<!ห้า)(?<!ลง)(?<!มุม)(?<!สภาฟิกฮ์มี)มติ(?!ด|ฐาน|อ์|ของสภา|ในการประชุม|ว่าอนุญาตให้ใช้ยา)", "อิจญ์มาอ์", s, "7 มติ→อิจญ์มาอ์")
    # 9 รายงาน
    s = sub(r"บันทึกโดย", "รายงานโดย", s, "9 บันทึกโดย→รายงานโดย")
    # 10 متفق عليه
    s = sub(r"หะดีษ(?:ที่เป็น)?มุตตะ(?:ฟัก|ฟะกุน)อะลัยฮ์", "หะดีษที่บุคอรีย์และมุสลิมรายงาน", s, "10 หะดีษมุตตะฟักอะลัยฮ์")
    s = sub(r"มุตตะ(?:ฟัก|ฟะกุน)อะลัยฮ์", "บุคอรีย์และมุสลิม", s, "10 มุตตะฟักอะลัยฮ์→บุคอรีย์และมุสลิม")
    # 11 บุคอรีย์
    s = sub(r"อัลบุคอรีย์", "บุคอรีย์", s, "11 อัลบุคอรีย์→บุคอรีย์")
    # 12 อัลหาฟิซ (keep 'อัลหาฟิซ อิบนุหะญัร' as is; not Ibn Hajar al-Haytami)
    s = sub(r"(?<!อัลหาฟิซ)(?<!อัลหาฟิซ )อิบนุหะญัร(?!\s*อัล(?:ฮัย|หัย)ตะมีย์)", "อัลหาฟิซ", s, "12 อิบนุหะญัร→อัลหาฟิซ")
    # 13 อิบนุตัยมิยะฮ์
    s = sub(r"ตัยมียะฮ์", "ตัยมิยะฮ์", s, "13 ตัยมียะฮ์→ตัยมิยะฮ์")
    # 14 วุฎูอ์
    s = sub(r"การอาบน้ำละหมาด", "การทำวุฎูอ์", s, "14 การอาบน้ำละหมาด→การทำวุฎูอ์")
    s = sub(r"(?<!\()อาบน้ำละหมาด(?!\))", "ทำวุฎูอ์", s, "14 อาบน้ำละหมาด→ทำวุฎูอ์")
    s = sub(r"ทำทำวุฎูอ์", "ทำวุฎูอ์", s, "14 fix")
    # 15 ชัยค์ (เชค in this corpus = other shaykhs, not the author)
    s = sub(r"เชคุล", "ชัยคุล", s, "15 เชคุล→ชัยคุล")
    s = sub(r"เชค", "ชัยค์", s, "15 เชค→ชัยค์")
    # 28 หุก่ม → ข้อตัดสิน (approved 2026-11-23)
    s = sub(r"หุก่ม", "ข้อตัดสิน", s, "28 หุก่ม→ข้อตัดสิน")
    s = sub(r"ข้อตัดสิน\s*\(ข้อตัดสิน\)", "ข้อตัดสิน", s, "28 fix dup")
    # 16 สาวก of the Prophet
    s = sub(r"สาวก(?=ของท่าน|ชั้นนำ|บางคน)", "เศาะหาบะฮ์", s, "16 สาวก→เศาะหาบะฮ์")
    return s

# ---------------------------------------------------------------- บิน spacing
def binfix(s, field):
    return sub(r"(?<=\s)บิน(?!ต|\s)(?=[ก-ฮเแโใไ])", "บิน ", s, "17 บิน→บิน␠")

# ---------------------------------------------------------------- quotes
odd = []
def quotes(s, field, where=None):
    n = s.count('"')
    if not n:
        return s
    if n % 2:
        odd.append(where)
        return s
    out, opening = [], True
    for ch in s:
        if ch == '"':
            out.append("«" if opening else "»"); opening = not opening
        else:
            out.append(ch)
    stats['18 " " → « »'] += n // 2
    return "".join(out)

# ---------------------------------------------------------------- ﷺ
PROPHET = re.compile(r"(ท่าน(?:นบี|เราะซูลุลลอฮ์|เราะซูล(?!ุ)))(?!\s*ﷺ)")
def saw(s, field):
    if field.startswith("translation_th"):
        n = len(PROPHET.findall(s))
        if n:
            stats["19 ﷺ เติมในคำแปล"] += n
            s = PROPHET.sub(r"\1 ﷺ", s)
    elif field.startswith("points_th") or field.startswith("key_rulings_th") or field.startswith("intro_th"):
        if "ﷺ" not in s and PROPHET.search(s):
            stats["19 ﷺ เติมครั้งแรกของข้อ"] += 1
            s = PROPHET.sub(r"\1 ﷺ", s, count=1)
    return s

FN = {"terms": terms, "bin": binfix, "quotes": None, "saw": saw}[GROUP]

def fix(s, field, where):
    if GROUP == "quotes":
        return quotes(s, field, where)
    return FN(s, field)

def walk_entry(e, where):
    e["topic_th"] = fix(e["topic_th"], "topic_th", where)
    for h in e["hadith"]:
        h["translation_th"] = fix(h["translation_th"], "translation_th", where)
        h["grade_th"] = fix(h["grade_th"], "grade_th", where)
    e["key_rulings_th"] = [fix(k, "key_rulings_th", where) for k in e["key_rulings_th"]]
    for v in e["vocab"]:
        v["th"] = fix(v["th"], "vocab", where)
    for sct in e["sections"]:
        if sct.get("heading_th"):
            sct["heading_th"] = fix(sct["heading_th"], "heading_th", where)
        sct["points_th"] = [fix(p, "points_th", where) for p in sct["points_th"]]
    if "tags_th" in e:
        e["tags_th"] = [fix(t, "tags_th", where) for t in e["tags_th"]]

def walk_toc(t, where):
    for k in t.get("kitabs", []):
        if k.get("th"): k["th"] = fix(k["th"], "toc_th", where)
        if k.get("intro_th"): k["intro_th"] = [fix(p, "intro_th", where) for p in k["intro_th"]]
    for b in t["babs"]:
        if b.get("th"): b["th"] = fix(b["th"], "toc_th", where)
        if b.get("intro_th"): b["intro_th"] = [fix(p, "intro_th", where) for p in b["intro_th"]]
        for tp in b["topics"]:
            if tp.get("th"): tp["th"] = fix(tp["th"], "toc_th", where)

changed = 0
for f in sorted(glob.glob(str(root / "vol*/entries/*.json"))) + sorted(glob.glob(str(root / "vol*/toc.json"))):
    e, fmt = jsonio.load(f)
    before = jsonio.dump(e, fmt)
    rel = str(pathlib.Path(f).relative_to(root))
    (walk_toc if f.endswith("toc.json") else walk_entry)(e, rel)
    after = jsonio.dump(e, fmt)
    if after != before:
        changed += 1
        if not DRY:
            open(f, "wb").write(after)

for k, v in sorted(stats.items()):
    print(f"{v:6d}  {k}")
print("files changed:", changed, "(dry run)" if DRY else "")
if odd:
    print("odd quote count, left unchanged:", len(odd), sorted(set(odd))[:20])
