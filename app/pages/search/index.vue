<script setup>
import { ref, computed, watch } from 'vue'

const redirect = (url) => {
  window.location.href = url
}

const searchQuery = ref('')
const selectedAllergen = ref(null)

const allergensList = [
  'Апельсин', 'Яблоко', 'Береза', 'Ольха', 'Кошачья шерсть',
  'Собачья шерсть', 'Клубника', 'Клещи пыли', 'Банан', 'Яйцо',
  'Молоко', 'Арахис', 'Лесной орех', 'Пшеница', 'Рожь',
  'Тимофеевка', 'Ежа сборная', 'Полынь', 'Амброзия', 'Плесень',
  'Краб', 'Креветка', 'Треска', 'Соя', 'Персик',
  'Морковь', 'Сельдерей', 'Горчица', 'Кунжут', 'Горох',
]

// Detailed data for allergens to display in the split view
const allergensData = [
  {
    name: 'Апельсин',
    description: 'Один из самых частных аллергенов',
    included: true,
    related: ['Кошачья шерсть', 'Кошачья шерсть', 'Пыльца берёзы', 'Кошачья шерсть', 'Банан', 'Пыль']
  },
  {
    name: 'Кошачья шерсть',
    description: 'Один из самых частных аллергенов',
    included: true,
    related: ['Собачья шерсть', 'Клещи пыли', 'Банан', 'Пыль']
  },
  {
    name: 'Пыльца берёзы',
    description: 'Один из самых частных аллергенов',
    included: true,
    related: ['Апельсин', 'Яблоко', 'Кошачья шерсть', 'Банан']
  },
  {
    name: 'Банан',
    description: 'Один из самых частных аллергенов',
    included: true,
    related: ['Апельсин', 'Кошачья шерсть', 'Пыль']
  },
  {
    name: 'Пыль',
    description: 'Один из самых частных аллергенов',
    included: true,
    related: ['Кошачья шерсть', 'Клещи пыли', 'Банан']
  },
  {
    name: 'Яблоко',
    description: 'Один из самых частных аллергенов',
    included: true,
    related: ['Пыльца берёзы', 'Апельсин', 'Банан']
  }
]

// Get allergen detail object (with fallback)
const getAllergenDetail = (name) => {
  const found = allergensData.find(a => a.name.toLowerCase() === name.toLowerCase())
  if (found) return found
  return {
    name: name,
    description: 'Один из самых частных аллергенов',
    included: true,
    related: ['Кошачья шерсть', 'Пыльца берёзы', 'Банан', 'Пыль']
  }
}

const popularAllergenPattern = [
  'Кошачья шерсть', 'Банан', 'Пыль', 'Клубника', 'Тараканы', 'Пыльца берёзы'
]

const allergenButtonWidths = {
  'Кошачья шерсть': 190,
  'Банан': 100,
  'Пыль': 96,
  'Клубника': 129,
  'Тараканы': 132,
  'Пыльца берёзы': 183,
  'Апельсин': 132
}

// The Figma frame contains twelve repetitions of the popular-allergen pattern.
// Keeping the data generated makes the visual rhythm easy to maintain.
const popularAllergens = Array.from(
  { length: 12 },
  () => popularAllergenPattern
).flat()

const filteredAllergens = computed(() => {
  if (!searchQuery.value.trim()) {
    return popularAllergens
  }
  const q = searchQuery.value.toLowerCase()
  // Объединяем оба списка, чтобы гарантировать поиск по всем аллергенам
  const combinedList = Array.from(new Set([...popularAllergens, ...allergensList]))
  return combinedList.filter(a => a.toLowerCase().includes(q))
})

const selectAllergen = (name) => {
  selectedAllergen.value = getAllergenDetail(name)
  searchQuery.value = name
}

const getAllergenButtonStyle = (name) => {
  const width = allergenButtonWidths[name]
  return width ? { width: `${width}px` } : undefined
}

const selectAllergenByName = (name) => {
  selectAllergen(name)
}

const goBackToSearch = () => {
  selectedAllergen.value = null
  searchQuery.value = ''
}

// If user types while viewing details, close detail view to show matching search results
watch(searchQuery, (newVal) => {
  if (selectedAllergen.value && newVal !== selectedAllergen.value.name) {
    selectedAllergen.value = null
  }
})

const redirectToCart = () => {
  navigateTo('/cart')
}
</script>

