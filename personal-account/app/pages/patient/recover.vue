<template>
  <div class="patient-page-layout">
    <!-- Шапка страницы -->
    <header class="header-nav">
      <NuxtLink to="/patient/login" class="back-link">
        <span class="back-arrow">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M15 18L9 12L15 6" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </span>
        Назад
      </NuxtLink>
    </header>

    <!-- Основной контент (Восстановление доступа) -->
    <main class="patient-main-content">
      <div class="recover-card-container">
        <!-- Заголовок -->
        <div class="title-block">
          <h2 class="recover-title">Восстановление доступа</h2>
          <p class="recover-subtitle">Введите электронную почту, которую указывали при оформлении заказа</p>
        </div>

        <!-- Форма восстановления -->
        <form @submit.prevent="handleRecover" class="recover-form">
          <div class="form-inputs-group">
            <!-- Поле E-mail -->
            <div class="form-group">
              <label for="email" class="form-label">E-mail</label>
              <input 
                id="email" 
                type="email" 
                v-model="email" 
                class="form-input" 
                :class="{ 'input-error': isError }"
                placeholder="max@inmuntex.com" 
                required
              />
              
              <!-- Сообщение об ошибке (Frame 1:119) -->
              <span v-if="isError" class="error-message">Почта не найдена</span>
            </div>
          </div>

          <!-- Кнопка Далее -->
          <div class="form-actions">
            <button type="submit" class="btn-black btn-next">
              <span>Далее</span>
              <span class="btn-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="12" cy="12" r="10" stroke="#FFFFFF" stroke-width="2"/>
                  <path d="M11 8L15 12L11 16" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </span>
            </button>
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
const isError = ref(false)

const handleRecover = () => {
  // Для интерактивности: если введена почта отличная от "max@inmuntex.com", показываем ошибку
  if (email.value !== 'max@inmuntex.com') {
    isError.value = true
  } else {
    isError.value = false
    // Переход на страницу подтверждения
    router.push('/patient/check-email')
  }
}
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

.recover-card-container {
  width: 541px;
  display: flex;
  flex-direction: column;
  gap: 48px; /* gap 48px из макета */
}

@media (max-width: 600px) {
  .recover-card-container {
    width: 100%;
    gap: 40px;
  }
}

.title-block {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.recover-title {
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  line-height: 1.16;
}

.recover-subtitle {
  font-size: 18px;
  line-height: 1.5;
  color: #000000;
  opacity: 0.5; /* Опасити 0.5 из макета */
  max-width: 398px;
  margin: 0 auto;
}

.recover-form {
  display: flex;
  flex-direction: column;
  gap: 48px;
}

.form-inputs-group {
  display: flex;
  flex-direction: column;
  gap: 24px;
  position: relative;
}

.input-error {
  border-color: #ff0000 !important;
}

.error-message {
  font-size: 14px;
  color: #ff0000;
  margin-top: 4px;
  text-align: left;
}

.form-actions {
  display: flex;
  flex-direction: column;
}
</style>
