<template>
  <div class="patient-page-layout">
    <!-- Шапка страницы -->
    <header class="header-nav">
      <HomeBackLink />
    </header>

    <!-- Основной контент (Вход пациента) -->
    <main class="patient-main-content">
      <div class="login-card-container">
        <!-- Заголовок -->
        <div class="title-block">
          <h2 class="login-title">Добро пожаловать!</h2>
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

          <!-- Кнопки управления (вертикальный стек) -->
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

            <!-- Кнопка Забыли пароль (полная ширина) -->
            <NuxtLink to="/personal-account/patient/recover" class="btn-outline btn-full">
              <span>Забыли пароль?</span>
              <span class="btn-icon">
                <!-- Стрелка в круге черная -->
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="12" cy="12" r="10" stroke="#000000" stroke-width="2"/>
                  <path d="M11 8L15 12L11 16" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </span>
            </NuxtLink>
          </div>

          <!-- Информационное сообщение (под кнопками) -->
          <div class="info-block">
            <span class="info-icon">
              <!-- Круг с точкой/восклицательным знаком -->
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="#000000" stroke-width="2"/>
                <path d="M12 8V12" stroke="#000000" stroke-width="2" stroke-linecap="round"/>
                <circle cx="12" cy="16" r="1" fill="#000000"/>
              </svg>
            </span>
            <p class="info-text">
              Первичные данные должны прийти на электронную почту, которую вы указали при оформлении заказа. Если что-то пошло не так — напишите нам.
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

  router.push('/personal-account/patient/dashboard')
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
  transform: translateY(-36px);
}

.login-card-container {
  width: 541px;
  display: flex;
  flex-direction: column;
  gap: 64px; /* gap 64px из макета */
}

.title-block {
  text-align: center;
}

.login-title {
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  line-height: 1.16;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.form-inputs-group {
  display: flex;
  flex-direction: column;
  gap: 24px;
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
  margin-top: 24px;
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
  gap: 4px; /* Расстояние между кнопками 4px */
  margin-top: 32px;
}

.login-error-message + .form-actions {
  margin-top: 32px;
}

.btn-full {
  width: 100%;
}

.info-block {
  display: flex;
  gap: 16px; /* gap 16px из макета */
  align-items: flex-start;
  text-align: left;
  margin-top: 48px;
}

.info-icon {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  margin-top: 2px;
}

.info-text {
  font-size: 18px;
  line-height: 1.2;
  color: #000000;
}

@media (max-width: 600px) {
  .patient-main-content {
    min-height: auto;
    align-items: flex-start;
    padding: 77px 16px 40px;
    transform: none;
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

  .form-actions {
    margin-top: 24px;
  }

  .info-block {
    margin-top: 32px;
  }
}
</style>