<template>
  <div class="search-page-container site-sidebar-layout">
    <SiteSidebar
      @register="redirectToCart"
      @about="$router.push('/')"
    />

    <!-- Правая панель — контент поиска -->
    <main class="search-main">
      <!-- "На главную" ссылка -->
      <div class="search-back-row home-back-area">
        <HomeBackLink stretched />
      </div>

      <!-- Центрированный контент -->
      <div
        class="search-center"
        :class="{
          'search-center--filtered': searchQuery.trim() && !selectedAllergen,
          'search-center--detail': selectedAllergen
        }"
      >
        <h1 class="search-heading">Поиск аллергенов,<br>которые покажет ALEX2</h1>
        <p class="search-subheading">Более 300 аллергенов в одном тесте —<br>убедитесь сами</p>

        <!-- Поисковая строка -->
        <div class="search-input-wrapper">
          <input
            id="allergen-search-input"
            v-model="searchQuery"
            type="text"
            class="search-input"
            placeholder="Введите продукт"
            autocomplete="off"
          />
          <button class="search-icon-btn" aria-label="Поиск">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="11" cy="11" r="7" stroke="#000" stroke-width="1.8"/>
              <path d="M16.5 16.5L21 21" stroke="#000" stroke-width="1.8" stroke-linecap="round"/>
            </svg>
          </button>
        </div>

        <!-- Разделитель (Vector 18 в Figma) -->
        <div class="search-divider"></div>

        <!-- Контент под строкой поиска: Результаты или Детали -->
        <div class="search-bottom-content">
          <!-- Режим детального просмотра выбранного аллергена -->
          <div v-if="selectedAllergen" class="search-details-grid">
            <!-- Левая колонка (Информация об аллергене) -->
            <div class="details-left-col">
              <div class="details-left-main">
                <!-- Иконка головы медведя (Panda/Bear) -->
                <div class="allergen-icon-box">
                  <svg width="42" height="42" viewBox="0 0 42 42" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <!-- Ушки -->
                    <circle cx="10" cy="10" r="6" stroke="black" stroke-width="2" fill="white" />
                    <circle cx="10" cy="10" r="3" fill="black" />
                    <circle cx="32" cy="10" r="6" stroke="black" stroke-width="2" fill="white" />
                    <circle cx="32" cy="10" r="3" fill="black" />
                    <!-- Контур головы -->
                    <rect x="4" y="11" width="34" height="27" rx="12" stroke="black" stroke-width="2" fill="white" />
                    <!-- Глаза -->
                    <circle cx="14" cy="20" r="2.5" fill="black" />
                    <circle cx="28" cy="20" r="2.5" fill="black" />
                    <!-- Мордочка -->
                    <ellipse cx="21" cy="26" rx="5" ry="3.5" stroke="black" stroke-width="1.5" fill="#f5f5f5" />
                    <polygon points="19,25 23,25 21,27.5" fill="black" />
                    <!-- Линия рта -->
                    <path d="M21 28.5V31C21 31.5 20.5 32 20 32M21 31C21 31.5 21.5 32 22 32" stroke="black" stroke-width="1.5" stroke-linecap="round" />
                  </svg>
                </div>

                <div class="detail-copy">
                  <!-- Зеленый бейдж -->
                  <div v-if="selectedAllergen.included" class="test-badge">
                    Входит в тест ALEX2
                  </div>

                  <div class="detail-text-group">
                    <!-- Название аллергена -->
                    <h2 class="detail-name">{{ selectedAllergen.name }}</h2>

                    <!-- Описание -->
                    <p class="detail-desc">{{ selectedAllergen.description }}</p>
                  </div>
                </div>
              </div>

              <!-- Футер левой колонки (Назад ко всем аллергенам) -->
              <div class="details-left-footer" @click="goBackToSearch">
                <div class="back-arrow-circle">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10" />
                    <path d="M12 8l-4 4 4 4M16 12H8" />
                  </svg>
                </div>
                <span>Назад ко всем аллергенам</span>
              </div>
            </div>

            <!-- Правая колонка (Связанные аллергены) -->
            <div class="details-right-col">
              <h3 class="related-title">Связанные аллергены:</h3>
              <div class="related-tags-container">
                <button
                  v-for="(rel, index) in selectedAllergen.related"
                  :key="index"
                  class="related-tag-btn"
                  :data-allergen="rel"
                  @click="selectAllergenByName(rel)"
                >
                  {{ rel }}
                </button>
              </div>
            </div>
          </div>

          <!-- Режим обычного поиска (список тегов результатов) -->
          <div v-else class="search-results">
            <button
              v-for="(allergen, index) in filteredAllergens"
              :key="`${allergen}-${index}`"
              class="allergen-tag"
              :style="getAllergenButtonStyle(allergen)"
              @click="selectAllergen(allergen)"
            >
              {{ allergen }}
            </button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
