<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref } from 'vue'

useSeoMeta({
  title: 'Лаборатория ALEX LAB',
  description: 'Научно-исследовательский центр молекулярной генетики и биотехнологий ALEX LAB.'
})

const router = useRouter()
const activeTab = ref('about')
const licenseQuery = ref('')
const tabButtons = ref([])
const tabsScroller = ref(null)
const canScrollTabsLeft = ref(false)
const canScrollTabsRight = ref(false)
let tabsResizeObserver

const tabs = [
  { id: 'about', label: 'О нас' },
  { id: 'licenses', label: 'Лицензии' },
  { id: 'doctors', label: 'Врачи и эксперты' },
  { id: 'contacts', label: 'Контакты' },
  { id: 'privacy', label: 'Политика конфеденциальности', legal: true },
  { id: 'cookies', label: 'О cookie-файлах', legal: true }
]

const licenses = [
  { title: '№ Л041-01126-23/00345678', date: 'От 12.04.2022' },
  { title: 'Стандарт ISO', date: 'От 12.04.2024' },
  { title: 'Ежегодный аудит 2025', date: 'От 02.01.2025' },
  { title: '№ Л041-01126-23/00345678', date: 'От 12.04.2022' },
  { title: '№ Л041-01126-23/00345678', date: 'От 12.04.2022' },
  { title: 'Стандарт ISO', date: 'От 12.04.2024' },
  { title: 'Ежегодный аудит 2025', date: 'От 02.01.2025' },
  { title: 'Ежегодный аудит 2025', date: 'От 02.01.2025' }
]

const filteredLicenses = computed(() => {
  const query = licenseQuery.value.trim().toLocaleLowerCase('ru')
  if (!query) return licenses
  return licenses.filter(item => `${item.title} ${item.date}`.toLocaleLowerCase('ru').includes(query))
})

const doctors = Array.from({ length: 9 }, (_, index) => ({
  name: 'Александра Ковальчук',
  role: 'Профессор МГУ',
  materials: index === 1 ? '32 материала' : '6 материалов',
  image: `/assets/alexlab-doctor-${index + 1}.png`
}))

