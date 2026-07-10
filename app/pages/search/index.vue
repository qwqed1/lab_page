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

const popularAllergens = [
  'Кошачья шерсть', 'Банан', 'Пыль', 'Клубника', 'Тараканы', 'Пыльца берёзы',
  'Кошачья шерсть', 'Банан', 'Пыль', 'Клубника', 'Тараканы', 'Пыльца берёзы',
  'Кошачья шерсть', 'Банан', 'Пыль', 'Клубника', 'Тараканы', 'Пыльца берёзы'
]

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
</script>

<template>
  <div class="search-page-container">
    <!-- Левый сайдбар (идентичен главной) -->
    <aside class="sidebar-container">
      <!-- Promo Banner Card -->
      <div class="promo-card" id="card-promo">
        <div class="promo-content">
          <img src="/assets/banner.svg" alt="ALEX2" class="promo-banner-img" />
          <p class="promo-text">
            Многокомпонентный анализ крови, который за один забор крови проверяет более 300 аллергенов, выявляя истинные причины реакции.
          </p>
        </div>
        <button class="promo-button" id="btn-register">
          <span class="promo-button-text">Записаться на тест</span>
          <div class="promo-button-icon">
            <img src="/assets/arrow-right-btn.svg" alt="arrow" />
          </div>
        </button>
      </div>

      <!-- Side-by-side cards -->
      <div class="cards-row">
        <!-- Search Card -->
        <div class="sub-card" id="card-search">
          <div class="card-icon-wrapper">
            <img src="/assets/search-icon.svg" alt="search" />
          </div>
          <div class="card-text-group">
            <h3 class="card-title">Поиск аллергенов</h3>
            <p class="card-subtitle">Убедитесь, что тест покажет, что вам нужно</p>
          </div>
        </div>

        <!-- Demo Card -->
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

      <!-- Quiz -->
      <div class="sidebar-row-card" id="row-quiz" @click="redirect('https://quiz-tan.vercel.app')">
        <div class="row-left-content">
          <span class="tag-badge">~5 минут</span>
          <span class="row-text">КВИЗ: Нужен ли вам тест на аллергены?</span>
        </div>
      </div>

      <!-- Profile -->
      <div class="sidebar-row-card" id="row-profile" @click="redirect('https://personal-account-tan.vercel.app')">
        <div class="row-left-content">
          <div class="row-icon-icon" style="margin-right: 4px;">
            <img src="/assets/profile-icon.svg" alt="profile" />
          </div>
          <span class="row-text">Личный кабинет</span>
        </div>
      </div>

      <!-- Lab -->
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

    <!-- Правая панель — контент поиска -->
    <main class="search-main">
      <!-- "На главную" ссылка -->
      <div class="search-back-row">
        <button class="search-back-btn" @click="$router.push('/')">
          <svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M7 13L1 7L7 1" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <span class="back-text">На главную</span>
        </button>
      </div>

      <!-- Центрированный контент -->
      <div class="search-center">
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

                <!-- Зеленый бейдж -->
                <div v-if="selectedAllergen.included" class="test-badge">
                  Входит в тест ALEX2
                </div>

                <!-- Название аллергена -->
                <h2 class="detail-name">{{ selectedAllergen.name }}</h2>

                <!-- Описание -->
                <p class="detail-desc">{{ selectedAllergen.description }}</p>
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
              v-for="allergen in filteredAllergens"
              :key="allergen"
              class="allergen-tag"
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
/* ========================================
   ОБЩАЯ СЕТКА СТРАНИЦЫ ПОИСКА (БЕЗ GAP)
   ======================================== */

.search-page-container {
  display: grid;
  grid-template-columns: 677px 1fr;
  gap: 0;
  max-width: 1920px;
  margin: 0;
  padding: 0;
  min-height: 100vh;
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
  min-height: 100vh;
  position: relative;
  overflow-y: auto;
}

/* "На главную" (Соответствует Frame 290 в Figma) */
.search-back-row {
  height: 72px;
  background: #ffffff;
  border-bottom: 1px solid #dfdfdf;
  padding: 24px 32px;
  display: flex;
  align-items: center;
}

.search-back-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 17px;
  font-family: 'Helvetica', sans-serif;
  color: #000;
  padding: 0;
  line-height: 1;
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
  padding: 60px 64px 48px;
}

.search-heading {
  font-size: 42px;
  font-weight: 400;
  font-family: 'Helvetica', sans-serif;
  color: #000;
  text-align: center;
  line-height: 1.2;
  margin: 0 0 16px;
}

.search-subheading {
  font-size: 16px;
  font-weight: 400;
  font-family: 'Helvetica', sans-serif;
  color: #888;
  text-align: center;
  line-height: 1.5;
  margin: 0 0 40px;
}

/* Строка поиска */
.search-input-wrapper {
  display: flex;
  align-items: center;
  width: 100%;
  max-width: 534px;
  background: #f8f8f8;
  border: 1px solid #dfdfdf;
  border-radius: 0;
  overflow: hidden;
}

.search-input {
  flex: 1;
  border: none;
  outline: none;
  padding: 18px 24px;
  font-size: 18px;
  font-family: inherit;
  color: #000;
  background: transparent;
}

.search-input::placeholder {
  color: #aaa;
}

.search-icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 62px;
  height: 61px;
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
  height: 1px;
  background: rgba(0, 0, 0, 0.2);
  margin: 32px 0 32px;
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
  gap: 12px;
  justify-content: center;
  width: 100%;
}

.allergen-tag {
  padding: 12px 24px;
  background: #fff;
  border: 1px solid #dfdfdf;
  border-radius: 0;
  font-size: 16px;
  font-family: inherit;
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
}

.allergen-icon-box {
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
}

.test-badge {
  background: #f1fff3;
  color: #0f5e1a;
  font-size: 14px;
  font-family: inherit;
  padding: 10px 24px;
  margin-bottom: 12px;
  border-radius: 0;
}

.detail-name {
  font-size: 32px;
  font-weight: 400;
  color: #000;
  margin: 0 0 12px;
}

.detail-desc {
  font-size: 18px;
  color: rgba(0, 0, 0, 0.5);
  margin: 0;
  line-height: 1.4;
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
}

.related-title {
  font-size: 21px;
  font-weight: 400;
  color: #000;
  margin: 0 0 24px;
}

.related-tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.related-tag-btn {
  background: #f8f8f8;
  border: 1px solid #dfdfdf;
  color: #000;
  padding: 16px 24px;
  font-size: 18px;
  font-family: inherit;
  cursor: pointer;
  transition: all 0.15s;
}

.related-tag-btn:hover {
  background: #eee;
  border-color: #ccc;
}

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
    padding: 24px 16px;
    height: 72px;
    border-bottom: 1px solid #dfdfdf;
    background: #ffffff;
  }

  .search-center {
    padding: 40px 16px 32px;
  }

  .search-heading {
    font-size: 28px;
  }

  .search-input-wrapper {
    max-width: 100%;
  }

  .search-divider {
    max-width: 100%;
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
    gap: 20px;
  }

  .details-left-col,
  .details-right-col {
    width: 100%;
  }

  .details-left-main {
    border: 1px solid #dfdfdf;
    height: auto;
    min-height: 250px;
  }

  .details-left-footer {
    order: -1; /* Кнопка Назад перемещается наверх над карточкой детального просмотра */
    border: 1px solid #dfdfdf;
    margin-bottom: 16px;
  }

  .details-right-col {
    border: 1px solid #dfdfdf;
    padding: 24px 16px;
    min-height: auto;
    background: #ffffff;
  }
}
</style>
