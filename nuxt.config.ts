// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: false },
  css: [
    '~/assets/css/main.css',
    '~/assets/css/personal-account.css'
  ],
  app: {
    head: {
      title: 'Лаборатория ALEX LAB',
      htmlAttrs: {
        lang: 'ru'
      },
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Научно-исследовательский центр молекулярной генетики и биотехнологий ALEX LAB.' }
      ],
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: 'anonymous' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap' },
        { rel: 'preload', as: 'image', type: 'image/svg+xml', href: '/assets/figma-alex-logo.svg' },
        { rel: 'preload', as: 'image', type: 'image/svg+xml', href: '/assets/figma-cta-arrow.svg' },
        { rel: 'preload', as: 'image', type: 'image/svg+xml', href: '/assets/figma-search-icon.svg' },
        { rel: 'preload', as: 'image', type: 'image/svg+xml', href: '/assets/figma-demo-icon.svg' },
        { rel: 'preload', as: 'image', type: 'image/svg+xml', href: '/assets/figma-profile-icon.svg' },
        { rel: 'preload', as: 'image', type: 'image/svg+xml', href: '/assets/figma-about-icon.svg' }
      ]
    }
  }
})
