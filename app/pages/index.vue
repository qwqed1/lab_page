<script setup>
import { ref, computed, onMounted, watch, nextTick } from 'vue'

// Active tab for the top navigation menu
const activeTab = ref('about') // 'about', 'licenses', 'doctors', 'contacts'

// Licenses and Certificates Data
const licenseSearchQuery = ref('')
const licenses = ref([
  { id: 1, title: '№ Л041-01126-23/00345678', date: 'От 12.04.2022', type: 'medical' },
  { id: 2, title: 'Стандарт ISO', date: 'От 12.04.2024', type: 'iso' },
  { id: 3, title: 'Ежегодный аудит 2025', date: 'От 02.01.2025', type: 'audit' },
  { id: 4, title: '№ Л041-01126-23/00345678', date: 'От 12.04.2022', type: 'medical' },
  { id: 5, title: '№ Л041-01126-23/00345678', date: 'От 12.04.2022', type: 'medical' },
  { id: 6, title: 'Стандарт ISO', date: 'От 12.04.2024', type: 'iso' },
  { id: 7, title: 'Ежегодный аудит 2025', date: 'От 02.01.2025', type: 'audit' },
  { id: 8, title: 'Ежегодный аудит 2025', date: 'От 02.01.2025', type: 'audit' }
])

const filteredLicenses = computed(() => {
  if (!licenseSearchQuery.value.trim()) {
    return licenses.value
  }
  const query = licenseSearchQuery.value.toLowerCase()
  return licenses.value.filter(l => 
    l.title.toLowerCase().includes(query) || 
    l.date.toLowerCase().includes(query)
  )
})

const doctors = ref([
  { id: 1, name: 'Александра Ковальчук', title: 'Профессор МГУ', materials: 6, image: '/assets/doctor1.png' },
  { id: 2, name: 'Александра Ковальчук', title: 'Профессор МГУ', materials: 32, image: '/assets/doctor2.png' },
  { id: 3, name: 'Александра Ковальчук', title: 'Профессор МГУ', materials: 6, image: '/assets/doctor3.png' },
  { id: 4, name: 'Александра Ковальчук', title: 'Профессор МГУ', materials: 6, image: '/assets/doctor4.png' },
  { id: 5, name: 'Александра Ковальчук', title: 'Профессор МГУ', materials: 6, image: '/assets/doctor5.png' },
  { id: 6, name: 'Александра Ковальчук', title: 'Профессор МГУ', materials: 6, image: '/assets/doctor6.png' },
  { id: 7, name: 'Александра Ковальчук', title: 'Профессор МГУ', materials: 6, image: '/assets/doctor7.png' },
  { id: 8, name: 'Александра Ковальчук', title: 'Профессор МГУ', materials: 6, image: '/assets/doctor8.png' },
  { id: 9, name: 'Александра Ковальчук', title: 'Профессор МГУ', materials: 6, image: '/assets/doctor9.png' }
])

const getMaterialsWord = (count) => {
  const mod10 = count % 10
  const mod100 = count % 100
  if (mod100 >= 11 && mod100 <= 19) {
    return 'материалов'
  }
  if (mod10 === 1) {
    return 'материал'
  }
  if (mod10 >= 2 && mod10 <= 4) {
    return 'материала'
  }
  return 'материалов'
}


const tabs = [
  { id: 'about', label: 'О нас' },
  { id: 'licenses', label: 'Лицензии' },
  { id: 'doctors', label: 'Врачи и эксперты' },
  { id: 'contacts', label: 'Контакты' }
]

// Modal states
const showDemoModal = ref(false)
const showSearchModal = ref(false)
const showQuizModal = ref(false)
const showRegisterModal = ref(false)

// Search State
const searchQuery = ref('')
const searchResult = ref(null)
const mockAllergens = [
  'Пыльца березы', 'Шерсть кошки', 'Шерсть собаки', 'Арахис', 
  'Молоко коровье', 'Яичный белок', 'Клещ домашней пыли', 
  'Пшеничная мука', 'Глютен', 'Полынь', 'Альфа-лактальбумин',
  'Креветки', 'Томаты', 'Шоколад', 'Пыльца ольхи', 'Яд осы'
]

const handleSearch = () => {
  if (!searchQuery.value.trim()) {
    searchResult.value = null
    return
  }
  const query = searchQuery.value.toLowerCase()
  const found = mockAllergens.filter(a => a.toLowerCase().includes(query))
  if (found.length > 0) {
    searchResult.value = {
      success: true,
      items: found
    }
  } else {
    searchResult.value = {
      success: false,
      message: 'Аллерген не найден в базе, но наш тест проверяет более 300 показателей. Скорее всего, он там есть!'
    }
  }
}

