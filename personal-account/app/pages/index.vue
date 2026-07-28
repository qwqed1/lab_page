<template>
  <div class="role-selection-wrapper">
    <div class="role-selection-container">
      <div class="logo-area">
        <h1 class="brand-title">ALEX LAB</h1>
        <p class="brand-subtitle">Центр молекулярной генетики и биотехнологий</p>
      </div>

      <h2 class="section-title">Личный кабинет</h2>
      <p class="section-desc">Пожалуйста, выберите вашу роль для входа в систему</p>

      <div class="cards-grid">
        <!-- Карточка Врача -->
        <NuxtLink to="/doctor/login" class="role-card doctor-card">
          <div class="card-glow"></div>
          <div class="card-content">
            <div class="card-icon-wrapper">
              <!-- Иконка стетоскопа / врача -->
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="card-icon">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <div class="card-text">
              <h3>Я врач</h3>
              <p>Создание промокодов, просмотр статистики пациентов и получение бонусов.</p>
            </div>
            <div class="card-arrow">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="arrow-svg">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
              </svg>
            </div>
          </div>
        </NuxtLink>

        <!-- Карточка Пациента -->
        <NuxtLink to="/patient/login" class="role-card patient-card">
          <div class="card-glow"></div>
          <div class="card-content">
            <div class="card-icon-wrapper">
              <!-- Иконка пациента / пользователя -->
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" class="card-icon">
                <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </div>
            <div class="card-text">
              <h3>Я пациент</h3>
              <p>Просмотр результатов анализов, направлений и истории посещений центра.</p>
            </div>
            <div class="card-arrow">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="arrow-svg">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
              </svg>
            </div>
          </div>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
// Скрипт очищен от логики открытия модального окна
</script>

<style scoped>
.role-selection-wrapper {
  min-height: 100vh;
  width: 100%;
  background: radial-gradient(circle at 10% 20%, rgba(245, 245, 245, 1) 0%, rgba(230, 235, 240, 1) 90%);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px 20px;
}

.role-selection-container {
  max-width: 900px;
  width: 100%;
  text-align: center;
}

.logo-area {
  margin-bottom: 48px;
}

.brand-title {
  font-size: 32px;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: #000000;
  margin-bottom: 8px;
}

.brand-subtitle {
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: rgba(0, 0, 0, 0.4);
}

.section-title {
  font-size: 36px;
  font-weight: 400;
  color: #000000;
  margin-bottom: 12px;
}

.section-desc {
  font-size: 18px;
  color: rgba(0, 0, 0, 0.5);
  margin-bottom: 56px;
}

.cards-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

@media (max-width: 768px) {
  .cards-grid {
    grid-template-columns: 1fr;
  }
  .section-title {
    font-size: 28px;
  }
}

.role-card {
  position: relative;
  background-color: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.08);
  padding: 40px 32px;
  display: flex;
  flex-direction: column;
  text-align: left;
  cursor: pointer;
  overflow: hidden;
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), border-color 0.3s ease;
}

.role-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.06);
  border-color: rgba(0, 0, 0, 0.15);
}

.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #000000, rgba(0, 0, 0, 0.4));
  opacity: 0;
  transition: opacity 0.3s ease;
}

.role-card:hover .card-glow {
  opacity: 1;
}

.card-content {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.card-icon-wrapper {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  background-color: #f5f5f5;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 24px;
  color: #000000;
  transition: background-color 0.3s ease;
}

.role-card:hover .card-icon-wrapper {
  background-color: #000000;
  color: #ffffff;
}

.card-icon {
  width: 28px;
  height: 28px;
}

.card-text h3 {
  font-size: 22px;
  font-weight: 500;
  color: #000000;
  margin-bottom: 12px;
}

.card-text p {
  font-size: 16px;
  line-height: 1.5;
  color: rgba(0, 0, 0, 0.5);
  margin-bottom: 32px;
}

.card-arrow {
  margin-top: auto;
  align-self: flex-end;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 1px solid rgba(0, 0, 0, 0.08);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #000000;
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}

.role-card:hover .card-arrow {
  background-color: #000000;
  color: #ffffff;
  border-color: #000000;
}

.arrow-svg {
  width: 16px;
  height: 16px;
}

/* Модальное окно */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
  padding: 20px;
}

.modal-card {
  background-color: #ffffff;
  max-width: 480px;
  width: 100%;
  padding: 40px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  text-align: center;
  border: 1px solid rgba(0, 0, 0, 0.08);
}

.modal-card h3 {
  font-size: 24px;
  font-weight: 500;
  margin-bottom: 16px;
  color: #000000;
}

.modal-card p {
  font-size: 16px;
  line-height: 1.6;
  color: rgba(0, 0, 0, 0.6);
  margin-bottom: 16px;
}

.modal-btn {
  width: 100%;
  height: 60px;
  background-color: #000000;
  color: #ffffff;
  font-size: 16px;
  border: none;
  cursor: pointer;
  margin-top: 24px;
  transition: opacity 0.2s ease;
}

.modal-btn:hover {
  opacity: 0.9;
}

/* Анимация Transition */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