const legalText = `Дата последнего обновления: [укажите дату]

1. Общие положения
1.1. Настоящая Политика использования cookie-файлов (далее — «Политика») разъясняет, какие cookie-файлы и аналогичные технологии использует сайт [укажите адрес сайта] (далее — «Сайт»), принадлежащий [укажите наименование владельца сайта] (далее — «Компания», «IZICOSM», «мы»), а также для каких целей.
1.2. Используя Сайт и не отключая cookie-файлы в настройках браузера (либо подтвердив согласие во всплывающем уведомлении), Пользователь соглашается с условиями настоящей Политики.
1.3. Настоящая Политика является дополнением к Политике конфиденциальности Сайта и должна рассматриваться совместно с ней.

2. Что такое cookie-файлы
Cookie-файлы — это небольшие текстовые файлы, которые сохраняются на устройстве Пользователя (компьютере, смартфоне, планшете) при посещении сайта. Они позволяют сайту «запоминать» действия и предпочтения пользователя (например, содержимое корзины, язык интерфейса) на определённый период времени, чтобы не запрашивать эту информацию повторно при каждом переходе на страницу или при следующем визите.
Помимо классических cookie-файлов, Сайт может использовать аналогичные технологии: пиксельные теги, веб-маяки, локальное хранилище браузера (Local Storage) и идентификаторы устройства.

3. Какие cookie-файлы мы используем
3.1. Строго необходимые (технические) cookie-файлы
Обеспечивают базовую работу Сайта и не могут быть отключены в наших системах. Без них невозможна корректная работа корзины, авторизация в личном кабинете и оформление заказа.
Назначение — Срок хранения
Сохранение содержимого корзины покупок — в течение сессии или до 30 дней
Авторизация пользователя в личном кабинете — в течение сессии или до выхода из аккаунта
Запоминание согласия на использование cookie — до 12 месяцев
Защита от мошеннических действий, безопасность форм — в течение сессии

3.2. Функциональные cookie-файлы
Позволяют Сайту запоминать сделанные Пользователем настройки (язык, регион, валюта) для повышения удобства использования.
Запоминание языка и региона — до 12 месяцев
Запоминание ранее просмотренных товаров — до 6 месяцев

3.3. Аналитические cookie-файлы
Используются для сбора обезличенной статистики о посещаемости и поведении пользователей на Сайте (например, Google Analytics, Яндекс.Метрика). Помогают нам понимать, какие страницы и товары наиболее популярны, и улучшать работу Сайта.
Статистика посещений, источники трафика — до 24 месяцев
Анализ поведения на страницах (карты скроллов, кликов) — до 12 месяцев

3.4. Маркетинговые (рекламные) cookie-файлы
Используются для показа релевантной рекламы товаров IZICOSM на сторонних площадках (например, в социальных сетях, поисковых системах) и для оценки эффективности рекламных кампаний.
Ретаргетинг и показ персонализированной рекламы — до 12 месяцев
Оценка эффективности рекламных кампаний — до 12 месяцев
Конкретный перечень используемых сервисов (Google Ads, Facebook Pixel, VK Реклама и т. д.) рекомендуется уточнить и указать отдельным списком исходя из реально подключённых на Сайте инструментов.

4. Управление cookie-файлами
4.1. При первом посещении Сайта Пользователю отображается уведомление (cookie-баннер) с возможностью принять все cookie-файлы или настроить их по категориям (за исключением строго необходимых, которые включены всегда).
4.2. Пользователь может в любой момент изменить настройки cookie-файлов через панель настроек cookie на Сайте [укажите ссылку или способ доступа к настройкам, если есть] или через настройки своего браузера — большинство браузеров позволяют просматривать, удалять и блокировать cookie-файлы по отдельным сайтам или полностью.
4.3. Отключение строго необходимых cookie-файлов может привести к некорректной работе Сайта: ошибкам при оформлении заказа, потере содержимого корзины, невозможности авторизации.
4.4. Инструкции по управлению cookie-файлами для популярных браузеров:
Google Chrome: Настройки → Конфиденциальность и безопасность → Файлы cookie и другие данные сайтов;
Mozilla Firefox: Настройки → Приватность и защита → Куки и данные сайтов;
Safari: Настройки → Конфиденциальность → Управление данными веб-сайтов;
Microsoft Edge: Настройки → Файлы cookie и разрешения сайтов.

5. Cookie-файлы третьих лиц
Некоторые cookie-файлы на Сайте устанавливаются не самой Компанией, а партнёрскими сервисами (аналитика, реклама, виджеты социальных сетей). Использование таких cookie-файлов регулируется политиками конфиденциальности соответствующих третьих лиц. Мы рекомендуем ознакомиться с их условиями отдельно.

6. Изменения в Политике
Компания имеет право вносить изменения в настоящую Политику, например, при подключении новых сервисов аналитики или рекламы. Актуальная версия всегда доступна на данной странице. Дата последнего обновления указана в начале документа.

7. Контактная информация
По вопросам, связанным с использованием cookie-файлов на Сайте, можно обратиться:
Наименование организации: [укажите]
Адрес электронной почты: [укажите]
Телефон: [укажите]
Документ является шаблоном и предоставлен в информационных целях. Перед публикацией рекомендуется уточнить фактический перечень используемых на сайте cookie-сервисов и при необходимости проконсультироваться с юристом на предмет соответствия применимому законодательству (152-ФЗ, GDPR, ePrivacy Directive и др.).`

const goBack = () => {
  if (window.history.length > 1) router.back()
  else router.push('/')
}

