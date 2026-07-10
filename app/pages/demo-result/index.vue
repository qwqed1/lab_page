<script setup>
import { ref, computed } from 'vue'

// Search query for the results table
const searchQuery = ref('')

// Mock Patient Data from the screenshot
const patient = {
  name: 'Елагин М.С.',
  age: '19 лет',
  dob: '11.06.2006',
  orderId: 'елагин',
  method: 'ALEX2',
  barcode: '030SU126',
  testDate: '16.12.2025',
  totalIge: 1440
}

// Table range helper for highlighting
const getClassByVal = (val) => {
  if (val < 0.3) return 'range-negative'
  if (val >= 0.3 && val <= 1.0) return 'range-low'
  if (val > 1.0 && val <= 5.0) return 'range-medium'
  if (val > 5.0 && val <= 15.0) return 'range-high'
  return 'range-very-high'
}

// Value formatter: removes trailing .0 for whole numbers
const formatValue = (val) => {
  return val % 1 === 0 ? val.toFixed(0) : val.toString()
}

// Mock Allergen Results grouped exactly as in the design screenshot
const allergenGroups = ref([
  {
    name: 'Пыльца трав',
    items: [
      { name: 'Свинорой пальчатый', val: 0.0, code: 'Cyn d', protein: '', type: 'E' },
      { name: 'Свинорой пальчатый', val: 0.0, code: 'Cyn d 1', protein: 'Beta-Expansin', type: 'M' },
      { name: 'Плевел многолетний', val: 0.0, code: 'Lol p 1', protein: 'Beta-Expansin', type: 'E' },
      { name: 'Паслен/Стрихнос лесной', val: 0.0, code: 'Pas s', protein: '', type: 'E' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 1', protein: 'Beta-Expansin', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.8, code: 'Phl p 5.0101', protein: 'Grass Group 5/6', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 6', protein: 'Grass Group 5/6', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 7', protein: 'Polcalcin', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 12', protein: 'Profilin', type: 'M' },
      { name: 'Тростник', val: 0.0, code: 'Phr c', protein: '', type: 'E' },
      { name: 'Рожь, пыльца', val: 0.0, code: 'Sec c_pollen', protein: '', type: 'E' }
    ]
  },
  {
    name: 'Пыльца деревьев',
    items: [
      { name: 'Свинорой пальчатый', val: 0.0, code: 'Cyn d', protein: '', type: 'E' },
      { name: 'Свинорой пальчатый', val: 0.0, code: 'Cyn d 1', protein: 'Beta-Expansin', type: 'M' },
      { name: 'Плевел многолетний', val: 0.0, code: 'Lol p 1', protein: 'Beta-Expansin', type: 'E' },
      { name: 'Паслен/Стрихнос лесной', val: 7.0, code: 'Pas s', protein: '', type: 'E' },
      { name: 'Тимофеевка луговая', val: 6.0, code: 'Phl p 1', protein: 'Beta-Expansin', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.6, code: 'Phl p 5.0101', protein: 'Grass Group 5/6', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 6', protein: 'Grass Group 5/6', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 7', protein: 'Polcalcin', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 12', protein: 'Profilin', type: 'M' },
      { name: 'Тростник', val: 0.0, code: 'Phr c', protein: '', type: 'E' },
      { name: 'Рожь, пыльца', val: 0.0, code: 'Sec c_pollen', protein: '', type: 'E' }
    ]
  },
  {
    name: 'Пыльца сорных трав',
    items: [
      { name: 'Свинорой пальчатый', val: 22.0, code: 'Cyn d', protein: '', type: 'E' },
      { name: 'Свинорой пальчатый', val: 0.0, code: 'Cyn d 1', protein: 'Beta-Expansin', type: 'M' },
      { name: 'Плевел многолетний', val: 0.0, code: 'Lol p 1', protein: 'Beta-Expansin', type: 'E' },
      { name: 'Паслен/Стрихнос лесной', val: 0.0, code: 'Pas s', protein: '', type: 'E' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 1', protein: 'Beta-Expansin', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.6, code: 'Phl p 5.0101', protein: 'Grass Group 5/6', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 6', protein: 'Grass Group 5/6', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 7', protein: 'Polcalcin', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 12', protein: 'Profilin', type: 'M' },
      { name: 'Тростник', val: 0.0, code: 'Phr c', protein: '', type: 'E' },
      { name: 'Рожь, пыльца', val: 0.0, code: 'Sec c_pollen', protein: '', type: 'E' }
    ]
  }
])

// Filter groups based on search query
const filteredGroups = computed(() => {
  if (!searchQuery.value.trim()) return allergenGroups.value

  const query = searchQuery.value.toLowerCase()
  return allergenGroups.value
    .map((group) => {
      const matchedItems = group.items.filter(
        (item) =>
          item.name.toLowerCase().includes(query) ||
          item.code.toLowerCase().includes(query) ||
          (item.protein && item.protein.toLowerCase().includes(query))
      )
      return { ...group, items: matchedItems }
    })
    .filter((group) => group.items.length > 0)
})

const downloadPDF = () => {
  alert('Скачивание PDF-версии отчета...')
}
</script>

<template>
  <div class="page-container">
    <!-- Left Column: Navigation controls & cards (Sidebar) -->
    <aside class="sidebar-container">
      <!-- Promo Banner Card -->
      <div class="promo-card" id="card-promo">
        <div class="promo-content">
          <img src="/assets/banner.svg" alt="Анализ крови" class="promo-banner-img" />
          <p class="promo-text">
            Многокомпонентный анализ крови, который за один забор крови проверяет более 300 аллергенов, выявляя истинные причины реакции.
          </p>
        </div>

        <button class="promo-button" id="btn-register" @click="$router.push('/')">
          <span class="promo-button-text">Записаться на тест на аллергию</span>
          <div class="promo-button-icon">
            <img src="/assets/arrow-right-btn.svg" alt="arrow" />
          </div>
        </button>
      </div>

      <!-- Side-by-side cards -->
      <div class="cards-row">
        <!-- Search Card -->
        <div class="sub-card" id="card-search" @click="$router.push('/')">
          <div class="card-icon-wrapper">
            <img src="/assets/search-icon.svg" alt="search" />
          </div>
          <div class="card-text-group">
            <h3 class="card-title">Поиск аллергенов</h3>
            <p class="card-subtitle">Убедитесь, что тест покажет, что вам нужно</p>
          </div>
        </div>

        <!-- Demo Card (Active state added inline) -->
        <div class="sub-card active-card" id="card-demo">
          <div class="card-icon-wrapper">
            <img src="/assets/doc-icon.svg" alt="doc" />
          </div>
          <div class="card-text-group">
            <h3 class="card-title">Посмотреть демо-результат</h3>
            <p class="card-subtitle">Объясняем результаты на человеческом языке</p>
          </div>
        </div>
      </div>

      <!-- Quiz Card -->
      <div class="sidebar-row-card" id="row-quiz" @click="$router.push('/')">
        <div class="row-left-content">
          <span class="tag-badge">~5 минут</span>
          <span class="row-text">КВИЗ: Нужен ли вам тест на аллергены?</span>
        </div>
      </div>

      <!-- Profile Card -->
      <div class="sidebar-row-card" id="row-profile" @click="$router.push('/')">
        <div class="row-left-content">
          <div class="row-icon-icon" style="margin-right: 4px;">
            <img src="/assets/profile-icon.svg" alt="profile" />
          </div>
          <span class="row-text">Личный кабинет</span>
        </div>
      </div>

      <!-- About/Bottom Card -->
      <div class="sidebar-row-card" id="row-about" @click="$router.push('/')">
        <div class="row-left-content">
          <span class="row-text">Лаборатория ALEX LAB</span>
        </div>
        <div class="row-icon-icon">
          <svg width="24" height="24" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M15.9974 29.3307C23.3612 29.3307 29.3307 23.3612 29.3307 15.9974C29.3307 8.6336 23.3612 2.66406 15.9974 2.66406C8.6336 2.66406 2.66406 8.6336 2.66406 15.9974C2.66406 23.3612 8.6336 29.3307 15.9974 29.3307Z" />
            <path d="M13.3359 10.6641L18.6693 15.9974L13.3359 21.3307" />
          </svg>
        </div>
      </div>
    </aside>

    <!-- Right Column: Patient report display -->
    <main class="content-container results-page-content">
      <!-- Mobile Top Navigation Bar (Frame 290) -->
      <div class="mobile-top-bar">
        <NuxtLink to="/" class="mobile-back-button" aria-label="Назад">
          <svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M7 13L1 7L7 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </NuxtLink>
        <span class="mobile-top-title">Результаты</span>
      </div>

      <!-- Back Link (Desktop only) -->
      <div class="back-link-wrapper desktop-only">
        <NuxtLink to="/" class="back-link">
          <svg width="10" height="10" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M7 13L1 7L7 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <span>На главную</span>
        </NuxtLink>
      </div>

      <!-- Main report structure -->
      <div class="report-wrapper">
        <!-- PDF download bar -->
        <div class="download-bar">
          <button class="download-pdf-btn" @click="downloadPDF">
            <span>Скачать pdf</span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 3V15" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              <path d="M7 10L12 15L17 10" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M3 16V21H21V16" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </div>

        <!-- Patient Header Info Card -->
        <div class="patient-card">
          <div class="patient-card-header">
            <div class="patient-name-block">
              <span class="card-small-label">Пациент</span>
              <h2 class="patient-title-name">{{ patient.name }}</h2>
            </div>
            <div class="patient-ige-block">
              <span class="card-small-label">Общий IgE</span>
              <div class="patient-ige-value">
                <span class="value">{{ patient.totalIge }}</span>
                <span class="unit">kU/l</span>
              </div>
            </div>
          </div>

          <div class="patient-meta-grid">
            <div class="meta-column">
              <span class="meta-label">Дата рождения</span>
              <span class="meta-value">{{ patient.dob }}</span>
            </div>
            <div class="meta-column">
              <span class="meta-label">Номер заказа</span>
              <span class="meta-value font-mono">{{ patient.orderId }}</span>
            </div>
            <div class="meta-column">
              <span class="meta-label">Метод</span>
              <span class="meta-value">{{ patient.method }}</span>
            </div>
            <div class="meta-column">
              <span class="meta-label">Штрих-код</span>
              <span class="meta-value font-mono">{{ patient.barcode }}</span>
            </div>
            <div class="meta-column">
              <span class="meta-label">Дата теста</span>
              <span class="meta-value">{{ patient.testDate }}</span>
            </div>
          </div>
        </div>

        <!-- How to Understand Results Block -->
        <div class="explain-card">
          <h3 class="explain-title">Как понять результаты</h3>
          <p class="explain-text">
            Мы добавили аллергены к вашей крови и измерили реакцию на каждый из них. Чем больше уровень чувствительности (kU_l/l), тем сильнее выражена реакция. Если на аллерген нет реакции — отрицательная или неопределенная.
          </p>
          <p class="explain-subtext">
            Е - экстракт аллергена, М - молекулярный аллерген
          </p>

          <div class="legend-table-wrapper">
            <table class="legend-table">
              <thead>
                <tr>
                  <th>Реакция организма</th>
                  <th class="text-right">Уровень чувствительности (kU_l/l)</th>
                </tr>
              </thead>
              <tbody>
                <tr class="range-negative">
                  <td>
                    <span class="color-dot negative-dot"></span>
                    Отрицательный или неопределенный
                  </td>
                  <td class="text-right">&lt; 0.3</td>
                </tr>
                <tr class="range-low">
                  <td>
                    <span class="color-dot low-dot"></span>
                    Низкий
                  </td>
                  <td class="text-right">0.3 – 1</td>
                </tr>
                <tr class="range-medium">
                  <td>
                    <span class="color-dot medium-dot"></span>
                    Умеренный
                  </td>
                  <td class="text-right">1 – 5</td>
                </tr>
                <tr class="range-high">
                  <td>
                    <span class="color-dot high-dot"></span>
                    Высокий
                  </td>
                  <td class="text-right">5 – 15</td>
                </tr>
                <tr class="range-very-high">
                  <td>
                    <span class="color-dot very-high-dot"></span>
                    Очень высокий
                  </td>
                  <td class="text-right">&gt; 15</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Allergen Search & Results Block -->
        <div class="results-container">
          <div class="results-header-row">
            <h3 class="explain-title">Результаты</h3>
            
            <!-- Table Search Input -->
            <div class="table-search-input-wrapper">
              <svg class="search-icon-svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
              </svg>
              <input 
                type="text" 
                v-model="searchQuery" 
                placeholder="Поиск по аллергенам, кодам или белкам..."
                class="search-allergens-input"
              />
              <button v-if="searchQuery" class="clear-query-btn" @click="searchQuery = ''">&times;</button>
            </div>
          </div>

          <div class="allergen-groups-list">
            <div 
              v-for="group in filteredGroups" 
              :key="group.name" 
              class="allergen-group-block"
            >
              <h4 class="group-title-label">{{ group.name }}</h4>
              
              <div class="table-container">
                <table class="allergen-results-table">
                  <thead>
                    <tr>
                      <th class="col-name-th">Название аллергена</th>
                      <th class="col-val-th text-right">kU_l/l</th>
                      <th class="col-code-th">Аллерген</th>
                      <th class="col-protein-th">Белок</th>
                      <th class="col-type-th text-center">E/M</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr 
                      v-for="item in group.items" 
                      :key="item.code"
                      :class="['allergen-row', getClassByVal(item.val)]"
                    >
                      <td class="col-name-td">• {{ item.name }}</td>
                      <td class="col-val-td text-right font-weight-bold">{{ formatValue(item.val) }}</td>
                      <td class="col-code-td font-mono">{{ item.code }}</td>
                      <td class="col-protein-td">{{ item.protein || '—' }}</td>
                      <td class="col-type-td text-center">{{ item.type }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            
            <div v-if="filteredGroups.length === 0" class="no-matched-results">
              Ничего не найдено. Попробуйте изменить поисковый запрос.
            </div>
          </div>
        </div>

        <!-- Footer Signature block -->
        <footer class="report-footer-note">
          <p class="thank-you-title">Спасибо, что выбрали нас!</p>
          <div class="footer-contacts">
            <span class="contacts-title">В случае вопросов:</span>
            <span class="contact-item font-weight-bold">+7 996 22 92 10</span>
            <span class="contact-item font-weight-bold">alex@lab.ru</span>
          </div>
          
          <!-- Legal / Disclaimer note -->
          <div class="report-legal-disclaimer">
            * Анализ выполнен с использованием технологии молекулярной аллергодиагностики ALEX2. Данный отчет носит ознакомительный характер и не является основанием для постановки окончательного медицинского диагноза. Диагноз ставит исключительно лечащий врач на основе комплексной клинической картины и анамнеза пациента.
          </div>
        </footer>
      </div>
    </main>
  </div>
</template>

<style scoped>
/* Page container styling overrides/additions to main.css */
.results-page-content {
  padding: 40px 64px 60px 0;
  display: flex;
  flex-direction: column;
  gap: 24px;
  overflow-y: auto !important;
}

.active-card {
  background-color: #fafafa !important;
}

.back-link-wrapper {
  margin-bottom: 8px;
}

.back-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--text-black);
  text-decoration: none;
  font-size: 15px;
  font-weight: 500;
  transition: opacity 0.2s ease;
}

