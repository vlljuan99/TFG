import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  base: '/openmonitor/',
  server: {
    port: 5173,
  },
})
