<script setup>
import { computed, ref } from 'vue'
import reportData from '~/data/demo-report.json'

const searchQuery = ref('')

const normalizeSearchValue = (value = '') =>
  value
    .toLocaleLowerCase('ru-RU')
    .replaceAll('ё', 'е')
    .replace(/\s+/g, ' ')
    .trim()

const normalizedQuery = computed(() => normalizeSearchValue(searchQuery.value))

const filteredItems = computed(() => {
  if (!normalizedQuery.value) return []

  return reportData.items.filter((item) =>
    [item.designation, item.allergen, item.protein, item.category, item.section]
      .map(normalizeSearchValue)
      .some((value) => value.includes(normalizedQuery.value))
  )
})

const downloadPDF = () => {
  const link = document.createElement('a')
  link.href = '/documents/elagin-demo-result-clean.pdf'
  link.download = 'elagin-demo-result.pdf'
  link.click()
}
</script>

<template>
  <div class="page-container site-sidebar-layout">
    <SiteSidebar
      @register="$router.push('/cart')"
      @about="$router.push('/')"
    />

    <main class="content-container results-page-content">
      <div class="mobile-top-bar home-back-area">
        <HomeBackLink stretched />
      </div>

      <div class="back-link-wrapper desktop-only home-back-area">
        <HomeBackLink stretched />
      </div>

      <div class="report-wrapper">
        <div class="report-actions">
          <button class="download-pdf-btn" type="button" @click="downloadPDF">
            <span>Скачать pdf</span>
            <img src="/assets/figma-demo-download.svg" alt="" />
          </button>

          <label class="allergen-search">
            <span class="visually-hidden">Поиск по аллергенам</span>
            <img src="/assets/figma-materials-search.svg" alt="" />
            <input
              v-model="searchQuery"
              type="search"
              autocomplete="off"
              placeholder="Поиск по аллергенам"
              @keydown.esc="searchQuery = ''"
            />
            <button
              v-if="searchQuery"
              type="button"
              aria-label="Очистить поиск"
              @click="searchQuery = ''"
            >
              ×
            </button>
          </label>
        </div>

        <p v-if="normalizedQuery" class="search-summary" aria-live="polite">
          Найдено: {{ filteredItems.length }}
        </p>

        <section v-if="!normalizedQuery" class="report-pages" aria-label="Демо-результат">
          <figure class="report-page report-page-image">
            <img
              src="/assets/demo-report/page-01.png"
              alt="Краткое изложение результатов исследования"
            />
          </figure>

          <article
            v-for="page in reportData.pages"
            :key="page.number"
            class="report-page report-table-page"
            :aria-label="`Страница ${page.number} отчёта`"
          >
            <table class="report-table">
              <colgroup>
                <col class="column-designation" />
                <col class="column-allergen" />
                <col class="column-type" />
                <col class="column-protein" />
                <col class="column-value" />
              </colgroup>
              <thead>
                <tr>
                  <th>Обозначение</th>
                  <th>Аллерген</th>
                  <th class="cell-center">E/M(*)</th>
                  <th>Семейство белков</th>
                  <th class="cell-right">kUA/L</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="(row, rowIndex) in page.rows"
                  :key="`${page.number}-${rowIndex}`"
                  :class="row.kind === 'section' ? `section-row section-level-${row.level}` : 'allergen-row'"
                >
                  <th v-if="row.kind === 'section'" colspan="5" scope="rowgroup">
                    {{ row.title }}
                  </th>
                  <template v-else>
                    <td>{{ row.designation }}</td>
                    <td>{{ row.allergen }}</td>
                    <td class="cell-center">{{ row.type }}</td>
                    <td>{{ row.protein }}</td>
                    <td class="cell-right">{{ row.value }}</td>
                  </template>
                </tr>
              </tbody>
            </table>
          </article>

          <figure class="report-page report-page-image">
            <img
              src="/assets/demo-report/page-10.png"
              alt="Краткое описание результата"
              loading="lazy"
            />
          </figure>
        </section>

        <section v-else class="search-results" aria-label="Результаты поиска по аллергенам">
          <div v-if="filteredItems.length" class="search-results-table-wrap">
            <table class="search-results-table">
              <thead>
                <tr>
                  <th>Обозначение</th>
                  <th>Аллерген</th>
                  <th>E/M</th>
                  <th>Семейство белков</th>
                  <th>kUA/L</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in filteredItems" :key="`${item.page}-${item.allergen}-${index}`">
                  <td>
                    <strong>{{ item.designation }}</strong>
                    <span class="result-path">
                      {{ [item.category, item.section].filter(Boolean).join(' / ') }}
                    </span>
                  </td>
                  <td>{{ item.allergen }}</td>
                  <td class="cell-center">{{ item.type }}</td>
                  <td>{{ item.protein }}</td>
                  <td class="cell-right">{{ item.value }}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div v-else class="empty-search-result">
            <p>Ничего не найдено</p>
            <span>Попробуйте название аллергена, его код или семейство белка.</span>
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

