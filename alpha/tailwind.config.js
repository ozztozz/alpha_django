/** @type {import('tailwindcss').Config} */
module.exports = {
  content:
  {
    files: [
      'main/templates/**/*.html',
      './node_modules/flowbite/**/*.js',
      'account/templates/**/*.html',
      'antrenor/templates/**/*.html',
    ],
    transform: (content) => content.replace(/taos:/g, ''),
    relative: true,
  },

  safelist: [
    '!duration-[0ms]',
    '!delay-[0ms]',
    'html.js :where([class*="taos:"]:not(.taos-init))'
  ],
  theme: {
    extend: {

    },

    plugins: [
      require('flowbite/plugin'),
      require('taos/plugin'),
      require("@designbycode/tailwindcss-text-shadow"),

    ],
  }
}