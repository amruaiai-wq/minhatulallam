"""Consistency audit of all vol*/entries/*.json and toc intros.

Writes a machine-readable report to tools/audit_out.json and prints a summary.
Run: python tools/audit.py
"""
import json, glob, re, collections, pathlib

root = pathlib.Path(__file__).resolve().parent.parent

# Variant families: canonical-candidate spellings to compare. Each family lists regexes.
FAMILIES = {
 "หะดีษ": [r"หะดีษ", r"ฮะดีษ", r"ฮาดีษ", r"หาดีษ"],
 "ศ่อฮีห์ (ระดับ)": [r"ศ่อฮีห์", r"ศอฮีห์", r"เศาะฮีห์", r"ซอฮีห์", r"ศ่อหีห์"],
 "หะซัน (ระดับ)": [r"หะซัน", r"ฮะซัน", r"หะสัน(?!\s*(?:อัล)?บัศรีย์)", r"หาซัน"],
 "ฎออีฟ": [r"ฎออีฟ", r"เฎาะอีฟ", r"ดออีฟ", r"ฎะอีฟ"],
 "มัรฟูอ์": [r"มัรฟูอ์", r"มัรฟูอฺ", r"มัรฟูอ(?!์)"],
 "เมากูฟ": [r"เมากูฟ", r"มัวกูฟ", r"เมาฆูฟ"],
 "มุตตะฟักอะลัยฮ์/บุคอรีย์และมุสลิม": [r"มุตตะฟะกุนอะลัยฮ์", r"มุตตะฟักอะลัยฮ์", r"บุคอรีย์และมุสลิม"],
 "เศาะหาบะฮ์": [r"เศาะหาบะฮ์", r"ศ่อฮาบะฮ์", r"เศาะฮาบะฮ์", r"ซอฮาบะฮ์", r"สาวก"],
 "ตาบิอีน": [r"ตาบิอีน", r"ตาบิอูน", r"ตาบิอีย์"],
 "อุละมาอ์": [r"อุละมาอ์", r"อุลามาอ์", r"นักวิชาการ", r"ผู้รู้"],
 "ฟุเกาะฮาอ์": [r"ฟุเกาะฮาอ์", r"ฟุกอฮาอ์", r"นักนิติศาสตร์"],
 "ญุมฮูร": [r"ญุมฮูร", r"ญุมฮูรฺ", r"ส่วนใหญ่ของนักวิชาการ"],
 "มติ/อิจญ์มาอ์": [r"อิจญ์มาอ์", r"อิจมาอ์", r"มติ(?:เอกฉันท์)?"],
 "หะรอม": [r"หะรอม", r"ฮะรอม", r"หะรอม", r"ต้องห้าม"],
 "มักรูฮ์": [r"มักรูฮ์", r"มักรูฮฺ", r"น่ารังเกียจ"],
 "วาญิบ": [r"วาญิบ", r"วายิบ", r"ฟัรฎู"],
 "สุนนะฮ์": [r"สุนนะฮ์", r"ซุนนะฮ์", r"สุนนะห์"],
 "ท่านเราะสูล": [r"เราะสูลุลลอฮ์", r"รสูลุลลอฮ์", r"ร่อซูลุลลอฮ์", r"เราะซูลุลลอฮ์", r"ท่านเราะสูล(?!ุ)", r"ท่านรสูล(?!ุ)", r"ท่านศาสดา"],
 "ท่านนบี": [r"ท่านนบี", r"ท่านนะบี", r"ศาสนทูต"],
 "การรายงาน (กริยา)": [r"บันทึกโดย", r"รายงานโดย", r"(?<!ผู้)รายงาน"],
 "ร.ฎ.": [r"\(ร\.ฎ\.\)", r"ร\.ด\.", r"\(รฎ\)", r"รอฎิยัลลอฮุ"],
 "ฮ.ศ.": [r"ฮ\.ศ\.", r"ฮิจเราะฮ์ศักราช"],
 "บุคอรีย์": [r"อัลบุคอรีย์", r"(?<!อัล)บุคอรีย์", r"บุคอรี(?!ย์)"],
 "อัตติรมิซีย์": [r"อัตติรมิซีย์", r"อัตติรมีซีย์", r"ติรมิซี(?!ย์)"],
 "อันนะสาอีย์": [r"อันนะสาอีย์", r"อันนะซาอีย์", r"นะสาอี(?!ย์)"],
 "อบูดาวูด": [r"อบูดาวูด", r"อบูดาวุด", r"อะบูดาวูด"],
 "อิบนุมาญะฮ์": [r"อิบนุมาญะฮ์", r"อิบนุมาจะฮ์", r"อิบนุ มาญะฮ์"],
 "อัลหาฟิซ": [r"อัลหาฟิซ", r"อัลฮาฟิซ", r"อัลหาฟิศ", r"อิบนุหะญัร", r"อิบนุฮะญัร"],
 "อิบนุตัยมิยะฮ์": [r"อิบนุตัยมิยะฮ์", r"อิบนุตัยมียะฮ์", r"อิบนุ ตัยมิยะฮ์"],
 "อิบนุลก็อยยิม": [r"อิบนุลก็อยยิม", r"อิบนุล ก็อยยิม", r"อิบนุก็อยยิม"],
 "อันนะวะวีย์": [r"อันนะวะวีย์", r"อันนะวาวีย์", r"นะวะวี(?!ย์)"],
 "อัชเชากานีย์": [r"อัชเชากานีย์", r"อัชเชากานี(?!ย์)", r"อัชเชาว์กานีย์"],
 "อัศศ็อนอานีย์": [r"อัศศ็อนอานีย์", r"อัศศอนอานีย์", r"อัศศันอานีย์"],
 "อิบนุกุดามะฮ์/อัลมุวัฟฟัก": [r"อิบนุกุดามะฮ์", r"อิบนุ กุดามะฮ์", r"อัลมุวัฟฟัก"],
 "บิน (ชื่อ)": [r"\sบิน\s", r"\sบิน(?=[ก-ฮ])", r"\sอิบนุ\s"],
 "ทัศนะของผู้แต่ง": [r"ผู้แต่ง:", r"ผู้แต่งเห็นว่า", r"ผู้เขียน", r"ผู้ประพันธ์", r"เชค(?:ฟัวซาน)?"],
 "อัลลอฮ์ทรง": [r"อัลลอฮ์ทรง", r"อัลลอฮฺ", r"พระเจ้า"],
 "อบูฮุร็อยเราะฮ์": [r"อบูฮุร็อยเราะฮ์", r"อบูฮุรอยเราะฮ์", r"อบูฮุรัยเราะฮ์"],
 "อาอิชะฮ์": [r"อาอิชะฮ์", r"อาอิชะห์", r"ท่านหญิงอาอิชะฮ์"],
 "ชัยคุลอิสลาม": [r"ชัยคุลอิสลาม", r"เชคุลอิสลาม", r"ชัยคุล อิสลาม"],
 "มัซฮับ": [r"มัซฮับ", r"มัษฮับ", r"มัสฮับ"],
 "กิศอศ": [r"กิศอศ", r"กิศ็อศ", r"กิซอศ"],
 "อายะฮ์": [r"อายะฮ์", r"อายะห์", r"โองการ"],
 "ซูเราะฮ์": [r"ซูเราะฮ์", r"สูเราะฮ์", r"ซูเราะห์"],
 "อัลกุรอาน": [r"อัลกุรอาน", r"อัลกุรอ่าน", r"กุรอาน(?<!อัลกุรอาน)"],
 "ญะนาบะฮ์": [r"ญะนาบะฮ์", r"ญุนุบ", r"ยะนาบะฮ์"],
 "ละหมาด": [r"ละหมาด", r"นมาซ", r"ศ่อลาฮ์"],
 "วุฎูอ์": [r"วุฎูอ์", r"วุฎู(?!อ์)", r"อาบน้ำละหมาด"],
}

