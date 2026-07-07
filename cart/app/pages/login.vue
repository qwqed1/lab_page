<template>
  <div class="page-layout">
    <!-- Header 72px — точно по макету -->
    <header class="header-nav">
      <NuxtLink to="/" class="back-link">
        <span class="back-arrow">
          <!-- chevron-left 24x24, stroke #000, strokeWidth 1.5 -->
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M15 18L9 12L15 6" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </span>
        На главную
      </NuxtLink>
    </header>

    <!-- Центрированный контент -->
    <main class="main-content">
      <!-- Контейнер 541px wide, gap 64px vertical -->
      <div class="form-container">

        <!-- Заголовок: 42px, Roboto Regular, center -->
        <h1 class="page-title">Добро пожаловать!</h1>

        <!-- Форма: gap 48px между группами -->
        <form @submit.prevent="handleLogin" class="login-form" novalidate>

          <!-- Группа инпутов: gap 24px -->
          <div class="inputs-group">

            <!-- E-mail -->
            <div class="field-group">
              <!-- Label: 16px, Roboto Regular, #000 -->
              <label for="login-email" class="field-label">E-mail</label>
              <!-- Input: 541×61px, border #dddddd, padding 24px, 18px text -->
              <input
                id="login-email"
                type="email"
                v-model="email"
                class="field-input"
                placeholder="max@inmuntex.com"
                autocomplete="email"
                required
              />
            </div>

            <!-- Пароль -->
            <div class="field-group">
              <label for="login-password" class="field-label">Пароль</label>
              <input
                id="login-password"
                type="password"
                v-model="password"
                class="field-input"
                placeholder="*************"
                autocomplete="current-password"
                required
              />
            </div>

          </div>

          <!-- Кнопки: gap 4px — точно по макету -->
          <div class="actions-group">

            <!-- Кнопка Войти: 541×72px, bg #000, text #fff, 18px Roboto -->
            <button type="submit" class="btn-primary" :disabled="loading">
              <span>{{ loading ? 'Входим...' : 'Войти' }}</span>
              <!-- Circle arrow icon 24×24 -->
              <span class="btn-icon-wrap">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="12" cy="12" r="10" stroke="#FFFFFF" stroke-width="2"/>
                  <path d="M10 8L14 12L10 16" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </span>
            </button>

            <!-- Кнопка Забыли пароль: 541×72px, bg #fff, border rgba(0,0,0,0.1), text #000, 18px -->
            <NuxtLink to="/recover" class="btn-secondary">
              <span>Забыли пароль?</span>
              <span class="btn-icon-wrap">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="12" cy="12" r="10" stroke="#000000" stroke-width="2"/>
                  <path d="M10 8L14 12L10 16" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </span>
            </NuxtLink>

          </div>

          <!-- Инфо-блок: icon 24px + текст 18px, gap 16px -->
          <div class="info-block">
            <span class="info-icon">
              <!-- Info circle: circle r10, line вертикальная, dot -->
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="#000000" stroke-width="2"/>
                <path d="M12 8V12" stroke="#000000" stroke-width="2" stroke-linecap="round"/>
                <circle cx="12" cy="16" r="1" fill="#000000"/>
              </svg>
            </span>
            <p class="info-text">
              Первичные данные должны прийти на электронную почту, которую вы указали при оформлении заказа.
              <br>Если что-то пошло не так — напишите нам.
            </p>
          </div>

        </form>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from '#app'

const router = useRouter()
const email = ref('')
const password = ref('')
const loading = ref(false)

const handleLogin = async () => {
  loading.value = true
  await new Promise(r => setTimeout(r, 700))
  loading.value = false
  router.push('/')
}
</script>

<style scoped>
/* ─── Layout ─────────────────────────────────────────── */
.page-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
}

/* ─── Header: 72px, white, border-bottom #dfdfdf ─────── */
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
  cursor: pointer;
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

/* ─── Main: flex центр ───────────────────────────────── */
.main-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

/* ─── Контейнер формы: 541px, gap 64px ─────────────── */
.form-container {
  width: 541px;
  display: flex;
  flex-direction: column;
  gap: 64px;
}

@media (max-width: 600px) {
  .form-container {
    width: 100%;
    gap: 40px;
  }
}

/* ─── Заголовок: 42px Roboto Regular, center ─────────── */
.page-title {
  font-family: 'Roboto', sans-serif;
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  line-height: 1.166; /* ~49px / 42px */
  text-align: center;
  margin: 0;
}

/* ─── Форма: gap 48px ─────────────────────────────────── */
.login-form {
  display: flex;
  flex-direction: column;
  gap: 48px;
}

/* ─── Группа инпутов: gap 24px ──────────────────────── */
.inputs-group {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

/* ─── Поле: label + input ────────────────────────────── */
.field-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
  width: 100%;
}

/* Label: 16px Roboto Regular #000 */
.field-label {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: #000000;
  line-height: 1.1875; /* ~19px */
}

/* Input: 541×61px, border #dddddd, padding 24px, 18px */
.field-input {
  width: 100%;
  height: 61px;
  border: 1px solid #dddddd;
  border-top-width: 1px;
  border-right-width: 1px;
  border-bottom-width: 1px;
  border-left-width: 1px;
  background-color: transparent;
  padding: 0 24px;
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
  font-weight: 400;
  color: #000000;
  outline: none;
  box-sizing: border-box;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
  appearance: none;
  -webkit-appearance: none;
  border-radius: 0;
}

.field-input::placeholder {
  color: #000000;
  opacity: 0.4;
}

.field-input:focus {
  border-color: #000000;
  box-shadow: 0 0 0 1px #000000;
}

/* ─── Группа кнопок: gap 4px ────────────────────────── */
.actions-group {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

/* Кнопка Войти: 541×72px, bg #000, text #fff */
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

/* Кнопка Забыли пароль: 541×72px, bg #fff, border rgba(0,0,0,0.1) */
.btn-secondary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 72px;
  background-color: #ffffff;
  color: #000000;
  border: 1px solid rgba(0, 0, 0, 0.1);
  padding: 0 32px;
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
  font-weight: 400;
  cursor: pointer;
  box-sizing: border-box;
  transition: border-color 0.2s ease, background-color 0.2s ease;
  text-decoration: none;
}

.btn-secondary:hover {
  border-color: rgba(0, 0, 0, 0.3);
  background-color: #fafafa;
}

/* Иконка стрелки в кнопке */
.btn-icon-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

/* ─── Info block: gap 16px, icon 24px + 18px text ─────── */
.info-block {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}

.info-icon {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 2px;
}

/* Текст: 18px Roboto Regular #000, lineHeight auto */
.info-text {
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
  font-weight: 400;
  color: #000000;
  line-height: 1.5;
  margin: 0;
}
</style>
