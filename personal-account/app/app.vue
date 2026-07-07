<template>
  <div class="app-container">
    <NuxtRouteAnnouncer />
    <NuxtPage />
  </div>
</template>

<style>
/* Корневой контейнер на весь экран */
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