const selectTab = async (tabId) => {
  activeTab.value = tabId
  await nextTick()
  window.scrollTo({ top: 0, left: 0 })
  const selectedButton = tabButtons.value.find(button => button?.dataset.tabId === tabId)
  const scroller = tabsScroller.value
  if (selectedButton && scroller) {
    const buttonLeft = selectedButton.offsetLeft
    const buttonRight = buttonLeft + selectedButton.offsetWidth
    const visibleLeft = scroller.scrollLeft
    const visibleRight = visibleLeft + scroller.clientWidth
    let nextScrollLeft = visibleLeft

    if (buttonLeft < visibleLeft) nextScrollLeft = buttonLeft
    else if (buttonRight > visibleRight) nextScrollLeft = buttonRight - scroller.clientWidth

    if (nextScrollLeft !== visibleLeft) {
      scroller.scrollTo({ left: nextScrollLeft, behavior: 'smooth' })
    }
  }
  requestAnimationFrame(() => {
    document.querySelector('.alexlab-scroll')?.scrollTo({ top: 0, behavior: 'smooth' })
  })
}

const updateTabsScrollState = () => {
  const scroller = tabsScroller.value
  if (!scroller) return
  const maxScrollLeft = scroller.scrollWidth - scroller.clientWidth
  canScrollTabsLeft.value = scroller.scrollLeft > 2
  canScrollTabsRight.value = maxScrollLeft - scroller.scrollLeft > 2
}

const scrollTabs = (direction) => {
  const scroller = tabsScroller.value
  if (!scroller) return
  scroller.scrollBy({
    left: direction * Math.max(220, scroller.clientWidth * 0.7),
    behavior: 'smooth'
  })
}

const handleTabKeydown = async (event, currentIndex) => {
  const lastIndex = tabs.length - 1
  const nextIndexByKey = {
    ArrowLeft: currentIndex === 0 ? lastIndex : currentIndex - 1,
    ArrowRight: currentIndex === lastIndex ? 0 : currentIndex + 1,
    Home: 0,
    End: lastIndex
  }
  const nextIndex = nextIndexByKey[event.key]
  if (nextIndex === undefined) return

  event.preventDefault()
  await selectTab(tabs[nextIndex].id)
  tabButtons.value[nextIndex]?.focus()
}

onMounted(async () => {
  await nextTick()
  updateTabsScrollState()
  tabsResizeObserver = new ResizeObserver(updateTabsScrollState)
  if (tabsScroller.value) tabsResizeObserver.observe(tabsScroller.value)
  window.addEventListener('resize', updateTabsScrollState)
})

onBeforeUnmount(() => {
  tabsResizeObserver?.disconnect()
  window.removeEventListener('resize', updateTabsScrollState)
})

