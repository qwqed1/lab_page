<script setup>
defineProps({
  error: {
    type: Object,
    required: true,
  },
})

const handleHome = () => clearError({ redirect: '/' })
</script>

<template>
  <Error404Page @home="handleHome" />
</template>
