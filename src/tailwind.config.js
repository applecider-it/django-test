/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'templates/**/*.html',
    '*/templates/**/*.html',
    '*/forms.py',
    'assets/**/*.{ts,vue}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
