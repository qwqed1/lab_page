<script setup>
const isVisible = ref(true)

const acceptCookies = () => {
  isVisible.value = false
}
</script>

<template>
  <Transition name="cookie-notice" appear>
    <aside v-if="isVisible" class="cookie-notice" aria-label="Уведомление об использовании cookie">
      <p class="cookie-notice__text">
        Сайт использует cookie с целью анализа поведения посетителей для улучшения Сайта.
        Продолжая пользоваться Сайтом, вы соглашаетесь на использование файлов cookie
        в соответствии с нашими
        <a href="#" @click.prevent>Cookie-правилами.</a>
      </p>

      <button class="cookie-notice__accept" type="button" @click="acceptCookies">
        Хорошо
      </button>
    </aside>
  </Transition>
</template>

<style scoped>
.cookie-notice {
  position: fixed;
  right: 27px;
  bottom: 27px;
  z-index: 1000;
  width: min(684px, calc(100vw - 32px));
  height: 172px;
  padding: 24px;
  border: 1px solid #dfdfdf;
  background: #fff;
  -webkit-backdrop-filter: blur(50px);
  backdrop-filter: blur(50px);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 24px;
  color: #000;
  font-family: 'Roboto', Arial, sans-serif;
}

.cookie-notice__text {
  width: 100%;
  margin: 0;
  font-size: 16px;
  font-weight: 400;
  line-height: 19px;
}

.cookie-notice__text a {
  color: inherit;
  text-decoration: underline;
  text-underline-offset: 1px;
}

.cookie-notice__accept {
  width: 108px;
  height: 43px;
  padding: 12px 24px;
  border: 0;
  border-radius: 0;
  background: #000;
  color: #fff;
  font: 400 16px/19px 'Roboto', Arial, sans-serif;
  text-align: left;
  cursor: pointer;
}

.cookie-notice__accept:hover {
  background: #1a1a1a;
}

.cookie-notice__accept:focus-visible {
  outline: 2px solid #000;
  outline-offset: 3px;
}

.cookie-notice-enter-active,
.cookie-notice-leave-active {
  transition: transform 420ms cubic-bezier(0.16, 1, 0.3, 1), opacity 260ms ease;
}

.cookie-notice-enter-from,
.cookie-notice-leave-to {
  opacity: 0;
  transform: translateX(105%);
}

@media (max-width: 700px) {
  .cookie-notice {
    right: 0;
    bottom: 0;
    width: 100%;
    height: auto;
    padding: 20px;
    gap: 20px;
  }

  .cookie-notice__text {
    font-size: 14px;
    line-height: 17px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cookie-notice-enter-active,
  .cookie-notice-leave-active {
    transition: opacity 160ms ease;
  }

  .cookie-notice-enter-from,
  .cookie-notice-leave-to {
    transform: none;
  }
}
</style>
