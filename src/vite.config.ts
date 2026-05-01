import { defineConfig } from 'vite';
import path from 'path';
import vue from '@vitejs/plugin-vue';
import fullReload from 'vite-plugin-full-reload';

export default defineConfig({
  plugins: [
    fullReload(['./templates/**/*.html', '*/templates/**/*.html']),
    vue(),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'assets/js'),
    },
  },
  build: {
    outDir: 'static/build',
    emptyOutDir: true,
    manifest: true,
    rollupOptions: {
      input: [
        'assets/js/entrypoints/app.ts',

        'assets/js/entrypoints/development/javascript-test.ts',

        'assets/css/app.css',
      ],
    },
  },
});
