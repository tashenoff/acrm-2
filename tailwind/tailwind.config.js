module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  purge: {
      enabled: false, //true for production build
      content: [
          '../**/templates/*.html',
          '../**/templates/**/*.html'
      ]
  },
  darkMode: 'class',
  theme: {
      
    container: {
        screens: {
          sm: "100%",
          md: "100%",
          lg: "1140px",
          xl: "1140px"
        }
      },
  
      extend: {
        zIndex: {
          '60': '60',
        }
      },
      colors: {
        primary: '#010101',
        darkLight: '#0c162d',
        primarylight: '#9361e2',
        secondary: '#e045e6',
        green: '#47E189',
        black: '#333',
        white: '#fff',
        red: '#e045e6',
        gray: '#F4F4F4',
        blueLight: '#c3d9f6'
      }
  },
  variants: {},
  plugins: [],
}