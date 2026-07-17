<script setup>
const handleHome = () => navigateTo('/')
</script>

<template>
  <Error404Page @home="handleHome" />
</template>
