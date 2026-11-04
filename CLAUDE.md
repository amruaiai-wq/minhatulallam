# Minhat al-Allam — Thai summary project

Thai summary website of **منحة العلام في شرح بلوغ المرام** by Sheikh Abdullah al-Fawzan
(a commentary on Ibn Hajar's Bulugh al-Maram). Source: scanned PDFs, one per volume.

## Current status

- Volume 1 (كتاب الطهارة, hadith 1–107, 431 pages): `vol1/toc.json` is complete.
- Done: **Volume 1 complete** (hadith 1–107, all 8 babs; `vol1/entries/h001.json` … `h106-107.json`).
- Volume 2 (`sources/vol2.pdf`, 520 pages, hadith 108–266; no OCR file): `vol2/toc.json` built from
  the book's own فهرس الموضوعات (pp. 516–520), with a `kitab` field per bab (taharah / hayd / salah).
  Done: باب الغسل (108–125), باب التيمم (126–137), كتاب الحيض (138–150), كتاب الصلاة intro
  (on the `salah` entry in `kitabs`), باب المواقيت (complete: intro + all topics, hadith 151–177, pages 167–235),
  باب الأذان (complete: intro + all topics, hadith 178–204, pages 236–316),
  باب شروط الصلاة (complete: intro + all topics, hadith 205–227, pages 317–394).
- Next: باب سترة المصلي (page 395: bab intro, then hadith 228 onward). Still open in vol 1: miyah bab intro.
- When the author comments before «الكلام عليه من وجوه», fold it into the most related wajh
  (no wajh 0).
- toc.json headings were drafted before reading; when the scan's heading differs, the scan
  wins (fixed so far: «بيان كيفية إزالة المني…», «حكم تخليل اللحية…», «بيان فضيلة الوضوء…», «بيان ما لا يُستنجى به» and 4 more in qada-hajah; vol 2: «بعض خصائص النبي ﷺ…»).
- Bab intros (author's text before the first topic) go in `toc.json` as `intro_th` on the bab
  (added for aniyah … qada-hajah; miyah not yet done; pending user approval).

## Source PDF

- `sources/vol1.pdf` (scanned images, no text layer). Read pages visually with the Read tool
  and the `pages` parameter (max 20 pages per call). On this Windows machine pdftoppm is not
  installed, so render pages to PNG with PyMuPDF (`fitz`, installed) into the scratchpad and
  read the images; zoom (dpi 220–300 with `clip`) to check harakat in the matn.
- PDF page number = printed page number in the book.
- `sources/vol1_ocr.docx` is an OCR text of the whole volume (from the user). Use it **only to
  locate passages**. It drops harakat, garbles matn, misreads numbers (e.g. 5426 → 477) and
  ﷺ / رضي الله عنه glyphs, so never copy matn, hadith numbers or names from it.
- Each topic starts with the author's heading in a decorative frame, then the hadith
  (numbered like `٥/٥`), then «الكلام عليه من وجوه» and numbered «الوجه الأول، الثاني…».

## Workflow per batch

1. Work one bab at a time (about 8–10 hadith / 30–40 pages per batch).
2. Read the pages, transcribe the matn, write one JSON file per **topic** (not per hadith;
   a topic can hold several hadith, e.g. `h003-004.json`).
3. Fill `hadith_nos` for those topics in `toc.json`.
4. Validate: every file parses, wajh numbers ascending, no hadith numbers missing.
5. Show the user a summary and list anything uncertain for review.

## File naming

`vol1/entries/h{first:03d}.json` or `h{first:03d}-{last:03d}.json`.

## JSON schema (one file per topic)

```json
{
  "id": "v1-h003-004",
  "volume": 1,
  "bab": "miyah",                       // bab id from toc.json
  "topic_ar": "حكم الماء إذا لاقته نجاسة",  // author's heading, exact
  "topic_th": "ข้อตัดสินเรื่องน้ำที่สัมผัสนะญิส",
  "pages": [32, 34],                    // first and last page of the topic
  "hadith": [
    {
      "no": 3,
      "matn_ar": "…full matn with harakat, incl. Ibn Hajar's takhrij line…",
      "translation_th": "…",
      "grade_th": "ฎออีฟ (อ่อน)"
    }
  ],
  "key_rulings_th": ["…"],              // 3–5 bullets, shown in quick-read mode
  "vocab": [{"ar": "…", "th": "…"}],
  "sections": [                         // one per wajh, in the author's order
    {
      "wajh": 1,
      "type": "rawi | takhrij | alfaz | fiqh | fawaid",
      "heading_ar": "في ترجمة الراوي",  // author's heading, or null if none
      "heading_th": "ชีวประวัติผู้รายงาน",
      "points_th": ["…"]
    }
  ],
  "tags_th": ["…"]
}
```

## Writing rules (approved by the user)

- **Concise summary focused on understanding, without dropping important content.**
  Roughly 30–40% of the original length.
- Matn: transcribe from the scan with full harakat. Write ﷺ for the Prophet and
  رَضِيَ اللهُ عَنْهُ / عَنْهُمَا / عَنْهَا in full instead of the book's glyphs.
- Thai terms: transliterate fiqh terms as used so far — ฏอฮูร, ฮะดัษ (เล็ก/ใหญ่), นะญิส,
  ญะนาบะฮ์, อิจญ์มาอ์, มักรูฮ์, หะรอม, วาญิบ, ศ่อฮีห์, หะซัน, ฎออีฟ, มุรสัล, เมากูฟ, มุดัลลิส.
  Honorific after a companion's name: (ร.ฎ.).
- Always keep the **author's own tarjih** (الراجح / الصواب / الصحيح) clear. When the author
  disagrees with a narration or an opinion, say so explicitly ("ผู้แต่งเห็นว่า…").
- Attribute claims: opinions to the scholar who holds them; scientific or modern claims
  as "ผู้แต่งอ้างถึง…", never as our own statement.
- Takhrij: keep book names and hadith numbers; drop footnote source lists.
- Do not invent content. If a figure or reading in the scan is unclear or inconsistent,
  keep the closest faithful reading and flag it to the user.
- Plain, natural Thai. No filler.

## Website (later phase)

**`design/prototype.html` is the approved design reference.** It is a working single-file
prototype built from the real JSON. The real site must match its screens, layout and colors.

- Mobile-first, max content width 520px, bottom tab bar: หน้าแรก / สารบัญ / ค้นหา / บุ๊กมาร์ก.
- Responsive (user request): tablet ≥768px widens to 760px with a 3-column kitab grid and
  2-column search results; desktop ≥1100px swaps the bottom tabs for a left side rail (232px)
  and shows the hadith page in two columns (matn + rulings sticky on the left, vocab +
  explanation on the right; quick mode collapses to one column).
- Local preview: `python tools/build_preview.py` merges all `vol*/` TOCs and entries into the prototype
  → `site/preview.html` (served by the `preview` config in `.claude/launch.json`).
- Home: green header band with Arabic + Thai title and search box, "continue reading" card
  with progress, kitab grid (2 columns), popular tags.
- Hadith page (one per topic): sticky top bar (breadcrumb, hadith no., bookmark),
  อ่านเร็ว / อ่านละเอียด toggle, author's heading, matn card(s) with grade, สรุปข้อตัดสิน,
  vocab (detailed only), author's explanation by wajh (detailed only), tags, prev/next.
- Search: Thai, Arabic (ignore harakat), hadith number; filters ทั้งหมด / ตัวบทอาหรับ /
  ข้อตัดสิน / หัวข้อ; result cards with highlight.
- TOC: every bab and topic from toc.json; topics not yet summarized shown as รอสรุป.
- **Light theme only** (do not auto-switch to dark). Colors:
  green #2E5641 (dark #1F3D2D, soft #EAEDDC), gold #8A5A16 (line #A8752B, soft #FBEFD9),
  ground #F8F2E7, cards #FFFCF6, ink #2A231D, muted #6B5F52, lines #E8DDCB.
- Fonts: Noto Sans Thai + Noto Naskh Arabic.
- Stack: Next.js or Astro static site on Vercel, reading `vol*/entries/*.json` at build time.

## Note

The book is under copyright (author and publisher). Get permission before publishing publicly.
