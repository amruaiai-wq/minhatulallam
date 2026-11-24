// Reads every volume's toc.json and entries/*.json (the same merge as tools/build_preview.py).
import fs from "node:fs";
import path from "node:path";

export type Hadith = { no: number; matn_ar: string; translation_th: string; grade_th: string };
export type Section = { wajh: number; type: string; heading_ar: string | null; heading_th: string; points_th: string[] };
export type Entry = {
  id: string; volume: number; bab: string; topic_ar: string; topic_th: string; pages: [number, number];
  hadith: Hadith[]; key_rulings_th: string[]; vocab?: { ar: string; th: string }[]; sections: Section[]; tags_th?: string[];
};
export type Topic = { ar: string; th?: string; page: number; hadith_nos: number[] };
export type Bab = { id: string; ar: string; th: string; page: number; kitab: string; volume: number; intro_th?: string[]; topics: Topic[] };
export type KitabIntro = { id: string; ar: string; th?: string; volume: number; intro_th: string[] };

const ROOT = path.resolve(process.cwd(), "..");
const read = (p: string) => JSON.parse(fs.readFileSync(p, "utf-8"));

const vols = fs.readdirSync(ROOT).filter((d) => /^vol\d+$/.test(d)).sort((a, b) => +a.slice(3) - +b.slice(3));
export const babs: Bab[] = [];
export const kitabIntros: KitabIntro[] = [];
export let entries: Entry[] = [];
export let TOTAL = 0;
for (const v of vols) {
  const toc = read(path.join(ROOT, v, "toc.json"));
  for (const b of toc.babs) babs.push({ ...b, kitab: b.kitab || "taharah", volume: toc.volume });
  for (const k of toc.kitabs || []) if (k.intro_th) kitabIntros.push({ ...k, volume: toc.volume });
  TOTAL = Math.max(TOTAL, toc.hadith_range[1]);
  const dir = path.join(ROOT, v, "entries");
  for (const f of fs.readdirSync(dir)) if (f.endsWith(".json")) entries.push(read(path.join(dir, f)));
}
entries.sort((a, b) => a.hadith[0].no - b.hadith[0].no);

export const KNAME: Record<string, string> = { taharah: "กิตาบฏอฮาเราะฮ์", hayd: "กิตาบอัลหัยฎ์", salah: "กิตาบอัศเศาะลาฮ์", janaiz: "กิตาบอัลญะนาอิซ", zakah: "กิตาบอัซซะกาฮ์", siyam: "กิตาบอัศศิยาม", hajj: "กิตาบอัลหัจญ์", buyu: "กิตาบอัลบุยูอ์", nikah: "กิตาบอันนิกาห์", talaq: "กิตาบอัฏเฏาะลาก", jinayat: "กิตาบอัลญินายาต", hudud: "กิตาบอัลหุดูด", jihad: "กิตาบอัลญิฮาด", atimah: "กิตาบอัลอัฏอิมะฮ์", ayman: "กิตาบอัลอัยมานวันนุซูร", qada: "กิตาบอัลเกาะฎออ์", itq: "กิตาบอัลอิตก์" };
export const KSHORT: Record<string, string> = { taharah: "ฏอฮาเราะฮ์", hayd: "อัลหัยฎ์", salah: "อัศเศาะลาฮ์", janaiz: "อัลญะนาอิซ", zakah: "อัซซะกาฮ์", siyam: "อัศศิยาม", hajj: "อัลหัจญ์", buyu: "อัลบุยูอ์", nikah: "อันนิกาห์", talaq: "อัฏเฏาะลาก", jinayat: "อัลญินายาต", hudud: "อัลหุดูด", jihad: "อัลญิฮาด", atimah: "อัลอัฏอิมะฮ์", ayman: "อัลอัยมาน", qada: "อัลเกาะฎออ์", itq: "อัลอิตก์" };

