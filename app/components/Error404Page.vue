<script setup>
defineEmits(['home'])

useHead({
  title: 'Ошибка 404 — ALEX2',
})
</script>

<template>
  <main class="error-page">
    <div class="error-page__shade" />

    <section class="error-page__content" aria-labelledby="error-title">
      <div class="error-page__heading">
        <h1 id="error-title">Ошибка 404</h1>
        <p>Вы попали на сайт ALEX2, но мы не смогли найти именно то, что вы искали</p>
      </div>

      <nav class="error-page__menu" aria-label="Навигация со страницы 404">
        <button class="error-page__item error-page__item--primary" type="button" @click="$emit('home')">
          <span>Вернутся на главную</span>
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <circle cx="12" cy="12" r="10" />
            <path d="m10 8 4 4-4 4" />
          </svg>
        </button>

        <NuxtLink class="error-page__item" to="/">
          <span>Блог</span>
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <circle cx="12" cy="12" r="10" />
            <path d="m10 8 4 4-4 4" />
          </svg>
        </NuxtLink>

        <NuxtLink class="error-page__item" to="/personal-account">
          <span>Личный кабинет</span>
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <circle cx="12" cy="12" r="10" />
            <path d="m10 8 4 4-4 4" />
          </svg>
        </NuxtLink>

        <NuxtLink class="error-page__item" to="/cart">
          <span>Корзина</span>
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <circle cx="12" cy="12" r="10" />
            <path d="m10 8 4 4-4 4" />
          </svg>
        </NuxtLink>
      </nav>
    </section>
  </main>
</template>

<style scoped>
.error-page {
  position: relative;
  width: 100%;
  height: 100vh;
  height: 100dvh;
  min-height: 600px;
  overflow: hidden;
  background: #78828a url('/assets/bg-404.png') center / cover no-repeat;
  font-family: 'Roboto', sans-serif;
}

.error-page__shade {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
}

.error-page__content {
  position: absolute;
  z-index: 1;
  top: 50%;
  left: 50%;
  display: flex;
  width: min(414px, calc(100% - 32px));
  flex-direction: column;
  align-items: center;
  gap: 64px;
  transform: translate(-50%, -50%);
  text-align: center;
}

.error-page__heading {
  display: flex;
  width: 100%;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  color: #fff;
}

.error-page__heading h1 {
  font-size: 42px;
  font-weight: 400;
  line-height: 49px;
}

.error-page__heading p {
  width: 400px;
  max-width: 100%;
  font-size: 21px;
  font-weight: 400;
  line-height: 20px;
}

.error-page__menu {
  display: flex;
  width: 100%;
  flex-direction: column;
  gap: 8px;
}

.error-page__item {
  display: flex;
  width: 100%;
  height: 72px;
  padding: 0 24px;
  align-items: center;
  justify-content: space-between;
  border: 1px solid #dfdfdf;
  border-radius: 0;
  background: #fff;
  color: #000;
  font: 400 21px/1 'Roboto', sans-serif;
  text-align: left;
  text-decoration: none;
  cursor: pointer;
  transition: background-color 160ms ease;
}

.error-page__item--primary {
  border-color: #000;
  background: #000;
  color: #fff;
}

.error-page__item:hover {
  background: #f5f5f5;
}

.error-page__item--primary:hover {
  background: #202020;
}

.error-page__item:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: -5px;
}

.error-page__item svg {
  width: 24px;
  height: 24px;
  flex: 0 0 24px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
}

.error-page__item path {
  stroke-linecap: round;
  stroke-linejoin: round;
}

@media (max-width: 1024px) {
  .error-page {
    min-height: 0;
    background-position: calc(50vw - 339px) -9px;
    background-size: 1927px 1084px;
  }

  .error-page__content {
    width: calc(100% - 32px);
    max-width: 388px;
  }

  .error-page__heading p {
    font-size: 20px;
    line-height: 18.5px;
  }

  .error-page__menu {
    gap: 0;
  }

  .error-page__item {
    height: 66px;
    font-size: 18px;
  }
}

@media (max-height: 599px) {
  .error-page {
    min-height: 520px;
  }

  .error-page__content {
    gap: 32px;
  }
}
</style>