FIELDS = ("topic_th",)

def texts(e):
    """Yield (path, text) for every Thai text field of an entry."""
    yield "topic_th", e.get("topic_th", "")
    for i, h in enumerate(e["hadith"]):
        yield f"hadith[{i}].translation_th", h.get("translation_th", "")
        yield f"hadith[{i}].grade_th", h.get("grade_th", "")
    for i, k in enumerate(e["key_rulings_th"]):
        yield f"key_rulings_th[{i}]", k
    for i, v in enumerate(e["vocab"]):
        yield f"vocab[{i}].th", v["th"]
    for i, s in enumerate(e["sections"]):
        yield f"sections[{i}].heading_th", s.get("heading_th") or ""
        for j, p in enumerate(s["points_th"]):
            yield f"sections[{i}].points_th[{j}]", p
    for i, t in enumerate(e.get("tags_th", [])):
        yield f"tags_th[{i}]", t

def strip_ar(s):
    return re.sub(r"[ً-ْٰـ]", "", s)

entries = []
for f in sorted(glob.glob(str(root / "vol*/entries/*.json")), key=lambda p: (int(re.search(r"vol(\d+)", p).group(1)), p)):
    e = json.load(open(f, encoding="utf-8"))
    e["_file"] = str(pathlib.Path(f).relative_to(root))
    entries.append(e)

intros = []
for f in sorted(glob.glob(str(root / "vol*/toc.json"))):
    t = json.load(open(f, encoding="utf-8"))
    v = int(re.search(r"vol(\d+)", f).group(1))
    for k in t.get("kitabs", []):
        for p in k.get("intro_th") or []:
            intros.append((v, f"kitab:{k['id']}", p))
    for b in t["babs"]:
        for p in b.get("intro_th") or []:
            intros.append((v, f"bab:{b['id']}", p))

out = {"families": {}, "issues": collections.defaultdict(list), "stats": {}}

# --- variant families, counted per volume
for fam, pats in FAMILIES.items():
    res = {}
    for pat in pats:
        per = collections.Counter()
        for e in entries:
            for _, t in texts(e):
                per[e["volume"]] += len(re.findall(pat, t))
        for v, _, t in intros:
            per[v] += len(re.findall(pat, t))
        if sum(per.values()):
            res[pat] = dict(sorted(per.items()))
    out["families"][fam] = res

