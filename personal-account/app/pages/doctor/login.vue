<template>
  <div class="doctor-page-layout">
    <!-- Шапка страницы -->
    <header class="header-nav">
      <NuxtLink to="/" class="back-link">
        <span class="back-arrow">
          <!-- Стрелка влево -->
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M15 18L9 12L15 6" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </span>
        На главную
      </NuxtLink>
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
        <form @submit.prevent="handleLogin" class="login-form">
          <div class="form-inputs-group">
            <!-- Поле E-mail -->
            <div class="form-group">
              <label for="email" class="form-label">E-mail</label>
              <input 
                id="email" 
                type="email" 
                v-model="email" 
                class="form-input" 
                placeholder="max@inmuntex.com" 
                required
              />
            </div>

            <!-- Поле Пароль -->
            <div class="form-group">
              <label for="password" class="form-label">Пароль</label>
              <input 
                id="password" 
                type="password" 
                v-model="password" 
                class="form-input" 
                placeholder="*************" 
                required
              />
            </div>
          </div>

          <!-- Кнопки управления -->
          <div class="form-actions">
            <!-- Кнопка Войти -->
            <button type="submit" class="btn-black btn-login">
              <span>Войти</span>
              <span class="btn-icon">
                <!-- Стрелка вправо -->
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M2 12H22M22 12L14 4M22 12L14 20" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </span>
            </button>

            <!-- Две кнопки снизу (Создать аккаунт / Забыли пароль) -->
            <div class="secondary-actions">
              <NuxtLink to="/doctor/register" class="btn-outline btn-half">
                <span>Создать аккаунт</span>
                <span class="btn-icon">
                  <!-- Плюс -->
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M5 12H19M12 5V19" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </span>
              </NuxtLink>

              <button type="button" @click="handleForgotPassword" class="btn-outline btn-half">
                <span>Забыли пароль?</span>
                <span class="btn-icon">
                  <!-- Стрелка вправо тонкая -->
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M2 12H22M22 12L14 4M22 12L14 20" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </span>
              </button>
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

const handleLogin = () => {
  // Имитация успешного входа
  router.push('/doctor/dashboard')
}

const handleForgotPassword = () => {
  alert('Ссылка для восстановления пароля отправлена на указанный E-mail (демо)')
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
  padding: 40px 20px;
}

.login-card-container {
  width: 541px;
  display: flex;
  flex-direction: column;
  gap: 64px; /* gap 64px из макета */
}

@media (max-width: 600px) {
  .login-card-container {
    width: 100%;
    gap: 40px;
  }
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
  gap: 48px; /* gap 48px из макета */
}

.form-inputs-group {
  display: flex;
  flex-direction: column;
  gap: 24px; /* gap 24px из макета */
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
  .secondary-actions {
    flex-direction: column;
  }
}
</style>
