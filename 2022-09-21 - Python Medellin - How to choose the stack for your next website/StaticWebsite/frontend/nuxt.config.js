import fs from 'fs'
import axios from 'axios'


export default {
  server: {
    port: 3000, // default: 3000
    host: '0.0.0.0', // default: localhost,
    timing: false
  },

  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Python Medellin',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'Icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },


  env: {},

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/assets/styles/globals/base'
  ],

  styleResources: {
    scss: [
      '~assets/styles/scss/main'
    ]
  },

  googleFonts: {
    display: 'swap',
    families: {
      Montserrat: {
        wght: [400, 600, 700],
      },
      'Old+Standard+TT': {
        wght: [400],
        ital: [400],
      },
    }
  },

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/stylelint
    '@nuxtjs/stylelint-module',
    // Global SCSS
    '@nuxtjs/style-resources',
    // Fonts
    '@nuxtjs/google-fonts',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa'
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: '/',
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en',
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},

  // Generate config
  router: {
    async extendRoutes(routes, resolve) {
      // Removing vue pages
      while (routes.length > 0) {
        routes.pop()
      }

      const response = await axios.get(`${process.env.API_URL}/api/v2/pages/?fields=*`)
      for (const page of response.data.items) {
        const path = resolve(__dirname, `pages/${page.meta.type.split('.')[1]}/index.vue`)
        const defaultPath = resolve(__dirname, `pages/DefaultPage.vue`)
        const component = fs.existsSync(path) ? path : defaultPath;
        const pageResponse = await axios.get(`${process.env.API_URL}/api/v2/pages/${page.id}/?fields=*`)
        routes.push({
          name: page.id,
          path: `${page.meta.relative_url}`,
          component,
          props: {
            page: pageResponse.data,
          },
        })
      }
    }
  }
}
