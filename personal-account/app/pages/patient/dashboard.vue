<template>
  <div class="patient-page-layout">
    <!-- Шапка дашборда -->
    <header class="header-nav dashboard-header">
      <div class="header-logo">ALEX LAB</div>
      
      <!-- Демо-переключатель статусов анализов для демонстрации всех экранов макета -->
      <div class="demo-status-selector">
        <span class="selector-label">Статус:</span>
        <button 
          v-for="statusNum in [1, 2, 3, 4]" 
          :key="statusNum" 
          @click="currentStatus = statusNum"
          class="status-tab-btn"
          :class="{ active: currentStatus === statusNum }"
        >
          {{ statusNum }}
        </button>
      </div>
    </header>

    <main class="patient-main-content">
      <div class="dashboard-container">
        
        <!-- СТАТУС 1: Ожидание сдачи крови (Frame 1:14) -->
        <div v-if="currentStatus === 1" class="status-content-wrapper">
          <div class="status-card-header">
            <h2 class="patient-welcome-title">Иван, вас ждут по адресу Казань, Островского 9. Здание Invitro.</h2>
            <p class="patient-welcome-desc">Сдайте кровь до 31 июля — потом запись автоматически отменится</p>
          </div>

          <!-- Заглушка под карту по ТЗ пользователя (размер 805x291px на десктопе) -->
          <div class="map-placeholder-box">
            <!-- Координатная сетка на SVG для имитации карты -->
            <svg class="map-grid-svg" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
                  <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(0, 0, 0, 0.05)" stroke-width="1"/>
                </pattern>
              </defs>
              <rect width="100%" height="100%" fill="url(#grid)" />
              
              <!-- Имитация дорог/линий карты -->
              <path d="M-10 100 Q 200 80 400 150 T 900 120" stroke="rgba(0,0,0,0.06)" stroke-width="12" fill="none" stroke-linecap="round"/>
              <path d="M150 -10 Q 180 150 120 350" stroke="rgba(0,0,0,0.06)" stroke-width="16" fill="none" stroke-linecap="round"/>
              <path d="M500 -10 L 530 350" stroke="rgba(0,0,0,0.06)" stroke-width="10" fill="none" stroke-linecap="round"/>
              
              <!-- Маркер геопозиции -->
              <g transform="translate(160, 130)">
                <circle cx="0" cy="0" r="10" fill="rgba(0,0,0,0.15)"/>
                <path d="M0 -20 C-6 -20 -10 -16 -10 -10 C-10 -3 0 10 0 10 C0 10 10 -3 10 -10 C10 -16 6 -20 0 -20 Z" fill="#000000"/>
                <circle cx="0" cy="-10" r="4" fill="#FFFFFF"/>
              </g>
            </svg>
            
            <div class="map-placeholder-info">
              <span class="map-label">КАРТА</span>
              <p class="map-subtext">Здесь будет интегрирована Яндекс.Карта</p>
            </div>
          </div>

          <!-- Кнопка Отменить запись -->
          <div class="status-action-row">
            <button @click="cancelAppointment" class="btn-cancel-appointment">
              <span>Отменить запись</span>
              <span class="btn-icon-circle-small">
                <!-- Восклицательный знак в круге -->
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="12" cy="12" r="10" stroke="#000000" stroke-width="2"/>
                  <path d="M12 8V12" stroke="#000000" stroke-width="2" stroke-linecap="round"/>
                  <circle cx="12" cy="16" r="1" fill="#000000"/>
                </svg>
              </span>
            </button>
          </div>
        </div>

        <!-- СТАТУС 2: Материал получен (Frame 1:188) -->
        <div v-else-if="currentStatus === 2" class="status-content-wrapper text-status-wrapper">
          <div class="text-status-card">
            <span class="status-badge">Новый статус</span>
            <h2 class="status-main-title">Материал получен,<br>ожидает расшифровки</h2>
            <p class="status-sub-desc">О новых статусах сообщаем по СМС<br>и на электронной почте</p>
          </div>
        </div>

        <!-- СТАТУС 3: Расшифровка (Frame 1:215) -->
        <div v-else-if="currentStatus === 3" class="status-content-wrapper text-status-wrapper">
          <div class="text-status-card">
            <span class="status-badge">Текущий статус</span>
            <h2 class="status-main-title">Расшифровка материала</h2>
            <p class="status-sub-desc">Всё будет готово примерно 29 августа</p>
          </div>
        </div>

        <!-- СТАТУС 4: Результат готов (Frame 1:240) -->
        <div v-else-if="currentStatus === 4" class="status-content-wrapper text-status-wrapper">
          <div class="text-status-card result-ready-card">
            <span class="status-badge success-badge">Результат готов</span>
            <h2 class="status-main-title">Ваш результат готов</h2>
            <p class="status-sub-desc">Его можно посмотреть здесь,<br>а также на электронной почте</p>
            
            <!-- Кнопки действий по результатам -->
            <div class="result-actions-group">
              <!-- Посмотреть онлайн -->
              <button @click="viewOnline" class="btn-black btn-result-action">
                <span>Посмотреть онлайн</span>
                <span class="btn-icon">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="12" cy="12" r="10" stroke="#FFFFFF" stroke-width="2"/>
                    <path d="M11 8L15 12L11 16" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </span>
              </button>

              <!-- Скачать PDF -->
              <a href="#" @click.prevent="downloadPdf" class="btn-outline btn-result-action">
                <span>Скачать PDF</span>
                <span class="btn-icon">
                  <!-- Иконка скачивания файла -->
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 4V16M12 16L8 12M12 16L16 12" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M4 20H20" stroke="#000000" stroke-width="2" stroke-linecap="round"/>
                  </svg>
                </span>
              </a>
            </div>
          </div>
        </div>

        <!-- Нижний блок кнопок управления аккаунтом (Frame 1:37) -->
        <div class="dashboard-actions">
          <!-- Данные аккаунта -->
          <NuxtLink to="/patient/profile" class="btn-outline dashboard-btn-left">
            <span>Данные аккаунта</span>
            <span class="btn-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </NuxtLink>

          <!-- Выйти из аккаунта -->
          <NuxtLink to="/patient/login" class="btn-outline dashboard-btn-right">
            <span>Выйти из аккаунта</span>
            <span class="btn-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </NuxtLink>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const currentStatus = ref(1) // Демо-статус по умолчанию (1, 2, 3 или 4)

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
  gap: 20px;
}