<style scoped>
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

.report-wrapper {
  width: min(1000px, calc(100% - 64px));
  margin: 64px auto 109px;
}

.report-actions {
  display: flex;
  align-items: stretch;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 20px;
}

.download-pdf-btn {
  box-sizing: border-box;
  width: 197px;
  height: 56px;
  padding: 16px 24px;
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  border: 1px solid #dfdfdf;
  border-radius: 0;
  background: #fff;
  color: #000;
  font-family: Roboto, Arial, sans-serif;
  font-size: 18px;
  line-height: 24px;
  cursor: pointer;
}

.download-pdf-btn:hover,
.download-pdf-btn:focus-visible {
  background: #f8f8f8;
  border-color: #aaa;
}

.download-pdf-btn img {
  width: 24px;
  height: 24px;
}

.allergen-search {
  position: relative;
  flex: 1 1 480px;
  max-width: 560px;
  height: 56px;
  background: #fff;
}

.allergen-search > img {
  position: absolute;
  z-index: 1;
  top: 50%;
  left: 20px;
  width: 22px;
  height: 22px;
  transform: translateY(-50%);
  pointer-events: none;
}

.allergen-search input {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  padding: 0 52px 0 56px;
  border: 1px solid #cfcfcf;
  border-radius: 0;
  outline: none;
  background: #fff;
  color: #000;
  font: 18px/24px Roboto, Arial, sans-serif;
  appearance: none;
}

.allergen-search input::-webkit-search-cancel-button {
  display: none;
}

.allergen-search input:focus {
  border-color: #000;
  box-shadow: inset 0 0 0 1px #000;
}

.allergen-search button {
  position: absolute;
  top: 50%;
  right: 14px;
  width: 34px;
  height: 34px;
  padding: 0;
  transform: translateY(-50%);
  border: 0;
  background: transparent;
  color: #777;
  font: 28px/32px Arial, sans-serif;
  cursor: pointer;
}

.search-summary {
  margin: -4px 0 12px;
  color: rgba(0, 0, 0, 0.55);
  font: 15px/20px Roboto, Arial, sans-serif;
}

.report-pages {
  display: grid;
  gap: 20px;
}

.report-page {
  box-sizing: border-box;
  width: 100%;
  margin: 0;
  aspect-ratio: 595 / 800;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 6px 24px rgba(30, 46, 52, 0.12);
}

.report-page-image img {
  display: block;
  width: 100%;
  height: auto;
}

.report-table-page {
  container-type: inline-size;
  padding: 4.7cqw 4.7cqw 3.5cqw;
}

.report-table {
  width: 100%;
  table-layout: fixed;
  border-collapse: collapse;
  color: #111;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 1.52cqw;
  line-height: 1.02;
}

