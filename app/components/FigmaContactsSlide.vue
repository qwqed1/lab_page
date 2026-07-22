<script setup>
import { ref } from 'vue'

const emit = defineEmits(['register', 'quiz', 'navigate'])
const activeTab = ref('contacts') // 'contacts' | 'navigation'
</script>

<template>
  <section class="figma-exact-contacts" aria-labelledby="contacts-title">
    <div class="exact-contacts-body">
      <header class="exact-contacts-header">
        <h2 id="contacts-title">Тест на аллергию ALEX² — один анализ, который даёт ответы</h2>

        <button class="exact-contacts-cta" type="button" @click="emit('register')">
          <span>Записаться на тест на аллергию</span>
          <img src="/assets/figma-contact-arrow.svg" alt="">
        </button>
      </header>

      <div class="exact-contacts-columns">
        <div class="mobile-tabs-header">
          <button
            type="button"
            class="tab-title"
            :class="{ active: activeTab === 'contacts' }"
            @click="activeTab = 'contacts'"
          >
            Контакты
          </button>
          <button
            type="button"
            class="tab-title"
            :class="{ active: activeTab === 'navigation' }"
            @click="activeTab = 'navigation'"
          >
            Навигация по сайту
          </button>
        </div>
        <div class="exact-column-rule" />

        <!-- Contacts Column (Desktop always, Mobile when activeTab === 'contacts') -->
        <section
          class="exact-contacts-column exact-contacts-info"
          :class="{ 'mobile-hidden': activeTab !== 'contacts' }"
        >
          <h3 class="desktop-only-heading">Контакты</h3>

          <div class="exact-contacts-links">
            <a href="https://yandex.ru/maps/?text=Москва%2C%20Пречистенка%2030%2F2" target="_blank" rel="noopener noreferrer">
              Москва, Пречистенка 30/2
            </a>
            <a href="tel:+74955076485">+7 495 507-64-85</a>
            <a href="mailto:info@kupitkartinu.ru">info@kupitkartinu.ru</a>
          </div>

          <div class="exact-contacts-legal">
            <span>ИНН: 9703021385</span>
            <span>ОГРН: 1207700425602</span>
            <span>КПП: 770301001</span>
          </div>
        </section>

        <!-- Site Navigation Column (Desktop always, Mobile when activeTab === 'navigation') -->
        <nav
          class="exact-contacts-column exact-site-navigation"
          :class="{ 'mobile-hidden': activeTab !== 'navigation' }"
          aria-label="Навигация по сайту"
        >
          <h3 class="desktop-only-heading">Навигация по сайту</h3>

          <div class="exact-site-links">
            <button type="button" class="exact-nav-link" @click="emit('navigate', 'slide-17')">Блог</button>
            <NuxtLink to="/personal-account" class="exact-nav-link">Личный кабинет</NuxtLink>
            <button type="button" class="exact-nav-link" @click="emit('register')">Сдать тест</button>
            <button type="button" class="exact-nav-link" @click="emit('quiz')">Квиз</button>
            <NuxtLink to="/search" class="exact-nav-link">Поиск аллергенов</NuxtLink>
            <NuxtLink to="/demo-result" class="exact-nav-link">Демо-результат</NuxtLink>
            <button type="button" class="exact-nav-link" @click="emit('navigate', 'slide-2')">Лаборатория ALEX2</button>
          </div>
        </nav>
      </div>

      <footer class="exact-contacts-footer" :class="{ 'nav-tab-active': activeTab === 'navigation' }">
        <div v-if="activeTab === 'contacts'" class="exact-policy-links">
          <a href="/policy">Политика конфиденциальности</a>
          <a href="/terms">Условия использования материалов сайта</a>
        </div>

        <div class="exact-studio-credit">
          <img src="/assets/figma-studio-logo.svg" alt="">
          <span>сайт сделан в студии «созерцание»</span>
        </div>
      </footer>
    </div>
  </section>
</template>

<style scoped>
.figma-exact-contacts {
  --ux: calc(100cqw / 1243);
  --uy: calc(100cqh / 1080);
  --ui: min(var(--ux), var(--uy));
  position: absolute;
  inset: 0;
  overflow: hidden;
  container-type: size;
  color: #000;
  font-family: 'Roboto', Arial, sans-serif;
}

.exact-contacts-body {
  position: absolute;
  left: calc(64 * var(--ux));
  top: calc(534 * var(--uy));
  width: calc(1115 * var(--ux));
  height: calc(482 * var(--ui));
}

.exact-contacts-header {
  position: absolute;
  inset: 0 auto auto 0;
  width: 100%;
  height: calc(129 * var(--ui));
}

.exact-contacts-header h2 {
  width: 100%;
  margin: 0;
  font-size: min(24px, calc(24 * var(--ui)));
  font-weight: 400;
  line-height: min(28px, calc(28 * var(--ui)));
  white-space: nowrap;
}

