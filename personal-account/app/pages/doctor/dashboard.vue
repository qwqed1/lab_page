<template>
  <div class="doctor-page-layout">
    <!-- Шапка страницы (пустая или на главную как в макете, но в макете для дашборда шапки нет, хотя для других страниц есть. Сделаем её без кнопки Назад, или оставим только скрытую панель) -->
    <header class="header-nav dashboard-header">
      <div class="header-logo">ALEX LAB</div>
    </header>

    <main class="doctor-main-content">
      <div class="dashboard-container">
        <!-- Приветствие -->
        <h2 class="welcome-title">Добрый день,<br>Бурмистров Павел Сергеевич!</h2>

        <!-- Основная карточка с промокодом -->
        <div class="promo-card">
          <div class="promo-header">
            <span class="usage-count">Использовано 0 раз</span>
          </div>

          <div class="promo-body">
            <!-- Блок промокода -->
            <div class="code-display-wrapper" @click="copyPromoCode" title="Нажмите, чтобы скопировать">
              <span class="promo-code">{{ promoCode }}</span>
              <button class="copy-btn" aria-label="Скопировать промокод">
                <!-- Иконка копирования (два квадрата) -->
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M11 11H27V27H11V11Z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M5 21V5H21" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
              
              <!-- Уведомление о копировании -->
              <span class="copy-tooltip" :class="{ show: showTooltip }">Скопировано!</span>
            </div>

            <!-- Описание промокода -->
            <p class="promo-desc">
              Это ваш личный промокод — поделитесь им с вашими пациентами. Вы получите бонусные баллы, а пациент 10% скидки. Промокод вводится на странице корзина.
            </p>

            <!-- Ссылка подробнее -->
            <a href="#" @click.prevent="showMechanicInfo" class="mechanic-link">Подробнее о механике</a>
          </div>
        </div>

        <!-- Нижний блок кнопок -->
        <div class="dashboard-actions">
          <!-- Данные аккаунта -->
          <NuxtLink to="/doctor/profile" class="btn-outline dashboard-btn-left">
            <span>Данные аккаунта</span>
            <span class="btn-icon">
              <!-- Иконка профиля/пользователя -->
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </NuxtLink>

          <!-- Выйти из аккаунта -->
          <NuxtLink to="/doctor/login" class="btn-outline dashboard-btn-right">
            <span>Выйти из аккаунта</span>
            <span class="btn-icon">
              <!-- Иконка выхода -->
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

const promoCode = ref('FDOHJ8392NFJVJD')
const showTooltip = ref(false)

const copyPromoCode = async () => {
  try {
    await navigator.clipboard.writeText(promoCode.value)
    showTooltip.value = true
    setTimeout(() => {
      showTooltip.value = false
    }, 2000)
  } catch (err) {
    console.error('Не удалось скопировать промокод', err)
  }
}

const showMechanicInfo = () => {
  alert('Механика начисления: \nЗа каждого пациента, воспользовавшегося вашим промокодом, вы получаете 500 бонусных баллов на ваш счет. Пациент получает 10% скидку на любые лабораторные исследования.')
}
</script>

<style scoped>
.doctor-page-layout {
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

.doctor-main-content {
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

.welcome-title {
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  line-height: 1.16;
  text-align: center;
}

.promo-card {
  background-color: #ffffff;
  border: 1px solid #dfdfdf;
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 64px; /* gap 64px по макету */
}

.usage-count {
  font-size: 18px;
  color: #000000;
  font-weight: 400;
}

.promo-body {
  display: flex;
  flex-direction: column;
  gap: 16px; /* gap 16px по макету */
}

.code-display-wrapper {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  align-self: flex-start;
  transition: opacity 0.2s ease;
}

.code-display-wrapper:hover {
  opacity: 0.8;
}

.promo-code {
  font-size: 32px;
  font-weight: 400;
  color: #000000;
  letter-spacing: 0.05em;
  user-select: all;
}

.copy-btn {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4px;
}

.copy-tooltip {
  position: absolute;
  top: -30px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #000000;
  color: #ffffff;
  padding: 4px 8px;
  font-size: 12px;
  border-radius: 4px;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.2s ease, visibility 0.2s ease;
}

.copy-tooltip.show {
  opacity: 1;
  visibility: visible;
}

.promo-desc {
  font-size: 18px;
  line-height: 1.5;
  color: #000000;
  max-width: 471px; /* ширина по макету */
}

.mechanic-link {
  font-size: 18px;
  color: #000000;
  text-decoration: underline;
  align-self: flex-start;
}

.mechanic-link:hover {
  opacity: 0.7;
}

.dashboard-actions {
  display: flex;
  width: 100%;
}

.dashboard-btn-left {
  width: 394px; /* ширина по макету */
  border-right: none; /* чтобы не было двойной рамки */
}

.dashboard-btn-right {
  width: 411px; /* ширина по макету */
  flex-grow: 1;
}

@media (max-width: 600px) {
  .dashboard-actions {
    flex-direction: column;
  }
  .dashboard-btn-left {
    width: 100%;
    border-right: 1px solid rgba(0, 0, 0, 0.1);
    border-bottom: none;
  }
  .dashboard-btn-right {
    width: 100%;
  }
}
</style>
