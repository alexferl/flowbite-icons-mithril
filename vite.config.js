import { resolve } from "path";
import { defineConfig } from "vite";

export default defineConfig({
  build: {
    lib: {
      entry: {
        outline: resolve(__dirname, "lib/outline/index.js"),
        solid: resolve(__dirname, "lib/solid/index.js"),
      },
      name: "Flowbite Icons Mithril",
      fileName: "[name]/index",
    },
  },
});