.exact-contacts-cta {
  position: absolute;
  left: 0;
  top: calc(49 * var(--ui));
  width: 100%;
  height: calc(80 * var(--ui));
  min-height: 48px;
  padding: 0 calc(24 * var(--ui));
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: #000;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #fff;
  font: inherit;
  font-size: clamp(15px, calc(21 * var(--ui)), 21px);
  font-weight: 400;
  line-height: 1;
  text-align: left;
  cursor: pointer;
}

.exact-contacts-cta img {
  width: calc(32 * var(--ui));
  height: calc(32 * var(--ui));
  min-width: 22px;
  min-height: 22px;
  flex: 0 0 auto;
}

.mobile-tabs-header {
  display: none;
}

.desktop-only-heading {
  display: block;
}

.exact-contacts-columns {
  position: absolute;
  left: 0;
  top: calc(177 * var(--ui));
  width: 100%;
  height: max(140px, calc(215 * var(--ui)));
}

.exact-contacts-columns::after {
  content: '';
  position: absolute;
  left: 0;
  top: calc(36 * var(--ui));
  width: 100%;
  height: 1px;
  background: rgba(0, 0, 0, 0.2);
}

.exact-contacts-column {
  position: absolute;
  top: 0;
  height: 100%;
}

.exact-contacts-info {
  left: 0;
  width: calc(299 * var(--ux));
}

.exact-site-navigation {
  left: calc(331 * var(--ux));
  width: calc(784 * var(--ux));
}

.exact-contacts-column h3 {
  height: max(18px, calc(25 * var(--ui)));
  margin: 0;
  font-size: clamp(15px, calc(21 * var(--ui)), 21px);
  font-weight: 400;
  line-height: max(18px, calc(25 * var(--ui)));
}

.exact-column-rule {
  display: none;
}

.exact-contacts-links,
.exact-site-links,
.exact-contacts-legal {
  position: absolute;
  left: 0;
  display: flex;
  flex-direction: column;
}

.exact-contacts-links,
.exact-site-links {
  top: calc(57 * var(--ui));
  gap: calc(8 * var(--ui));
}

.exact-contacts-links a,
.exact-site-links a,
.exact-site-links button,
.exact-nav-link,
.exact-policy-links a {
  width: fit-content;
  margin: 0;
  padding: 0;
  border: 0;
  background: transparent;
  color: inherit;
  font: inherit;
  font-size: clamp(13px, calc(16 * var(--ui)), 16px);
  font-weight: 400;
  line-height: max(1em, calc(19 * var(--ui)));
  text-align: left;
  text-decoration: none;
  cursor: pointer;
}

.exact-contacts-links a:hover,
.exact-site-links a:hover,
.exact-site-links button:hover,
.exact-nav-link:hover,
.exact-policy-links a:hover {
  text-decoration: underline;
}

.exact-contacts-legal {
  top: calc(151 * var(--ui));
  gap: calc(8 * var(--ui));
  color: rgba(0, 0, 0, 0.4);
}

.exact-contacts-legal span {
  font-size: clamp(11px, calc(14 * var(--ui)), 14px);
  line-height: max(1em, calc(16 * var(--ui)));
}

.exact-contacts-footer {
  position: absolute;
  left: 0;
  top: calc(440 * var(--ui));
  width: 100%;
  height: calc(42 * var(--ui));
}

.exact-policy-links {
  position: absolute;
  left: 0;
  top: 0;
  display: flex;
  flex-direction: column;
  gap: calc(8 * var(--ui));
}

.exact-policy-links a {
  color: rgba(0, 0, 0, 0.4);
  font-size: clamp(11px, calc(14 * var(--ui)), 14px);
  line-height: max(1em, calc(16 * var(--ui)));
  text-decoration: none;
}

.exact-policy-links a:hover {
  text-decoration: none;
}

.exact-studio-credit {
  position: absolute;
  left: calc(919 * var(--ux));
  top: auto;
  bottom: 0;
  width: calc(196 * var(--ux));
  height: calc(28 * var(--ui));
  color: rgba(0, 0, 0, 0.32);
}

.exact-studio-credit img {
  position: absolute;
  left: calc(-20 * var(--ui));
  top: calc(2.5 * var(--ui));
  width: calc(52 * var(--ui));
  height: calc(23 * var(--ui));
  display: block;
}

.exact-studio-credit span {
  position: absolute;
  left: calc(50 * var(--ui));
  top: 0;
  width: calc(146 * var(--ui));
  height: calc(28 * var(--ui));
  font-family: 'Roboto', Arial, sans-serif;
  font-size: calc(12 * var(--ui));
  font-weight: 400;
  line-height: normal;
  text-transform: uppercase;
}

