module.exports = {
  presets: [
    require('frappe-ui/src/utils/tailwind.config')
  ],
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        primary:"#84754E",
        secondary:"#D8E0E1",
        heading:"#253031",
        body_text:"#596263",
        transparent:"transparent"
      }
    },
  },
  plugins: [],
}
