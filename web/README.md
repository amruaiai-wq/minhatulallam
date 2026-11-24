# เว็บไซต์ (Astro)

Static site built from `../vol*/toc.json` and `../vol*/entries/*.json`; it follows `design/prototype.html`.

```bash
cd web
npm install
npm run dev      # http://localhost:4321
npm run build    # -> web/dist (969 pages)
```

Pages: `/` home · `/toc/` · `/h/<first hadith no.>/` one page per topic · `/search/?q=…&f=all|ar|rul|tag` ·
`/saved/` · `/intros/#intro-<vol>-<bab>` · `/glossary/`.
Data files: `/topics.json` (home card, bookmarks), `/search.json` (light index), `/search-text.json`
(explanation text, loaded only when the "ทั้งหมด" filter needs it).
Bookmarks, reading mode and "continue reading" use the same localStorage keys as the prototype (`saved`, `mode`, `last`).

## Deploy on Vercel

1. Import the GitHub repository in Vercel.
2. Root Directory: `web`. The framework is detected as Astro (build `npm run build`, output `dist`).
3. Keep "Include files outside the root directory in the Build Step" on (default): the build reads `../vol*`.
