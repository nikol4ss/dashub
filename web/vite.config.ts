import path from 'node:path'
import tailwindcss from '@tailwindcss/vite'
import vue from '@vitejs/plugin-vue'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [vue(), tailwindcss()],
  build: {
        outDir: '../web/dist',
        emptyOutDir: true,
        rollupOptions: {
            input: './index.html',
        },
    },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
})