.report-table .column-designation { width: 35%; }
.report-table .column-allergen { width: 21%; }
.report-table .column-type { width: 7%; }
.report-table .column-protein { width: 31%; }
.report-table .column-value { width: 6%; }

.report-table th,
.report-table td {
  box-sizing: border-box;
  height: 2.58cqw;
  padding: 0.35cqw 0.5cqw;
  border: 0.11cqw solid #d0d0d0;
  text-align: left;
  vertical-align: middle;
  overflow-wrap: anywhere;
}

.report-table thead th {
  height: 3.05cqw;
  font-weight: 700;
  white-space: nowrap;
}

.report-table .section-row th {
  height: 3.45cqw;
  font-size: 1.62cqw;
  font-weight: 700;
}

.report-table .section-level-1 th {
  font-size: 1.86cqw;
}

.cell-center {
  text-align: center !important;
}

.cell-right {
  text-align: right !important;
  white-space: nowrap;
}

.search-results {
  min-height: 520px;
  background: #fff;
  box-shadow: 0 6px 24px rgba(30, 46, 52, 0.12);
}

.search-results-table-wrap {
  overflow-x: auto;
}

.search-results-table {
  width: 100%;
  min-width: 760px;
  border-collapse: collapse;
  color: #111;
  font: 16px/1.25 Arial, Helvetica, sans-serif;
}

.search-results-table th,
.search-results-table td {
  padding: 14px 16px;
  border: 1px solid #d4d4d4;
  text-align: left;
  vertical-align: top;
}

.search-results-table thead th {
  background: #f7f7f7;
  font-weight: 700;
}

.search-results-table th:nth-child(1) { width: 35%; }
.search-results-table th:nth-child(2) { width: 21%; }
.search-results-table th:nth-child(3) { width: 7%; }
.search-results-table th:nth-child(4) { width: 29%; }
.search-results-table th:nth-child(5) { width: 8%; }

.search-results-table strong {
  display: block;
  font-weight: 400;
}

.result-path {
  display: block;
  margin-top: 5px;
  color: rgba(0, 0, 0, 0.46);
  font-size: 13px;
}

.empty-search-result {
  min-height: 520px;
  display: grid;
  place-content: center;
  padding: 32px;
  text-align: center;
}

.empty-search-result p {
  margin: 0 0 8px;
  font: 24px/30px Arial, Helvetica, sans-serif;
}

.empty-search-result span {
  color: rgba(0, 0, 0, 0.5);
  font: 16px/22px Arial, Helvetica, sans-serif;
}

.visually-hidden {
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

.desktop-only {
  display: block;
}

@media (max-width: 1024px) {
  .desktop-only {
    display: none !important;
  }

  .results-page-content {
    height: 100dvh !important;
    max-height: 100dvh !important;
    padding: 0 16px 64px !important;
    -webkit-overflow-scrolling: touch;
  }

  .mobile-top-bar {
    box-sizing: border-box;
    width: calc(100% + 32px);
    height: 72px;
    margin: 0 -16px 45px;
    padding: 24px 32px;
    position: static;
  }

  .report-wrapper {
    width: 100%;
    margin: 0;
  }
}

@media (max-width: 680px) {
  .report-actions {
    flex-direction: column-reverse;
    gap: 10px;
  }

  .allergen-search,
  .download-pdf-btn {
    flex: none;
    width: 100%;
    max-width: none;
    height: 58px;
  }

  .allergen-search input {
    font-size: 16px;
  }

  .report-pages {
    gap: 12px;
  }

  .search-results {
    min-height: 420px;
  }
}

@media print {
  .site-sidebar,
  .mobile-top-bar,
  .back-link-wrapper,
  .report-actions,
  .search-summary {
    display: none !important;
  }

  .results-page-content,
  .report-wrapper {
    width: 100% !important;
    height: auto !important;
    margin: 0 !important;
    overflow: visible !important;
    background: #fff !important;
  }

  .report-page {
    break-after: page;
    box-shadow: none;
  }
}
</style>
