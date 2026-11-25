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
  Done: باب الوقف (complete: intro + all topics, bab `waqf`, hadith 927–929, pages 5–25). باب الهبة (complete: intro + all topics, bab `hibah`, hadith 930–940, pages 26–70). باب اللقطة (complete: intro + all topics, bab `luqatah`, hadith 941–946, pages 71–93). باب الفرائض (complete: intro + all topics, bab `faraid`, hadith 947–959, pages 94–138). باب الوصايا (complete: intro + all topics, bab `wasaya`, hadith 960–967, pages 139–163). باب الوديعة (complete: intro + all topics, bab `wadiah`, hadith 968, pages 164–168). كتاب النكاح kitab intro (on the `nikah` entry in `kitabs`, p. 169); all the kitab's own topics complete (bab `nikah`, no separate bab intro, hadith 969–1003, pages 170–276). باب الكفاءة والخيار (complete: intro + all topics, bab `kafaah`, hadith 1004–1017, pages 277–320; the Umar athar on the عنين after h1017 is unnumbered, kept in h1015-1017). باب عشرة النساء (complete: intro + all topics, bab `ishrah`, hadith 1018–1031, pages 321–369). باب الصداق (complete: intro + all topics, bab `sadaq`, hadith 1032–1043, pages 370–405). باب الوليمة (complete: intro + all topics, bab `walimah`, hadith 1044–1060, pages 406–454). باب القسم (complete: intro + all topics, bab `qasm`, hadith 1061–1070, pages 455–487). باب الخلع (complete: intro + its one topic, bab `khul`, hadith 1071–1074, pages 488–506). كتاب الطلاق kitab intro (on the `talaq` entry in `kitabs`, pp. 507–508); all the kitab's own topics complete (bab `talaq`, no separate bab intro, hadith 1075–1092, pages 509–588). باب الرجعة (complete: intro + its one topic, bab `rajah`, hadith 1093–1094, pages 589–596). **Volume 7 complete.**
