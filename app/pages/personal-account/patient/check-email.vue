<template>
  <div class="patient-page-layout">
    <!-- Шапка страницы -->
    <header class="header-nav">
      <NuxtLink to="/personal-account/patient/recover" class="back-link">
        <span class="back-arrow">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M15 18L9 12L15 6" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </span>
        Назад
      </NuxtLink>
    </header>

    <!-- Основной контент (Проверьте почту) -->
    <main class="patient-main-content">
      <div class="check-card-container">
        <!-- Заголовок -->
        <div class="title-block">
          <h2 class="check-title">Проверьте почту</h2>
          <p class="check-subtitle">На вашу почту пришли новые данные для входа</p>
        </div>

        <!-- Кнопка Войти еще раз -->
        <div class="form-actions">
          <NuxtLink to="/personal-account/patient/login" class="btn-black btn-relogin">
            <span>Войти ещё раз</span>
            <span class="btn-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="#FFFFFF" stroke-width="2"/>
                <path d="M11 8L15 12L11 16" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </NuxtLink>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
// Никакого сложного JS не требуется, только навигация
</script>

<style scoped>
.patient-page-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
}

.patient-main-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.check-card-container {
  width: 411px; /* Ширина 411px по макету */
  display: flex;
  flex-direction: column;
  gap: 48px; /* gap 48px из макета */
}

@media (max-width: 480px) {
  .check-card-container {
    width: 100%;
  }
}

.title-block {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.check-title {
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  line-height: 1.16;
}

.check-subtitle {
  font-size: 18px;
  line-height: 1.5;
  color: #000000;
  opacity: 0.5;
  max-width: 228px; /* ширина по макету */
  margin: 0 auto;
}

.form-actions {
  display: flex;
  flex-direction: column;
}
</style>
