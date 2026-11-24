// Full explanation text for the "ทั้งหมด" filter, loaded lazily; array in the same order as search.json.
import { entries, strip } from "../lib/data";
export function GET() {
  const list = entries.map((e) => strip([...e.hadith.map((h) => h.translation_th), ...e.sections.flatMap((s) => s.points_th)].join(" ").toLowerCase()));
  return new Response(JSON.stringify(list));
}