const downloadLicense = (item) => {
  const blob = new Blob([`${item.title}\n${item.date}\nALEX LAB`], { type: 'text/plain;charset=utf-8' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = `${item.title.replaceAll(/[^\p{L}\p{N}]+/gu, '-')}.txt`
  link.click()
  URL.revokeObjectURL(url)
}
</script>

<template>
  <div class="alexlab-page site-sidebar-layout">
    <SiteSidebar
      class="alexlab-sidebar"
      @register="router.push('/cart')"
      @home="router.push('/')"
      @close="router.push('/')"
    />

    <main class="alexlab-shell">
      <button class="alexlab-back" type="button" aria-label="Вернуться назад" @click="goBack">
        <img src="/assets/alexlab-back.svg" alt="" width="24" height="24">
        <span>Назад</span>
      </button>

      <div class="alexlab-scroll">
        <div class="alexlab-content">
          <h1>Лаборатория ALEX LAB</h1>

          <div
            class="alexlab-tabs-shell"
            :class="{ 'has-left-arrow': canScrollTabsLeft, 'has-right-arrow': canScrollTabsRight }"
          >
            <button
              v-show="canScrollTabsLeft"
              class="alexlab-tabs-arrow alexlab-tabs-arrow-left"
              type="button"
              aria-label="Показать предыдущие разделы"
              @click="scrollTabs(-1)"
            >
              <img src="/assets/alexlab-back.svg" alt="" width="24" height="24">
            </button>

            <nav
              ref="tabsScroller"
              class="alexlab-tabs"
              aria-label="Разделы лаборатории"
              role="tablist"
              @scroll.passive="updateTabsScrollState"
            >
              <button
                v-for="(tab, index) in tabs"
                :key="tab.id"
                class="alexlab-tab"
                :class="{ active: activeTab === tab.id, legal: tab.legal }"
                :ref="element => { if (element) tabButtons[index] = element }"
                :data-tab-id="tab.id"
                type="button"
                role="tab"
                :aria-selected="activeTab === tab.id"
                :tabindex="activeTab === tab.id ? 0 : -1"
                @click="selectTab(tab.id)"
                @keydown="handleTabKeydown($event, index)"
              >
                {{ tab.label }}
              </button>
            </nav>

            <button
              v-show="canScrollTabsRight"
              class="alexlab-tabs-arrow alexlab-tabs-arrow-right"
              type="button"
              aria-label="Показать следующие разделы"
              @click="scrollTabs(1)"
            >
              <img src="/assets/alexlab-back.svg" alt="" width="24" height="24">
            </button>
          </div>

          <section v-if="activeTab === 'about'" class="alexlab-panel about-panel" role="tabpanel">
            <aside class="about-toc" aria-label="Содержание">
              <strong>Содержание</strong>
              <a href="#inside">Что внутри</a>
              <a href="#since-2001">Работаем с 2001</a>
            </aside>

            <p class="about-lead">
              Лаборатория Alex Lab — ведущий научно-исследовательский центр молекулярной генетики и биотехнологий, созданный в 2018 году. Мы объединили передовую науку и высокие технологии, чтобы сделать сложнейшую высокоточную диагностику доступной для каждого пациента. Наша главная миссия — внедрение инновационных медицинских тестов в повседневную врачебную практику для выявления скрытых угроз здоровью на самых ранних стадиях.
            </p>

            <div id="inside" class="about-section">
              <h2>Что внутри?</h2>
              <p>Производственный комплекс лаборатории оснащен роботизированными анализаторами последнего поколения от лидеров мирового рынка. Полная автоматизация процессов исключает человеческий фактор, гарантируя абсолютную точность результатов. Благодаря оптимизации логистики и собственной IT-платформе, мы сократили время ожидания: большинство сложных генетических исследований выполняются всего за 24 часа.</p>
              <p>Центр строго соблюдает принципы медицинской этики и гарантирует полную анонимность персональных данных. Каждый этап — от взятия биоматериала до выдачи заключения — защищен современными протоколами шифрования. Нам доверяют как частные пациенты, так и крупнейшие государственные и коммерческие клиники по всей стране.</p>
            </div>

            <div id="since-2001" class="about-section about-last-section">
              <h2>Работаем с 2001</h2>
              <p>Производственный комплекс лаборатории оснащен роботизированными анализаторами последнего поколения от лидеров мирового рынка. Полная автоматизация процессов исключает человеческий фактор, гарантируя абсолютную точность результатов. Благодаря оптимизации логистики и собственной IT-платформе, мы сократили время ожидания: большинство сложных генетических исследований выполняются всего за 24 часа.</p>
            </div>
          </section>

          <section v-else-if="activeTab === 'licenses'" class="alexlab-panel licenses-panel" role="tabpanel">
            <label class="license-search">
              <span class="sr-only">Поиск по лицензиям</span>
              <input v-model="licenseQuery" type="search" placeholder="Поиск">
              <img src="/assets/alexlab-search.svg" alt="" width="24" height="24">
            </label>

            <div class="license-list" aria-live="polite">
              <article v-for="(item, index) in filteredLicenses" :key="`${item.title}-${index}`" class="license-card">
                <div>
                  <h2>{{ item.title }}</h2>
                  <p>{{ item.date }}</p>
                </div>
                <button type="button" :aria-label="`Скачать ${item.title}`" @click="downloadLicense(item)">
                  <img src="/assets/alexlab-download.svg" alt="" width="24" height="24">
                </button>
              </article>
              <p v-if="filteredLicenses.length === 0" class="license-empty">Ничего не найдено</p>
            </div>
          </section>

          <section v-else-if="activeTab === 'doctors'" class="alexlab-panel doctors-panel" role="tabpanel">
            <h2 class="doctors-count">
              <span class="desktop-count">Всего 482 специалиста</span>
              <span class="mobile-count">Всего 482 автора</span>
            </h2>
            <div class="doctor-grid">
              <article v-for="doctor in doctors" :key="doctor.image" class="doctor-card">
                <img class="doctor-photo" :src="doctor.image" :alt="doctor.name" width="317" height="317">
                <div class="doctor-copy">
                  <h3>{{ doctor.name }}</h3>
                  <p>{{ doctor.role }}</p>
                </div>
                <span class="doctor-badge">{{ doctor.materials }}</span>
              </article>
            </div>
          </section>

          <section v-else-if="activeTab === 'contacts'" class="alexlab-panel contacts-panel" role="tabpanel">
            <div class="contact-map">
              <div class="map-placeholder" role="img" aria-label="Карта">Карта</div>
              <article class="contact-card">
                <div class="contact-details">
                  <p class="office-label">Главный офис</p>
                  <h2>Москва, Пречистенка 30/2</h2>
                  <div class="contact-links">
                    <a href="tel:+74955076485">+7 495 507-64-85</a>
                    <a href="mailto:alex@lab.com">alex@lab.com</a>
                  </div>
                  <dl class="office-hours">
                    <dt>ПН — ПТ</dt><dd>9:00 — 19:00</dd>
                    <dt>СБ — ВС</dt><dd>Выходные</dd>
                  </dl>
                </div>
                <a class="map-link" href="https://yandex.ru/maps/?text=Москва%2C%20Пречистенка%2030%2F2" target="_blank" rel="noopener noreferrer">
                  <span>Открыть на картах</span>
                  <img src="/assets/alexlab-map-arrow.svg" alt="" width="24" height="24">
                </a>
              </article>
            </div>

            <div class="company-info">
              <p><span>ИНН:</span> 9703021385</p>
              <p><span>ОГРН:</span> 1207700425602</p>
              <p><span>КПП:</span> 770301001</p>
              <div class="social-links" aria-label="Социальные сети">
                <a href="#" aria-label="Telegram"><img src="/assets/alexlab-telegram.svg" alt="" width="56" height="56"></a>
                <a href="#" aria-label="ВКонтакте"><img src="/assets/alexlab-vk.svg" alt="" width="57" height="56"></a>
                <a href="#" aria-label="YouTube"><img src="/assets/alexlab-youtube.svg" alt="" width="76" height="56"></a>
              </div>
            </div>
          </section>

          <section v-else class="alexlab-panel legal-panel" role="tabpanel">
            <div class="legal-copy">{{ legalText }}</div>
          </section>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
.alexlab-page {
  width: 100vw;
  height: 100dvh;
  overflow: hidden;
  display: grid;
  grid-template-columns: minmax(420px, 677px) minmax(0, 1fr);
  background: #f5f5f5;
  color: #000;
  font-family: Roboto, Arial, sans-serif;
}

.alexlab-shell {
  position: relative;
  min-width: 0;
  height: 100dvh;
  overflow: hidden;
  background: #f5f5f5;
}

.alexlab-back {
  position: absolute;
  z-index: 5;
  inset: 0 0 auto 0;
  height: 72px;
  padding: 0 32px;
  border: 1px solid #dfdfdf;
  background: #fff;
  display: flex;
  align-items: center;
  gap: 8px;
  color: #000;
  font-size: 17px;
  line-height: 20px;
  cursor: pointer;
}

.alexlab-back img {
  width: 24px;
  height: 24px;
}

.alexlab-scroll {
  position: absolute;
  inset: 72px 0 0;
  overflow-x: hidden;
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
}

.alexlab-content {
  min-height: 100%;
  padding: 64px 64px 72px;
  box-sizing: border-box;
}

.alexlab-content h1 {
  width: max-content;
  margin: 0;
  font-size: 42px;
  font-weight: 400;
  line-height: 49px;
  white-space: nowrap;
}

.alexlab-tabs-shell {
  position: relative;
  width: 100%;
  margin-top: 24px;
}

.alexlab-tabs {
  width: 100%;
  display: flex;
  gap: 4px;
  overflow-x: auto;
  overflow-y: hidden;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
  touch-action: pan-x;
}

.alexlab-tabs-arrow {
  position: absolute;
  z-index: 2;
  top: 50%;
  width: 36px;
  height: 36px;
  padding: 0;
  border: 1px solid rgba(0, 0, 0, 0.4);
  border-radius: 10px;
  background: #f5f5f5;
  display: grid;
  place-items: center;
  transform: translateY(-50%);
  cursor: pointer;
}

.alexlab-tabs-arrow-left {
  left: -48px;
}

.alexlab-tabs-arrow-right {
  right: -48px;
}

.alexlab-tabs-arrow-right img {
  transform: rotate(180deg);
}

.alexlab-tabs::-webkit-scrollbar {
  display: none;
}

.alexlab-tab {
  flex: 0 0 auto;
  height: 45px;
  padding: 0 24px;
  border: 1px solid rgba(0, 0, 0, 0.4);
  border-radius: 10px;
  background: transparent;
  color: #000;
  font-size: 18px;
  font-weight: 400;
  line-height: 1;
  white-space: nowrap;
  cursor: pointer;
}

.alexlab-tab.active {
  border-color: #000;
  background: #000;
  color: #fff;
}

.alexlab-panel {
  margin-top: 64px;
}

.about-panel,
.licenses-panel,
.legal-panel {
  width: min(723px, 100%);
}

.about-toc {
  width: 100%;
  height: 128px;
  padding: 24px;
  border-radius: 12px;
  background: #f0f0f0;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.about-toc strong,
.about-toc a {
  font-size: 18px;
  font-weight: 400;
  line-height: 21px;
}

.about-toc a {
  position: relative;
  padding-left: 10px;
  color: rgba(0, 0, 0, 0.3);
  text-decoration: none;
}

.about-toc a::before {
  content: '';
  position: absolute;
  left: 0;
  top: 8px;
  width: 4px;
  height: 4px;
  background: #b2b2b2;
}

.about-lead,
.about-section p {
  margin: 0;
  font-size: 18px;
  font-weight: 400;
  line-height: 21px;
}

.about-lead {
  margin-top: 48px;
}

.about-section {
  margin-top: 48px;
  scroll-margin-top: 24px;
}

.about-section h2 {
  margin: 0 0 16px;
  font-size: 24px;
  font-weight: 400;
  line-height: 28px;
}

.about-section p + p {
  margin-top: 32px;
}

.about-last-section {
  margin-bottom: 4px;
}

.licenses-panel {
  margin-top: 64px;
}

.license-search {
  width: 100%;
  height: 61px;
  padding: 0 24px;
  border-bottom: 1px solid #656565;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.license-search input {
  min-width: 0;
  flex: 1;
  border: 0;
  outline: 0;
  background: transparent;
  color: #000;
  font: inherit;
  font-size: 18px;
}

.license-search input::placeholder {
  color: rgba(0, 0, 0, 0.3);
  opacity: 1;
}

.license-search img {
  opacity: 0.35;
}

.license-list {
  margin-top: 21px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.license-card {
  width: 100%;
  height: 94px;
  min-height: 94px;
  padding: 24px;
  border: 1px solid #dfdfdf;
  border-radius: 0;
  background: #fff;
  box-sizing: border-box;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  transition: none;
}

.license-card:hover {
  transform: none;
  border-color: #dfdfdf;
  box-shadow: none;
}

.license-card h2,
.license-card p {
  margin: 0;
  font-weight: 400;
}

.license-card h2 {
  font-size: 21px;
  line-height: 24px;
}

.license-card p {
  margin-top: 3px;
  font-size: 16px;
  line-height: 19px;
}

.license-card button {
  width: 32px;
  height: 32px;
  padding: 4px;
  border: 0;
  background: transparent;
  cursor: pointer;
}

.license-empty {
  margin: 24px 0;
  font-size: 18px;
}

.doctors-panel {
  width: min(1115px, 100%);
}

.doctors-count {
  margin: 0 0 24px;
  font-size: 32px;
  font-weight: 400;
  line-height: 38px;
}

.mobile-count {
  display: none;
}

.doctor-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 360px), 1fr));
  gap: 8px;
}