.back-link:hover {
  opacity: 0.7;
}

.report-wrapper {
  display: flex;
  flex-direction: column;
  gap: 24px;
  width: 100%;
  max-width: 800px;
}

.download-bar {
  display: flex;
  justify-content: flex-start;
  margin-bottom: -12px;
}

.download-pdf-btn {
  display: inline-flex;
  align-items: center;
  height: 44px;
  gap: 14px;
  background-color: #ffffff;
  border: 1px solid #dfdfdf;
  padding: 10px 18px;
  font-family: inherit;
  font-size: 16px;
  font-weight: 400;
  color: var(--text-black);
  border-radius: 0;
  backdrop-filter: blur(4px);
  cursor: pointer;
  transition: all 0.2s ease;
}

.download-pdf-btn:hover {
  background-color: #f7f7f7;
  border-color: #bbb;
}

/* Patient Card styling */
.patient-card {
  background-color: var(--bg-card-white);
  border: 1px solid var(--border-color-grey);
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.patient-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-bottom: 1px solid #f0f0f0;
  padding-bottom: 16px;
}

.card-small-label {
  font-size: 12px;
  text-transform: uppercase;
  color: var(--text-muted);
  letter-spacing: 0.5px;
  display: block;
  margin-bottom: 4px;
}

.patient-title-name {
  font-size: 32px;
  font-weight: 700;
  color: var(--text-black);
  margin: 0;
  line-height: 1.1;
}

