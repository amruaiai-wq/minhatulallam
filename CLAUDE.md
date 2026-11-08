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
  باب شروط الصلاة (complete: intro + all topics, hadith 205–227, pages 317–394),
  باب سترة المصلي (complete: intro + all topics, hadith 228–237, pages 395–428),
  باب الحث على الخشوع في الصلاة (complete: intro + all topics, hadith 238–250, pages 429–463),
  باب المساجد (complete: intro + all topics, hadith 251–266, pages 464–505). **Volume 2 complete.**
- Volume 3 (`sources/vol3.pdf`, 511 pages, hadith 267–441, all كتاب الصلاة): `vol3/toc.json` built from the
  book's فهرس الموضوعات (pp. 506–511); babs sifah / sahw / tatawwu / jamaah / musafir.
  Done: باب صفة الصلاة (complete: intro + all topics, hadith 267–329, pages 5–208); باب سجود السهو (complete: intro + all topics, hadith 330–349, pages 209–262); باب صلاة التطوع (complete: intro + all topics, hadith 350–396, pages 263–350); باب صلاة الجماعة والإمامة (complete: intro + all topics, hadith 397–428, pages 351–449); باب صلاة المسافر والمريض (complete: intro + all topics, hadith 429–441, pages 450–490). **Volume 3 complete.**