const babById = new Map(babs.map((b) => [b.volume + ":" + b.id, b]));
export const babOf = (e: Entry) => babById.get(e.volume + ":" + e.bab)!;
export const nos = (e: Entry) => e.hadith.map((h) => h.no);
export const label = (e: Entry) => { const n = nos(e); return n.length > 1 ? n[0] + "–" + n[n.length - 1] : String(n[0]); };
export const slug = (e: Entry) => String(e.hadith[0].no);
export const BASE = import.meta.env.BASE_URL.replace(/\/?$/, "/");
export const url = (p = "") => BASE + p;
export const topicUrl = (e: Entry) => url("h/" + slug(e) + "/");
export const strip = (s: string) => s.replace(/[ً-ٰٟ]/g, "");

export const KITABS = [
  { ar: "كتاب الطهارة", th: "ความสะอาด", ids: ["taharah", "hayd"] },
  { ar: "كتاب الصلاة", th: "การละหมาด", ids: ["salah"] },
  { ar: "كتاب الجنائز", th: "ศพและการจัดการ", ids: ["janaiz"] },
  { ar: "كتاب الزكاة", th: "ซะกาต", ids: ["zakah"] },
  { ar: "كتاب الصيام", th: "การถือศีลอด", ids: ["siyam"] },
  { ar: "كتاب الحج", th: "ฮัจญ์", ids: ["hajj"] },
  { ar: "كتاب البيوع", th: "การซื้อขาย", ids: ["buyu"] },
  { ar: "كتاب النكاح", th: "การแต่งงาน", ids: ["nikah"] },
  { ar: "كتاب الطلاق", th: "การหย่า", ids: ["talaq"] },
  { ar: "كتاب الجنايات", th: "อาชญากรรมต่อชีวิต", ids: ["jinayat"] },
  { ar: "كتاب الحدود", th: "บทลงโทษหัดด์", ids: ["hudud"] },
  { ar: "كتاب الجهاد", th: "ญิฮาด", ids: ["jihad"] },
  { ar: "كتاب الأطعمة", th: "อาหาร", ids: ["atimah"] },
  { ar: "كتاب الأيمان والنذور", th: "การสาบานและการบนบาน", ids: ["ayman"] },
  { ar: "كتاب القضاء", th: "การตัดสินคดี", ids: ["qada"] },
  { ar: "كتاب العتق", th: "การปลดปล่อยทาส", ids: ["itq"] },
  { ar: "كتاب الجامع", th: "รวมเรื่องมารยาท" },
].map((k: { ar: string; th: string; ids?: string[] }) => {
  if (!k.ids) return { ...k, ready: false, done: 0, total: 0 };
  const es = entries.filter((e) => k.ids!.includes(babOf(e).kitab));
  const ts = babs.filter((b) => k.ids!.includes(b.kitab)).flatMap((b) => b.topics);
  const total = ts.length && ts.every((t) => t.hadith_nos.length) ? ts.reduce((a, t) => a + t.hadith_nos.length, 0) : 0;
  return { ...k, ready: es.length > 0, done: es.reduce((a, e) => a + e.hadith.length, 0), total };
});

export const tagCounts = () => {
  const c: Record<string, number> = {};
  for (const e of entries) for (const t of e.tags_th || []) c[t] = (c[t] || 0) + 1;
  return Object.keys(c).sort((a, b) => c[b] - c[a]);
};

export type Term = { ar: string; key: string; defs: string[]; src: Entry[] };
export const glossary: Term[] = (() => {
  const map = new Map<string, Term>();
  for (const e of entries) for (const v of e.vocab || []) {
    const k = strip(v.ar).replace(/[\sـ]+/g, " ").trim();
    let g = map.get(k);
    if (!g) map.set(k, (g = { ar: v.ar, key: k.replace(/^ال/, "").replace(/^[آأإٱ]/, "ا"), defs: [], src: [] }));
    if (!g.defs.includes(v.th)) g.defs.push(v.th);
    if (!g.src.includes(e)) g.src.push(e);
  }
  return [...map.values()].sort((a, b) => a.key.localeCompare(b.key, "ar"));
})();

// Topic for each toc slot: bab topics are matched to entries by (volume, bab, first page).
const have = new Map(entries.map((e) => [e.volume + ":" + e.bab + ":" + e.pages[0], e]));
export const entryForTopic = (b: Bab, t: Topic) => have.get(b.volume + ":" + b.id + ":" + t.page);