.active-card {
  background-color: #fafafa !important;
}

/* ========================================
   ОБЩАЯ СЕТКА СТРАНИЦЫ ПОИСКА (БЕЗ GAP)
   ======================================= */

.search-page-container {
  display: grid;
  grid-template-columns: 677px 1fr;
  gap: 0;
  max-width: 1920px;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100dvh;
  min-height: 0;
  overflow: hidden;
  background: #f5f5f5;
}

/* ========================================
   ПРАВАЯ ПАНЕЛЬ ПОИСКА
   ======================================== */

.search-main {
  flex: 1;
  background: #f5f5f5;
  display: flex;
  flex-direction: column;
  height: 100dvh;
  min-height: 0;
  position: relative;
  overflow-y: auto;
  scrollbar-width: none;
}

.search-main::-webkit-scrollbar {
  display: none;
}

/* "На главную" (Соответствует Frame 290 в Figma) */
.search-back-row {
  height: 72px;
  background: #ffffff;
  border-bottom: 1px solid #dfdfdf;
  padding: 24px 32px;
  display: flex;
  align-items: center;
  flex: 0 0 72px;
}

.search-back-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background: none;
  border: none;
  cursor: pointer;
  text-decoration: none;
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  color: #000;
  padding: 0;
  line-height: 24px;
}

.search-back-icon {
  width: 24px;
  height: 24px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 24px;
}

.search-back-btn:hover {
  opacity: 0.7;
}

/* Центрированный блок */
.search-center {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 218px 64px 48px;
}

.search-center--filtered,
.search-center--detail {
  padding-top: 128px;
}

.search-heading {
  font-size: 42px;
  font-weight: 400;
  font-family: 'Roboto', sans-serif;
  color: #000;
  text-align: center;
  line-height: 49px;
  margin: 0 0 16px;
}

.search-subheading {
  font-size: 21px;
  font-weight: 400;
  font-family: 'Roboto', sans-serif;
  color: rgba(0, 0, 0, 0.5);
  text-align: center;
  line-height: 20px;
  margin: 0 0 32px;
}

/* Строка поиска */
.search-input-wrapper {
  display: flex;
  align-items: center;
  width: 100%;
  max-width: 534px;
  height: 61px;
  background: #f8f8f8;
  border: 1px solid #dfdfdf;
  border-radius: 0;
  overflow: hidden;
}

.search-input {
  flex: 1;
  border: none;
  outline: none;
  min-width: 0;
  height: 100%;
  padding: 0 24px;
  font-size: 18px;
  font-family: inherit;
  color: #000;
  background: transparent;
}

.search-input::placeholder {
  color: rgba(0, 0, 0, 0.16);
  opacity: 1;
}

.search-icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 62px;
  height: 100%;
  background: none;
  border-left: 1px solid #dfdfdf;
  border-top: none;
  border-bottom: none;
  border-right: none;
  cursor: pointer;
  flex-shrink: 0;
}

.search-icon-btn:hover {
  background: #f0f0f0;
}

/* Разделитель */
.search-divider {
  width: 100%;
  max-width: 1115px;
  height: 0;
  border-top: 1px solid rgba(0, 0, 0, 0.2);
  margin: 64px 0 63px;
}

.search-bottom-content {
  width: 100%;
  max-width: 1115px;
  display: flex;
  justify-content: center;
}

/* Результаты (Обычный поиск) */
.search-results {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  justify-content: center;
  width: 100%;
}

.allergen-tag {
  min-height: 61px;
  /* Figma strokes are drawn inside; 23px + the CSS border preserves its 24px inset. */
  padding: 0 23px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #f8f8f8;
  border: 1px solid #dfdfdf;
  border-radius: 0;
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  line-height: 1;
  color: #000;
  cursor: pointer;
  transition: background 0.15s;
}

.allergen-tag:hover {
  background: #f0f0f0;
}

/* ========================================
   ДЕТАЛЬНЫЙ ПРОСМОТР АЛЛЕРГЕНА
   ======================================== */

.search-details-grid {
  display: flex;
  width: 100%;
  background: transparent;
}

/* Левая колонка */
.details-left-col {
  width: 50%;
  display: flex;
  flex-direction: column;
}

.details-left-main {
  background: #ffffff;
  border: 1px solid #dfdfdf;
  border-right: none;
  padding: 32px;
  height: 312px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
}

.allergen-icon-box {
  margin-bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
}

.detail-copy {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
}