// Quiz State
const quizStep = ref(0) // 0: intro, 1-3: questions, 4: result
const quizAnswers = ref([])
const quizQuestions = [
  { text: 'Испытываете ли вы зуд, насморк или слезотечение без простуды?', category: 'symptoms' },
  { text: 'Бывают ли у вас высыпания на коже после еды или контакта с животными?', category: 'skin' },
  { text: 'Есть ли у ваших близких родственников подтвержденная аллергия?', category: 'heredity' }
]

const startQuiz = () => {
  quizStep.value = 1
  quizAnswers.value = []
}

const answerQuiz = (answer) => {
  quizAnswers.value.push(answer)
  if (quizStep.value < quizQuestions.length) {
    quizStep.value++
  } else {
    quizStep.value = 4 // show result
  }
}

const getQuizRecommendation = () => {
  const yesCount = quizAnswers.value.filter(a => a === 'yes').length
  if (yesCount === 3) {
    return 'У вас высокая вероятность аллергических реакций. Рекомендуем пройти полный многокомпонентный тест на 300+ аллергенов для точной диагностики.'
  } else if (yesCount >= 1) {
    return 'У вас наблюдаются некоторые признаки предрасположенности к аллергии. Рекомендуем проконсультироваться с аллергологом ALEX LAB и сдать направленный тест.'
  } else {
    return 'Симптомы аллергии минимальны. Однако, если вы хотите убедиться в безопасности для здоровья или планируете завести питомца, превентивный тест не будет лишним.'
  }
}

const resetQuiz = () => {
  quizStep.value = 0
  quizAnswers.value = []
}

// Map Initialization and Contacts Logic
let mapInstance = null
let isLeafletLoaded = false

onMounted(() => {
  if (process.client) {
    // Dynamically inject Leaflet CSS
    const link = document.createElement('link')
    link.rel = 'stylesheet'
    link.href = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css'
    document.head.appendChild(link)

    // Dynamically inject Leaflet JS
    const script = document.createElement('script')
    script.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js'
    script.onload = () => {
      isLeafletLoaded = true
      if (activeTab.value === 'contacts') {
        initMap()
      }
    }
    document.head.appendChild(script)
  }
})

const initMap = () => {
  if (!window.L) return
  
  if (mapInstance) {
    mapInstance.remove()
    mapInstance = null
  }
  
  const coords = [55.741487, 37.594754] // Москва, Пречистенка 30/2
  
  mapInstance = L.map('leaflet-map', {
    center: coords,
    zoom: 16,
    zoomControl: false,
    attributionControl: false
  })

  // CartoDB Positron - grayscale tiles
  L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    maxZoom: 19
  }).addTo(mapInstance)

  // Custom pulsing location marker matching Figma blue dot
  const customIcon = L.divIcon({
    className: 'custom-map-pin',
    html: '<div class="map-pin-pulse"></div>',
    iconSize: [20, 20],
    iconAnchor: [10, 10]
  })

  L.marker(coords, { icon: customIcon }).addTo(mapInstance)
}

watch(activeTab, (newTab) => {
  if (newTab === 'contacts') {
    nextTick(() => {
      if (isLeafletLoaded) {
        initMap()
      }
    })
  }
})

const openMapLink = () => {
  window.open('https://yandex.ru/maps/?text=Москва, Пречистенка 30/2', '_blank')
}

