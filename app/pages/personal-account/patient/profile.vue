<template>
  <div class="patient-page-layout">
    <!-- Шапка страницы -->
    <header class="header-nav">
      <NuxtLink to="/personal-account/patient/dashboard" class="back-link">
        <span class="back-arrow">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M15 18L9 12L15 6" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </span>
        Вернутся назад
      </NuxtLink>
    </header>

    <!-- Основной контент (Профиль пациента) -->
    <main class="patient-main-content">
      <div class="profile-card-container">
        <!-- Заголовок -->
        <h2 class="profile-title">Личные данные</h2>

        <!-- Форма профиля -->
        <form @submit.prevent="handleSave" class="profile-form">
          <div class="form-inputs-group">
            <!-- Поле ФИО (размер заголовка по макету 21px) -->
            <div class="form-group">
              <label for="name" class="form-label profile-label">ФИО</label>
              <input 
                id="name" 
                type="text" 
                v-model="name" 
                class="form-input" 
                placeholder="Бурмистров Павел Сергеевич" 
                required
              />
            </div>

            <!-- Поле Номер телефона -->
            <div class="form-group">
              <label for="phone" class="form-label profile-label">Номер телефона</label>
              <input 
                id="phone" 
                type="tel" 
                v-model="phone" 
                class="form-input" 
                placeholder="+7 999 999 99 99" 
                required
              />
            </div>

            <!-- Поле E-mail -->
            <div class="form-group">
              <label for="email" class="form-label profile-label">E-mail</label>
              <input 
                id="email" 
                type="email" 
                v-model="email" 
                class="form-input" 
                placeholder="max@inmuntex.com" 
                required
              />
            </div>
          </div>

          <!-- Кнопка Сохранить -->
          <div class="form-actions">
            <button type="submit" class="btn-black btn-save">
              <span>{{ saveButtonText }}</span>
              <span class="btn-icon">
                <!-- Галочка в круге -->
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="12" cy="12" r="10" stroke="#FFFFFF" stroke-width="2"/>
                  <path d="M8 12L11 15L16 9" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
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
const name = ref('Бурмистров Павел Сергеевич')
const phone = ref('+7 999 999 99 99')
const email = ref('max@inmuntex.com')

const saveButtonText = ref('Сохранить')

const handleSave = () => {
  saveButtonText.value = 'Сохранено!'
  setTimeout(() => {
    saveButtonText.value = 'Сохранить'
    // Переход обратно на дашборд пациента после сохранения
    router.push('/personal-account/patient/dashboard')
  }, 1000)
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
  transform: translateY(-23px);
}

.profile-card-container {
  width: 805px; /* Ширина по макету */
  display: flex;
  flex-direction: column;
  gap: 64px; /* gap 64px по макету */
}

.profile-title {
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  line-height: 1.16;
}

.profile-form {
  display: flex;
  flex-direction: column;
  gap: 64px; /* gap 64px по макету */
}

.form-inputs-group {
  display: flex;
  flex-direction: column;
  gap: 48px; /* gap 48px по макету */
}

.profile-label {
  font-size: 21px; /* Размер шрифта меток по макету */
  font-weight: 400;
  color: #000000;
}

.form-actions {
  display: flex;
  flex-direction: column;
}

@media (max-width: 840px) {
  .patient-main-content {
    min-height: auto;
    align-items: flex-start;
    padding: 116px 16px 48px;
    transform: none;
  }

  .profile-card-container {
    width: 100%;
    gap: 48px;
  }

  .profile-title {
    font-size: 32px;
    line-height: 38px;
  }

  .profile-form {
    gap: 32px;
  }

  .form-inputs-group {
    gap: 24px;
  }

  .profile-label {
    font-size: 16px;
    color: rgba(0, 0, 0, 0.5);
  }
}
</style>
