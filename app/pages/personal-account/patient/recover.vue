<template>
  <div class="patient-page-layout">
    <!-- Шапка страницы -->
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

    <!-- Основной контент (Восстановление доступа) -->
    <main class="patient-main-content">
      <div class="recover-card-container">
        <!-- Заголовок -->
        <div class="title-block">
          <h2 class="recover-title">Восстановление доступа</h2>
          <p class="recover-subtitle">Введите электронную почту, которую указывали при оформлении заказа</p>
        </div>

        <!-- Форма восстановления -->
        <form @submit.prevent="handleRecover" class="recover-form" novalidate>
          <div class="form-inputs-group">
            <!-- Поле E-mail -->
            <div class="form-group">
              <label for="email" class="form-label" :class="{ 'error-label': isError }">E-mail</label>
              <input 
                id="email" 
                type="email" 
                v-model="email" 
                class="form-input" 
                :class="{ 'input-error': isError }"
                :aria-invalid="isError"
                placeholder="max@inmuntex.com" 
                required
              />
              
              <!-- Сообщение об ошибке (Frame 1:119) -->
              <div v-if="isError" class="error-message" role="alert">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                  <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
                  <path d="M12 8V12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                  <circle cx="12" cy="16" r="1" fill="currentColor"/>
                </svg>
                <span>Почта не найдена</span>
              </div>
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
import { computed, ref } from 'vue'
import { useRouter } from '#app'

const props = defineProps({
  role: {
    type: String,
    default: 'patient'
  }
})

const router = useRouter()
const email = ref('')
const isError = ref(false)
const accountBasePath = computed(() => `/personal-account/${props.role === 'doctor' ? 'doctor' : 'patient'}`)
const loginPath = computed(() => `${accountBasePath.value}/login`)

const handleRecover = () => {
  // Для интерактивности: если введена почта отличная от "max@inmuntex.com", показываем ошибку
  if (email.value !== 'max@inmuntex.com') {
    isError.value = true
  } else {
    isError.value = false
    // Переход на страницу подтверждения
    router.push(`${accountBasePath.value}/check-email`)
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
  min-height: calc(100vh - 72px);
  padding: 0 20px;
  transform: translateY(-54px);
}

.recover-card-container {
  width: 541px;
  display: flex;
  flex-direction: column;
  gap: 48px; /* gap 48px из макета */
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
  gap: 32px;
}

.form-inputs-group {
  display: flex;
  flex-direction: column;
  gap: 24px;
  position: relative;
}

.input-error {
  border-color: #ff0000 !important;
  color: #ff0000;
}

.input-error::placeholder,
.error-label {
  color: #ff0000;
}

.error-message {
  display: flex;
  align-items: center;
  gap: 16px;
  min-height: 24px;
  font-size: 18px;
  color: #ff0505;
  margin-top: 18px;
  text-align: left;
}

.error-message svg {
  flex: 0 0 24px;
}

.form-actions {
  display: flex;
  flex-direction: column;
}

@media (max-width: 600px) {
  .patient-main-content {
    min-height: auto;
    align-items: flex-start;
    padding: 202px 16px 40px;
    transform: none;
  }

  .recover-card-container {
    width: 100%;
    gap: 48px;
  }

  .recover-title {
    font-size: clamp(28px, 7.62vw, 32px);
    line-height: 38px;
    white-space: nowrap;
  }

  .recover-subtitle {
    line-height: 1.2;
  }

  .recover-form {
    gap: 24px;
  }
}
</style>
