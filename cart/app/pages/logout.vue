<template>
  <div class="page-layout">
    <!-- Header 72px — точно по макету -->
    <header class="header-nav">
      <NuxtLink to="/" class="back-link">
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
          <h1 class="page-title">Выход из аккаунта</h1>
          <!-- 18px, Roboto Regular, opacity 0.5, center -->
          <p class="page-subtitle">Вы уверены, что хотите выйти? Ваша корзина будет сохранена.</p>
        </div>

        <!-- Кнопки действия -->
        <div class="actions-group">
          <!-- Выйти: черная кнопка -->
          <button @click="handleLogout" class="btn-primary">
            <span>Выйти</span>
            <span class="btn-icon-wrap">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="#FFFFFF" stroke-width="2"/>
                <path d="M10 8L14 12L10 16" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </button>

          <!-- Остаться: белая кнопка -->
          <NuxtLink to="/" class="btn-secondary">
            <span>Остаться</span>
            <span class="btn-icon-wrap">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="#000000" stroke-width="2"/>
                <path d="M10 8L14 12L10 16" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </NuxtLink>
        </div>

      </div>
    </main>
  </div>
</template>

<script setup>
import { useRouter } from '#app'

const router = useRouter()

const handleLogout = () => {
  // Имитация выхода из аккаунта
  router.push('/login')
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

/* ─── Header: 72px ─── */
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

/* ─── Контейнер: 541px ────────────────── */
.form-container {
  width: 541px;
  display: flex;
  flex-direction: column;
  gap: 48px;
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

/* Кнопки */
.actions-group {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

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

.btn-icon-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}
</style>
