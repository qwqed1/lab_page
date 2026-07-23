<template>
  <div class="page-layout">
    <!-- Header 72px — точно по макету, кнопка "Назад" -->
    <header class="header-nav">
      <NuxtLink :to="loginPath" class="back-link">
        <span class="back-arrow">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M15 18L9 12L15 6" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </span>
        Назад
      </NuxtLink>
    </header>

    <main class="main-content">
      <!-- Контейнер: 541px, gap 48px -->
      <div class="form-container">

        <!-- Заголовок блок: gap 16px -->
        <div class="title-block">
          <!-- 42px, Roboto Regular, center -->
          <h1 class="page-title">Восстановление доступа</h1>
          <!-- 18px, Roboto Regular, opacity 0.5, center -->
          <p class="page-subtitle">Введите электронную почту, которую указывали при оформлении заказа</p>
        </div>

        <!-- Форма: gap 48px -->
        <form v-if="!sent" @submit.prevent="handleSubmit" class="recover-form" novalidate>

          <!-- E-mail поле -->
          <div class="field-group">
            <label for="recover-email" class="field-label">E-mail</label>
            <input
              id="recover-email"
              type="email"
              v-model="email"
              class="field-input"
              placeholder="max@inmuntex.com"
              autocomplete="email"
              required
            />
          </div>

          <!-- Кнопка Далее: 541×72px, bg #000, text #fff -->
          <button type="submit" class="btn-primary" :disabled="loading">
            <span>{{ loading ? 'Отправляем...' : 'Далее' }}</span>
            <span class="btn-icon-wrap">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="#FFFFFF" stroke-width="2"/>
                <path d="M10 8L14 12L10 16" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </button>

        </form>

        <!-- Экран «Проверьте почту» — отдельный state по макету -->
        <div v-else class="check-email-block">
          <!-- Title: 42px Roboto Regular center -->
          <h1 class="page-title check-title">Проверьте почту</h1>
          <!-- Subtitle: 18px Roboto Regular opacity 0.5 center -->
          <p class="page-subtitle check-subtitle">На вашу почту пришли новые данные для входа</p>
          <!-- Кнопка Войти -->
          <NuxtLink :to="loginPath" class="btn-primary check-btn">
            <span>Войти</span>
            <span class="btn-icon-wrap">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="#FFFFFF" stroke-width="2"/>
                <path d="M10 8L14 12L10 16" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </NuxtLink>
        </div>

      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from '#app'

const route = useRoute()
const loginPath = route.path.startsWith('/cart') ? '/cart/login' : '/login'

const email = ref('')
const loading = ref(false)
const sent = ref(false)

const handleSubmit = async () => {
  loading.value = true
  await new Promise(r => setTimeout(r, 800))
  loading.value = false
  sent.value = true
}
</script>

<style scoped>
/* ─── Layout ────────────────────────────────────────── */
.page-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
}

/* ─── Header: 72px, bg #fff, border-bottom #dfdfdf ─── */
.header-nav {
  width: 100%;
  height: 72px;
  background-color: #ffffff;
  border-bottom: 1px solid #dfdfdf;
  display: flex;
  align-items: center;
  padding: 24px 32px;
  position: sticky;
  top: 0;
  z-index: 10;
  box-sizing: border-box;
}

.back-link {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: 'Helvetica', Arial, sans-serif;
  font-size: 17px;
  font-weight: 400;
  color: #000000;
  text-decoration: none;
}

.back-link:hover {
  opacity: 0.7;
}

.back-arrow {
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

/* ─── Main ───────────────────────────────────────────── */
.main-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

/* ─── Форм-контейнер: 541px, gap 48px ────────────────── */
.form-container {
  width: 541px;
  display: flex;
  flex-direction: column;
  gap: 48px;
}

@media (max-width: 1024px) {
  .page-layout {
    height: 100dvh !important;
    max-height: 100dvh !important;
    overflow-x: hidden !important;
    overflow-y: auto !important;
    -webkit-overflow-scrolling: touch;
  }
}

@media (max-width: 600px) {
  .form-container {
    width: 100%;
    gap: 40px;
  }
}

/* ─── Title block: gap 16px ──────────────────────────── */
.title-block {
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: center;
}

/* 42px Roboto Regular, center */
.page-title {
  font-family: 'Roboto', sans-serif;
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  line-height: 1.166;
  text-align: center;
  margin: 0;
}

/* 18px Roboto Regular, opacity 0.5, center */
.page-subtitle {
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
  font-weight: 400;
  color: #000000;
  opacity: 0.5;
  text-align: center;
  line-height: 1.55;
  margin: 0;
  max-width: 398px;
}

/* ─── Форма: gap 48px ─────────────────────────────────── */
.recover-form {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

/* ─── Поле ───────────────────────────────────────────── */
.field-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
  width: 100%;
}

.field-label {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: #000000;
  line-height: 1.1875;
}

.field-input {
  width: 100%;
  height: 61px;
  border: 1px solid #dddddd;
  background-color: transparent;
  padding: 0 24px;
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
  font-weight: 400;
  color: #000000;
  outline: none;
  box-sizing: border-box;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
  border-radius: 0;
  appearance: none;
  -webkit-appearance: none;
}

.field-input::placeholder {
  color: #000000;
  opacity: 0.4;
}

.field-input:focus {
  border-color: #000000;
  box-shadow: 0 0 0 1px #000000;
}

/* ─── Кнопка Далее: 541×72px, bg #000 ────────────────── */
.btn-primary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 72px;
  background-color: #000000;
  color: #ffffff;
  border: none;
  padding: 0 32px;
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
  font-weight: 400;
  cursor: pointer;
  box-sizing: border-box;
  transition: opacity 0.2s ease;
  text-decoration: none;
}

.btn-primary:hover {
  opacity: 0.9;
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-icon-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

/* ─── Check-email state ──────────────────────────────── */
.check-email-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.check-title {
  /* наследует .page-title */
}

.check-subtitle {
  /* наследует .page-subtitle */
  max-width: 228px;
}

.check-btn {
  margin-top: 32px;
  width: 100%;
}
</style>