- Volume 8 (`sources/vol8.pdf`, 574 pages, hadith 1095–1265): `vol8/toc.json` built from the book's
  فهرس الموضوعات (pp. 569–574). Kitabs talaq (cont.) / jinayat (p. 211) / hudud (p. 373); babs ila, lian, iddah, rada,
  nafaqat, hadanah (talaq), jinayat (kitab's own topics), diyat, qasamah, baghy, murtadd (jinayat), zina, qadhf, sariqah,
  sharib, tazir (hudud; the kitab has no topics of its own). Validate with `fin4.py 8 1095`; write entries with `w8h.py`.
  The prototype's KITABS list now has ids `jinayat` and `hudud`.
  Done: باب الإيلاء والظهار والكفارة (complete: intro + all topics, bab `ila`, hadith 1095–1100, pages 5–23). باب اللعان (complete: intro + all topics, bab `lian`, hadith 1101–1109, pages 24–53). باب العدة والإحداد والاستبراء (complete: intro + all topics, bab `iddah`, hadith 1110–1133, pages 54–124). باب الرضاع (complete: intro + all topics, bab `rada`, hadith 1134–1144, pages 125–155). باب النفقات (complete: intro + all topics, bab `nafaqat`, hadith 1145–1157, pages 156–188). باب الحضانة (complete: intro + all topics, bab `hadanah`, hadith 1158–1164, pages 189–210). كتاب الجنايات kitab intro (on the `jinayat` entry in `kitabs`, p. 211); all the kitab's own topics complete (bab `jinayat`, no separate bab intro, hadith 1165–1183, pages 212–274). باب الديات (complete: intro + all topics, bab `diyat`, hadith 1184–1196, pages 275–320). باب دعوى الدم والقسامة (complete: intro + all topics, bab `qasamah`, hadith 1197–1198, pages 321–333). باب قتال أهل البغي (complete: intro + all topics, bab `baghy`, hadith 1199–1204, pages 334–350). باب قتال الجاني وقتل المرتد (complete: intro + all topics, bab `murtadd`, hadith 1205–1211, pages 351–371; its first topic heading «ما جاء فيمن قتل دون ماله» recurs in bab `tazir` (p. 548), so fin4 matches topics by (bab, heading)). كتاب الحدود kitab intro (on the `hudud` entry in `kitabs`, pp. 373–374). باب حد الزاني (complete: intro pp. 374–375 + all topics, bab `zina`, hadith 1212–1229, pages 376–437). باب حد القذف (complete: intro + all topics, bab `qadhf`, hadith 1230–1234, pages 438–450). باب حد السرقة (complete: intro pp. 451–452 + all topics, bab `sariqah`, hadith 1235–1247, pages 453–496). باب حد الشارب وبيان المسكر (complete: intro + all topics, bab `sharib`, hadith 1248–1259, pages 497–533). باب التعزير وحكم الصائل (complete: intro + all topics, bab `tazir`, hadith 1260–1265, pages 534–553). **Volume 8 complete.**
- Next (user's plan, 2026-11-23): **review and polish vols 1–8 before any new volume.** Step 1–2 done (audit + style guide, applied). Step 3 in progress: grade_th standardized (all 1262, `docs/grades_review.md`); vol 1 fully polished (scan check for miyah/aniyah/najasah). Fast pass (user chose 2026-11-24) done for vols 2–8: all grade_th now `head (note)` with nothing after the paren (`tools/grade_merge.py`, check `tools/grade_issues.py <vol>` → empty), dialogue quotes in « », «ﷺ» followed by a space. Tools: `tools/polish.py`, `tools/polish_scan.py`, `tools/fin4.py`. The 7 "views without verdict" entries checked against the scan (2026-11-24): verdict or "(ผู้แต่งไม่ได้ชี้ขาด)" added; h682/h1021 had no real dispute. หุกุม → ข้อตัดสิน (177). v7 h1077 long paragraphs split. Polish pass per bab: author's verdict as ผู้แต่ง: «…», grade parenthesis short and specific, quotes in « », scan check. Edits via scratch `polish.py` (old/new pairs, each must match once). Full polish pass (user 2026-11-24: "no time limit, maximum quality") done for all 8 vols (2026-11-24): **vol 4 complete**, **vol 2 complete**, **vol 3 complete** (Thai-in-« » verdicts in vol 3 jamaah/musafir and 6 vol 4 entries replaced with the Arabic), **vols 6, 7, 8 complete** (remaining tarjih + grades ≤115 chars), **vol 1 babs 4–8 complete** (41 tarjih; 29 located via the OCR file, 7 sampled against the scan and all matched; 12 read from the scan), **vol 5 complete** (h742 gaps filled from the scan; per-page density check: all vols 800–1000 chars/page, so no volume lost content systematically) (2026-11-24; vol 4 entries were already near-full length, so the pass was verdicts/grades/style, not missing content). Per bab: `tools/verdicts.py <vol> <bab>` lists verdict points lacking the author's Arabic → read those scan pages → `ผู้แต่ง: «<Arabic>» <Thai>`; shorten grades >140 chars; `tools/show.py` prints an entry. Scholar quotes « » → ( ) done globally by `tools/scholar_quotes.py` (822). Step 4 (Astro site in `web/`) built and tested; deploy needs the user's Vercel account. Vol 9 (`sources/vol9.pdf`, كتاب الجهاد) waits; the artifact is now 3.4 MB (build_artifact.py gzips the data, 2026-11-24), so vols 9+ fit (16 MB limit).
- Volume 9 (`sources/vol9.pdf`, 614 pages, hadith 1266–1446): `vol9/toc.json` built from the book's
  فهرس الموضوعات (pp. 607–614). Kitabs jihad (p. 5) / atimah (p. 172) / ayman (p. 325) / qada (p. 406) / itq (p. 532);
  babs jihad (kitab's own topics), jizyah, sabq (jihad), atimah (kitab's own topics), sayd, adahi, aqiqah (atimah),
  ayman (kitab's own topics), qada (kitab's own topics), shahadat, dawa (qada), itq (kitab's own topics), mudabbar (itq).
  Kitab title pages are approximate until each kitab is read. The index prints 339 for «من نذر الصلاة في المكان المفضول…»
  (must be 393–402; 396 provisional). Write entries with `tools/w9.py BATCH.py`, validate with `fin4.py 9 1266`.
  The prototype and web KITABS lists now have ids jihad / atimah / ayman / qada / itq.
  Done: كتاب الجهاد kitab intro (pp. 5–7, on the `jihad` entry in `kitabs`); all the kitab's own topics complete (bab `jihad`, hadith 1266–1314, pages 8–127); باب الجزية والهدنة (complete: intro pp. 128–129 + all topics, bab `jizyah`, hadith 1315–1322, pages 130–150). باب السبق والرمي (complete: intro p. 151 + all topics, bab `sabq`, hadith 1323–1327, pages 152–170). **كتاب الجهاد complete.** كتاب الأطعمة kitab intro (pp. 171–172, on the `atimah` entry in `kitabs`; kitab page corrected to 171); all the kitab's own topics complete (bab `atimah`, hadith 1328–1340, pages 173–213). باب الصيد والذبائح (complete: intro pp. 214–215 + all topics, bab `sayd`, hadith 1341–1354, pages 216–266). باب الأضاحي (complete: intro pp. 267–268 + all topics, bab `adahi`, hadith 1355–1363, pages 269–302). باب العقيقة (complete: intro pp. 303–304 + all topics, bab `aqiqah`, hadith 1364–1368, pages 305–322). **كتاب الأطعمة complete.** كتاب الأيمان والنذور starts p. 323 (kitab page corrected). Vol 9 entries are denser than vols 1–8 (avg ~2700 section chars/topic vs 2800–4200) — fine, the jihad topics are short in the book.
- When the author comments before «الكلام عليه من وجوه», fold it into the most related wajh
  (no wajh 0).
- toc.json headings were drafted before reading; when the scan's heading differs, the scan
  wins (fixed so far: «بيان كيفية إزالة المني…», «حكم تخليل اللحية…», «بيان فضيلة الوضوء…», «بيان ما لا يُستنجى به» and 4 more in qada-hajah; vol 9: «إباحة لحم الضبِّ», «النهي عن قتل الضِّفْدِع», «من آداب الذَّبح», «السنّ المعتبر في الأضحية» (harakat as in the scan); vol 2: «بعض خصائص النبي ﷺ…»; vol 3: «ثواب من صلى في اليوم والليلة من النوافل…», «حكم القصر في السفر», and shadda in 3 jamaah headings; vol 4: «وجوب المبادرة بقضاء دَين الميت», «ما يكفَّن فيه الرجل», «بيان أجر المرأة إذا تصدَّقت من بيت زوجها»; vol 5: «حكم الحج عمن نذره ثم مات قبل أدائه» (no comma), «الدواب التي تُقتل في الحل والحرم», «مشروعية الرمل في الطواف وبيان موضعه» (no comma), «حكم المبيت بمنى»; vol 6: «حكم شراء السلعة بثمن مؤجل», «من عمر أرضاً ليست لأحد فهو أحق بها» (no shadda); vol 7: «النهي عن التنفس في الإناء أو النفخ فيه»).
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
- **Style guide (approved 2026-11-23, full table in `docs/style_guide.md`; applied to vols 1–8 by
  `tools/style_fix.py`, check with `tools/audit.py`):** ท่านเราะซูล / เราะซูลุลลอฮ์ · สุนนะฮ์ ·
  ศ่อฮีห์ = grade, เศาะฮีห์ = book title (เศาะฮีห์บุคอรีย์, เศาะฮีห์ทั้งสอง) · หะซัน = grade, หะสัน = name ·
  อุละมาอ์ (นักหะดีษ, นักภาษา) · ฟุเกาะฮาอ์ · อิจญ์มาอ์ (not มติ) · ฟัรฎู/วาญิบ follow the Arabic word ·
  รายงาน / รายงานโดย (not บันทึกโดย) · (บุคอรีย์และมุสลิม) for متفق عليه · บุคอรีย์ (no อัล) ·
  อัลหาฟิซ for Ibn Hajar · อิบนุตัยมิยะฮ์ · วุฎูอ์ / ทำวุฎูอ์ · ข้อตัดสิน (not หุก่ม) · ผู้แต่ง = al-Fawzan only, ชัยค์ for other
  shaykhs, ผู้เขียน «…» for authors of other books · names with a space: «อับดุลลอฮ์ บิน อัมร์» (บินต์ joined) ·
  « » for the Prophet's words and quoted text, ( ) for scholars' quotations · ﷺ after every mention in
  hadith translations and at the first mention in each explanation point · grade_th: a fixed head word
  (ศ่อฮีห์ · หะซัน · ฎออีฟ · ฎออีฟมาก · เมาฎูอ์ · เมากูฟ · มุรสัล · มีข้อขัดแย้ง) + a short parenthesis ·
  author's verdict as ผู้แต่ง: «الراجح…» + Thai, or "(ผู้แต่งไม่ได้ชี้ขาด)" · key rulings 3–5 (fewer only
  when the source has fewer points) · paragraphs ≤ ~700 chars.
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
- Stack: **Astro 5.18.2 static site in `web/`** (built 2026-11-24, see `web/README.md`): one page per topic at `/h/<first hadith no.>/`, search via `/search.json` + lazy `/search-text.json`. Deploy on Vercel with Root Directory `web`. The artifact (`site/artifact.html`) stays as a private preview.

## Note

The book is under copyright (author and publisher). The user reports that permission to publish has been obtained (2026-11-08).

## Published link

- Private claude.ai artifact: https://claude.ai/artifact/1zDYc7mTGgFRKgGXevYjyW (sharing is set by the user from the page's Share menu).
- To update after new batches: `python tools/build_preview.py`, then `python tools/build_artifact.py`, then publish
  `site/artifact.html` with the Artifact tool, passing the URL above as `url` (keeps the same link).