.header-logo {
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 0.1em;
}

/* Демо-селектор статусов */
.demo-status-selector {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: #f0f2f5;
  padding: 6px 12px;
  border-radius: 30px;
  border: 1px solid #dfdfdf;
}

.selector-label {
  font-size: 12px;
  text-transform: uppercase;
  color: rgba(0,0,0,0.5);
  font-weight: 700;
}

.status-tab-btn {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 1px solid rgba(0,0,0,0.1);
  background: white;
  font-size: 12px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.status-tab-btn.active {
  background-color: #000000;
  color: white;
  border-color: #000000;
}

.patient-main-content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.dashboard-container {
  width: 805px; /* Ширина по макету */
  display: flex;
  flex-direction: column;
  gap: 64px; /* gap 64px по макету */
}

@media (max-width: 840px) {
  .dashboard-container {
    width: 100%;
    gap: 40px;
  }
}

.status-content-wrapper {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.status-card-header {
  text-align: left;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.patient-welcome-title {
  font-size: 24px; /* 24px по макету */
  font-weight: 400;
  line-height: 1.3;
  color: #000000;
}

.patient-welcome-desc {
  font-size: 21px; /* 21px по макету */
  font-weight: 400;
  color: rgba(0, 0, 0, 0.5); /* opacity 0.5 */
}

/* Заглушка карты */
.map-placeholder-box {
  width: 100%;
  height: 291px; /* 291px по макету */
  background-color: #ffffff;
  border: 1px solid #dfdfdf;
  position: relative;
  overflow: hidden;
}

.map-grid-svg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.map-placeholder-info {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  background-color: rgba(255, 255, 255, 0.9);
  padding: 24px 40px;
  border: 1px solid rgba(0,0,0,0.08);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  gap: 6px;
  pointer-events: none;
}

.map-label {
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 0.2em;
  color: #000000;
}

.map-subtext {
  font-size: 14px;
  color: rgba(0, 0, 0, 0.5);
}

.status-action-row {
  display: flex;
}

/* Кнопка отмены */
.btn-cancel-appointment {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 251px; /* ширина по макету */
  height: 56px;  /* высота по макету */
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

/* Текстовые дашборды для статусов 2, 3, 4 */
.text-status-wrapper {
  background-color: #ffffff;
  border: 1px solid #dfdfdf;
  padding: 64px 32px;
  text-align: left;
}

.text-status-card {
  display: flex;
  flex-direction: column;
  gap: 24px;
  max-width: 600px;
}

.status-badge {
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: rgba(0,0,0,0.5);
  font-weight: 700;
  align-self: flex-start;
}

.success-badge {
  color: #008800;
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

/* Кнопки действий результатов */
.result-actions-group {
  display: flex;
  gap: 12px;
  margin-top: 16px;
}

.btn-result-action {
  flex: 1;
  max-width: 270px;
}

@media (max-width: 600px) {
  .result-actions-group {
    flex-direction: column;
    width: 100%;
  }
  .btn-result-action {
    max-width: 100%;
    width: 100%;
  }
}

/* Стили нижних кнопок управления аккаунтом */
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
  .dashboard-container {
    width: 100%;
    gap: 32px;
    padding: 0 16px;
  }

  .patient-welcome-title {
    font-size: 20px;
  }

  .patient-welcome-desc {
    font-size: 16px;
  }

  .map-placeholder-box {
    height: 250px;
  }

  .btn-cancel-appointment {
    width: 100%; /* На мобильном кнопка отмены на всю ширину */
  }

  .status-main-title {
    font-size: 28px;
  }

  .status-sub-desc {
    font-size: 16px;
  }

  .text-status-wrapper {
    padding: 40px 24px;
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