// Smooth scroll to sections
const scrollToSection = (id) => {
  const el = document.getElementById(id)
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>

<template>
  <div class="page-container">
    <!-- Left Column: Navigation controls & cards (Frame 1 / Frame 52) -->
    <aside class="sidebar-container">
      <!-- Promo Banner Card (Frame 41) -->
      <div class="promo-card" id="card-promo">
        <div class="promo-content">
          <img src="/assets/banner.svg" alt="Анализ крови" class="promo-banner-img" />
          <p class="promo-text">
            Многокомпонентный анализ крови, который за один забор крови проверяет более 300 аллергенов, выявляя истинные причины реакции.
          </p>
        </div>
        
        <!-- Button (Frame 111) -->
        <button class="promo-button" id="btn-register" @click="showRegisterModal = true">
          <span class="promo-button-text">Записаться на тест на аллергию</span>
          <div class="promo-button-icon">
            <img src="/assets/arrow-right-btn.svg" alt="arrow" />
          </div>
        </button>
      </div>

      <!-- Side-by-side cards (Frame 109) -->
      <div class="cards-row">
        <!-- Search Card (Frame 101) -->
        <div class="sub-card" id="card-search" @click="showSearchModal = true">
          <div class="card-icon-wrapper">
            <img src="/assets/search-icon.svg" alt="search" />
          </div>
          <div class="card-text-group">
            <h3 class="card-title">Поиск аллергенов</h3>
            <p class="card-subtitle">Убедитесь, что тест покажет, что вам нужно</p>
          </div>
        </div>

        <!-- Demo Card (Frame 36) -->
        <div class="sub-card" id="card-demo" @click="$router.push('/demo-result')">
          <div class="card-icon-wrapper">
            <img src="/assets/doc-icon.svg" alt="doc" />
          </div>
          <div class="card-text-group">
            <h3 class="card-title">Посмотреть демо-результат</h3>
            <p class="card-subtitle">Объясняем результаты на человеческом языке</p>
          </div>
        </div>
      </div>

      <!-- Quiz Card (Frame 47) -->
      <div class="sidebar-row-card" id="row-quiz" @click="showQuizModal = true">
        <div class="row-left-content">
          <span class="tag-badge">~5 минут</span>
          <span class="row-text">КВИЗ: Нужен ли вам тест на аллергены?</span>
        </div>
      </div>

      <!-- Profile Card (Frame 38) -->
      <div class="sidebar-row-card" id="row-profile">
        <div class="row-left-content">
          <div class="row-icon-icon" style="margin-right: 4px;">
            <img src="/assets/profile-icon.svg" alt="profile" />
          </div>
          <span class="row-text">Личный кабинет</span>
        </div>
      </div>

      <!-- About/Bottom Card (Frame 113) -->
      <div class="sidebar-row-card" id="row-about" @click="scrollToSection('section-about')">
        <div class="row-left-content">
          <span class="row-text">Лаборатория ALEX LAB</span>
        </div>
        <div class="row-icon-icon">
          <!-- Circular chevron SVG matching Figma -->
          <svg width="24" height="24" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M15.9974 29.3307C23.3612 29.3307 29.3307 23.3612 29.3307 15.9974C29.3307 8.6336 23.3612 2.66406 15.9974 2.66406C8.6336 2.66406 2.66406 8.6336 2.66406 15.9974C2.66406 23.3612 8.6336 29.3307 15.9974 29.3307Z" />
            <path d="M13.3359 10.6641L18.6693 15.9974L13.3359 21.3307" />
          </svg>
        </div>
      </div>
    </aside>

    <!-- Right Column: Content & Navigation (Frame 116 / Frame 117) -->
    <main class="content-container">
      <!-- Mobile Top Navigation Bar (Frame 290) -->
      <div class="mobile-top-bar">
        <button class="mobile-back-button" aria-label="Назад">
          <svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M7 13L1 7L7 1" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
      </div>

      <!-- Header with nav tabs -->
      <header class="content-header">
        <h1 class="main-title">Лаборатория ALEX LAB</h1>
        
        <nav class="nav-menu">
          <button 
            v-for="tab in tabs" 
            :key="tab.id"
            :class="['nav-item', activeTab === tab.id ? 'active' : 'outline']"
            @click="activeTab = tab.id"
          >
            {{ tab.label }}
          </button>
        </nav>
      </header>

      <!-- Main Body content -->
      <div class="content-body" v-if="activeTab === 'about'">
        <!-- Table of contents (Frame 336089) -->
        <div class="toc-card">
          <h4 class="toc-title">Содержание</h4>
          <ul class="toc-list">
            <li class="toc-item" @click="scrollToSection('section-inside')">
              <span class="toc-dot"></span>
              Что внутри
            </li>
            <li class="toc-item" @click="scrollToSection('section-history')">
              <span class="toc-dot"></span>
              Работаем с 2001
            </li>
          </ul>
        </div>

        <!-- Intro Text -->
        <p class="intro-text" id="section-about">
          Лаборатория Alex Lab — ведущий научно-исследовательский центр молекулярной генетики и биотехнологий, созданный в 2018 году. Мы объединили передовую науку и высокие технологии, чтобы сделать сложнейшую высокоточную диагностику доступной для каждого пациента. Наша главная миссия — внедрение инновационных медицинских тестов в повседневную врачебную практику для выявления скрытых угроз здоровью на самых ранних стадиях.
        </p>

        <!-- Information Sections -->
        <div class="sections-wrapper">
          <!-- Section: Что внутри? (Frame 336113) -->
          <section class="info-section" id="section-inside">
            <h2 class="section-title">Что внутри?</h2>
            <p class="section-body">
              Производственный комплекс лаборатории оснащен роботизированными анализаторами последнего поколения от лидеров мирового рынка. Полная автоматизация процессов исключает человеческий фактор, гарантируя абсолютную точность результатов. Благодаря оптимизации логистики и собственной IT-платформе, мы сократили время ожидания: большинство сложных генетических исследований выполняются всего за 24 часа.
            </p>
            <p class="section-body-secondary">
              Центр строго соблюдает принципы медицинской этики и гарантирует полную анонимность персональных данных. Каждый этап — от взятия биоматериала до выдачи заключения — защищен современными протоколами шифрования. Нам доверяют как частные пациенты, так и крупнейшие государственные и коммерческие клиники по всей стране.
            </p>
          </section>

          <!-- Section: Работаем с 2001 -->
          <section class="info-section" id="section-history">
            <h2 class="section-title">Работаем с 2001</h2>
            <p class="section-body">
              Производственный комплекс лаборатории оснащен роботизированными анализаторами последнего поколения от лидеров мирового рынка. Полная автоматизация процессов исключает человеческий фактор, гарантируя абсолютную точность результатов. Благодаря оптимизации логистики и собственной IT-платформе, мы сократили время ожидания: большинство сложных генетических исследований выполняются всего за 24 часа.
            </p>
          </section>
        </div>
      </div>

      <!-- Licenses Tab content (Figma Frame 1570:11040) -->
      <div class="content-body" v-else-if="activeTab === 'licenses'">
        <section class="info-section">
          <!-- Search Bar -->
          <div class="licenses-search-wrapper">
            <svg class="search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <input 
              type="text" 
              v-model="licenseSearchQuery" 
              placeholder="Поиск лицензии по названию или дате..." 
              class="licenses-search-input"
            />
          </div>

          <!-- Licenses Grid -->
          <div class="licenses-grid">
            <div 
              class="license-card" 
              v-for="license in filteredLicenses" 
              :key="license.id"
            >
              <div class="license-icon">
                <!-- Premium Sage-green PDF document icon -->
                <svg width="40" height="48" viewBox="0 0 40 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M22 2V14H34" stroke="#7e8f7c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M34 14V42C34 43.1 33.1 44 32 44H8C6.9 44 6 43.1 6 42V6C6 4.9 6.9 4 8 4H22L34 14Z" stroke="#7e8f7c" stroke-width="2" stroke-linejoin="round"/>
                  <path d="M12 24H28" stroke="#7e8f7c" stroke-width="2" stroke-linecap="round"/>
                  <path d="M12 32H28" stroke="#7e8f7c" stroke-width="2" stroke-linecap="round"/>
                  <path d="M12 16H16" stroke="#7e8f7c" stroke-width="2" stroke-linecap="round"/>
                </svg>
              </div>
              <div class="license-info">
                <h4 class="license-title">{{ license.title }}</h4>
                <p class="license-date">{{ license.date }}</p>
              </div>
              <button 
                class="license-download-btn"
                @click="alert(`Скачивание документа: ${license.title}`)"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                  <polyline points="7 10 12 15 17 10" />
                  <line x1="12" y1="15" x2="12" y2="3" />
                </svg>
                <span>Скачать PDF</span>
              </button>
            </div>
          </div>
        </section>
      </div>

      <!-- Doctors Tab content (Figma Frame 1571:11833) -->
      <div class="content-body" v-else-if="activeTab === 'doctors'">
        <section class="info-section">
          <!-- Main count title block -->
          <h2 class="doctors-main-count">Всего 482 специалиста</h2>

          <!-- Doctors Grid -->
          <div class="doctors-grid">
            <div 
              class="doctor-card" 
              v-for="doctor in doctors" 
              :key="doctor.id"
            >
              <!-- Card Photo wrapper -->
              <div class="doctor-photo-wrapper">
                <img :src="doctor.image" :alt="doctor.name" class="doctor-photo" />
              </div>
              
              <!-- Card Text info -->
              <div class="doctor-info">
                <h3 class="doctor-name">{{ doctor.name }}</h3>
                <p class="doctor-title">{{ doctor.title }}</p>
              </div>

              <!-- Button materials -->
              <button 
                class="doctor-materials-btn"
                @click="alert(`Переход к материалам автора: ${doctor.name}`)"
              >
                <span>{{ doctor.materials }} {{ getMaterialsWord(doctor.materials) }}</span>
              </button>
            </div>
          </div>
        </section>
      </div>

      <!-- Contacts Tab content (Figma Frame 1805:137 + 1805:342 + 1805:286) -->
      <div class="content-body contacts-tab-content" v-else-if="activeTab === 'contacts'">
        <!-- Map + Card wrapper (desktop: card overlays map; mobile: card flows below) -->
        <div class="contacts-map-wrapper">
          <!-- Map Container (Frame 336147: 1115x517) -->
          <div class="contacts-map-container">
            <div id="leaflet-map" class="leaflet-map-element"></div>
          </div>

          <!-- Contacts Card (Frame 336180: desktop=465x475 overlaid; mobile=420x341 below) -->
          <div class="contacts-card">
            <!-- Frame 336146: upper info block -->
            <div class="contacts-info-block">
              <!-- Header row: dot + "Главный офис" (Frame 336186) -->
              <div class="contacts-header-row">
                <span class="contacts-badge-dot"></span>
                <span class="contacts-badge-text">Главный офис</span>
              </div>

              <!-- Frame 336185: address + contacts + schedule -->
              <div class="contacts-details-block">
                <!-- Frame 336184: address + phone/email -->
                <div class="contacts-address-contacts">
                  <!-- Address: Roboto 32px, line-height 37.5px -->
                  <h2 class="contacts-address-text">Москва, Пречистенка 30/2</h2>
                  <!-- Frame 336181: phone + email, vertical gap 12px -->
                  <div class="contacts-links-group">
                    <a href="tel:+74955076485" class="contacts-link-item">+7 495 507-64-85</a>
                    <a href="mailto:alex@lab.com" class="contacts-link-item">alex@lab.com</a>
                  </div>
                </div>

                <!-- Frame 336175: Schedule grid (193x42) -->
                <div class="contacts-schedule-grid">
                  <span class="schedule-days">ПН — ПТ</span>
                  <span class="schedule-time">9:00 — 19:00</span>
                  <span class="schedule-days">СБ — ВС</span>
                  <span class="schedule-time">Выходные</span>
                </div>
              </div>
            </div>

            <!-- Action Button (Frame 111: black bg, 72px height) -->
            <button class="contacts-btn-map" @click="openMapLink">
              <span class="contacts-btn-text">Открыть на картах</span>
              <div class="contacts-btn-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"/>
                  <polyline points="10 8 14 12 10 16"/>
                </svg>
              </div>
            </button>
          </div>
        </div>

        <!-- Legal Footer (Figma Frame 335960: vertical gap 28px) -->
        <div class="contacts-footer">
          <!-- Legal info block (Frame 335968: 3 lines) -->
          <div class="footer-legal-info">
            <p>ИНН: 9703021385</p>
            <p>ОГРН: 1207700425602</p>
            <p>КПП: 770301001</p>
          </div>
          
          <!-- Social icons (Frame 335961: horizontal gap 8px) -->
          <div class="footer-social-links">
            <!-- Telegram (Logo 1: 56x56) — Original Figma SVG -->
            <a href="https://t.me/alexlab" target="_blank" class="social-link-icon" aria-label="Telegram">
              <svg width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_tg)">
                  <path d="M28 56C43.464 56 56 43.464 56 28C56 12.536 43.464 0 28 0C12.536 0 0 12.536 0 28C0 43.464 12.536 56 28 56Z" fill="black"/>
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M12.6724 27.7046C20.835 24.1483 26.278 21.8037 29.0014 20.671C36.7773 17.4367 38.3931 16.8749 39.4462 16.8563C39.6778 16.8523 40.1957 16.9097 40.5312 17.1819C40.8145 17.4117 40.8924 17.7222 40.9297 17.9402C40.967 18.1581 41.0134 18.6545 40.9765 19.0424C40.5551 23.4699 38.7318 34.2142 37.8042 39.173C37.4117 41.2713 36.6389 41.9748 35.8907 42.0436C34.2647 42.1933 33.03 40.9691 31.4551 39.9367C28.9907 38.3213 27.5985 37.3157 25.2064 35.7393C22.442 33.9176 24.2341 32.9163 25.8095 31.28C26.2218 30.8517 33.3861 24.3353 33.5247 23.7442C33.5421 23.6702 33.5582 23.3946 33.3945 23.2491C33.2307 23.1036 32.9891 23.1534 32.8147 23.1929C32.5676 23.249 28.6307 25.8512 21.0042 30.9993C19.8867 31.7666 18.8745 32.1405 17.9677 32.1209C16.9679 32.0993 15.0448 31.5556 13.6152 31.0909C11.8617 30.5209 10.468 30.2196 10.5894 29.2515C10.6526 28.7473 11.3469 28.2317 12.6724 27.7046Z" fill="white"/>
                </g>
                <defs>
                  <clipPath id="clip0_tg">
                    <rect width="56" height="56" fill="white"/>
                  </clipPath>
                </defs>
              </svg>
            </a>
            
            <!-- VK (VK Logo 1: 57x56) — Original Figma SVG -->
            <a href="https://vk.com/alexlab" target="_blank" class="social-link-icon" aria-label="VK">
              <svg width="57" height="56" viewBox="0 0 57 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_vk)">
                  <mask id="mask0_vk" style="mask-type:luminance" maskUnits="userSpaceOnUse" x="0" y="0" width="57" height="56">
                    <path d="M56.7188 0H0.283203V56H56.7188V0Z" fill="white"/>
                  </mask>
                  <g mask="url(#mask0_vk)">
                    <path d="M0.283203 26.88C0.283203 14.2087 0.283203 7.87298 4.25031 3.93649C8.21743 0 14.6024 0 27.3723 0H29.6297C42.3997 0 48.7846 0 52.7518 3.93649C56.7188 7.87298 56.7188 14.2087 56.7188 26.88V29.12C56.7188 41.7913 56.7188 48.127 52.7518 52.0635C48.7846 56 42.3997 56 29.6297 56H27.3723C14.6024 56 8.21743 56 4.25031 52.0635C0.283203 48.127 0.283203 41.7913 0.283203 29.12V26.88Z" fill="black"/>
                    <path d="M30.3155 40.3434C17.4528 40.3434 10.1163 31.5934 9.81055 17.0334H16.2536C16.4653 27.7201 21.2152 32.2467 24.9775 33.1801V17.0334H31.0446V26.25C34.7599 25.8534 38.6629 21.6534 39.9797 17.0334H46.0467C45.0356 22.7268 40.8029 26.9267 37.793 28.6534C40.8029 30.0534 45.6237 33.7167 47.4579 40.3434H40.7794C39.345 35.9101 35.7711 32.4801 31.0446 32.0134V40.3434H30.3155Z" fill="white"/>
                  </g>
                </g>
                <defs>
                  <clipPath id="clip0_vk">
                    <rect width="57" height="56" fill="white"/>
                  </clipPath>
                </defs>
              </svg>
            </a>
            
            <!-- YouTube (youtube-sign-logo 1: 76x56) — Original Figma SVG -->
            <a href="https://youtube.com/alexlab" target="_blank" class="social-link-icon" aria-label="YouTube">
              <svg width="76" height="56" viewBox="0 0 76 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_yt)">
                  <path d="M74.4116 8.744C73.5376 5.304 70.9612 2.592 67.6932 1.672C61.7652 0 38 0 38 0C38 0 14.2348 0 8.3068 1.672C5.0388 2.592 2.4624 5.304 1.5884 8.744C0 14.984 0 28 0 28C0 28 0 41.016 1.5884 47.256C2.4624 50.696 5.0388 53.408 8.3068 54.328C14.2348 56 38 56 38 56C38 56 61.7652 56 67.6932 54.328C70.9612 53.408 73.5376 50.696 74.4116 47.256C76 41.016 76 28 76 28C76 28 76 14.984 74.4116 8.744Z" fill="black"/>
                  <path d="M30.3984 39.9999L50.1432 27.9999L30.3984 15.9999V39.9999Z" fill="white"/>
                </g>
                <defs>
                  <clipPath id="clip0_yt">
                    <rect width="76" height="56" fill="white"/>
                  </clipPath>
                </defs>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </main>
  </div>

  <!-- ==========================================================================
       MODALS & OVERLAYS
       ========================================================================== -->

  <!-- Modal: Demo Results -->
  <Transition name="fade">
    <div class="modal-overlay" v-if="showDemoModal" @click.self="showDemoModal = false">
      <div class="modal-card">
        <button class="modal-close-btn" @click="showDemoModal = false">&times;</button>
        <h3 class="modal-title">Пример результатов теста</h3>
        <p class="modal-desc">Здесь показано, как выглядит расшифровка теста на 300+ аллергенов на понятном языке.</p>
        
        <div class="demo-results-list">
          <div class="demo-result-item high">
            <span class="allergen-name">Пыльца березы (t3)</span>
            <span class="allergen-level">Высокий уровень (45.2 kU/l)</span>
            <div class="level-bar"><div class="fill" style="width: 90%; background: #ff4d4f;"></div></div>
          </div>
          <div class="demo-result-item medium">
            <span class="allergen-name">Шерсть кошки (e1)</span>
            <span class="allergen-level">Средний уровень (12.4 kU/l)</span>
            <div class="level-bar"><div class="fill" style="width: 50%; background: #faad14;"></div></div>
          </div>
          <div class="demo-result-item low">
            <span class="allergen-name">Арахис (f13)</span>
            <span class="allergen-level">Следовые реакции (0.2 kU/l)</span>
            <div class="level-bar"><div class="fill" style="width: 5%; background: #52c41a;"></div></div>
          </div>
        </div>
        <p style="font-size: 14px; color: #666; margin-top: 15px; line-height: 1.4;">
          * Полный отчет включает рекомендации аллерголога, разбор перекрестных реакций и карту диеты.
        </p>
      </div>
    </div>
  </Transition>

  <!-- Modal: Search Allergens -->
  <Transition name="fade">
    <div class="modal-overlay" v-if="showSearchModal" @click.self="showSearchModal = false">
      <div class="modal-card">
        <button class="modal-close-btn" @click="showSearchModal = false">&times;</button>
        <h3 class="modal-title">Проверить аллерген</h3>
        <p class="modal-desc">Введите название продукта, растения или животного, чтобы узнать, входит ли он в наш тест.</p>
        
        <div style="display: flex; gap: 10px; margin-top: 15px; margin-bottom: 15px;">
          <input 
            type="text" 
            v-model="searchQuery" 
            @input="handleSearch"
            placeholder="Например: береза, кошка, яйцо" 
            style="flex: 1; padding: 12px 16px; border: 1px solid #dfdfdf; border-radius: 8px; font-size: 16px; outline: none;"
          />
        </div>

        <div v-if="searchResult" class="search-results-box">
          <div v-if="searchResult.success" style="color: #52c41a; font-weight: 500;">
            <p style="margin-bottom: 8px;">✓ Да, эти показатели проверяются в тесте:</p>
            <ul style="list-style: inside; color: #333; font-weight: normal; margin-left: 10px;">
              <li v-for="item in searchResult.items" :key="item">{{ item }}</li>
            </ul>
          </div>
          <div v-else style="color: #ff4d4f;">
            {{ searchResult.message }}
          </div>
        </div>
        <div v-else style="color: #999; font-size: 14px; text-align: center; padding: 10px 0;">
          Начните вводить название...
        </div>
      </div>
    </div>
  </Transition>

  <!-- Modal: Interactive Quiz -->
  <Transition name="fade">
    <div class="modal-overlay" v-if="showQuizModal" @click.self="showQuizModal = false">
      <div class="modal-card">
        <button class="modal-close-btn" @click="showQuizModal = false">&times;</button>
        <h3 class="modal-title">Нужен ли вам тест?</h3>
        
        <!-- Quiz Steps -->
        <div v-if="quizStep === 0" style="text-align: center; padding: 15px 0;">
          <p class="modal-desc">Ответьте на 3 простых вопроса, чтобы узнать, рекомендуется ли вам обследование на аллергены.</p>
          <button @click="startQuiz" class="quiz-btn-primary" style="margin-top: 15px;">Начать квиз</button>
        </div>

        <div v-else-if="quizStep >= 1 && quizStep <= 3" style="padding: 15px 0;">
          <div style="font-size: 14px; color: #999; margin-bottom: 10px;">Вопрос {{ quizStep }} из 3</div>
          <p style="font-size: 18px; font-weight: 500; line-height: 1.4; margin-bottom: 20px;">
            {{ quizQuestions[quizStep - 1].text }}
          </p>
          <div style="display: flex; gap: 12px;">
            <button @click="answerQuiz('yes')" class="quiz-btn-choice">Да</button>
            <button @click="answerQuiz('no')" class="quiz-btn-choice outline">Нет</button>
          </div>
        </div>

        <div v-else-if="quizStep === 4" style="text-align: center; padding: 15px 0;">
          <h4 style="font-size: 20px; font-weight: bold; color: #52c41a; margin-bottom: 15px;">Результат квиза</h4>
          <p style="font-size: 16px; line-height: 1.6; color: #333; margin-bottom: 20px;">
            {{ getQuizRecommendation() }}
          </p>
          <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 15px;">
            <button @click="showQuizModal = false; $router.push('/demo-result')" class="quiz-btn-primary">Посмотреть демо-отчет</button>
            <div style="display: flex; gap: 12px;">
              <button @click="resetQuiz" class="quiz-btn-choice outline" style="flex: 1;">Пройти заново</button>
              <button @click="showQuizModal = false; showRegisterModal = true" class="quiz-btn-choice" style="flex: 1;">Записаться на тест</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Transition>

  <!-- Modal: Registration -->
  <Transition name="fade">
    <div class="modal-overlay" v-if="showRegisterModal" @click.self="showRegisterModal = false">
      <div class="modal-card">
        <button class="modal-close-btn" @click="showRegisterModal = false">&times;</button>
        <h3 class="modal-title">Запись на тест</h3>
        <p class="modal-desc">Оставьте ваши контакты, администратор ALEX LAB свяжется с вами для подбора даты забора крови.</p>
        
        <form @submit.prevent="alert('Заявка успешно отправлена! Наш администратор свяжется с вами в течение 15 минут.'); showRegisterModal = false" style="display: flex; flex-direction: column; gap: 16px; margin-top: 15px;">
          <div style="display: flex; flex-direction: column; gap: 6px;">
            <label style="font-size: 14px; font-weight: 500; color: #666;">Ваше имя</label>
            <input type="text" required placeholder="Иван Иванов" style="padding: 12px; border: 1px solid #dfdfdf; border-radius: 8px; font-size: 16px;" />
          </div>
          <div style="display: flex; flex-direction: column; gap: 6px;">
            <label style="font-size: 14px; font-weight: 500; color: #666;">Номер телефона</label>
            <input type="tel" required placeholder="+7 (999) 999-99-99" style="padding: 12px; border: 1px solid #dfdfdf; border-radius: 8px; font-size: 16px;" />
          </div>
          <button type="submit" class="quiz-btn-primary" style="margin-top: 10px;">Отправить заявку</button>
        </form>
      </div>
    </div>
  </Transition>
