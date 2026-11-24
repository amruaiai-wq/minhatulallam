// Small list of every topic, for the home "continue" card and the bookmarks page.
import { entries, babOf, KNAME, label, slug, nos } from "../lib/data";
export function GET() {
  const list = entries.map((e) => { const b = babOf(e), n = nos(e); return { s: slug(e), l: label(e), end: n[n.length - 1], k: KNAME[b.kitab], b: b.th, t: e.topic_th }; });
  return new Response(JSON.stringify(list));
}
