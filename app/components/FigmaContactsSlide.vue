<script setup>
const emit = defineEmits(['register', 'quiz', 'navigate'])
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
        <section class="exact-contacts-column exact-contacts-info">
          <h3>Контакты</h3>
          <div class="exact-column-rule" />

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

        <nav class="exact-contacts-column exact-site-navigation" aria-label="Навигация по сайту">
          <h3>Навигация по сайту</h3>
          <div class="exact-column-rule" />

          <div class="exact-site-links">
            <NuxtLink to="/search">Поиск аллергентов</NuxtLink>
            <NuxtLink to="/demo-result">Демо-результат</NuxtLink>
            <button type="button" @click="emit('quiz')">КВИЗ: Нужен ли вам тест</button>
            <NuxtLink to="/personal-account">Личный кабинет</NuxtLink>
            <button type="button" @click="emit('navigate', 'slide-2')">О лаборатории ALEXLAB</button>
            <button type="button" @click="emit('navigate', 'slide-17')">Блог</button>
          </div>
        </nav>
      </div>

      <footer class="exact-contacts-footer">
        <div class="exact-policy-links">
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
  top: calc(366 * var(--uy));
  width: calc(1115 * var(--ux));
  height: calc(644 * var(--ui));
}

.exact-contacts-header {
  position: absolute;
  inset: 0 auto auto 0;
  width: 100%;
  height: calc(210 * var(--ui));
}

.exact-contacts-header h2 {
  width: calc(954 * var(--ui));
  margin: 0;
  font-size: clamp(26px, calc(42 * var(--ui)), 42px);
  font-weight: 400;
  line-height: calc(49 * var(--ui));
}

.exact-contacts-cta {
  position: absolute;
  left: 0;
  top: calc(130 * var(--ui));
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

.exact-contacts-columns {
  position: absolute;
  left: 0;
  top: calc(274 * var(--ui));
  width: 100%;
  height: max(140px, calc(215 * var(--ui)));
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
  position: absolute;
  left: 0;
  top: calc(36 * var(--ui));
  width: 100%;
  height: 1px;
  background: rgba(0, 0, 0, 0.2);
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
  top: calc(553 * var(--ui));
  width: 100%;
  height: max(68px, calc(91 * var(--ui)));
}

.exact-policy-links {
  position: absolute;
  left: 0;
  top: calc(49 * var(--ui));
  display: flex;
  flex-direction: column;
  gap: calc(4 * var(--ui));
}

.exact-policy-links a {
  text-decoration: underline;
}

.exact-studio-credit {
  position: absolute;
  left: calc(919 * var(--ux));
  top: 0;
  width: calc(196 * var(--ux));
  height: max(68px, calc(91 * var(--ui)));
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: calc(18 * var(--ui));
  color: rgba(0, 0, 0, 0.32);
}

.exact-studio-credit img {
  width: calc(79 * var(--ui));
  height: calc(35 * var(--ui));
  display: block;
}

.exact-studio-credit span {
  width: calc(193 * var(--ui));
  font-size: clamp(11px, calc(16 * var(--ui)), 16px);
  font-weight: 400;
  line-height: max(1em, calc(19 * var(--ui)));
}

@media (max-width: 700px) {
  .exact-contacts-header h2 {
    width: 100%;
    font-size: clamp(23px, calc(42 * var(--ui)), 42px);
  }

  .exact-contacts-cta {
    padding-inline: 16px;
  }
}
</style>
