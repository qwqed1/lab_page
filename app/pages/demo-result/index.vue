<script setup>
import { ref, computed } from 'vue'

const redirect = (url) => {
  window.location.href = url
}

// Search query for the results table
const searchQuery = ref('')

// Mock Patient Data from the screenshot
const patient = {
  name: 'Елагин М.С.',
  dob: '11.06.2006',
  orderId: 'елагин',
  method: 'ALEX2',
  barcode: '02CSU126',
  testDate: '16.12.2025',
  totalIge: 1440
}

// Table range helper for highlighting
const getClassByVal = (item) => {
  if (item.level) return `range-${item.level}`
  const val = item.val
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
    id: 'grass-1',
    name: 'Пыльца трав',
    items: [
      { name: 'Свинорой пальчатый', val: 0.0, code: 'Cyn d', protein: '', type: 'E' },
      { name: 'Свинорой пальчатый', val: 0.0, code: 'Cyn d 1', protein: 'Beta-Expansin', type: 'M' },
      { name: 'Плевел многолетний', val: 0.0, code: 'Lol p 1', protein: 'Beta-Expansin', type: 'E' },
      { name: 'Паслен/Стрихнос лесной', val: 0.0, code: 'Pas s', protein: '', type: 'E' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 1', protein: 'Beta-Expansin', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.6, code: 'Phl p 5.0101', protein: 'Grass Group 5/6', type: 'M', level: 'low' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 6', protein: 'Grass Group 5/6', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 7', protein: 'Polcalcin', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 12', protein: 'Profilin', type: 'M' },
      { name: 'Тростник', val: 0.0, code: 'Phr c', protein: '', type: 'E' },
      { name: 'Рожь, пыльца', val: 0.0, code: 'Sec c_pollen', protein: '', type: 'E' }
    ]
  },
  {
    id: 'grass-2',
    name: 'Пыльца трав',
    items: [
      { name: 'Свинорой пальчатый', val: 0.0, code: 'Cyn d', protein: '', type: 'E' },
      { name: 'Свинорой пальчатый', val: 0.0, code: 'Cyn d 1', protein: 'Beta-Expansin', type: 'M' },
      { name: 'Плевел многолетний', val: 0.0, code: 'Lol p 1', protein: 'Beta-Expansin', type: 'E' },
      { name: 'Паслен/Стрихнос лесной', val: 7.0, code: 'Pas s', protein: '', type: 'E', level: 'high' },
      { name: 'Тимофеевка луговая', val: 6.0, code: 'Phl p 1', protein: 'Beta-Expansin', type: 'M', level: 'medium' },
      { name: 'Тимофеевка луговая', val: 0.6, code: 'Phl p 5.0101', protein: 'Grass Group 5/6', type: 'M', level: 'low' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 6', protein: 'Grass Group 5/6', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 7', protein: 'Polcalcin', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 12', protein: 'Profilin', type: 'M' },
      { name: 'Тростник', val: 0.0, code: 'Phr c', protein: '', type: 'E' },
      { name: 'Рожь, пыльца', val: 0.0, code: 'Sec c_pollen', protein: '', type: 'E' }
    ]
  },
  {
    id: 'grass-3',
    name: 'Пыльца трав',
    items: [
      { name: 'Свинорой пальчатый', val: 32.0, code: 'Cyn d', protein: '', type: 'E', level: 'very-high' },
      { name: 'Свинорой пальчатый', val: 0.0, code: 'Cyn d 1', protein: 'Beta-Expansin', type: 'M' },
      { name: 'Плевел многолетний', val: 0.0, code: 'Lol p 1', protein: 'Beta-Expansin', type: 'E' },
      { name: 'Паслен/Стрихнос лесной', val: 0.0, code: 'Pas s', protein: '', type: 'E' },
      { name: 'Тимофеевка луговая', val: 0.0, code: 'Phl p 1', protein: 'Beta-Expansin', type: 'M' },
      { name: 'Тимофеевка луговая', val: 0.6, code: 'Phl p 5.0101', protein: 'Grass Group 5/6', type: 'M', level: 'low' },
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
  window.print()
}
</script>

<template>
  <div class="page-container site-sidebar-layout">
    <SiteSidebar
      @register="$router.push('/cart')"
      @about="$router.push('/')"
    />

    <!-- Right Column: Patient report display -->
    <main class="content-container results-page-content">
      <!-- Mobile Top Navigation Bar (Frame 290) -->
      <div class="mobile-top-bar">
        <HomeBackLink />
      </div>

      <!-- Back Link (Desktop only) -->
      <div class="back-link-wrapper desktop-only">
        <HomeBackLink />
      </div>

      <!-- Main report structure -->
      <div class="report-wrapper">
        <!-- PDF download bar -->
        <div class="download-bar">
          <button class="download-pdf-btn" @click="downloadPDF">
            <span>Скачать pdf</span>
            <img src="/assets/figma-demo-download.svg" alt="" />
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
              </div>
            </div>
          </div>

          <div class="patient-meta-grid">
            <div class="meta-column">
              <span class="meta-label">Дата рождения</span>
              <span class="meta-value">{{ patient.dob }}</span>
            </div>
            <div class="meta-column">
              <span class="meta-label">Номер образца</span>
              <span class="meta-value font-mono">{{ patient.orderId }}</span>
            </div>
            <div class="meta-column">
              <span class="meta-label">Метод</span>
              <span class="meta-value">{{ patient.method }}</span>
            </div>
            <div class="meta-column">
              <span class="meta-label">QR-код</span>
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
            Мы добавили аллергены к вашей крови и измерили реакцию на каждый из них. Чем больше уровень чувствительности (kU A/L), тем сильнее выражена реакция. Если на аллерген нет — реакция отрицательная или неопределённая.
          </p>
          <p class="explain-subtext">
            E = экстракт аллергена, M = молекулярный аллерген
          </p>

          <div class="legend-table-wrapper">
            <table class="legend-table">
              <thead>
                <tr>
                  <th>Реакция организма</th>
                  <th class="text-right">Уровень чувствительности <span>(kU A/L)</span></th>
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
                    Умеренная
                  </td>
                  <td class="text-right">5 – 15</td>
                </tr>
                <tr class="range-high">
                  <td>
                    <span class="color-dot high-dot"></span>
                    Высокая
                  </td>
                  <td class="text-right">5 – 15</td>
                </tr>
                <tr class="range-very-high">
                  <td>
                    <span class="color-dot very-high-dot"></span>
                    Очень высокая
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
              <img class="search-icon-svg" src="/assets/figma-search-icon.svg" alt="" />
              <input 
                type="text" 
                v-model="searchQuery" 
                placeholder="Поиск по аллергенам, кодам или белкам..."
                class="search-allergens-input"
              />
              <button v-if="searchQuery" class="clear-query-btn" @click="searchQuery = ''">&times;</button>
            </div>
          </div>

          <div class="results-column-head" aria-hidden="true">
            <span>Название аллергена</span>
            <span>kU A/L</span>
            <span>Аллерген</span>
            <span>Белки</span>
            <span>E/M</span>
          </div>

          <div class="allergen-groups-list">
            <div 
              v-for="group in filteredGroups" 
              :key="group.id"
              class="allergen-group-block"
            >
              <h4 class="group-title-label">{{ group.name }}</h4>
              
              <div class="table-container">
                <table class="allergen-results-table">
                  <thead>
                    <tr>
                      <th class="col-name-th">Название аллергена</th>
                      <th class="col-val-th text-right">kU A/L</th>
                      <th class="col-code-th">Аллерген</th>
                      <th class="col-protein-th">Белок</th>
                      <th class="col-type-th text-center">E/M</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr 
                      v-for="item in group.items" 
                      :key="item.code"
                      :class="['allergen-row', getClassByVal(item)]"
                    >
                      <td class="col-name-td">• {{ item.name }}</td>
                      <td class="col-val-td text-right font-weight-bold">{{ formatValue(item.val) }}</td>
                      <td class="col-code-td font-mono">{{ item.code }}</td>
                      <td class="col-protein-td">{{ item.protein || '-' }}</td>
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
          <p class="thank-you-title">Спасибо, что выбрали нас!<br />В случае вопросов:</p>
          <div class="footer-contacts">
            <span class="contact-item">+7 999 43 94 94</span>
            <span class="contact-item">alexlab@lab.ru</span>
          </div>
          
          <!-- Legal / Disclaimer note -->
          <div class="report-legal-disclaimer">
            ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ: ИНТЕРПРЕТАЦИЯ РАВЕН — ЭТО ИНСТРУМЕНТ, ПОМОГАЮЩИЙ ВРАЧУ В ДИАГНОСТИКЕ АЛЛЕРГИИ И В ПОНИМАНИИ РЕЗУЛЬТАТОВ МОЛЕКУЛЯРНЫХ ТЕСТОВ. ТЕСТЫ IN VITRO ПОКАЗЫВАЮТ ЧУВСТВИТЕЛЬНОСТЬ ТОЛЬКО К ОСОБЫМ АЛЛЕРГЕНАМ. ДИАГНОЗ ДОЛЖЕН ПОДТВЕРЖДАТЬСЯ СПЕЦИАЛИСТОМ.
          </div>
        </footer>
      </div>
    </main>
  </div>
</template>

<style scoped>
/* Page container styling overrides/additions to main.css */
.results-page-content {
  padding: 40px 64px 60px 64px;
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
  gap: 20px;
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

/* Figma 23:73 — report geometry and typography */
.results-page-content {
  box-sizing: border-box;
  height: 100dvh !important;
  padding: 0 !important;
  gap: 0;
  align-items: stretch;
  background: #f5f5f5;
  overflow-x: hidden !important;
  overflow-y: auto !important;
}

.back-link-wrapper {
  box-sizing: border-box;
  width: 100%;
  height: 72px;
  margin: 0;
  padding: 24px 32px;
  display: flex;
  align-items: center;
  background: #fff;
  border-bottom: 1px solid #dfdfdf;
}

.back-link {
  gap: 8px;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 17px;
  line-height: 24px;
  font-weight: 400;
}

.back-link img,
.mobile-back-button img {
  display: block;
  width: 24px;
  height: 24px;
}

.report-wrapper {
  width: min(1000px, calc(100% - 64px));
  max-width: none;
  margin: 64px auto 109px;
  gap: 0;
}

.download-bar {
  margin: 0 0 12px;
}

.download-pdf-btn {
  box-sizing: border-box;
  width: 197px;
  height: 56px;
  padding: 16px 24px;
  justify-content: space-between;
  gap: 24px;
  border-color: #dfdfdf;
  font-family: Roboto, Arial, sans-serif;
  font-size: 18px;
  line-height: 24px;
  white-space: nowrap;
}

.download-pdf-btn span {
  flex: 0 0 auto;
}

.download-pdf-btn img {
  display: block;
  width: 24px;
  height: 24px;
}

.patient-card,
.explain-card,
.results-container {
  box-sizing: border-box;
  width: 100%;
  border: 0;
  border-radius: 0;
}

.patient-card {
  height: 220px;
  padding: 38px 32px 58px;
  gap: 24px;
}

.patient-card-header {
  justify-content: flex-start;
  align-items: flex-start;
  gap: 24px;
  padding: 0;
  border: 0;
}

.patient-name-block,
.patient-ige-block {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.card-small-label {
  margin: 0;
  color: #000;
  opacity: 0.3;
  font-size: 16px;
  line-height: 19px;
  font-weight: 400;
  text-transform: none;
  letter-spacing: 0;
}

.patient-title-name,
.patient-ige-value .value {
  font-size: 32px;
  line-height: 38px;
  font-weight: 400;
}

.patient-meta-grid {
  display: grid;
  grid-template-columns: 106px 102px 62px 99px 106px;
  gap: 48px;
  justify-content: start;
}

.meta-column {
  gap: 10px;
}

.meta-label {
  color: #000;
  opacity: 0.3;
  font-size: 14px;
  line-height: 16px;
}

.meta-value {
  font-family: Roboto, Arial, sans-serif;
  font-size: 21px;
  line-height: 15px;
  font-weight: 400;
  white-space: nowrap;
}

.font-mono {
  font-family: Roboto, Arial, sans-serif;
}

.explain-card {
  height: 690px;
  padding: 64px 32px;
  gap: 0;
  background: rgba(0, 0, 0, 0.03);
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

.explain-title {
  font-size: 24px;
  line-height: 29px;
  font-weight: 400;
}

.explain-text {
  width: 481px;
  max-width: 100%;
  margin: 21px 0 0;
  color: #000;
  opacity: 0.5;
  font-size: 18px;
  line-height: 18px;
}

.explain-subtext {
  margin: 8px 0 0;
  color: #000;
  opacity: 0.1;
  font-size: 18px;
  line-height: 18px;
}

.legend-table-wrapper {
  margin-top: 32px;
  padding-top: 32px;
  border: 0;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

.legend-table {
  font-size: 18px;
  line-height: 13px;
}

.legend-table th {
  height: 29px;
  padding: 0;
  background: transparent;
  border: 0;
  color: #000;
  font-weight: 400;
  vertical-align: top;
}

.legend-table th span {
  opacity: 0.2;
}

.legend-table td {
  box-sizing: border-box;
  height: 61px;
  padding: 24px;
  border: 0;
}

.color-dot {
  display: none;
}

.range-negative { background: #fff; }
.range-low { background: #fffacd; }
.range-medium { background: #ffc99a; }
.range-high { background: #ffa888; }
.range-very-high { background: #ff7a7a; }

.results-container {
  padding: 64px 32px;
  gap: 0;
  background: #fff;
}

.results-header-row {
  margin: 0 0 24px;
  align-items: center;
  gap: 32px;
}

.results-header-row .explain-title {
  flex: 0 0 auto;
  font-size: 32px;
  line-height: 38px;
}

.table-search-input-wrapper {
  width: min(420px, 48%);
  margin-left: auto;
}

.search-icon-svg {
  width: 20px;
  height: 20px;
  left: 16px;
  opacity: 0.45;
}

.search-allergens-input {
  box-sizing: border-box;
  height: 48px;
  padding: 0 44px 0 48px;
  border: 1px solid #dfdfdf;
  border-radius: 0;
  font-size: 16px;
}

.results-column-head {
  display: grid;
  grid-template-columns: 35% 12% 19% 30% 4%;
  margin-bottom: 24px;
  color: #000;
  opacity: 0.2;
  font-size: 18px;
  line-height: 16px;
}

.results-column-head span:nth-child(2),
.results-column-head span:nth-child(5) {
  text-align: center;
}

.allergen-groups-list {
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.allergen-group-block,
.allergen-group-block:last-child {
  margin: 0;
}

.group-title-label {
  margin: 0 0 10px;
  padding: 0;
  border: 0;
  font-size: 18px;
  line-height: 18px;
  font-weight: 400;
}

.allergen-results-table {
  table-layout: fixed;
  font-size: 18px;
  line-height: 13px;
}

.allergen-results-table thead {
  display: none;
}

.allergen-results-table td {
  box-sizing: border-box;
  height: 29px;
  padding: 8px 0;
  border: 0;
  color: rgba(0, 0, 0, 0.5);
  font-weight: 400;
}

.allergen-results-table .col-name-td { width: 35%; padding-left: 2px; }
.allergen-results-table .col-val-td { width: 12%; text-align: center; }
.allergen-results-table .col-code-td { width: 19%; }
.allergen-results-table .col-protein-td { width: 30%; }
.allergen-results-table .col-type-td { width: 4%; text-align: center; }

.report-footer-note {
  box-sizing: border-box;
  width: 100%;
  margin: 0;
  padding: 36px 32px 38px;
  gap: 0;
  border: 0;
  background: #fff;
}

.thank-you-title {
  margin: 0;
  font-size: 24px;
  line-height: 24px;
  font-weight: 400;
}

.footer-contacts {
  margin-top: 24px;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
  color: #000;
  opacity: 0.5;
  font-size: 18px;
  line-height: 13px;
}

.report-legal-disclaimer {
  width: 726px;
  max-width: 100%;
  margin-top: 64px;
  padding: 0;
  border: 0;
  color: #000;
  opacity: 0.2;
  font-size: 14px;
  line-height: 16px;
}

@media (max-width: 1024px) {
  .desktop-only {
    display: none !important;
  }

  .results-page-content {
    height: auto !important;
    min-height: 100dvh;
    padding: 0 16px 64px !important;
    overflow: visible !important;
  }

  .mobile-top-bar {
    box-sizing: border-box;
    width: calc(100% + 32px);
    height: 72px;
    margin: 0 -16px 45px;
    padding: 24px 32px;
    position: static;
  }

  .mobile-back-button {
    padding: 0;
  }

  .report-wrapper {
    width: 100%;
    margin: 0;
  }

  .download-pdf-btn {
    width: 100%;
    height: 66px;
    padding: 21px 24px;
  }

  .patient-meta-grid {
    grid-template-columns: repeat(5, minmax(0, 1fr));
  }
}

@media (max-width: 600px) {
  .patient-card {
    height: 85px;
    padding: 15px 12px 22px;
    gap: 9px;
  }

  .patient-card-header {
    gap: 9px;
  }

  .patient-name-block,
  .patient-ige-block {
    gap: 1px;
  }

  .card-small-label {
    font-size: 6.2px;
    line-height: 7.4px;
  }

  .patient-title-name,
  .patient-ige-value .value {
    font-size: 12.4px;
    line-height: 14.7px;
  }

  .patient-meta-grid {
    gap: 18px;
  }

  .meta-column {
    gap: 4px;
  }

  .meta-label {
    font-size: 5.4px;
    line-height: 6.2px;
  }

  .meta-value {
    font-size: 8.1px;
    line-height: 6px;
  }

  .explain-card {
    height: 268px;
    padding: 25px 12px;
  }

  .explain-title {
    font-size: 9.3px;
    line-height: 11.2px;
  }

  .explain-text {
    width: 187px;
    margin-top: 8px;
    font-size: 7px;
    line-height: 7px;
  }

  .explain-subtext {
    margin-top: 3px;
    font-size: 7px;
    line-height: 7px;
  }

  .legend-table-wrapper {
    margin-top: 12px;
    padding-top: 12px;
  }

  .legend-table {
    font-size: 7px;
    line-height: 5px;
  }

  .legend-table th {
    height: 11px;
  }

  .legend-table td {
    height: 24px;
    padding: 9px;
  }

  .results-container {
    padding: 25px 12px;
  }

  .results-header-row {
    margin-bottom: 12px;
    gap: 10px;
    align-items: flex-start;
  }

  .results-header-row .explain-title {
    font-size: 12.4px;
    line-height: 15px;
  }

  .table-search-input-wrapper {
    width: 100%;
  }

  .search-allergens-input {
    height: 36px;
    padding-left: 38px;
    font-size: 11px;
  }

  .search-icon-svg {
    left: 12px;
    width: 16px;
    height: 16px;
  }

  .results-column-head {
    margin-bottom: 9px;
    font-size: 7px;
    line-height: 6px;
  }

  .allergen-groups-list {
    gap: 9px;
  }

  .group-title-label {
    margin-bottom: 4px;
    font-size: 7px;
    line-height: 7px;
  }

  .allergen-results-table {
    font-size: 7px;
    line-height: 5px;
  }

  .allergen-results-table td {
    height: 11px;
    padding: 3px 0;
  }

  .report-footer-note {
    padding: 14px 12px 15px;
  }

  .thank-you-title {
    font-size: 9.3px;
    line-height: 9.3px;
  }

  .footer-contacts {
    margin-top: 9px;
    gap: 5px;
    font-size: 7px;
    line-height: 5px;
  }

  .report-legal-disclaimer {
    width: 282px;
    margin-top: 25px;
    font-size: 5.4px;
    line-height: 6.2px;
  }
}

@media print {
  .site-sidebar,
  .mobile-top-bar,
  .back-link-wrapper,
  .download-bar,
  .table-search-input-wrapper {
    display: none !important;
  }

  .results-page-content,
  .report-wrapper {
    width: 100% !important;
    height: auto !important;
    margin: 0 !important;
    overflow: visible !important;
  }
}
</style>