.patient-ige-value {
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.patient-ige-value .value {
  font-size: 36px;
  font-weight: 700;
  color: var(--text-black);
}

.patient-ige-value .unit {
  font-size: 16px;
  color: var(--text-muted);
  font-weight: 500;
}

.patient-meta-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
}

.meta-column {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.meta-label {
  font-size: 12px;
  color: var(--text-muted);
}

.meta-value {
  font-size: 14px;
  font-weight: 500;
  color: var(--text-black);
}

.font-mono {
  font-family: monospace;
}

/* Explain Card styling */
.explain-card {
  background-color: var(--bg-card-white);
  border: 1px solid var(--border-color-grey);
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.explain-title {
  font-size: 20px;
  font-weight: 700;
  color: var(--text-black);
  margin: 0;
}

.explain-text {
  font-size: 15px;
  line-height: 1.5;
  color: #333;
  margin: 0;
}

.explain-subtext {
  font-size: 13px;
  color: var(--text-muted);
  margin-top: -4px;
}

.legend-table-wrapper {
  margin-top: 8px;
  border: 1px solid #f0f0f0;
}

.legend-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.legend-table th {
  background-color: #fafafa;
  color: var(--text-muted);
  font-weight: 500;
  padding: 10px 16px;
  text-align: left;
  border-bottom: 1px solid #eeeded;
}

.legend-table td {
  padding: 12px 16px;
  border-bottom: 1px solid #f0f0f0;
  vertical-align: middle;
}

.legend-table tr:last-child td {
  border-bottom: none;
}

.color-dot {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-right: 8px;
  vertical-align: middle;
}

/* Range dot colors */
.negative-dot { background-color: #d9d9d9; }
.low-dot { background-color: #ffeb3b; }
.medium-dot { background-color: #ff9800; }
.high-dot { background-color: #ff5722; }
.very-high-dot { background-color: #f44336; }

/* Range background highlights */
.range-negative { background-color: transparent; }
.range-low { background-color: #fffbe6; }
.range-medium { background-color: #fff0db; }
.range-high { background-color: #ffddba; }
.range-very-high { background-color: #ffd2cf; }

.text-right {
  text-align: right;
}

.text-center {
  text-align: center;
}

/* Search input styling */
.results-header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.table-search-input-wrapper {
  position: relative;
  width: 320px;
}

.search-icon-svg {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #999;
  pointer-events: none;
}

.search-allergens-input {
  width: 100%;
  padding: 8px 12px 8px 36px;
  font-size: 14px;
  font-family: inherit;
  border: 1px solid var(--border-color-grey);
  border-radius: 4px;
  outline: none;
  transition: border-color 0.2s ease;
}

.search-allergens-input:focus {
  border-color: #7e8f7c;
}

.clear-query-btn {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  border: none;
  background: none;
  font-size: 18px;
  color: #999;
  cursor: pointer;
}

/* Results container and tables */
.results-container {
  background-color: var(--bg-card-white);
  border: 1px solid var(--border-color-grey);
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.allergen-group-block {
  margin-bottom: 24px;
}

.allergen-group-block:last-child {
  margin-bottom: 0;
}

.group-title-label {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-black);
  margin: 0 0 12px 0;
  border-bottom: 2px solid #7e8f7c;
  padding-bottom: 6px;
}

.allergen-results-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}

.allergen-results-table th {
  color: var(--text-muted);
  font-weight: 500;
  padding: 8px 12px;
  text-align: left;
  border-bottom: 1px solid var(--border-color-grey);
}

.allergen-results-table td {
  padding: 10px 12px;
  border-bottom: 1px solid #f0f0f0;
}

.col-name-th, .col-name-td { width: 35%; }
.col-val-th, .col-val-td { width: 15%; }
.col-code-th, .col-code-td { width: 20%; }
.col-protein-th, .col-protein-td { width: 20%; }
.col-type-th, .col-type-td { width: 10%; }

.font-weight-bold {
  font-weight: 700;
}

.no-matched-results {
  text-align: center;
  padding: 40px 0;
  color: var(--text-muted);
  font-size: 15px;
}

/* Footer note styling */
.report-footer-note {
  border-top: 1px solid var(--border-color-grey);
  padding-top: 24px;
  margin-top: 16px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.thank-you-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-black);
  margin: 0;
}

.footer-contacts {
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 12px;
  color: #555;
}

.contact-item {
  color: var(--text-black);
}

.report-legal-disclaimer {
  font-size: 11px;
  color: var(--text-muted);
  opacity: 0.7;
  line-height: 1.5;
  margin-top: 8px;
  border-top: 1px dashed var(--border-color-grey);
  padding-top: 12px;
}

/* Mobile responsive navigation overrides */
.desktop-only {
  display: block;
}

.mobile-top-title {
  font-size: 21px;
  font-weight: 500;
  color: var(--text-black);
  margin-left: 16px;
}

@media (max-width: 1200px) {
  .patient-meta-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 768px) {
  .desktop-only {
    display: none;
  }
  .results-page-content {
    padding: 0 16px 64px 16px;
  }
  .patient-meta-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }
  .patient-card {
    padding: 20px;
  }
  .explain-card, .results-container {
    padding: 20px;
  }
  .results-header-row {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
  .table-search-input-wrapper {
    width: 100%;
  }
}
</style>