- Volume 4 (`sources/vol4.pdf`, 534 pages, hadith 445–649): `vol4/toc.json` built from the book's
  فهرس الموضوعات (pp. 527–534). Kitabs salah / janaiz / zakah; babs jumuah, khawf, idayn, kusuf, istisqa,
  libas (salah), janaiz (whole kitab, no babs), zakah (kitab's own topics), fitr, sadaqah, qasm.
  The book's numbering skips 442–444 (صلاة المريض, already explained in vol 3 h328–329), so vol 4 starts at 445.
  Validate with a fin script that starts at 445. Done: باب صلاة الجمعة (complete: intro + all topics, hadith 445–474, pages 5–88). باب صلاة الخوف (complete: intro + all topics, hadith 475–484, pages 89–108). باب صلاة العيدين (complete: intro + all topics, hadith 485–501, pages 109–147). باب صلاة الكسوف (complete: intro + all topics, hadith 502–512, pages 148–168). باب صلاة الاستسقاء (complete: intro + all topics, hadith 513–523, pages 169–200). باب اللباس (complete: intro + all topics, hadith 524–533, pages 201–227). كتاب الجنائز (complete: kitab intro on the `janaiz` entry in `kitabs` + all topics, hadith 534–598, pages 229–387). كتاب الزكاة: kitab intro (on the `zakah` entry in `kitabs`, pp. 389–390) + all the kitab's own topics complete (bab `zakah`, hadith 599–626, pages 391–456). باب صدقة الفطر (complete: intro + all topics, hadith 627–630, pages 457–465). باب صدقة التطوع (complete: intro + all topics, hadith 631–642, pages 466–492). باب قسم الصدقات (complete: intro + all topics, hadith 643–649, pages 493–511). **Volume 4 complete.**
- Volume 5 (`sources/vol5.pdf`, 392 pages, hadith 650–781): `vol5/toc.json` built from the book's
  فهرس الموضوعات (pp. 388–392). Kitabs siyam / hajj; babs siyam (kitab's own topics), tatawwu, itikaf (siyam),
  fadl, mawaqit, wujuh (one topic = the bab heading), ihram, sifah, fawat (hajj). Validate with `fin4.py 5 650`.
  Done: كتاب الصيام kitab intro (on the `siyam` entry in `kitabs`, pp. 5–6); all the kitab's own topics complete (bab `siyam`, hadith 650–679, pages 7–75). باب صوم التطوع (complete: intro + all topics, bab `tatawwu`, hadith 680–696, pages 76–121). باب الاعتكاف وقيام رمضان (complete: intro + all topics, bab `itikaf`, hadith 697–707, pages 122–155). كتاب الحج kitab intro (on the `hajj` entry in `kitabs`, pp. 156–157). باب فضله وبيان من فرض عليه (complete: bab `fadl`, no separate bab intro, hadith 708–721, pages 158–190). باب المواقيت (complete: intro + all topics, hadith 722–726, pages 191–200). باب وجوه الإحرام وصفته (complete: bab `wujuh`, no separate bab intro, hadith 727, pages 201–205). باب الإحرام وما يتعلق به (complete: intro + all topics, hadith 728–741, pages 206–248). باب صفة الحج ودخول مكة (complete: intro + all topics, bab `sifah`, hadith 742–778, pages 249–365). باب الفوات والإحصار (complete: intro + all topics, bab `fawat`, hadith 779–781, pages 366–377). **Volume 5 complete.**
- Volume 6 (`sources/vol6.pdf`, 504 pages, hadith 782–926, all كتاب البيوع): `vol6/toc.json` built from the book's
  فهرس الموضوعات (pp. 501–504); kitab `buyu` (intro on the `buyu` entry in `kitabs`, pp. 5–6); babs shurut, khiyar, riba,
  araya, salam, taflis, sulh, hawalah, sharikah, iqrar, ariyah, ghasb, shufah, qirad, musaqah, mawat. Validate with `fin4.py 6 782`.
  Done: باب شروطه وما نهي عنه (complete: intro + all topics, bab `shurut`, hadith 782–825, pages 5–147). باب الخيار (complete: intro + all topics, hadith 826–829, pages 148–161). باب الربا (complete: intro + all topics, hadith 830–847, pages 162–224). باب الرخصة في العرايا وبيع الأصول والثمار (complete: intro + all topics, bab `araya`, hadith 848–854, pages 225–246). أبواب السلم والقرض والرهن (complete: intro + all topics, bab `salam`, hadith 855–864, pages 247–277). باب التفليس والحجر (complete: intro + all topics, bab `taflis`, hadith 865–872, pages 278–308). باب الصلح (complete: intro + all topics, bab `sulh`, hadith 873–876, pages 309–324). باب الحوالة والضمان (complete: intro + all topics, bab `hawalah`, hadith 877–880, pages 325–341). باب الشركة والوكالة (complete: intro + all topics, bab `sharikah`, hadith 881–888, pages 342–361). باب الإقرار (complete: intro + all topics, bab `iqrar`, hadith 889, pages 362–366). باب العارية (complete: intro + all topics, bab `ariyah`, hadith 890–894, pages 367–384). باب الغصب (complete: intro + all topics, bab `ghasb`, hadith 895–900, pages 385–403). باب الشفعة (complete: intro + all topics, bab `shufah`, hadith 901–905, pages 404–424). باب القراض (complete: intro + all topics, bab `qirad`, hadith 906–907, pages 425–433; the Malik athar after h907 is unnumbered in the book). باب المساقاة (complete: intro + all topics, bab `musaqah`, hadith 908–916, pages 434–464). باب إحياء الموات (complete: intro + all topics, bab `mawat`, hadith 917–926, pages 465–491). **Volume 6 complete.**
- Volume 7 (`sources/vol7.pdf`, 614 pages, hadith 927–1094): `vol7/toc.json` built from the book's
  فهرس الموضوعات (pp. 609–614). Kitabs buyu (cont.) / nikah (p. 169) / talaq (p. 507); babs waqf, hibah, luqatah, faraid,
  wasaya, wadiah (buyu), nikah (kitab's own topics), kafaah, ishrah, sadaq, walimah, qasm, khul (nikah), talaq (kitab's own
  topics), rajah (talaq). Validate with `fin4.py 7 927`. The index prints 247 for the topic «ما جاء في أن المطلقة ثلاثاً…»;
  the hadith index gives 274 (used).
  Done: باب الوقف (complete: intro + all topics, bab `waqf`, hadith 927–929, pages 5–25). باب الهبة (complete: intro + all topics, bab `hibah`, hadith 930–940, pages 26–70).
- Next: باب اللقطة (bab `luqatah` in vol 7, intro from page 71; hadith 941).
- When the author comments before «الكلام عليه من وجوه», fold it into the most related wajh
  (no wajh 0).
- toc.json headings were drafted before reading; when the scan's heading differs, the scan
  wins (fixed so far: «بيان كيفية إزالة المني…», «حكم تخليل اللحية…», «بيان فضيلة الوضوء…», «بيان ما لا يُستنجى به» and 4 more in qada-hajah; vol 2: «بعض خصائص النبي ﷺ…»; vol 3: «ثواب من صلى في اليوم والليلة من النوافل…», «حكم القصر في السفر», and shadda in 3 jamaah headings; vol 4: «وجوب المبادرة بقضاء دَين الميت», «ما يكفَّن فيه الرجل», «بيان أجر المرأة إذا تصدَّقت من بيت زوجها»; vol 5: «حكم الحج عمن نذره ثم مات قبل أدائه» (no comma), «الدواب التي تُقتل في الحل والحرم», «مشروعية الرمل في الطواف وبيان موضعه» (no comma), «حكم المبيت بمنى»; vol 6: «حكم شراء السلعة بثمن مؤجل», «من عمر أرضاً ليست لأحد فهو أحق بها» (no shadda)).
- Bab intros (author's text before the first topic) go in `toc.json` as `intro_th` on the bab
  (all babs so far, incl. miyah; shown on the บทนำ page).

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
- Extra sections (user request, linked from home "หมวดเสริม", not in the tab bar):
  `#intros` บทนำ — every kitab intro (`kitabs[].intro_th`) and bab intro (`intro_th`), collapsible,
  deep link `#intro-<vol>-<babid>` (TOC bab cards link to it); `#glossary` อภิธานศัพท์ — all `vocab`
  merged across entries (deduped by Arabic without harakat), searchable, grouped by first letter,
  each term linking back to its hadith pages.
- **Light theme only** (do not auto-switch to dark). Colors:
  green #2E5641 (dark #1F3D2D, soft #EAEDDC), gold #8A5A16 (line #A8752B, soft #FBEFD9),
  ground #F8F2E7, cards #FFFCF6, ink #2A231D, muted #6B5F52, lines #E8DDCB.
- Fonts: Noto Sans Thai + Noto Naskh Arabic.
- Stack: Next.js or Astro static site on Vercel, reading `vol*/entries/*.json` at build time.

## Note

The book is under copyright (author and publisher). The user reports that permission to publish has been obtained (2026-11-08).

## Published link

- Private claude.ai artifact: https://claude.ai/artifact/1zDYc7mTGgFRKgGXevYjyW (sharing is set by the user from the page's Share menu).
- To update after new batches: `python tools/build_preview.py`, then `python tools/build_artifact.py`, then publish
  `site/artifact.html` with the Artifact tool, passing the URL above as `url` (keeps the same link).
