<script setup>
import { ref } from 'vue'

const emit = defineEmits(['register', 'quiz', 'navigate'])
const activeTab = ref('contacts') // 'contacts' | 'navigation'
</script>

<template>
  <section class="figma-exact-contacts" aria-labelledby="contacts-title">
    <!-- =========================================================================
         1. DESKTOP VIEW (min-width: 701px) - Matches Figma Node 109:102 exactly
         ========================================================================= -->
    <div class="contacts-desktop-root desktop-only-container">
      <div class="exact-contacts-body-desktop">
        <!-- Desktop Header + CTA Banner -->
        <div class="desktop-contacts-header">
          <h2 id="contacts-title">Тест на аллергию ALEX² — один анализ, который даёт ответы</h2>

          <button class="desktop-cta-banner" type="button" @click="emit('register')">
            <span class="cta-banner-text">Записаться на тест на аллергию</span>
            <div class="cta-banner-icon" aria-hidden="true">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="16" cy="16" r="14" stroke="white" stroke-width="2"/>
                <path d="M14 11L19 16L14 21" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </button>
        </div>

        <!-- Desktop 2 Columns -->
        <div class="desktop-contacts-columns">
          <!-- Column 1: Contacts -->
          <div class="desktop-col contacts-col">
            <h3 class="col-heading">Контакты</h3>
            <div class="col-rule"></div>

            <div class="contacts-info-group">
              <a href="https://yandex.ru/maps/?text=Москва%2C%20Пречистенка%2030%2F2" target="_blank" rel="noopener noreferrer" class="contact-item-link">
                Москва, Пречистенка 30/2
              </a>
              <a href="tel:+74955076485" class="contact-item-link">+7 495 507-64-85</a>
              <a href="mailto:info@kupitkartinu.ru" class="contact-item-link">info@kupitkartinu.ru</a>
            </div>

            <div class="legal-info-group">
              <span>ИНН: 9703021385</span>
              <span>ОГРН: 1207700425602</span>
              <span>КПП: 770301001</span>
            </div>
          </div>

          <!-- Column 2: Site Navigation -->
          <div class="desktop-col navigation-col">
            <h3 class="col-heading">Навигация по сайту</h3>
            <div class="col-rule"></div>

            <div class="site-nav-links-grid">
              <NuxtLink to="/search" class="desktop-nav-item">Поиск аллергентов</NuxtLink>
              <NuxtLink to="/demo-result" class="desktop-nav-item">Демо-результат</NuxtLink>
              <button type="button" class="desktop-nav-item" @click="emit('quiz')">КВИЗ: Нужен ли вам тест</button>
              <NuxtLink to="/personal-account" class="desktop-nav-item">Личный кабинет</NuxtLink>
              <button type="button" class="desktop-nav-item" @click="emit('navigate', 'slide-2')">О лаборатории ALEXLAB</button>
              <button type="button" class="desktop-nav-item" @click="emit('navigate', 'slide-17')">Блог</button>
            </div>
          </div>
        </div>

        <!-- Desktop Footer -->
        <footer class="desktop-contacts-footer">
          <div class="desktop-policy-links">
            <a href="/policy">Политика конфиденциальности</a>
            <a href="/terms">Условия использования материалов сайта</a>
          </div>

          <div class="desktop-studio-credit">
            <img src="/assets/figma-studio-logo.svg" alt="" />
            <span>сайт сделан в студии «созерцание»</span>
          </div>
        </footer>
      </div>
    </div>

    <!-- =========================================================================
         2. MOBILE VIEW (max-width: 700px) - Matches Figma Mobile Frames 1 & 2
         ========================================================================= -->
    <div class="contacts-mobile-root mobile-only-container">
      <div class="mobile-contacts-body">
        <!-- Title -->
        <header class="mobile-contacts-header">
          <h2>Тест на аллергию ALEX² — один анализ, который даёт ответы</h2>
        </header>

        <!-- Main Tabs Section -->
        <div class="mobile-contacts-main">
          <!-- Tab Buttons Row -->
          <div class="mobile-tabs-row">
            <button
              type="button"
              class="mobile-tab-btn"
              :class="{ active: activeTab === 'contacts' }"
              @click="activeTab = 'contacts'"
            >
              Контакты
            </button>
            <button
              type="button"
              class="mobile-tab-btn"
              :class="{ active: activeTab === 'navigation' }"
              @click="activeTab = 'navigation'"
            >
              Навигация по сайту
            </button>
          </div>
          <div class="mobile-tab-rule"></div>

          <!-- Tab Content 1: Contacts -->
          <div v-show="activeTab === 'contacts'" class="mobile-tab-content contacts-tab-content">
            <div class="mobile-contacts-list">
              <a href="https://yandex.ru/maps/?text=Москва%2C%20Пречистенка%2030%2F2" target="_blank" rel="noopener noreferrer">
                Москва, Пречистенка 30/2
              </a>
              <a href="tel:+74955076485">+7 495 507-64-85</a>
              <a href="mailto:info@kupitkartinu.ru">info@kupitkartinu.ru</a>
            </div>

            <div class="mobile-legal-list">
              <span>ИНН: 9703021385</span>
              <span>ОГРН: 1207700425602</span>
              <span>КПП: 770301001</span>
            </div>

            <div class="mobile-policy-list">
              <a href="/policy">Политика конфиденциальности</a>
              <a href="/terms">Условия использования материалов сайта</a>
            </div>
          </div>

          <!-- Tab Content 2: Navigation -->
          <div v-show="activeTab === 'navigation'" class="mobile-tab-content navigation-tab-content">
            <div class="mobile-nav-list">
              <button type="button" class="mobile-nav-link" @click="emit('navigate', 'slide-17')">Блог</button>
              <NuxtLink to="/personal-account" class="mobile-nav-link">Личный кабинет</NuxtLink>
              <button type="button" class="mobile-nav-link" @click="emit('register')">Сдать тест</button>
              <button type="button" class="mobile-nav-link" @click="emit('quiz')">Квиз</button>
              <NuxtLink to="/search" class="mobile-nav-link">Поиск аллергенов</NuxtLink>
              <NuxtLink to="/demo-result" class="mobile-nav-link">Демо-результат</NuxtLink>
              <button type="button" class="mobile-nav-link" @click="emit('navigate', 'slide-2')">Лаборатория ALEX2</button>
            </div>
          </div>
        </div>

        <!-- Studio Credit Footer -->
        <footer class="mobile-contacts-footer">
          <div class="mobile-studio-credit">
            <img src="/assets/figma-studio-logo.svg" alt="" />
            <span>сайт сделан в студии «созерцание»</span>
          </div>
        </footer>
      </div>
    </div>
  </section>