.detail-text-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.test-badge {
  background: #f1fff3;
  color: #0f5e1a;
  font-size: 14px;
  font-family: inherit;
  height: 40px;
  padding: 0 24px;
  margin: 0;
  border-radius: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.detail-name {
  font-size: 32px;
  font-weight: 400;
  color: #000;
  line-height: 38px;
  margin: 0;
}

.detail-desc {
  font-size: 18px;
  color: rgba(0, 0, 0, 0.5);
  margin: 0;
  line-height: 13px;
}

/* Футер левой колонки */
.details-left-footer {
  background: #ffffff;
  border: 1px solid #dfdfdf;
  border-right: none;
  border-top: none;
  padding: 0 24px;
  height: 72px;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  user-select: none;
}

.details-left-footer:hover {
  background: #fcfcfc;
}

.details-left-footer span {
  font-size: 18px;
  color: #000;
}

.back-arrow-circle {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
}

/* Правая колонка */
.details-right-col {
  width: 50%;
  background: transparent;
  border: 1px solid #dfdfdf;
  padding: 32px;
  min-height: 384px;
  position: relative;
}

.related-title {
  font-size: 21px;
  font-weight: 400;
  color: #000;
  margin: 0 0 24px;
}

.related-tags-container {
  position: absolute;
  top: 37px;
  left: 50%;
  width: min(470px, calc(100% - 64px));
  height: 311px;
  transform: translateX(-50%);
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  align-content: center;
}

.related-tag-btn {
  background: #f8f8f8;
  border: 1px solid #dfdfdf;
  color: #000;
  min-height: 61px;
  padding: 0 23px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  font-family: inherit;
  cursor: pointer;
  transition: all 0.15s;
}

.related-tag-btn:hover {
  background: #eee;
  border-color: #ccc;
}

.related-tag-btn[data-allergen='Кошачья шерсть'] { width: 190px; }
.related-tag-btn[data-allergen='Пыльца берёзы'] { width: 183px; }
.related-tag-btn[data-allergen='Банан'] { width: 100px; }
.related-tag-btn[data-allergen='Пыль'] { width: 96px; }

/* ========================================
   АДАПТИВНОСТЬ
   ======================================== */

  @media (max-width: 1024px) {
  .search-page-container {
    grid-template-columns: 1fr;
    gap: 0;
  }

  .sidebar-container {
    display: none;
  }

  .back-text {
    display: none;
  }

  .search-back-row {
    padding: 24px 32px;
    height: 72px;
    border-bottom: 1px solid #dfdfdf;
    background: #ffffff;
  }

  .search-center {
    padding: 102px 16px 32px;
  }

  .search-center--filtered,
  .search-center--detail {
    padding-top: 102px;
  }

  .search-heading {
    width: 100%;
    font-size: 32px;
    line-height: 38px;
  }

  .search-subheading {
    width: 100%;
    font-size: 18px;
    line-height: 17px;
    margin-bottom: 32px;
  }

  .search-input-wrapper {
    max-width: 100%;
  }

  .search-divider {
    max-width: 100%;
    margin: 32px 0 31px;
  }

  .search-bottom-content {
    max-width: 100%;
  }

  .search-results {
    max-width: 100%;
  }

  /* Сетка деталей на мобильных устройствах */
  .search-details-grid {
    flex-direction: column;
    gap: 0;
  }

  .details-left-col,
  .details-right-col {
    width: 100%;
  }

  .details-left-main {
    border: 1px solid #dfdfdf;
    height: 266px;
    min-height: 266px;
  }

  .test-badge {
    height: 32px;
    padding: 0 12px;
  }

  .details-left-footer {
    order: -1; /* Кнопка Назад перемещается наверх над карточкой детального просмотра */
    border: 1px solid #dfdfdf;
    height: 66px;
    flex: 0 0 66px;
    margin-bottom: 0;
  }

  .details-right-col {
    border: 1px solid #dfdfdf;
    padding: 32px;
    height: 394px;
    min-height: 394px;
    background: transparent;
  }

  .related-title {
    line-height: 15px;
  }

  .related-tags-container {
    top: 71px;
    left: 32px;
    width: calc(100% - 64px);
    height: 291px;
    transform: none;
    gap: 4px;
    justify-content: flex-start;
    align-content: flex-start;
  }

  .related-tag-btn {
    min-height: 55px;
    /* Keep the 14px Figma inset after accounting for the inside stroke. */
    padding: 0 13px;
  }

  .related-tag-btn[data-allergen='Кошачья шерсть'] { width: 170px; }
  .related-tag-btn[data-allergen='Пыльца берёзы'] { width: 163px; }
  .related-tag-btn[data-allergen='Банан'] { width: 80px; }
  .related-tag-btn[data-allergen='Пыль'] { width: 76px; }
}
</style>
