<template>
  <div class="doctor-page-layout">
    <!-- Шапка страницы -->
    <header class="header-nav home-back-area">
      <HomeBackLink stretched />
    </header>

    <!-- Основной контент (Центрированный блок) -->
    <main class="doctor-main-content">
      <div class="login-card-container">
        <!-- Заголовок -->
        <div class="title-block">
          <h2 class="login-title">Добро пожаловать!</h2>
          <p class="login-subtitle">Создавайте QR-код со скидкой для ваших пациентов и получайте бонус за каждого.</p>
        </div>

        <!-- Форма входа -->
        <form @submit.prevent="handleLogin" class="login-form" novalidate>
          <div class="form-inputs-group">
            <!-- Поле E-mail -->
            <div class="form-group">
              <label for="email" class="form-label" :class="{ 'error-label': emailError }">E-mail</label>
              <input 
                id="email" 
                type="email" 
                v-model="email" 
                class="form-input" 
                :class="{ 'input-error': emailError }"
                :aria-invalid="emailError"
                placeholder="max@inmuntex.com" 
                @input="clearLoginError"
                required
              />
            </div>

            <!-- Поле Пароль -->
            <div class="form-group">
              <label for="password" class="form-label" :class="{ 'error-label': passwordError }">Пароль</label>
              <input 
                id="password" 
                type="password" 
                v-model="password" 
                class="form-input" 
                :class="{ 'input-error': passwordError }"
                :aria-invalid="passwordError"
                placeholder="*************" 
                @input="clearLoginError"
                required
              />
            </div>
          </div>

          <div v-if="loginError" class="login-error-message" role="alert">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true">
              <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
              <path d="M12 8V12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              <circle cx="12" cy="16" r="1" fill="currentColor"/>
            </svg>
            <span>Неверные данные</span>
          </div>

          <!-- Кнопки управления -->
          <div class="form-actions">
            <!-- Кнопка Войти -->
            <button type="submit" class="btn-black btn-login">
              <span>Войти</span>
              <span class="btn-icon">
                <!-- Стрелка в круге -->
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="12" cy="12" r="10" stroke="#FFFFFF" stroke-width="2"/>
                  <path d="M11 8L15 12L11 16" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </span>
            </button>

            <!-- Две кнопки снизу (Создать аккаунт / Забыли пароль) -->
            <div class="secondary-actions">
              <NuxtLink to="/personal-account/doctor/register" class="btn-outline btn-half">
                <span>Создать аккаунт</span>
                <span class="btn-icon">
                  <!-- Плюс -->
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M5 12H19M12 5V19" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </span>
              </NuxtLink>

              <NuxtLink to="/personal-account/doctor/recover" class="btn-outline btn-half">
                <span>Забыли пароль?</span>
                <span class="btn-icon">
                  <!-- Стрелка в круге -->
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="12" cy="12" r="10" stroke="#000000" stroke-width="2"/>
                    <path d="M11 8L15 12L11 16" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </span>
              </NuxtLink>
            </div>
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
const emailError = ref(false)
const passwordError = ref(false)
const loginError = ref(false)

const isValidEmail = (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value.trim())
const isValidPassword = (value) => value.length >= 8 && /[A-Za-zА-Яа-яЁё]/.test(value)

const clearLoginError = () => {
  emailError.value = false
  passwordError.value = false
  loginError.value = false
}

const handleLogin = () => {
  emailError.value = !isValidEmail(email.value)
  passwordError.value = !isValidPassword(password.value)
  loginError.value = emailError.value || passwordError.value

  if (loginError.value) return

  router.push('/personal-account/doctor/dashboard')
}
</script>

<style scoped>
.doctor-page-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
}

.doctor-main-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: calc(100vh - 72px);
  padding: 0 20px;
}

.login-card-container {
  width: 541px;
  display: flex;
  flex-direction: column;
  gap: 64px; /* gap 64px из макета */
}

.title-block {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 12px; /* gap 12px из макета */
}

.login-title {
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  line-height: 1.16;
}

.login-subtitle {
  font-size: 18px;
  line-height: 1.5;
  color: #000000;
  max-width: 375px; /* ширина из макета */
  margin: 0 auto;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-inputs-group {
  display: flex;
  flex-direction: column;
  gap: 24px; /* gap 24px из макета */
}

.input-error {
  border-bottom-color: #ff0505 !important;
  color: #ff0505;
}

.input-error::placeholder,
.error-label {
  color: #ff0505;
}

.login-error-message {
  display: flex;
  align-items: center;
  gap: 16px;
  min-height: 24px;
  margin-top: -4px;
  color: #ff0505;
  font-size: 18px;
  line-height: 1;
}

.login-error-message svg {
  flex: 0 0 24px;
}

.form-actions {
  display: flex;
  flex-direction: column;
  gap: 4px; /* gap 4px из макета */
}

.secondary-actions {
  display: flex;
  gap: 4px; /* gap 4px из макета */
  width: 100%;
}

.btn-half {
  flex: 1;
  padding: 24px 32px;
  font-size: 18px;
}

@media (max-width: 480px) {
  .doctor-main-content {
    min-height: auto;
    align-items: flex-start;
    padding: 77px 16px 40px;
  }

  .login-card-container {
    width: 100%;
    gap: 64px;
  }

  .login-title {
    font-size: 32px;
    line-height: 38px;
    white-space: nowrap;
  }

  .login-subtitle {
    line-height: 1.2;
  }

  .secondary-actions {
    flex-direction: column;
  }
}
</style>
