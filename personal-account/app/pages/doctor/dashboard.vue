<template>
  <div class="doctor-page-layout">
    <!-- Шапка страницы -->
    <header class="header-nav dashboard-header">
      <div class="header-logo">ALEX LAB</div>
    </header>

    <main class="doctor-main-content">
      <div class="dashboard-container">
        <!-- Приветствие (42px на десктопе, 32px на мобильном) -->
        <h2 class="welcome-title">Добрый день,<br>Бурмистров Павел Сергеевич!</h2>

        <!-- Основная карточка с промокодом -->
        <div class="promo-card">
          <div class="promo-header">
            <span class="usage-count">Использовано 0 раз</span>
          </div>

          <div class="promo-body">
            <!-- ДЕСКТОПНАЯ ВЕРСИЯ: Текстовый промокод и кнопка скопировать (скрывается на мобильных) -->
            <div class="desktop-promo-wrapper">
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
            </div>

            <!-- МОБИЛЬНАЯ ВЕРСИЯ: QR-код (скрывается на десктопе) -->
            <div class="mobile-qr-wrapper">
              <div class="qr-code-svg-container" @click="copyPromoCode" title="Нажмите, чтобы скопировать промокод">
                <!-- Отрисовка QR-кода на базе SVG согласно Frame 1:743 -->
                <svg width="154" height="154" viewBox="0 0 154 154" fill="none" xmlns="http://www.w3.org/2000/svg" class="qr-svg">
                  <rect width="154" height="154" fill="white"/>
                  <!-- Угловой маркер: Верхний-Левый -->
                  <rect x="0" y="0" width="44" height="44" fill="black"/>
                  <rect x="6.28" y="6.28" width="31.42" height="31.42" fill="white"/>
                  <rect x="12.57" y="12.57" width="18.85" height="18.85" fill="black"/>

                  <!-- Угловой маркер: Верхний-Правый -->
                  <rect x="110" y="0" width="44" height="44" fill="black"/>
                  <rect x="116.28" y="6.28" width="31.42" height="31.42" fill="white"/>
                  <rect x="122.57" y="12.57" width="18.85" height="18.85" fill="black"/>

                  <!-- Угловой маркер: Нижний-Левый -->
                  <rect x="0" y="110" width="44" height="44" fill="black"/>
                  <rect x="6.28" y="116.28" width="31.42" height="31.42" fill="white"/>
                  <rect x="12.57" y="122.57" width="18.85" height="18.85" fill="black"/>

                  <!-- Выравнивающий маркер (внизу справа) -->
                  <rect x="116.28" y="116.28" width="18.85" height="18.85" fill="black"/>
                  <rect x="122.57" y="122.57" width="6.28" height="6.28" fill="white"/>
                  <rect x="128.85" y="128.85" width="6.28" height="6.28" fill="black"/>

                  <!-- Генеративные блоки QR-кода -->
                  <rect x="56.5" y="6.28" width="6.28" height="12.57" fill="black"/>
                  <rect x="75.4" y="0" width="12.57" height="6.28" fill="black"/>
                  <rect x="94.2" y="12.57" width="6.28" height="6.28" fill="black"/>
                  
                  <rect x="50.2" y="25.1" width="18.8" height="6.28" fill="black"/>
                  <rect x="81.7" y="18.8" width="6.28" height="12.57" fill="black"/>
                  <rect x="94.2" y="31.4" width="12.57" height="6.28" fill="black"/>

                  <rect x="6.28" y="56.5" width="12.57" height="6.28" fill="black"/>
                  <rect x="31.4" y="50.2" width="6.28" height="12.57" fill="black"/>
                  <rect x="50.2" y="50.2" width="12.57" height="6.28" fill="black"/>
                  <rect x="69.1" y="56.5" width="6.28" height="18.8" fill="black"/>
                  <rect x="87.9" y="50.2" width="18.8" height="6.28" fill="black"/>
                  <rect x="116.2" y="56.5" width="12.57" height="6.28" fill="black"/>
                  <rect x="138.2" y="50.2" width="6.28" height="12.57" fill="black"/>

                  <rect x="12.5" y="75.4" width="6.28" height="12.57" fill="black"/>
                  <rect x="31.4" y="81.7" width="12.57" height="6.28" fill="black"/>
                  <rect x="56.5" y="75.4" width="6.28" height="6.28" fill="black"/>
                  <rect x="81.7" y="75.4" width="12.57" height="12.57" fill="black"/>
                  <rect x="106.8" y="75.4" width="18.8" height="6.28" fill="black"/>
                  <rect x="131.9" y="81.7" width="12.57" height="12.57" fill="black"/>

                  <rect x="50.2" y="94.2" width="6.28" height="18.8" fill="black"/>
                  <rect x="69.1" y="100.5" width="12.57" height="6.28" fill="black"/>
                  <rect x="94.2" y="94.2" width="6.28" height="12.57" fill="black"/>
                  
                  <rect x="56.5" y="116.2" width="12.57" height="6.28" fill="black"/>
                  <rect x="81.7" y="122.5" width="6.28" height="18.8" fill="black"/>
                  <rect x="94.2" y="131.9" width="12.57" height="6.28" fill="black"/>
                  
                  <rect x="6.28" y="25.1" width="31.4" height="2" fill="black" opacity="0.3"/>
                  <rect x="25.1" y="6.28" width="2" height="31.4" fill="black" opacity="0.3"/>
                </svg>
              </div>
              <div class="qr-toast" :class="{ show: showTooltip }">Промокод скопирован!</div>
            </div>

            <!-- Описание промокода (18px) -->
            <p class="promo-desc">
              Это ваш личный промокод — поделитесь им с вашими пациентами. Вы получите ______, а пациент 10% скидки. Промокод вводится на странице корзина.
            </p>

            <!-- Ссылка подробнее (18px) -->
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
  alert('Механика начисления: \nЗа каждого пациента, воспользовавшегося вашим промокодом, вы получаете бонусные баллы на ваш счет. Пациент получает 10% скидку на любые лабораторные исследования.')
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