</template>

<style scoped>
/* Modal and Interactive Component Styles scoped here to avoid cluttering main.css */

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-card {
  background: white;
  border-radius: 20px;
  width: 90%;
  max-width: 500px;
  padding: 32px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.15);
  position: relative;
  border: 1px solid #f0f0f0;
}

.modal-close-btn {
  position: absolute;
  top: 20px;
  right: 24px;
  background: transparent;
  border: none;
  font-size: 28px;
  cursor: pointer;
  color: #999;
  transition: color 0.2s ease;
}

.modal-close-btn:hover {
  color: #333;
}

.modal-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 12px;
}

.modal-desc {
  font-size: 16px;
  color: #666;
  line-height: 1.5;
  margin-bottom: 16px;
}

/* Demo results graphic inside modal */
.demo-results-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 20px;
}

.demo-result-item {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.allergen-name {
  font-weight: bold;
  font-size: 16px;
}

.allergen-level {
  font-size: 14px;
  color: #666;
}

.level-bar {
  width: 100%;
  height: 8px;
  background: #f0f0f0;
  border-radius: 4px;
  overflow: hidden;
}

.level-bar .fill {
  height: 100%;
  border-radius: 4px;
  transition: width 1s ease;
}

/* Search Box style */
.search-results-box {
  background: #f9f9f9;
  border: 1px dashed #dfdfdf;
  border-radius: 8px;
  padding: 16px;
  margin-top: 15px;
  font-size: 15px;
  line-height: 1.5;
}

/* Quiz button styles */
.quiz-btn-primary {
  width: 100%;
  background: black;
  color: white;
  border: 1px solid black;
  padding: 14px;
  font-size: 16px;
  font-weight: 500;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.quiz-btn-primary:hover {
  background: #333;
  border-color: #333;
}

.quiz-btn-choice {
  flex: 1;
  padding: 12px;
  font-size: 16px;
  font-weight: 500;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  background: black;
  color: white;
  border: 1px solid black;
  text-align: center;
}

.quiz-btn-choice:hover {
  background: #333;
  border-color: #333;
}

.quiz-btn-choice.outline {
  background: transparent;
  color: black;
  border: 1px solid black;
}

.quiz-btn-choice.outline:hover {
  background: #f5f5f5;
}

/* Vue Transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
