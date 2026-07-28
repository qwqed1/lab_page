<script setup>
const route = useRoute()
const showCookieNotice = computed(() => (
  !route.path.startsWith('/cart') &&
  !route.path.startsWith('/personal-account') &&
  !route.path.startsWith('/demo-result') &&
  !route.path.startsWith('/materials-for-doctors')
))
</script>

<template>
  <NuxtPage />
  <CookieNotice v-if="showCookieNotice" />
</template>
