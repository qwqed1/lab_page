<template>
  <div class="patient-page-layout">
    <main class="patient-main-content">
      <div class="dashboard-container">
        <div class="dashboard-panel">

        <!-- Единая карточка статуса пациента (Frame 336211) -->
        <div class="status-card">
          <!-- Карта на статус 1 (заглушка) -->
          <div v-if="currentStatus === 1" class="map-placeholder-box">
            <span class="map-label">Карта</span>
          </div>

          <!-- Контентная часть карточки -->
          <div class="status-card-body">
            
            <!-- Пошаговый интерактивный элемент (Stepper) на макете Frame 336201 -->
            <div class="stepper-container">
              <!-- Шаг 1 -->
              <button 
                class="step-dot" 
                :class="{ filled: currentStatus >= 1 }" 
                @click="currentStatus = 1"
                title="Шаг 1: Запись на анализы"
                aria-label="Шаг 1"
              ></button>
              <span class="step-line"></span>

              <!-- Шаг 2 -->
              <button 
                class="step-dot" 
                :class="{ filled: currentStatus >= 2 }" 
                @click="currentStatus = 2"
                title="Шаг 2: Материал получен"
                aria-label="Шаг 2"
              ></button>
              <span class="step-line"></span>

              <!-- Шаг 3 -->
              <button 
                class="step-dot" 
                :class="{ filled: currentStatus >= 3 }" 
                @click="currentStatus = 3"
                title="Шаг 3: Расшифровка материала"
                aria-label="Шаг 3"
              ></button>
              <span class="step-line"></span>

              <!-- Шаг 4 -->
              <button 
                class="step-dot" 
                :class="{ filled: currentStatus >= 4 }" 
                @click="currentStatus = 4"
                title="Шаг 4: Результат готов"
                aria-label="Шаг 4"
              ></button>
            </div>

            <!-- Контент в зависимости от выбранного шага -->
            <div class="status-details">
              
              <!-- Шаг 1: Карта и Отмена записи -->
              <div v-if="currentStatus === 1" class="step-content">
                <div class="status-card-header">
                  <h2 class="patient-welcome-title">Иван, вас ждут по адресу Казань, Островского 9. Здание Invitro.</h2>
                  <p class="patient-welcome-desc">Сдайте кровь до 31 июля — потом запись автоматически отменится</p>
                </div>
                <div class="status-action-row">
                  <button @click="cancelAppointment" class="btn-cancel-appointment">
                    <span>Отменить запись</span>
                    <span class="btn-icon-circle-small">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="12" cy="12" r="10" stroke="#000000" stroke-width="2"/>
                        <path d="M12 8V12" stroke="#000000" stroke-width="2" stroke-linecap="round"/>
                        <circle cx="12" cy="16" r="1" fill="#000000"/>
                      </svg>
                    </span>
                  </button>
                </div>
              </div>

              <!-- Шаг 2: Материал получен (Frame 1:188) -->
              <div v-else-if="currentStatus === 2" class="step-content text-left">
                <div class="status-badge-container">
                  <span class="status-badge-blue">Новый статус</span>
                </div>
                <h2 class="status-main-title">Материал получен,<br>ожидает расшифровки</h2>
                <p class="status-sub-desc">О новых статусах сообщаем по СМС<br>и на электронной почте</p>
              </div>

              <!-- Шаг 3: Расшифровка (Frame 1:215) -->
              <div v-else-if="currentStatus === 3" class="step-content text-left">
                <h2 class="status-main-title">Расшифровка материала</h2>
                <p class="status-sub-desc">Всё будет готово примерно 29 августа</p>
              </div>

              <!-- Шаг 4: Результат готов (Frame 1:240) -->
              <div v-else-if="currentStatus === 4" class="step-content text-left">
                <h2 class="status-main-title">Ваш результат готов</h2>
                <p class="status-sub-desc">Его можно посмотреть здесь,<br>а также на электронной почте</p>
                
                <div class="result-actions-group">
                  <button @click="viewOnline" class="btn-black btn-view-online">
                    <span>Посмотреть онлайн</span>
                    <span class="btn-icon">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="12" cy="12" r="10" stroke="#FFFFFF" stroke-width="2"/>
                        <path d="M11 8L15 12L11 16" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                    </span>
                  </button>

                  <a href="#" @click.prevent="downloadPdf" class="btn-outline btn-download-pdf">
                    <span>Скачать PDF</span>
                    <span class="btn-icon">
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 4V16M12 16L8 12M12 16L16 12" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M4 20H20" stroke="#000000" stroke-width="2" stroke-linecap="round"/>
                      </svg>
                    </span>
                  </a>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- Нижний блок кнопок управления аккаунтом (Frame 1:37) -->
        <div class="dashboard-actions">
          <NuxtLink to="/personal-account/patient/profile" class="btn-outline dashboard-btn-left">
            <span>Данные аккаунта</span>
            <span class="btn-icon">
              <img src="/assets/account-profile.svg" alt="" width="24" height="24">
            </span>
          </NuxtLink>

          <NuxtLink to="/personal-account/patient/login" class="btn-outline dashboard-btn-right">
            <span>Выйти из аккаунта</span>
            <span class="btn-icon">
              <img src="/assets/account-logout.svg" alt="" width="24" height="24">
            </span>
          </NuxtLink>
        </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const currentStatus = ref(1) // Текущий статус по умолчанию (1, 2, 3 или 4)