</template>

<style scoped>
.figma-exact-contacts {
  position: absolute;
  inset: 0;
  overflow: hidden;
  container-type: size;
  color: #000;
  font-family: 'Roboto', Arial, sans-serif;
}

/* ==========================================================================
   DESKTOP STYLES (min-width: 701px)
   ========================================================================== */
@media (min-width: 1025px) {
  .mobile-only-container {
    display: none !important;
  }

  .desktop-only-container {
    display: block !important;
    position: absolute;
    inset: 0;
    --ux: calc(100cqw / 1243);
    --uy: calc(100cqh / 1080);
    --ui: min(var(--ux), var(--uy));
  }

  .exact-contacts-body-desktop {
    position: absolute;
    left: calc(64 * var(--ux));
    top: calc(534 * var(--uy));
    width: calc(1115 * var(--ux));
    height: calc(482 * var(--ui));
  }

  .desktop-contacts-header {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: calc(32 * var(--ui));
  }

  .desktop-contacts-header h2 {
    width: 100%;
    margin: 0;
    font-size: 24px;
    font-weight: 400;
    line-height: 28px;
    color: #000000;
    white-space: nowrap;
  }

  .desktop-cta-banner {
    width: 100%;
    height: calc(80 * var(--ui));
    background: #000000;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: calc(24 * var(--ui));
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    transition: background 0.2s ease;
  }

  .desktop-cta-banner:hover {
    background: #1a1a1a;
  }

  .cta-banner-text {
    font-size: calc(21 * var(--ui));
    font-weight: 400;
    color: #ffffff;
  }

  .cta-banner-icon {
    width: calc(32 * var(--ui));
    height: calc(32 * var(--ui));
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .cta-banner-icon svg {
    width: 100%;
    height: 100%;
  }

  .desktop-contacts-columns {
    position: absolute;
    left: 0;
    top: calc(177 * var(--ui));
    width: 100%;
    display: flex;
    gap: calc(32 * var(--ux));
  }

  .contacts-col {
    width: calc(299 * var(--ux));
    flex-shrink: 0;
  }

  .navigation-col {
    width: calc(784 * var(--ux));
    flex-grow: 1;
  }

  .col-heading {
    margin: 0 0 calc(21 * var(--ui)) 0;
    font-size: calc(21 * var(--ui));
    font-weight: 400;
    color: #000000;
    line-height: calc(25 * var(--ui));
  }

  .col-rule {
    width: 100%;
    height: 1px;
    background: rgba(0, 0, 0, 0.2);
    margin-bottom: calc(21 * var(--ui));
  }

  .contacts-info-group {
    display: flex;
    flex-direction: column;
    gap: calc(8 * var(--ui));
    margin-bottom: calc(21 * var(--ui));
  }

  .contact-item-link {
    font-size: calc(16 * var(--ui));
    font-weight: 400;
    color: #000000;
    line-height: calc(19 * var(--ui));
    text-decoration: none;
  }

  .contact-item-link:hover,
  .desktop-nav-item:hover,
  .desktop-policy-links a:hover {
    text-decoration: underline;
  }

  .legal-info-group {
    display: flex;
    flex-direction: column;
    gap: calc(8 * var(--ui));
    color: rgba(0, 0, 0, 0.4);
    font-size: calc(14 * var(--ui));
    font-weight: 400;
    line-height: calc(16 * var(--ui));
  }

  .site-nav-links-grid {
    display: flex;
    flex-direction: column;
    gap: calc(8 * var(--ui));
  }

  .desktop-nav-item {
    width: fit-content;
    margin: 0;
    padding: 0;
    border: 0;
    background: transparent;
    color: #000000;
    font-family: 'Roboto', Arial, sans-serif;
    font-size: calc(16 * var(--ui));
    font-weight: 400;
    line-height: calc(19 * var(--ui));
    text-align: left;
    text-decoration: none;
    cursor: pointer;
  }

  .desktop-contacts-footer {
    position: absolute;
    left: 0;
    top: calc(440 * var(--ui));
    width: 100%;
    height: calc(42 * var(--ui));
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }

  .desktop-policy-links {
    display: flex;
    flex-direction: column;
    gap: calc(4 * var(--ui));
  }

  .desktop-policy-links a {
    font-size: calc(16 * var(--ui));
    font-weight: 400;
    color: #000000;
    line-height: calc(19 * var(--ui));
    text-decoration: none;
  }

  .desktop-studio-credit {
    display: flex;
    align-items: center;
    gap: calc(18 * var(--ui));
    color: rgba(0, 0, 0, 0.3);
  }

  .desktop-studio-credit img {
    width: calc(52 * var(--ui));
    height: calc(23 * var(--ui));
    flex-shrink: 0;
  }

  .desktop-studio-credit span {
    display: block;
    width: calc(146 * var(--ui));
    font-family: 'Roboto', Arial, sans-serif;
    font-size: calc(12 * var(--ui));
    font-weight: 400;
    line-height: calc(14 * var(--ui));
    color: rgba(0, 0, 0, 0.3);
    text-transform: uppercase;
    white-space: normal;
    word-wrap: break-word;
  }
}

/* ==========================================================================
   MOBILE STYLES (max-width: 700px) - FIGMA FRAME 1 & FRAME 2 SPECIFICATIONS
   ========================================================================== */
@media (max-width: 1024px) {
  .desktop-only-container {
    display: none !important;
  }

  .mobile-only-container {
    display: block !important;
    position: absolute;
    inset: 0;
  }
}

@media (max-width: 700px) {
  .mobile-only-container {
    --mu: calc(100cqw / 420);
  }

  .mobile-contacts-body {
    position: absolute;
    left: calc(16 * var(--mu));
    top: calc(100cqh - 682 * var(--mu));
    width: calc(388 * var(--mu));
    height: calc(584 * var(--mu));
  }

  .mobile-contacts-header {
    width: calc(388 * var(--mu));
  }

  .mobile-contacts-header h2 {
    width: calc(388 * var(--mu));
    margin: 0;
    font-size: calc(24 * var(--mu));
    font-weight: 400;
    line-height: calc(28 * var(--mu));
    color: #000000;
    white-space: normal;
  }

  .mobile-contacts-main {
    position: absolute;
    left: 0;
    top: calc(93 * var(--mu));
    width: calc(388 * var(--mu));
    height: calc(328 * var(--mu));
  }

  .mobile-tabs-row {
    display: flex;
    gap: calc(21 * var(--mu));
    height: calc(25 * var(--mu));
  }

  .mobile-tab-btn {
    font-family: 'Roboto', Arial, sans-serif;
    font-size: calc(21 * var(--mu));
    font-weight: 400;
    line-height: calc(25 * var(--mu));
    color: #000000;
    opacity: 0.3;
    background: transparent;
    border: none;
    padding: 0;
    margin: 0;
    cursor: pointer;
    white-space: nowrap;
    transition: opacity 0.2s ease;
  }

  .mobile-tab-btn.active {
    opacity: 1;
  }

  .mobile-tab-rule {
    width: calc(388 * var(--mu));
    height: 1px;
    background: rgba(0, 0, 0, 0.2);
    margin-top: calc(11 * var(--mu));
    margin-bottom: calc(20 * var(--mu));
  }

  .mobile-tab-content {
    position: absolute;
    left: 0;
    top: calc(57 * var(--mu));
    width: calc(388 * var(--mu));
  }

  .mobile-contacts-list {
    display: flex;
    flex-direction: column;
    gap: calc(8 * var(--mu));
    margin-bottom: calc(24 * var(--mu));
  }

  .mobile-contacts-list a {
    font-size: calc(16 * var(--mu));
    line-height: calc(19 * var(--mu));
    font-weight: 400;
    color: #000000;
    text-decoration: none;
    white-space: nowrap;
  }

  .mobile-legal-list {
    display: flex;
    flex-direction: column;
    gap: calc(8 * var(--mu));
    margin-bottom: calc(32 * var(--mu));
    color: rgba(0, 0, 0, 0.3);
  }

  .mobile-legal-list span {
    font-size: calc(14 * var(--mu));
    line-height: calc(16 * var(--mu));
    font-weight: 400;
    white-space: nowrap;
  }

  .mobile-policy-list {
    display: flex;
    flex-direction: column;
    gap: calc(8 * var(--mu));
  }

  .mobile-policy-list a {
    font-size: calc(14 * var(--mu));
    line-height: calc(16 * var(--mu));
    font-weight: 400;
    color: rgba(0, 0, 0, 0.3);
    text-decoration: none;
    white-space: nowrap;
  }

  .mobile-nav-list {
    display: flex;
    flex-direction: column;
    gap: calc(2 * var(--mu));
  }

  .mobile-nav-link {
    display: flex;
    align-items: center;
    width: 100%;
    height: calc(37 * var(--mu));
    padding: calc(12 * var(--mu)) 0;
    margin: 0;
    border: 0;
    background: transparent;
    color: #000000;
    font-family: 'Roboto', Arial, sans-serif;
    font-size: calc(18 * var(--mu));
    font-weight: 400;
    line-height: 1;
    text-align: left;
    text-decoration: none;
    cursor: pointer;
  }

  .mobile-contacts-footer {
    position: absolute;
    left: 0;
    top: calc(513 * var(--mu));
    width: calc(388 * var(--mu));
    height: calc(71 * var(--mu));
  }

  .mobile-studio-credit {
    position: absolute;
    left: 0;
    bottom: 0;
    width: calc(196 * var(--mu));
    height: calc(71 * var(--mu));
  }

  .mobile-studio-credit img {
    position: absolute;
    left: 0;
    top: 0;
    width: calc(70 * var(--mu));
    height: calc(31 * var(--mu));
  }

  .mobile-studio-credit span {
    position: absolute;
    left: 0;
    top: calc(39 * var(--mu));
    width: calc(193 * var(--mu));
    height: calc(32 * var(--mu));
    font-family: 'Roboto', Arial, sans-serif;
    font-size: calc(14 * var(--mu));
    font-weight: 400;
    line-height: calc(16 * var(--mu));
    color: rgba(0, 0, 0, 0.3);
    text-transform: uppercase;
  }
}

@media (min-width: 701px) and (max-width: 1024px) {
  .mobile-contacts-body {
    position: absolute;
    left: 40px;
    top: 180px;
    width: calc(100% - 80px);
    max-width: 600px;
    height: auto;
  }

  .mobile-contacts-header {
    width: 100%;
  }

  .mobile-contacts-header h2 {
    width: 100%;
    margin: 0;
    font-size: 24px;
    font-weight: 400;
    line-height: 28px;
    color: #000000;
    white-space: normal;
  }

  .mobile-contacts-main {
    position: relative;
    left: 0;
    top: 36px;
    width: 100%;
    height: auto;
  }

  .mobile-tabs-row {
    display: flex;
    gap: 32px;
    height: 32px;
  }

  .mobile-tab-btn {
    font-family: 'Roboto', Arial, sans-serif;
    font-size: 24px;
    font-weight: 400;
    line-height: 28px;
    color: #000000;
    opacity: 0.3;
    background: transparent;
    border: none;
    padding: 0;
    margin: 0;
    cursor: pointer;
    white-space: nowrap;
    transition: opacity 0.2s ease;
  }

  .mobile-tab-btn.active {
    opacity: 1;
  }

  .mobile-tab-rule {
    width: 100%;
    height: 1px;
    background: rgba(0, 0, 0, 0.2);
    margin-top: 12px;
    margin-bottom: 24px;
  }

  .mobile-tab-content {
    position: relative;
    left: 0;
    top: 0;
    width: 100%;
    min-height: 330px;
  }

  .mobile-contacts-list {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 28px;
  }

  .mobile-contacts-list a {
    font-size: 20px;
    line-height: 26px;
    font-weight: 400;
    color: #000000;
    text-decoration: none;
    white-space: nowrap;
  }

  .mobile-legal-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 32px;
    color: rgba(0, 0, 0, 0.3);
  }

  .mobile-legal-list span {
    font-size: 16px;
    line-height: 20px;
    font-weight: 400;
    white-space: nowrap;
  }

  .mobile-policy-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .mobile-policy-list a {
    font-size: 16px;
    line-height: 20px;
    font-weight: 400;
    color: rgba(0, 0, 0, 0.3);
    text-decoration: none;
    white-space: nowrap;
  }

  .mobile-nav-list {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .mobile-nav-link {
    display: flex;
    align-items: center;
    width: 100%;
    height: 44px;
    padding: 10px 0;
    margin: 0;
    border: 0;
    background: transparent;
    color: #000000;
    font-family: 'Roboto', Arial, sans-serif;
    font-size: 22px;
    font-weight: 400;
    line-height: 1;
    text-align: left;
    text-decoration: none;
    cursor: pointer;
  }

  .mobile-contacts-footer {
    position: relative;
    left: 0;
    top: 120px;
    width: 100%;
    height: auto;
  }

  .mobile-studio-credit {
    position: relative;
    left: 0;
    bottom: 0;
    width: 100%;
    height: auto;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .mobile-studio-credit img {
    position: relative;
    left: 0;
    top: 0;
    width: 80px;
    height: 35px;
  }

  .mobile-studio-credit span {
    position: relative;
    left: 0;
    top: 0;
    width: auto;
    height: auto;
    font-family: 'Roboto', Arial, sans-serif;
    font-size: 14px;
    font-weight: 400;
    line-height: 16px;
    color: rgba(0, 0, 0, 0.3);
    text-transform: uppercase;
  }
}

/* Height-tiered footer offsets for iPad Air (+20px) and iPad Pro (+40px) */
@media (min-width: 701px) and (max-width: 1024px) and (min-height: 1051px) and (max-height: 1250px) {
  .mobile-contacts-footer {
    top: 140px !important;
  }
}

@media (min-width: 701px) and (max-width: 1024px) and (min-height: 1251px) {
  .mobile-contacts-footer {
    top: 160px !important;
  }
}
</style>
