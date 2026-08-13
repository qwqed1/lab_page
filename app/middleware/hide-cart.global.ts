export default defineNuxtRouteMiddleware((to) => {
  if (to.path === '/cart' || to.path.startsWith('/cart/')) {
    return navigateTo('/', { redirectCode: 302 })
  }
})