const cancelAppointment = () => {
  if (confirm('Вы уверены, что хотите отменить запись на анализы?')) {
    alert('Запись отменена.')
  }
}

const viewOnline = () => {
  alert('Открытие результатов онлайн-расшифровки (демо-режим).')
}

const downloadPdf = () => {
  alert('Скачивание PDF-файла с результатами (демо-режим).')
}
</script>

<style scoped>
.patient-page-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
}

.dashboard-header {
  justify-content: space-between;
}

.header-logo {
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 0.1em;
}

.patient-main-content {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 20px;
}

.dashboard-container {
  width: 805px;
  display: flex;
  flex-direction: column;
}

.dashboard-panel {
  width: 100%;
  display: flex;
  flex-direction: column;
}

@media (max-width: 840px) {
  .dashboard-container {
    width: 100%;
    gap: 0;
  }
}

.status-card-header {
  text-align: left;
  display: flex;
  flex-direction: column;
  gap: 21px;
}

.patient-welcome-title {
  font-size: 24px;
  font-weight: 400;
  line-height: 1.15;
  color: #000000;
}

.patient-welcome-desc {
  font-size: 21px;
  font-weight: 400;
  color: rgba(0, 0, 0, 0.5);
  line-height: 1.15;
}

/* Карточка статуса */
.status-card {
  background-color: #ffffff;
  border: 1px solid #dfdfdf;
  display: flex;
  flex-direction: column;
  position: relative;
}

/* Заглушка карты */
.map-placeholder-box {
  width: 100%;
  height: 291px;
  background-color: #eceff4;
  border-bottom: 1px solid #dfdfdf;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.map-label {
  font-size: 18px;
  font-weight: 400;
  color: rgba(0, 0, 0, 0.45);
}

/* Тело карточки */
.status-card-body {
  padding: 32px; /* 32px отступ по макету */
  height: 393px; /* Фиксированная высота по макету */
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}

/* Пошаговый индикатор (Stepper) */
.stepper-container {
  display: flex;
  align-items: center;
  gap: 0;
  align-self: flex-start; /* Размещается слева */
}

.step-dot {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  border: 1px solid #000000;
  background-color: transparent;
  cursor: pointer;
  padding: 0;
  margin: 0;
  transition: background-color 0.2s ease, transform 0.2s ease;
  z-index: 2;
  box-sizing: border-box;
}