.doctor-card {
  width: 100%;
  min-width: 0;
  height: 510px;
  padding: 24px;
  border-radius: 20px;
  background: #fff;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  transition: none;
}

.doctor-card:hover {
  transform: none;
  box-shadow: none;
}

.doctor-photo {
  width: min(317px, 100%);
  height: auto;
  max-width: 100%;
  aspect-ratio: 1;
  border-radius: 20px;
  object-fit: cover;
}

.doctor-copy {
  margin-top: 16px;
  text-align: center;
}

.doctor-copy h3,
.doctor-copy p {
  margin: 0;
  font-weight: 400;
}

.doctor-copy h3 {
  font-size: 24px;
  line-height: 28px;
}

.doctor-copy p {
  color: rgba(0, 0, 0, 0.45);
  font-size: 21px;
  line-height: 25px;
}

.doctor-badge {
  min-width: 159px;
  height: 45px;
  margin-top: auto;
  padding: 0 21px;
  border-radius: 10px;
  background: #f5f5f5;
  box-sizing: border-box;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  line-height: 21px;
  white-space: nowrap;
}

.contacts-panel {
  width: min(1115px, 100%);
  margin-top: 47px;
}

.contact-map {
  position: relative;
  width: 100%;
  height: 517px;
  overflow: hidden;
}

