import { defineConfig } from "astro/config";

// Static site; one page per topic. Data is read from ../vol*/ at build time.
export default defineConfig({
  output: "static",
  trailingSlash: "always",
  build: { format: "directory" },
});
