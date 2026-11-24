"""Style rule: scholars' quotations use ( ), the Prophet's words and quoted text use « ».
Turns «…» into (…) when it directly follows a later scholar's name + ว่า / กล่าวว่า.
Hadith compilers (บุคอรีย์, มุสลิม, อบูดาวูด, …) are left alone: after their names « » is usually hadith text.
Usage: python tools/scholar_quotes.py [--apply]  (dry run prints samples)"""
import glob, re, sys, random
sys.path.insert(0, 'tools'); import jsonio
NAMES = """อัลหาฟิซ อบูหาติม อิบนุอับดิลบัรร์ อิบนุตัยมิยะฮ์ ชัยคุลอิสลาม อันนะวะวีย์ อิบนุลก็อยยิม อิบนุมะอีน อัซซะฮะบีย์ อัษษะฮะบีย์
อัลอัลบานีย์ อิบนุกะษีร อิบนุกุดามะฮ์ อิบนุอะดีย์ อิบนุเราะญับ อิบนุร็อจญับ อบูซุรอะฮ์ อัลค็อฏฏอบีย์ อิบนุหัซม์ อิบนุลมุนซิร อัชเชากานีย์
อัลกุรฏุบีย์ อิบนุบาซ อิบนุลก็อฏฏอน อิบนุลมะดีนีย์ อิบนุอับดิลฮาดีย์ อิบนุอับดิลฮาดี อัชชาฟิอีย์ อัลกอฎีอิยาฎ อัลอิรอกีย์ อิบนุดะกีกิลอีด
อิบนุดะกีกอัลอีด อิบนุลมุลักกิน อิบนุบัฏฏ็อล อัศศ็อนอานีย์ อัลมุนซิรีย์ อัสสะอ์ดีย์ อิบนุอุษัยมีน อัลบัยฮะกีย์ อัดดาเราะกุฏนีย์
อัดดารุกุฏนีย์ อัลหากิม อัลอุก็อยลีย์ อัลบัฆวีย์ อัลบะเฆาะวีย์ อิบนุหิบบาน อิบนุคุซัยมะฮ์ อิบนุลอะษีร อิบนุลอะเราะบีย์ อัลมาซิรีย์
อัลมิซซีย์ อัลอัยนีย์ อัสสินดีย์ อิบนุรุชด์ อิบนุฮุบัยเราะฮ์ อัลมัรดาวีย์ อิบนุมุฟลิห์ อะห์มัด_ชากิร อัฏเฏาะหาวีย์
อัซซัยละอีย์ อัลบูศีรีย์ อัลฮัยษะมีย์ อิบนุลเญาซีย์ อัลอัษร็อม อิมามอะห์มัด อะห์มัด""".split()
NAMES = [n.replace("_", " ") for n in NAMES]
NAMES = sorted(set(NAMES), key=len, reverse=True)
PAT = re.compile(r'(' + '|'.join(map(re.escape, NAMES)) + r')([^«»()\n]{0,14}?)(กล่าวว่า|ว่า|กล่าว:)\s?«')
BAD = re.compile(r'ท่านนบี|ท่านเราะซูล|รายงาน|บันทึก|หะดีษ|สำนวน|ตรัส|ถาม|ตอบ|จาก|เห็น|คำ|ปฏิเสธ|ว่า|:|ผู้แต่ง|เพิ่ม|;')
PRE = re.compile(r'(?:ของ|โดย|ใน|จาก|ผ่าน|สาย)\s?$')
def conv(s, log):
    out, i = [], 0
    for m in PAT.finditer(s):
        if m.start() < i or BAD.search(m.group(2)) or PRE.search(s[max(0, m.start() - 6):m.start()]): continue
        start = m.end() - 1; d = 0; j = start
        while j < len(s):
            d += (s[j] == '«') - (s[j] == '»')
            if d == 0: break
            j += 1
        if j >= len(s): continue
        out.append(s[i:start]); out.append('(' + s[start + 1:j] + ')'); i = j + 1
        log.append(s[max(0, m.start() - 10): min(len(s), j + 3)])
    out.append(s[i:]); return ''.join(out)
def walk(x, log, key=None):
    if isinstance(x, str): return conv(x, log) if key != 'matn_ar' else x
    if isinstance(x, list): return [walk(y, log, key) for y in x]
    if isinstance(x, dict): return {k: walk(v, log, k) for k, v in x.items()}
    return x
log = []
for f in sorted(glob.glob('vol*/entries/*.json')) + sorted(glob.glob('vol*/toc.json')):
    e, fmt = jsonio.load(f); e2 = walk(e, log)
    if '--apply' in sys.argv and e2 != e: jsonio.save(f, e2, fmt)
print(len(log))
random.seed(1)
for x in random.sample(log, min(25, len(log))): print('-', x[:200])