.step-dot:hover {
  transform: scale(1.15);
}

.step-dot.filled {
  background-color: #000000;
}

.step-line {
  width: 12px; /* ровно 12px по макету */
  height: 1px;
  background-color: #000000; /* сплошная линия */
  margin: 0;
  padding: 0;
  z-index: 1;
}

.status-details {
  margin-top: 116px;
  display: flex;
  flex-direction: column;
}

/* Шаг 1: кнопка отмены */
.status-action-row {
  display: flex;
  align-self: flex-start;
}

.btn-cancel-appointment {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 251px;
  height: 56px;
  background-color: #ffffff;
  border: 1px solid #dfdfdf;
  padding: 16px 24px;
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  color: #000000;
  cursor: pointer;
  transition: background-color 0.2s ease, border-color 0.2s ease;
}

.btn-cancel-appointment:hover {
  background-color: #fafafa;
  border-color: rgba(0, 0, 0, 0.3);
}

.btn-icon-circle-small {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
}

/* Шаги 2, 3, 4: текстовые стили */
.step-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.step-content:first-child {
  gap: 32px;
}

.text-left {
  text-align: left;
}

.status-badge-container {
  display: flex;
  margin-bottom: 8px;
}

.status-badge-blue {
  background-color: #f1faff;
  color: #2baac9;
  padding: 12px 24px;
  font-size: 14px;
  font-weight: 500;
  line-height: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 0;
  border: 1px solid rgba(0,0,0,0.03);
}

.status-main-title {
  font-size: 42px;
  font-weight: 400;
  line-height: 1.2;
  color: #000000;
}

.status-sub-desc {
  font-size: 21px;
  line-height: 1.5;
  color: rgba(0, 0, 0, 0.5);
}

/* Группа кнопок результатов */
.result-actions-group {
  display: flex;
  gap: 4px; /* gap 4px по макету */
  margin-top: 8px;
}

.btn-view-online {
  width: 265px; /* ширина по макету */
}

.btn-download-pdf {
  width: 197px; /* ширина по макету */
}

@media (max-width: 600px) {
  .result-actions-group {
    flex-direction: column;
    width: 100%;
  }
  .btn-view-online,
  .btn-download-pdf {
    width: 100% !important;
    max-width: 100%;
  }
}

/* Нижний блок кнопок управления аккаунтом */
.dashboard-actions {
  display: flex;
  width: 100%;
}

.dashboard-btn-left {
  width: 394px;
  border-right: none;
}

.dashboard-btn-right {
  width: 411px;
  flex-grow: 1;
}

/* Мобильная адаптация */
@media (max-width: 768px) {
  .patient-main-content {
    min-height: auto;
    align-items: flex-start;
    padding: 69px 16px 80px;
  }

  .dashboard-container {
    width: 100%;
    gap: 0;
    padding: 0;
  }

  .patient-welcome-title {
    font-size: 24px;
    line-height: 1.15;
  }

  .patient-welcome-desc {
    font-size: 18px;
    line-height: 1.15;
  }

  .map-placeholder-box {
    height: 161px;
  }

  .status-card-body {
    height: 393px;
  }

  .status-details {
    margin-top: 85px;
  }

  .status-badge-blue {
    padding: 8px 12px; /* Компактные отступы плашки на мобильных */
  }

  .btn-cancel-appointment {
    width: 251px;
  }

  .status-main-title {
    font-size: 28px;
  }

  .status-sub-desc {
    font-size: 16px;
  }

  .dashboard-actions {
    flex-direction: column;
  }

  .dashboard-btn-left {
    width: 100% !important;
    height: 66px !important;
    border: 1px solid #dfdfdf !important;
    border-bottom: none !important;
  }

  .dashboard-btn-right {
    width: 100% !important;
    height: 66px !important;
    border: 1px solid #dfdfdf !important;
  }
}
</style>
