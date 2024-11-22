/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // Включаем поддержку темной темы
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        primary: '#141C22',
        secondary: '#3BC1CD',
      },
    },
  },
  plugins: [],
}