/* Мобильный QR-код и стили адаптивности */
.mobile-qr-wrapper {
  display: none;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  position: relative;
}

.qr-code-svg-container {
  width: 154px;
  height: 154px;
  border: 1px solid #dfdfdf;
  padding: 8px;
  background-color: #ffffff;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.qr-code-svg-container:hover {
  transform: scale(1.02);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.qr-svg {
  width: 100%;
  height: 100%;
}

.qr-toast {
  position: absolute;
  bottom: -36px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #000000;
  color: #ffffff;
  padding: 6px 12px;
  font-size: 14px;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.2s ease, visibility 0.2s ease;
  z-index: 5;
}

.qr-toast.show {
  opacity: 1;
  visibility: visible;
}

/* Стили адаптивности под мобильный макет Frame 1:734 */
@media (max-width: 768px) {
  .dashboard-container {
    width: 100%;
    gap: 32px; /* gap 32px на мобильных */
    padding: 0 16px;
  }
  
  .welcome-title {
    font-size: 32px; /* 32px по мобильному макету */
    text-align: left; /* Текст выравнивается по левому краю */
  }

  .promo-card {
    padding: 32px; /* Внутренний отступ 32px со всех сторон */
    gap: 64px; /* gap 64px сохраняется */
  }

  .usage-count {
    font-size: 16px; /* 16px на мобильных */
  }

  /* Переключение промокода на QR-код */
  .desktop-promo-wrapper {
    display: none;
  }

  .mobile-qr-wrapper {
    display: flex;
    align-self: flex-start; /* Прижимается к левой стороне по макету */
  }

  .promo-desc {
    font-size: 18px;
    max-width: 320px; /* Ширина 320px на мобильных */
  }

  .mechanic-link {
    font-size: 18px;
  }

  /* Смена раскладки кнопок на вертикальный стек */
  .dashboard-actions {
    flex-direction: column;
  }

  .dashboard-btn-left {
    width: 100% !important;
    height: 66px !important; /* Высота 66px */
    border: 1px solid #dfdfdf !important;
    border-bottom: none !important; /* Убираем двойную рамку посередине */
  }

  .dashboard-btn-right {
    width: 100% !important;
    height: 66px !important; /* Высота 66px */
    border: 1px solid #dfdfdf !important;
  }
}
</style>
