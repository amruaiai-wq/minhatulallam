// Light search index (loaded first). The long explanation text is in search-text.json, same order.
import { entries, babOf, KSHORT, label, slug, strip } from "../lib/data";
const n = (s: string) => strip(s.toLowerCase());
export function GET() {
  const list = entries.map((e) => {
    const b = babOf(e), m = e.hadith[0].matn_ar.match(/«([^»]+)»/);
    return {
      s: slug(e), l: label(e), k: KSHORT[b.kitab], b: b.th, t: e.topic_th, m: m ? m[1] : e.topic_ar,
      no: e.hadith.map((h) => h.no), r: e.key_rulings_th, g: (e.tags_th || []).join(" "),
      a: n(e.topic_ar + " " + e.hadith.map((h) => h.matn_ar).join(" ")),
      t2: n(e.topic_th),
    };
  });
  return new Response(JSON.stringify(list));
}