@media (max-width: 700px) {
  .figma-exact-contacts {
    --mu: calc(100cqw / 420);
  }

  .exact-contacts-body {
    left: calc(16 * var(--mu));
    top: calc(100cqh - 682 * var(--mu));
    width: calc(388 * var(--mu));
    height: calc(584 * var(--mu));
  }

  .exact-contacts-header {
    width: calc(388 * var(--mu));
    height: calc(45 * var(--mu));
  }

  .exact-contacts-header h2 {
    width: calc(388 * var(--mu));
    font-size: calc(24 * var(--mu));
    line-height: calc(28 * var(--mu));
    white-space: normal;
  }

  .exact-contacts-cta {
    display: none;
  }

  .mobile-tabs-header {
    display: flex;
    gap: calc(21 * var(--mu));
    align-items: center;
    width: 100%;
    height: calc(25 * var(--mu));
  }

  .tab-title {
    padding: 0;
    margin: 0;
    border: 0;
    background: transparent;
    font-family: 'Roboto', Arial, sans-serif;
    font-size: calc(21 * var(--mu));
    font-weight: 400;
    line-height: calc(25 * var(--mu));
    color: #000;
    opacity: 0.3;
    cursor: pointer;
    white-space: nowrap;
  }

  .tab-title.active {
    opacity: 1;
  }

  .desktop-only-heading {
    display: none !important;
  }

  .exact-contacts-columns {
    top: calc(93 * var(--mu));
    width: calc(388 * var(--mu));
    height: calc(328 * var(--mu));
  }

  .exact-contacts-columns::after {
    top: calc(36 * var(--mu));
  }

  .exact-contacts-info {
    left: 0;
    width: calc(170 * var(--mu));
  }

  .exact-contacts-info.mobile-hidden,
  .exact-site-navigation.mobile-hidden {
    display: none !important;
  }

  .exact-site-navigation {
    left: 0 !important;
    width: 100% !important;
    top: calc(57 * var(--mu));
    height: auto !important;
  }

  .exact-contacts-column h3 {
    height: calc(25 * var(--mu));
    font-size: calc(21 * var(--mu));
    line-height: calc(25 * var(--mu));
    white-space: nowrap;
  }

  .exact-column-rule {
    top: calc(36 * var(--mu));
  }

  .exact-contacts-links {
    top: calc(57 * var(--mu));
    gap: calc(8 * var(--mu));
  }

  .exact-site-links {
    display: flex !important;
    flex-direction: column !important;
    gap: calc(2 * var(--mu)) !important;
    position: static !important;
    top: auto !important;
    width: 100% !important;
  }

  .exact-nav-link {
    display: flex;
    align-items: center;
    width: 100%;
    height: calc(37 * var(--mu));
    padding: calc(12 * var(--mu)) 0;
    border: 0;
    background: transparent;
    color: #000;
    font-family: 'Roboto', Arial, sans-serif;
    font-size: calc(18 * var(--mu));
    font-weight: 400;
    line-height: 1;
    text-align: left;
    text-decoration: none;
    cursor: pointer;
  }

  .exact-contacts-links a {
    font-size: calc(16 * var(--mu));
    line-height: calc(19 * var(--mu));
    white-space: nowrap;
  }

  .exact-contacts-legal {
    top: calc(151 * var(--mu));
    gap: calc(8 * var(--mu));
  }

  .exact-contacts-legal span {
    font-size: calc(14 * var(--mu));
    line-height: calc(16 * var(--mu));
    white-space: nowrap;
  }

  .exact-contacts-footer {
    top: calc(513 * var(--mu));
    width: calc(388 * var(--mu));
    height: calc(71 * var(--mu));
  }

  .exact-contacts-footer.nav-tab-active {
    top: calc(513 * var(--mu));
  }

  .exact-policy-links {
    gap: calc(8 * var(--mu));
  }

  .exact-policy-links a {
    font-size: calc(14 * var(--mu));
    line-height: calc(16 * var(--mu));
    white-space: nowrap;
  }

  .exact-studio-credit {
    left: 0;
    right: auto;
    top: auto;
    bottom: 0;
    width: calc(196 * var(--mu));
    height: calc(71 * var(--mu));
    transform: none;
  }

  .exact-studio-credit img {
    left: 0;
    top: 0;
    width: calc(70 * var(--mu));
    height: calc(31 * var(--mu));
    opacity: 0.3;
  }

  .exact-studio-credit span {
    left: 0;
    top: calc(39 * var(--mu));
    width: calc(193 * var(--mu));
    height: calc(32 * var(--mu));
    font-size: calc(14 * var(--mu));
    line-height: calc(16 * var(--mu));
    opacity: 0.3;
    text-transform: lowercase;
  }
}

@media (min-width: 701px) and (max-width: 1440px) {
  .exact-contacts-footer {
    top: calc(440 * var(--uy));
    height: calc(42 * var(--uy));
  }

  .exact-studio-credit {
    left: auto;
    right: 0;
    bottom: 0;
    width: 196px;
    height: 28px;
    transform: scale(1.5);
    transform-origin: right bottom;
  }

  .exact-studio-credit img {
    left: -20px;
    top: 2.5px;
    width: 52px;
    height: 23px;
  }

  .exact-studio-credit span {
    left: 50px;
    width: 146px;
    height: 28px;
    font-size: 12px;
  }
}
</style>
