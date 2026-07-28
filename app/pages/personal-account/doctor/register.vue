<template>
  <div class="doctor-page-layout">
    <!-- Шапка страницы -->
    <header class="header-nav">
      <NuxtLink to="/personal-account/doctor/login" class="back-link">
        <span class="back-arrow">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M15 18L9 12L15 6" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </span>
        Назад
      </NuxtLink>
    </header>

    <!-- Основной контент (Регистрация) -->
    <main class="doctor-main-content">
      <div class="register-card-container">
        <!-- Заголовок -->
        <div class="title-block">
          <h2 class="register-title">Создание аккаунта</h2>
          <p class="register-subtitle">
            Внутри личного кабинета вы сможете создать QR-код, который даст вашим пациентам небольшую скидку — а вы, статистику по его использованию и небольшой бонус за каждого приведённого пациента.
          </p>
        </div>

        <!-- Форма регистрации -->
        <form @submit.prevent="handleRegister" class="register-form">
          <div class="form-inputs-group">
            <!-- Поле ФИО -->
            <div class="form-group">
              <label for="name" class="form-label">ФИО</label>
              <input 
                id="name" 
                type="text" 
                v-model="name" 
                class="form-input" 
                placeholder="Бурмистров Павел Сергеевич" 
                required
              />
            </div>

            <!-- Поле Место работы -->
            <div class="form-group">
              <label for="workplace" class="form-label">Место работы</label>
              <input 
                id="workplace" 
                type="text" 
                v-model="workplace" 
                class="form-input" 
                placeholder="Москва, Городская больница №91" 
                required
              />
            </div>

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

          <!-- Кнопка Создать аккаунт -->
          <div class="form-actions">
            <button type="submit" class="btn-black btn-register">
              <span>Создать аккаунт</span>
              <span class="btn-icon">
                <!-- Стрелка в круге -->
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
const name = ref('')
const workplace = ref('')
const email = ref('')
const password = ref('')

const handleRegister = () => {
  // Имитация успешной регистрации и автоматического входа на дашборд
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
  transform: translateY(20px);
}

.register-card-container {
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

.register-title {
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  line-height: 1.16;
}

.register-subtitle {
  font-size: 18px;
  line-height: 1.5;
  color: #000000;
  max-width: 472px; /* ширина из макета */
  margin: 0 auto;
}

.register-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-inputs-group {
  display: flex;
  flex-direction: column;
  gap: 24px; /* gap 24px из макета */
}

.form-actions {
  display: flex;
  flex-direction: column;
}

@media (max-width: 600px) {
  .doctor-main-content {
    min-height: auto;
    align-items: flex-start;
    padding: 77px 16px 48px;
    transform: none;
  }

  .register-card-container {
    width: 100%;
    gap: 64px;
  }

  .register-title {
    font-size: 32px;
    line-height: 38px;
    white-space: nowrap;
  }

  .register-subtitle {
    line-height: 1.2;
  }
}
</style>