# --- grade_th forms
grades = collections.Counter()
for e in entries:
    for h in e["hadith"]:
        g = h.get("grade_th", "")
        head = re.split(r"[\s(]", g, maxsplit=1)[0]
        grades[head] += 1
out["stats"]["grade_heads"] = grades.most_common()

# --- per-entry mechanical issues
lens = []
for e in entries:
    f = e["_file"]
    for path, t in texts(e):
        if '"' in t:
            out["issues"]["ascii_double_quote"].append(f"{f} {path}")
        if re.search(r"  ", t):
            out["issues"]["double_space"].append(f"{f} {path}")
        if re.search(r"[A-Za-z]{3,}", t):
            out["issues"]["latin_text"].append(f"{f} {path}: {re.findall(r'[A-Za-z]{3,}', t)[:3]}")
        if t != t.strip():
            out["issues"]["leading_trailing_space"].append(f"{f} {path}")
        if re.search(r"ท่าน(?:นบี|เราะสูล(?:ุลลอฮ์)?|รสูล(?:ุลลอฮ์)?)(?! ﷺ)", t) and path.startswith("hadith"):
            out["issues"]["prophet_without_saw_in_translation"].append(f"{f} {path}")
        if path.startswith("sections") and len(t) > 1800:
            out["issues"]["very_long_point"].append(f"{f} {path} ({len(t)} chars)")
    kr = e["key_rulings_th"]
    if not 3 <= len(kr) <= 5:
        out["issues"]["key_rulings_count"].append(f"{f} ({len(kr)})")
    for i, k in enumerate(kr):
        lens.append(len(k))
        if len(k) > 400:
            out["issues"]["key_ruling_too_long"].append(f"{f} key_rulings_th[{i}] ({len(k)} chars)")
        if len(k) < 25:
            out["issues"]["key_ruling_too_short"].append(f"{f} key_rulings_th[{i}] ({len(k)} chars)")
    for h in e["hadith"]:
        m = h["matn_ar"]
        if re.search(r"[﵀-﵏]", m) or "صلى الله عليه وسلم" in m:
            out["issues"]["matn_honorific_glyph"].append(f"{f} hadith {h['no']}")
        if not re.search(r"[ً-ْ]", m):
            out["issues"]["matn_no_harakat"].append(f"{f} hadith {h['no']}")
        if "(ร.ฎ.)" not in h["translation_th"] and re.search(r"رَضِيَ اللهُ", m):
            out["issues"]["ra_missing_in_translation"].append(f"{f} hadith {h['no']}")
        if not h.get("grade_th"):
            out["issues"]["grade_missing"].append(f"{f} hadith {h['no']}")
    if not e.get("vocab"):
        out["issues"]["no_vocab"].append(f)
    if not e.get("tags_th"):
        out["issues"]["no_tags"].append(f)
    # tarjih signal: entries where sections mention a ruling term but no author verdict marker
    alltext = " ".join(t for _, t in texts(e))
    if re.search(r"ทัศนะที่สอง", alltext) and not re.search(r"ผู้แต่ง|«والراجح|«والصواب|«والأظهر|«والأقرب", alltext):
        out["issues"]["disagreement_without_author_verdict"].append(f)

# --- vocab conflicts: same Arabic (no harakat) with different Thai
voc = collections.defaultdict(set)
for e in entries:
    for v in e["vocab"]:
        voc[strip_ar(v["ar"]).strip()].add(v["th"].strip())
out["stats"]["vocab_terms"] = len(voc)
out["stats"]["vocab_with_multiple_glosses"] = sum(1 for k, s in voc.items() if len(s) > 1)
out["vocab_conflicts_sample"] = {k: sorted(s) for k, s in list((k, s) for k, s in voc.items() if len(s) > 2)[:40]}

# --- length stats per volume (Thai chars of sections)
per_vol = collections.defaultdict(list)
for e in entries:
    n = sum(len(p) for s in e["sections"] for p in s["points_th"])
    per_vol[e["volume"]].append(n)
out["stats"]["avg_section_chars_per_topic"] = {v: round(sum(x) / len(x)) for v, x in sorted(per_vol.items())}
out["stats"]["avg_key_ruling_chars"] = round(sum(lens) / len(lens))
out["stats"]["entries"] = len(entries)
out["stats"]["intro_paragraphs"] = len(intros)

out["issues"] = {k: v for k, v in out["issues"].items()}
(root / "tools/audit_out.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

print("entries", len(entries), "intros", len(intros))
for fam, res in out["families"].items():
    if len(res) > 1:
        print(f"\n[{fam}]")
        for pat, per in res.items():
            print(f"  {pat:40s} total={sum(per.values()):5d}  {per}")
print("\nGRADES", grades.most_common(15))
print("\nISSUES")
for k, v in out["issues"].items():
    print(f"  {k}: {len(v)}  e.g. {v[:3]}")
print("\nSTATS", {k: v for k, v in out["stats"].items() if k != 'grade_heads'})