.map-placeholder {
  position: absolute;
  inset: 0;
  background: #e9ecf2;
  display: grid;
  place-items: center;
  color: #8a9099;
  font-size: 32px;
  line-height: 38px;
}

.contact-card {
  position: absolute;
  left: 21px;
  top: 21px;
  width: 465px;
  height: 475px;
  padding: 32px;
  background: #fff;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}

.office-label {
  position: relative;
  margin: 0;
  padding-left: 12px;
  color: rgba(0, 0, 0, 0.3);
  font-size: 18px;
  line-height: 21px;
}

.office-label::before {
  content: '';
  position: absolute;
  left: 0;
  top: 8px;
  width: 4px;
  height: 4px;
  background: #b2b2b2;
}

.contact-details h2 {
  margin: 12px 0 14px;
  font-size: 32px;
  font-weight: 400;
  line-height: 38px;
  white-space: nowrap;
}

.contact-links {
  display: flex;
  flex-direction: column;
}

.contact-links a {
  width: max-content;
  color: #000;
  font-size: 21px;
  line-height: 25px;
  text-decoration: none;
}

.office-hours {
  margin: 28px 0 0;
  display: grid;
  grid-template-columns: 92px auto;
  row-gap: 4px;
  font-size: 16px;
  line-height: 19px;
}

.office-hours dt {
  color: #929292;
}

.office-hours dd {
  margin: 0;
}

.map-link {
  width: 100%;
  height: 72px;
  margin-top: auto;
  padding: 0 32px;
  background: #000;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #fff;
  font-size: 18px;
  line-height: 21px;
  text-decoration: none;
}

.company-info {
  margin-top: 93px;
}

.company-info p {
  margin: 0 0 10px;
  font-size: 24px;
  line-height: 28px;
}

.company-info p span {
  color: rgba(0, 0, 0, 0.2);
}

.social-links {
  height: 56px;
  margin-top: 21px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.social-links a,
.social-links img {
  display: block;
  height: 56px;
}

.legal-panel {
  margin-top: 58px;
}

.legal-copy {
  padding-bottom: 48px;
  font-size: 18px;
  line-height: 21px;
  white-space: pre-wrap;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

@media (max-width: 1024px) {
  .alexlab-page {
    display: block;
    min-width: 0;
  }

  .alexlab-sidebar {
    display: none !important;
  }

  .alexlab-back {
    position: fixed;
    height: 72px;
    padding: 0 32px;
  }

  .alexlab-back span {
    display: none;
  }

  .alexlab-scroll {
    inset: 72px 0 0;
    scrollbar-gutter: auto;
  }

  .alexlab-content {
    padding: 32px 16px 72px;
  }

  .alexlab-content h1 {
    font-size: 32px;
    line-height: 38px;
  }

  .alexlab-tabs {
    width: 100%;
    padding: 0 16px;
    box-sizing: border-box;
    overflow-x: auto;
    overflow-y: hidden;
    scrollbar-width: none;
  }

  .alexlab-tabs-shell {
    width: calc(100% + 32px);
    margin: 24px -16px 0;
  }

  .alexlab-tabs-arrow {
    display: none !important;
  }

  .alexlab-tabs::-webkit-scrollbar {
    display: none;
  }

  .alexlab-panel {
    width: 100%;
  }

  .about-panel {
    margin-top: 76px;
  }

  .about-toc {
    height: 128px;
  }

  .about-lead {
    margin-top: 48px;
  }

  .about-section {
    margin-top: 38px;
  }

  .licenses-panel {
    margin-top: 32px;
  }

  .license-search {
    height: 61px;
  }

  .license-list {
    margin-top: 21px;
  }

  .doctors-panel {
    margin-top: 58px;
  }

  .doctors-count {
    margin-bottom: 14px;
    font-size: 24px;
    line-height: 28px;
  }

  .desktop-count {
    display: none;
  }

  .mobile-count {
    display: inline;
  }

  .doctor-grid {
    grid-template-columns: minmax(0, 1fr);
    gap: 8px;
  }

  .doctor-card {
    width: 100%;
  }

  .doctor-copy p {
    font-size: 18px;
    line-height: 21px;
  }

  .doctor-badge {
    font-size: 21px;
    line-height: 25px;
  }

  .contacts-panel {
    width: calc(100% + 32px);
    margin: 32px -16px 0;
  }

  .contact-map {
    height: auto;
    overflow: visible;
  }

  .map-placeholder {
    position: relative;
    inset: auto;
    width: 100%;
    height: 283px;
    font-size: 24px;
  }

  .contact-card {
    position: relative;
    left: auto;
    top: auto;
    width: 100%;
    height: 341px;
    padding: 32px;
  }

  .contact-details h2 {
    margin: 8px 0 2px;
    font-size: 24px;
    line-height: 28px;
  }

  .contact-links a {
    font-size: 20px;
    line-height: 24px;
  }

  .office-hours {
    margin-top: 28px;
  }

  .company-info {
    margin: 36px 16px 0;
  }

  .company-info p {
    margin-bottom: 10px;
  }

}

@media (max-width: 379px) {
  .alexlab-content h1 {
    width: auto;
    white-space: normal;
  }

  .doctor-card {
    height: auto;
    min-height: 510px;
  }

  .contact-details h2 {
    white-space: normal;
  }
}
</style>
