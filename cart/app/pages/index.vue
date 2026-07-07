<template>
  <div class="page-layout">
    
    <!-- ───────────────────── ГЛАВНЫЙ ЭКРАН КОРЗИНЫ ───────────────────── -->
    <div v-if="!showMapSelector" class="main-cart-screen">
      <!-- HEADER 72px -->
      <header class="header-nav">
        <NuxtLink to="/" class="back-link">
          <span class="back-arrow">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path d="M15 18L9 12L15 6" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </span>
          Назад
        </NuxtLink>
      </header>

      <!-- BODY AREA -->
      <div class="page-body">
        <div class="content-container">
          
          <!-- LEFT COLUMN (Товары + Место сдачи + Личные данные) -->
          <main class="left-col">
            
            <!-- БЛОК ТОВАРОВ -->
            <section class="products-section">
              
              <!-- Товар 1: ALEX2 (Всегда добавлен) -->
              <div class="product-row product-row--added">
                <!-- Десктопный thumbnail -->
                <div class="product-thumb product-thumb--added desktop-only">
                  <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                    <circle cx="16" cy="16" r="14" stroke="#ffffff" stroke-width="1.5"/>
                    <path d="M10 16L14 20L22 12" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <span class="product-thumb-label">Добавлено</span>
                </div>
                <div class="product-info">
                  <div class="product-header">
                    <div>
                      <!-- Теги мобильные (сверху названия) -->
                      <div class="product-tags-top mobile-only">
                        <span class="tag tag--blue">+ Забор крови</span>
                        <span class="tag tag--blue">+IgE</span>
                      </div>
                      <h2 class="product-name">Сдача анализа ALEX2</h2>
                      <p class="product-desc">Мультикомплексный анализ на 300 аллергенов<br>за один забор крови. Включает в себя общий IgE</p>
                      <!-- Теги десктопные -->
                      <div class="product-tags desktop-only">
                        <span class="tag tag--blue">+ Забор крови</span>
                        <span class="tag tag--blue">+IgE</span>
                      </div>
                    </div>
                    <span class="product-price desktop-only">24&thinsp;900₽</span>
                  </div>

                  <!-- Мобильная кнопка статуса/цены -->
                  <div class="product-mobile-action mobile-only">
                    <div class="product-mobile-btn product-mobile-btn--added">
                      <span class="product-mobile-btn-icon">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                          <circle cx="12" cy="12" r="10" stroke="#ffffff" stroke-width="2"/>
                          <path d="M9 12l2 2 4-4" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                      </span>
                      <span class="product-mobile-btn-price">24 900₽</span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Товар 2: Консультация -->
              <div class="product-row" :class="{'product-row--added-border': isConsultationAdded}">
                <!-- Десктопный thumbnail -->
                <div class="product-thumb desktop-only" :class="isConsultationAdded ? 'product-thumb--added' : 'product-thumb--add'" @click="toggleConsultation">
                  <template v-if="isConsultationAdded">
                    <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                      <circle cx="16" cy="16" r="14" stroke="#ffffff" stroke-width="1.5"/>
                      <path d="M10 16L14 20L22 12" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span class="product-thumb-label">Добавлено</span>
                  </template>
                  <template v-else>
                    <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                      <circle cx="16" cy="16" r="14" stroke="#000000" stroke-width="1.5"/>
                      <path d="M16 10V22M10 16H22" stroke="#000000" stroke-width="1.5" stroke-linecap="round"/>
                    </svg>
                    <span class="product-thumb-label product-thumb-label--dark">Добавить</span>
                  </template>
                </div>
                <div class="product-info">
                  <div class="product-header">
                    <div>
                      <!-- Мобильная плашка акции сверху -->
                      <div class="product-tags-top mobile-only">
                        <span class="tag tag--green">Скидка 99% в лаборатории ALEX
                          <svg class="tag-icon" width="14" height="14" viewBox="0 0 14 14" fill="none">
                            <circle cx="7" cy="7" r="6" stroke="#1a8a4a" stroke-width="1.2"/>
                            <path d="M7 4.5V7" stroke="#1a8a4a" stroke-width="1.2" stroke-linecap="round"/>
                            <circle cx="7" cy="9.5" r="0.7" fill="#1a8a4a"/>
                          </svg>
                        </span>
                      </div>
                      <h2 class="product-name">Консультация</h2>
                      <p class="product-desc">Онлайн-разбор результатов с профессиональными врачами</p>
                      <!-- Десктопная плашка акции -->
                      <div class="product-tags desktop-only">
                        <span class="tag tag--green">Скидка 99% в лаборатории ALEX
                          <svg class="tag-icon" width="14" height="14" viewBox="0 0 14 14" fill="none">
                            <circle cx="7" cy="7" r="6" stroke="#1a8a4a" stroke-width="1.2"/>
                            <path d="M7 4.5V7" stroke="#1a8a4a" stroke-width="1.2" stroke-linecap="round"/>
                            <circle cx="7" cy="9.5" r="0.7" fill="#1a8a4a"/>
                          </svg>
                        </span>
                      </div>
                    </div>
                    <span class="product-price desktop-only">2&thinsp;000₽</span>
                  </div>

                  <!-- Мобильная кнопка действия -->
                  <div class="product-mobile-action mobile-only">
                    <button 
                      class="product-mobile-btn" 
                      :class="{ 'product-mobile-btn--added': isConsultationAdded }"
                      @click="toggleConsultation"
                    >
                      <span class="product-mobile-btn-icon">
                        <svg v-if="isConsultationAdded" width="20" height="20" viewBox="0 0 24 24" fill="none">
                          <circle cx="12" cy="12" r="10" stroke="#ffffff" stroke-width="2"/>
                          <path d="M9 12l2 2 4-4" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none">
                          <circle cx="12" cy="12" r="10" stroke="#000000" stroke-width="2"/>
                          <path d="M12 8v8M8 12h8" stroke="#000000" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                      </span>
                      <span class="product-mobile-btn-price">2 000₽</span>
                    </button>
                  </div>
                </div>
              </div>

              <!-- Товар 3: Срочный результат -->
              <div class="product-row" :class="{'product-row--added-border': isExpressAdded}">
                <!-- Десктопный thumbnail -->
                <div class="product-thumb desktop-only" :class="isExpressAdded ? 'product-thumb--added' : 'product-thumb--add'" @click="toggleExpress">
                  <template v-if="isExpressAdded">
                    <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                      <circle cx="16" cy="16" r="14" stroke="#ffffff" stroke-width="1.5"/>
                      <path d="M10 16L14 20L22 12" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span class="product-thumb-label">Добавлено</span>
                  </template>
                  <template v-else>
                    <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
                      <circle cx="16" cy="16" r="14" stroke="#000000" stroke-width="1.5"/>
                      <path d="M16 10V22M10 16H22" stroke="#000000" stroke-width="1.5" stroke-linecap="round"/>
                    </svg>
                    <span class="product-thumb-label product-thumb-label--dark">Добавить</span>
                  </template>
                </div>
                <div class="product-info">
                  <div class="product-header">
                    <div>
                      <h2 class="product-name">Срочный результат</h2>
                      <p class="product-desc">Отправим за 24 часа</p>
                    </div>
                    <span class="product-price desktop-only">5&thinsp;000₽</span>
                  </div>

                  <!-- Мобильная кнопка действия -->
                  <div class="product-mobile-action mobile-only">
                    <button 
                      class="product-mobile-btn" 
                      :class="{ 'product-mobile-btn--added': isExpressAdded }"
                      @click="toggleExpress"
                    >
                      <span class="product-mobile-btn-icon">
                        <svg v-if="isExpressAdded" width="20" height="20" viewBox="0 0 24 24" fill="none">
                          <circle cx="12" cy="12" r="10" stroke="#ffffff" stroke-width="2"/>
                          <path d="M9 12l2 2 4-4" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none">
                          <circle cx="12" cy="12" r="10" stroke="#000000" stroke-width="2"/>
                          <path d="M12 8v8M8 12h8" stroke="#000000" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                      </span>
                      <span class="product-mobile-btn-price">5 000₽</span>
                    </button>
                  </div>
                </div>
              </div>
            </section>

            <!-- МЕСТО СДАЧИ АНАЛИЗА -->
            <section class="section-block">
              <h2 class="section-title">Место сдачи анализа</h2>

              <!-- Состояние: не выбрано -->
              <div v-if="!selectedLab" class="location-empty">
                <div class="field-group">
                  <label class="field-label">Выберите город</label>
                  <div class="select-field" @click="openMapSelector">
                    <span class="select-placeholder">Выберите из списка</span>
                    <span class="select-arrow">
                      <!-- Стрелка-шеврон в круге по мобильному макету -->
                      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                        <circle cx="12" cy="12" r="10" stroke="#000000" stroke-width="1.5"/>
                        <path d="M10 8L14 12L10 16" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                    </span>
                  </div>
                </div>
              </div>

              <!-- Состояние: выбрано -->
              <div v-else class="location-selected">
                <div class="location-card">
                  <div class="location-info">
                    <span v-if="selectedLab.discount" class="location-badge">-100% на консультацию</span>
                    <p class="location-name">{{ selectedLab.name }}</p>
                    <div class="location-schedule">
                      <span class="schedule-days">ПН – ПТ</span>
                      <span class="schedule-hours">{{ selectedLab.hoursWeekdays }}</span>
                    </div>
                    <div class="location-schedule">
                      <span class="schedule-days">СБ – ВС</span>
                      <span class="schedule-hours">{{ selectedLab.hoursWeekend }}</span>
                    </div>
                  </div>
                  <button class="change-btn" @click="openMapSelector">
                    <svg width="46" height="46" viewBox="0 0 46 46" fill="none">
                      <path d="M16 23a7 7 0 1 0 14 0 7 7 0 0 0-14 0" stroke="#000" stroke-width="1.5" fill="none"/>
                      <path d="M28 18l3-3 3 3" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                      <path d="M31 15v5" stroke="#000" stroke-width="1.5" stroke-linecap="round"/>
                    </svg>
                    Изменить
                  </button>
                </div>
              </div>
            </section>

            <!-- ЛИЧНЫЕ ДАННЫЕ -->
            <section class="section-block">
              <h2 class="section-title">Личные данные</h2>

              <form class="personal-form" @submit.prevent>
                <div class="form-row-two">
                  <div class="field-group">
                    <label class="field-label field-label--md">ФИО</label>
                    <input type="text" v-model="fullName" class="field-input" placeholder="Иванов Иван Иванович"/>
                  </div>
                  <div class="field-group">
                    <label class="field-label field-label--md">Дата рождения</label>
                    <input type="text" v-model="birthDate" class="field-input" placeholder="11.06.2006"/>
                  </div>
                </div>

                <div class="field-group field-group--full">
                  <label class="field-label field-label--md">Номер телефона</label>
                  <input type="tel" v-model="phone" class="field-input" placeholder="+7 999 999 99 99"/>
                </div>

                <div class="field-group field-group--full">
                  <label class="field-label field-label--md">E-mail</label>
                  <input type="email" v-model="email" class="field-input" placeholder="max@inmuntex.com"/>
                  <div class="field-info">
                    <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
                      <circle cx="10" cy="10" r="8.5" stroke="#000000" stroke-width="1.2"/>
                      <path d="M10 7V10" stroke="#000000" stroke-width="1.2" stroke-linecap="round"/>
                      <circle cx="10" cy="13" r="0.8" fill="#000000"/>
                    </svg>
                    <span class="field-info-text">На указанную почту придут данные от личного кабинета.<br>В нём можно онлайн отслеживать результаты.</span>
                  </div>
                </div>
              </form>
            </section>
          </main>

          <!-- RIGHT COLUMN (Сводка заказа / Блок Итого) -->
          <!-- На мобильном: рендерится в потоке страницы после личных данных -->
          <aside class="right-col">
            
            <h2 class="section-title mobile-only mobile-summary-title">Итого</h2>

            <!-- Блок: Место -->
            <div class="summary-block">
              <h3 class="summary-label">Место</h3>
              <div v-if="!selectedLab">
                <p class="summary-value summary-value--muted">Не выбрано</p>
              </div>
              <div v-else>
                <span v-if="selectedLab.discount" class="summary-badge">-100% на консультацию</span>
                <p class="summary-value summary-value--location">{{ selectedLab.name }}</p>
                <div class="summary-schedule">
                  <div class="summary-schedule-row">
                    <span class="summary-schedule-days">ПН – ПТ</span>
                    <span>{{ selectedLab.hoursWeekdays }}</span>
                  </div>
                  <div class="summary-schedule-row">
                    <span class="summary-schedule-days">СБ – ВС</span>
                    <span>{{ selectedLab.hoursWeekend }}</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Блок: Время на результат -->
            <div class="summary-block">
              <h3 class="summary-label">Время на результат</h3>
              <p class="summary-value summary-value--big">3 дня</p>
            </div>

            <!-- Блок: Комплектация -->
            <div class="summary-block">
              <h3 class="summary-label">Комплектация</h3>
              <div class="summary-items">
                <div class="summary-item">
                  <span class="summary-item-name">ALEX2</span>
                  <span class="summary-item-price">24&thinsp;900₽</span>
                </div>
                <div class="summary-item" v-if="isConsultationAdded">
                  <span class="summary-item-name">Консультация</span>
                  <span class="summary-item-price">2&thinsp;000₽</span>
                </div>
                <div class="summary-item" v-if="isExpressAdded">
                  <span class="summary-item-name">Срочный результат</span>
                  <span class="summary-item-price">5&thinsp;000₽</span>
                </div>
                <div class="summary-item">
                  <span class="summary-item-name">Забор крови</span>
                  <span class="summary-item-price">0₽</span>
                </div>
                <div class="summary-item">
                  <span class="summary-item-name">Общий IgE</span>
                  <span class="summary-item-price">0₽</span>
                </div>
              </div>
            </div>

            <!-- Промокод -->
            <div class="promo-row">
              <div class="promo-input-wrap">
                <input type="text" v-model="promo" class="promo-input" placeholder="Введите промокод"/>
              </div>
              <button class="promo-btn" @click="applyPromo">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                  <circle cx="12" cy="12" r="10" stroke="#000000" stroke-width="2"/>
                  <path d="M10 8L14 12L10 16" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>

            <!-- Итоговая стоимость и чекбокс согласия -->
            <div class="total-block">
              <div class="total-inner">
                <div class="total-price-group">
                  <span class="total-label">Итого к оплате</span>
                  <span class="total-price">{{ formattedTotalPrice }}₽</span>
                </div>
                <label class="consent-row">
                  <input type="checkbox" v-model="consent" class="consent-checkbox"/>
                  <span class="consent-text">Я даю <span class="consent-link">согласие</span> на передачу моих персональных данных с целью осуществления доставки (возврата) товара третьим лицам</span>
                </label>
              </div>
              
              <!-- Кнопка Продолжить (на мобильном фиксированная внизу, на десктопе внизу сайдбара) -->
              <div class="continue-btn-wrapper">
                <button class="continue-btn" :disabled="!consent" @click="handleContinue">
                  <span>Продолжить</span>
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <circle cx="12" cy="12" r="10" stroke="#ffffff" stroke-width="2"/>
                    <path d="M10 8L14 12L10 16" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
            </div>

          </aside>

        </div>
      </div>
    </div>

    <!-- ───────────────────── ЭКРАН ВЫБОРА ЛАБОРАТОРИИ (КАРТА) ───────────────────── -->
    <div v-else class="map-selector-screen" :class="{ 'map-selector-screen--mobile-map': showMapOnMobile }">
      <!-- HEADER 72px -->
      <header class="header-nav">
        <button class="back-link" @click="handleMapBack">
          <span class="back-arrow">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path d="M15 18L9 12L15 6" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </span>
          Назад
        </button>
      </header>

      <div class="map-selector-body">
        
        <!-- САЙДБАР (Слева) -->
        <aside class="map-sidebar" :class="{ 'map-sidebar--hidden': showMapOnMobile }">
          
          <!-- ШАГ 1: Выбор города -->
          <div v-if="mapStep === 1" class="map-step-1">
            <h2 class="map-sidebar-title">Выберите город</h2>
            <div class="field-group">
              <div class="city-select-dropdown" @click="showCityList = !showCityList">
                <span class="selected-city-name">{{ selectedCity || 'Выберите из списка' }}</span>
                <span class="select-arrow" :class="{ 'select-arrow--open': showCityList }">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M6 9L12 15L18 9" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </span>
              </div>
              
              <!-- Список городов -->
              <div v-if="showCityList" class="city-options-list">
                <div v-for="city in cities" :key="city.name" class="city-option" @click="selectCity(city.name)">
                  {{ city.name }}
                </div>
              </div>
            </div>
          </div>

          <!-- ШАГ 2: Список лабораторий города -->
          <div v-else class="map-step-2">
            <div class="city-header-row">
              <span class="city-badge">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.5">
                  <path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
                {{ selectedCity }}
              </span>
              <button class="change-city-btn" @click="changeCity">Изменить город</button>
            </div>
            
            <h2 class="map-sidebar-title">Выберите лабораторию</h2>

            <!-- Зеленый инфо-блок о бесплатной консультации -->
            <div class="promo-alert-card">
              <h4 class="promo-alert-title">Бесплатная консультация в лабораториях ALEX</h4>
              <p class="promo-alert-desc">Выберите точку ALEX как место сдачи крови и скидка автоматически появится в корзине</p>
            </div>

            <!-- Список лабораторий -->
            <div class="labs-list">
              <div 
                v-for="lab in filteredLabs" 
                :key="lab.id" 
                class="lab-card"
                :class="{ 
                  'lab-card--active': activeLabId === lab.id,
                  'lab-card--detailed': detailedLabId === lab.id 
                }"
                @click="clickLabCard(lab)"
              >
                <div class="lab-card-content">
                  <span v-if="lab.discount" class="lab-card-badge">-100% на консультацию</span>
                  <h3 class="lab-card-name">{{ lab.name }}</h3>
                  
                  <div class="lab-card-schedule">
                    <div class="schedule-row">
                      <span class="schedule-days">ПН – ПТ</span>
                      <span class="schedule-hours">{{ lab.hoursWeekdays }}</span>
                    </div>
                    <div class="schedule-row">
                      <span class="schedule-days">СБ – ВС</span>
                      <span class="schedule-hours">{{ lab.hoursWeekend }}</span>
                    </div>
                  </div>
                </div>

                <!-- Блок детального выбора (Шаг 3) на десктопе -->
                <div v-if="detailedLabId === lab.id" class="lab-card-action desktop-only">
                  <button class="select-lab-btn" @click.stop="confirmLabSelection(lab)">
                    <span>Выбрать</span>
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                      <circle cx="12" cy="12" r="10" stroke="#ffffff" stroke-width="2"/>
                      <path d="M10 8L14 12L10 16" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </button>
                </div>
              </div>
            </div>

            <!-- Мобильная кнопка «Выбрать на карте» -->
            <button class="mobile-map-trigger-btn" @click="showMapOnMobile = true">
              <span>Выбрать на карте</span>
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <circle cx="12" cy="12" r="10" stroke="#ffffff" stroke-width="2"/>
                <path d="M10 8L14 12L10 16" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>

          </div>

        </aside>

        <!-- ИНТЕРАКТИВНАЯ КАРТА (Справа / Полноэкранная на мобильных) -->
        <main class="map-view-container" :class="{ 'map-view-container--visible': showMapOnMobile || isDesktop }">
          
          <!-- КАРТА РОССИИ (Шаг 1) -->
          <div v-if="mapStep === 1" class="russia-map-layer">
            <svg class="map-svg" viewBox="0 0 1000 600" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M50 150 C150 100, 300 80, 500 120 C650 150, 800 100, 950 130 C980 200, 900 350, 850 400 C750 430, 600 480, 450 450 C300 430, 150 500, 80 400 C30 350, 20 200, 50 150 Z" fill="#e8ebf0" stroke="#cdd3de" stroke-width="2"/>
              <path d="M120 280 C180 250, 240 290, 280 240 C320 200, 380 240, 450 200" stroke="#cdd3de" stroke-width="1.5" stroke-dasharray="4 4"/>
              
              <g 
                v-for="city in cities" 
                :key="city.name" 
                class="map-city-marker" 
                @click="selectCity(city.name)"
              >
                <circle :cx="city.x" :cy="city.y" r="8" fill="#000000" class="marker-pulse"/>
                <circle :cx="city.x" :cy="city.y" r="4" fill="#ffffff"/>
                <text :x="city.x" :y="city.y - 12" text-anchor="middle" class="map-city-label">{{ city.name }}</text>
              </g>
            </svg>
          </div>

          <!-- КАРТА МОСКВЫ (Шаг 2 & 3) -->
          <div v-else class="moscow-map-layer" :class="{ 'moscow-map-layer--zoomed': mapStep === 3 || detailedLabId }">
            <svg 
              class="map-svg map-svg--moscow" 
              :viewBox="mapViewport" 
              fill="none" 
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M-100 200 L1100 200 M-100 500 L1100 500 M300 -100 L300 700 M700 -100 L700 700" stroke="#e0e4ec" stroke-width="3"/>
              <path d="M0 0 L1000 600 M1000 0 L0 600" stroke="#e0e4ec" stroke-width="2"/>
              <circle cx="500" cy="300" r="180" stroke="#e0e4ec" stroke-width="4" fill="none"/>
              <circle cx="500" cy="300" r="320" stroke="#e8ecf3" stroke-width="6" fill="none"/>
              
              <path d="M-100 100 Q 200 80, 350 250 T 650 350 T 1100 250" stroke="#d4e2f8" stroke-width="32" stroke-linecap="round" fill="none"/>
              <path d="M-100 100 Q 200 80, 350 250 T 650 350 T 1100 250" stroke="#c0d6f6" stroke-width="20" stroke-linecap="round" fill="none"/>

              <!-- Точки лабораторий -->
              <g 
                v-for="lab in filteredLabs" 
                :key="lab.id" 
                class="map-lab-marker"
                :class="{ 
                  'map-lab-marker--active': activeLabId === lab.id,
                  'map-lab-marker--detailed': detailedLabId === lab.id 
                }"
                @click="clickMapMarker(lab)"
              >
                <template v-if="detailedLabId === lab.id">
                  <rect :x="lab.x - 22" :y="lab.y - 48" width="44" height="44" rx="10" fill="#000000"/>
                  <path d="M0 -4 L-6 -10 L6 -10 Z" fill="#000000" :transform="`translate(${lab.x}, ${lab.y - 34})`"/>
                  <text v-if="lab.discount" :x="lab.x" :y="lab.y - 22" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="700">%</text>
                  <circle v-else :cx="lab.x" :cy="lab.y - 26" r="4" fill="#ffffff"/>
                </template>
                <template v-else>
                  <circle :cx="lab.x" :cy="lab.y" r="14" :fill="lab.discount ? '#1a8a4a' : '#000000'"/>
                  <text v-if="lab.discount" :x="lab.x" :y="lab.y + 4" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">%</text>
                  <circle v-else :cx="lab.x" :cy="lab.y" r="4" fill="#ffffff"/>
                </template>
              </g>
            </svg>
          </div>

          <!-- МОБИЛЬНАЯ ВЫДВИЖНАЯ ПЛАШКА ИНФОРМАЦИИ (Bottom Sheet) -->
          <div 
            class="mobile-lab-sheet" 
            :class="{ 'mobile-lab-sheet--open': showMapOnMobile && detailedLabId }"
          >
            <div v-if="selectedMobileLab" class="mobile-sheet-content">
              <!-- Кнопка Закрыть (крестик) -->
              <button class="close-sheet-btn" @click="closeMobileSheet">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                  <path d="M18 6L6 18M6 6l12 12" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>

              <span v-if="selectedMobileLab.discount" class="lab-card-badge">-100% на консультацию</span>
              <h3 class="mobile-sheet-title">{{ selectedMobileLab.name }}</h3>

              <div class="mobile-sheet-schedule">
                <div class="schedule-row">
                  <span class="schedule-days">ПН – ПТ</span>
                  <span class="schedule-hours">{{ selectedMobileLab.hoursWeekdays }}</span>
                </div>
                <div class="schedule-row">
                  <span class="schedule-days">СБ – ВС</span>
                  <span class="schedule-hours">{{ selectedMobileLab.hoursWeekend }}</span>
                </div>
              </div>

              <!-- Кнопка Выбрать -->
              <button class="mobile-select-confirm-btn" @click="confirmLabSelection(selectedMobileLab)">
                <span>Выбрать</span>
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                  <circle cx="12" cy="12" r="10" stroke="#ffffff" stroke-width="2"/>
                  <path d="M10 8L14 12L10 16" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
          </div>

        </main>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from '#app'

// Состояние добавленных опций
const isConsultationAdded = ref(false)
const isExpressAdded = ref(false)

// Данные корзины
const fullName = ref('Иванов Иван Иванович')
const birthDate = ref('11.06.2006')
const phone = ref('+7 938 910 92 22')
const email = ref('hi@mail.com')
const promo = ref('')
const consent = ref(false)

// Опции для выбора города
const cities = [
  { name: 'Москва', x: 210, y: 220 },
  { name: 'Санкт-Петербург', x: 150, y: 160 },
  { name: 'Казань', x: 300, y: 230 },
  { name: 'Екатеринбург', x: 420, y: 270 },
  { name: 'Краснодар', x: 180, y: 310 }
]

// Список лабораторий
const labs = [
  {
    id: 1,
    city: 'Москва',
    name: 'ALEX, Москва, Маршала Бирюзова 9',
    hoursWeekdays: '9:00 – 19:00',
    hoursWeekend: 'Выходные',
    discount: true,
    x: 350,
    y: 250
  },
  {
    id: 2,
    city: 'Москва',
    name: 'ALEX, Ленинградская 4',
    hoursWeekdays: '9:00 – 19:00',
    hoursWeekend: '11:00 – 16:00',
    discount: true,
    x: 650,
    y: 350
  },
  {
    id: 3,
    city: 'Москва',
    name: 'Invitro, Большая морская 55',
    hoursWeekdays: '9:00 – 19:00',
    hoursWeekend: '11:00 – 16:00',
    discount: false,
    x: 500,
    y: 150
  },
  {
    id: 4,
    city: 'Санкт-Петербург',
    name: 'ALEX, Невский проспект 12',
    hoursWeekdays: '9:00 – 20:00',
    hoursWeekend: '10:00 – 18:00',
    discount: true,
    x: 400,
    y: 200
  },
  {
    id: 5,
    city: 'Казань',
    name: 'Invitro, Островского 9',
    hoursWeekdays: '8:00 – 19:00',
    hoursWeekend: '9:00 – 15:00',
    discount: false,
    x: 450,
    y: 250
  }
]

// Состояние выбора лаборатории
const showMapSelector = ref(false)
const mapStep = ref(1) // 1: Выбор города, 2: Выбор лабы
const selectedCity = ref('Москва')
const showCityList = ref(false)
const activeLabId = ref(null)
const detailedLabId = ref(null)
const selectedLab = ref(labs[0]) // По умолчанию выбрана первая

// Для мобильной версии карты
const showMapOnMobile = ref(false)
const isDesktop = ref(true)

const checkViewport = () => {
  if (typeof window !== 'undefined') {
    isDesktop.value = window.innerWidth > 900
  }
}

onMounted(() => {
  checkViewport()
  window.addEventListener('resize', checkViewport)
})

onUnmounted(() => {
  window.removeEventListener('resize', checkViewport)
})

const filteredLabs = computed(() => {
  return labs.filter(lab => lab.city === selectedCity.value)
})

const selectedMobileLab = computed(() => {
  return labs.find(l => l.id === detailedLabId.value) || null
})

// Управление отображением карты (viewport viewBox)
const mapViewport = computed(() => {
  const targetId = detailedLabId.value || activeLabId.value
  if (targetId) {
    const lab = labs.find(l => l.id === targetId)
    if (lab) {
      return `${lab.x - 150} ${lab.y - 120} 300 240`
    }
  }
  return '0 0 1000 600'
})

// Открытие интерфейса карты
const openMapSelector = () => {
  showMapSelector.value = true
  showMapOnMobile.value = false
  detailedLabId.value = null
  activeLabId.value = null
  
  if (selectedLab.value) {
    selectedCity.value = selectedLab.value.city
    mapStep.value = 2
  } else {
    mapStep.value = 1
  }
}

const closeMapSelector = () => {
  showMapSelector.value = false
  showMapOnMobile.value = false
}

const handleMapBack = () => {
  if (showMapOnMobile.value) {
    showMapOnMobile.value = false
    detailedLabId.value = null
    activeLabId.value = null
  } else if (mapStep.value === 2) {
    mapStep.value = 1
  } else {
    showMapSelector.value = false
  }
}

// Выбор города
const selectCity = (cityName) => {
  selectedCity.value = cityName
  showCityList.value = false
  mapStep.value = 2
  activeLabId.value = null
  detailedLabId.value = null
}

const changeCity = () => {
  mapStep.value = 1
  showCityList.value = false
}

// Интерактив кликов
const clickLabCard = (lab) => {
  activeLabId.value = lab.id
  detailedLabId.value = lab.id
  
  if (!isDesktop.value) {
    showMapOnMobile.value = true
  }
}

const clickMapMarker = (lab) => {
  activeLabId.value = lab.id
  detailedLabId.value = lab.id
}

const closeMobileSheet = () => {
  detailedLabId.value = null
}

const confirmLabSelection = (lab) => {
  selectedLab.value = lab
  showMapSelector.value = false
  showMapOnMobile.value = false
}

const toggleConsultation = () => {
  isConsultationAdded.value = !isConsultationAdded.value
}

const toggleExpress = () => {
  isExpressAdded.value = !isExpressAdded.value
}

// Подсчет цены
const formattedTotalPrice = computed(() => {
  let total = 24900
  if (isConsultationAdded.value) total += 2000
  if (isExpressAdded.value) total += 5000
  return total.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ")
})

const applyPromo = () => {
  // Promo logic
}

const handleContinue = () => {
  useRouter().push('/login')
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

*, *::before, *::after {
  box-sizing: border-box;
}

/* ─── Вспомогательные классы скрытия/показа ─── */
.desktop-only {
  display: block;
}
.mobile-only {
  display: none !important;
}

@media (max-width: 900px) {
  .desktop-only {
    display: none !important;
  }
  .mobile-only {
    display: block !important;
  }
}

/* ─── LAYOUT ─── */
.page-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
  font-family: 'Roboto', sans-serif;
}

/* HEADER: 72px */
.header-nav {
  width: 100%;
  height: 72px;
  background-color: #ffffff;
  border-bottom: 1px solid #dfdfdf;
  display: flex;
  align-items: center;
  padding: 0 32px;
  position: sticky;
  top: 0;
  z-index: 100;
  flex-shrink: 0;
}

.back-link {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: 'Helvetica', Arial, sans-serif;
  font-size: 17px;
  font-weight: 400;
  color: #000000;
  text-decoration: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}
.back-link:hover { opacity: 0.7; }

.back-arrow {
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

/* ───────────────────── MAIN CART SCREEN ───────────────────── */
.main-cart-screen {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.page-body {
  flex: 1;
  display: flex;
  justify-content: center;
  width: 100%;
  background-color: #f5f5f5;
}

.content-container {
  display: flex;
  width: 100%;
  max-width: 1920px;
  min-height: 100%;
  position: relative;
}

.left-col {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 84px;
  padding: 106px 64px 80px 64px;
}

.right-col {
  width: 610px;
  flex-shrink: 0;
  border-left: 1px solid #dfdfdf;
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
  position: sticky;
  top: 72px;
  height: calc(100vh - 72px);
  overflow-y: auto;
}

/* ───────────────────── PRODUCTS SECTION (Товары) ───────────────────── */
.products-section {
  display: flex;
  flex-direction: column;
  background-color: #ffffff;
  border: 1px solid #dfdfdf;
}

.product-row {
  display: flex;
  align-items: stretch;
  border-bottom: 1px solid #dfdfdf;
}
.product-row:last-child {
  border-bottom: none;
}

.product-thumb {
  width: 204px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 24px 32px;
  border-right: 1px solid #dfdfdf;
  user-select: none;
}

.product-thumb--added {
  background-color: #000000;
}

.product-thumb--add {
  background-color: #ffffff;
  cursor: pointer;
  transition: background-color 0.2s;
}
.product-thumb--add:hover {
  background-color: #f5f5f5;
}

.product-thumb-label {
  font-size: 16px;
  font-weight: 400;
  color: #ffffff;
  font-family: 'Roboto', sans-serif;
  text-align: center;
}
.product-thumb-label--dark {
  color: #000000;
}

.product-info {
  flex: 1;
  padding: 32px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.product-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 24px;
}

.product-name {
  font-family: 'Roboto', sans-serif;
  font-size: 24px;
  font-weight: 400;
  color: #000000;
  margin: 0 0 8px 0;
  line-height: 1.2;
}

.product-desc {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: #000000;
  opacity: 0.5;
  margin: 0 0 16px 0;
  line-height: 1.5;
}

.product-price {
  font-family: 'Roboto', sans-serif;
  font-size: 24px;
  font-weight: 400;
  color: #000000;
  white-space: nowrap;
  flex-shrink: 0;
}

/* Теги */
.product-tags, .product-tags-top {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.product-tags-top {
  margin-bottom: 12px;
}

.tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: 'Roboto', sans-serif;
  font-size: 14px;
  font-weight: 400;
  padding: 4px 12px;
  border-radius: 100px;
}

.tag--blue {
  background-color: #f1faff;
  color: #2baac9;
  border: none;
}

.tag--green {
  background-color: #f1fff3;
  color: #0f5e1a;
  border: none;
}

.tag-icon {
  flex-shrink: 0;
}

/* Мобильная кнопка товара */
.product-mobile-action {
  width: 100%;
  margin-top: 16px;
}

.product-mobile-btn {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 61px;
  background-color: #ffffff;
  border: 1px solid #dddddd;
  padding: 0 24px;
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
  font-weight: 400;
  color: #000000;
  cursor: pointer;
  transition: background-color 0.2s, border-color 0.2s;
  outline: none;
}

.product-mobile-btn--added {
  background-color: #000000;
  border-color: #000000;
  color: #ffffff;
}

.product-mobile-btn-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-mobile-btn-price {
  font-weight: 500;
}

/* ─── SECTION BLOCK ─── */
.section-block {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.section-title {
  font-family: 'Roboto', sans-serif;
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  margin: 0;
  line-height: 1.166;
}

/* ─── LOCATION ─── */
.select-field {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  height: 61px;
  border: 1px solid #dddddd;
  background: #ffffff;
  cursor: pointer;
  transition: border-color 0.2s;
}
.select-field:hover {
  border-color: #000000;
}

.select-placeholder {
  font-size: 18px;
  font-weight: 400;
  color: #000000;
  opacity: 0.4;
}

.select-arrow {
  display: flex;
  align-items: center;
}

.location-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #ffffff;
  border: 1px solid #dfdfdf;
  padding: 24px;
  gap: 24px;
}

.location-info {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.location-badge {
  display: inline-block;
  font-size: 14px;
  font-weight: 400;
  color: #0f5e1a;
  background: #f1fff3;
  padding: 2px 10px;
  border-radius: 100px;
  width: fit-content;
}

.location-name {
  font-size: 24px;
  font-weight: 400;
  color: #000000;
  margin: 0;
  font-family: 'Roboto', sans-serif;
}

.location-schedule {
  display: flex;
  gap: 16px;
  font-size: 16px;
  font-weight: 400;
  color: #000000;
  opacity: 0.6;
}

.schedule-days {
  min-width: 70px;
}

.change-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 18px;
  font-weight: 400;
  color: #000000;
  font-family: 'Roboto', sans-serif;
  padding: 12px 24px;
  flex-shrink: 0;
  transition: opacity 0.2s;
}
.change-btn:hover { opacity: 0.7; }

/* ─── PERSONAL FORM ─── */
.personal-form {
  display: flex;
  flex-direction: column;
  gap: 48px;
}

.form-row-two {
  display: flex;
  gap: 8px;
}

.form-row-two .field-group {
  flex: 1;
  min-width: 0;
}

.field-group--full {
  width: 100%;
}

.field-label {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: #000000;
  margin-bottom: 12px;
  display: block;
}

.field-label--md {
  font-size: 21px;
  font-weight: 400;
  color: #000000;
}

.field-input {
  display: block;
  width: 100%;
  height: 61px;
  border: none;
  border-bottom: 1px solid #dddddd;
  background: transparent;
  padding: 0;
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
  font-weight: 400;
  color: #000000;
  outline: none;
  transition: border-color 0.2s;
}

.field-input::placeholder {
  color: #000000;
  opacity: 0.4;
}

.field-input:focus {
  border-bottom-color: #000000;
}

.field-info {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  margin-top: 16px;
}

.field-info svg {
  flex-shrink: 0;
  margin-top: 1px;
}

.field-info-text {
  font-size: 16px;
  font-weight: 400;
  color: #000000;
  opacity: 0.5;
  line-height: 1.55;
}

/* ─── SUMMARY BLOCK (Сводка) ─── */
.summary-block {
  padding: 32px;
  border-bottom: 1px solid #dfdfdf;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.summary-label {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: #000000;
  opacity: 0.5;
  margin: 0;
}

.summary-value {
  font-family: 'Roboto', sans-serif;
  font-size: 24px;
  font-weight: 400;
  color: #000000;
  margin: 0;
}

.summary-value--muted {
  opacity: 0.4;
}

.summary-value--location {
  font-size: 18px;
}

.summary-value--big {
  font-size: 24px;
}

.summary-badge {
  display: inline-block;
  font-size: 12px;
  color: #0f5e1a;
  background: #f1fff3;
  padding: 2px 8px;
  border-radius: 100px;
  font-family: 'Roboto', sans-serif;
  margin-bottom: 4px;
}

.summary-schedule {
  display: flex;
  flex-direction: column;
  gap: 2px;
  font-size: 15px;
  color: #000000;
  opacity: 0.5;
}

.summary-schedule-row {
  display: flex;
  gap: 16px;
}

.summary-schedule-days {
  min-width: 60px;
}

.summary-items {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.summary-item {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-family: 'Roboto', sans-serif;
  font-size: 17px;
  font-weight: 400;
  color: #000000;
}

/* ─── PROMO ─── */
.promo-row {
  display: flex;
  border-top: 1px solid #dfdfdf;
  border-bottom: 1px solid #dfdfdf;
  flex-shrink: 0;
}

.promo-input-wrap {
  flex: 1;
}

.promo-input {
  width: 100%;
  height: 61px;
  border: none;
  background: #f8f8f8;
  padding: 0 24px;
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
  font-weight: 400;
  color: #000000;
  outline: none;
}

.promo-input::placeholder {
  color: #000000;
  opacity: 0.4;
}

.promo-btn {
  width: 62px;
  height: 61px;
  background: #f8f8f8;
  border: none;
  border-left: 1px solid #dfdfdf;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  flex-shrink: 0;
  transition: background 0.2s;
}
.promo-btn:hover {
  background: #eeeeee;
}

/* ─── TOTAL ─── */
.total-block {
  margin-top: auto;
  display: flex;
  flex-direction: column;
}

.total-inner {
  padding: 32px;
  background: #ffffff;
  border-top: 1px solid #dfdfdf;
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.total-price-group {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.total-label {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: #000000;
  opacity: 0.5;
}

.total-price {
  font-family: 'Roboto', sans-serif;
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  line-height: 1.166;
}

.consent-row {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  cursor: pointer;
}

.consent-checkbox {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
  margin: 0;
  margin-top: 2px;
  cursor: pointer;
  accent-color: #000000;
}

.consent-text {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: #000000;
  line-height: 1.5;
}

.consent-link {
  text-decoration: underline;
  cursor: pointer;
}

.continue-btn-wrapper {
  width: 100%;
}

.continue-btn {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 72px;
  background-color: #000000;
  color: #ffffff;
  border: none;
  padding: 0 32px;
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
  font-weight: 400;
  cursor: pointer;
  transition: opacity 0.2s;
  flex-shrink: 0;
}
.continue-btn:hover { opacity: 0.9; }
.continue-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.right-col::-webkit-scrollbar {
  width: 4px;
}
.right-col::-webkit-scrollbar-thumb {
  background: #dddddd;
  border-radius: 2px;
}

/* ───────────────────── MAP SELECTOR SCREEN (ЭКРАН КАРТЫ) ───────────────────── */
.map-selector-screen {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #ffffff;
  overflow: hidden;
}

.map-selector-body {
  display: flex;
  flex: 1;
  min-height: 0;
  position: relative;
}

/* Левый сайдбар на карте */
.map-sidebar {
  width: 624px;
  flex-shrink: 0;
  border-right: 1px solid #dfdfdf;
  padding: 64px 48px;
  display: flex;
  flex-direction: column;
  gap: 32px;
  overflow-y: auto;
  background-color: #ffffff;
  z-index: 10;
}

.map-sidebar-title {
  font-family: 'Roboto', sans-serif;
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  margin: 0;
}

/* Шаг 1: Выбор города */
.city-select-dropdown {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  height: 61px;
  border: 1px solid #dddddd;
  background: #ffffff;
  cursor: pointer;
  transition: border-color 0.2s;
}
.city-select-dropdown:hover {
  border-color: #000000;
}

.selected-city-name {
  font-size: 18px;
  font-weight: 400;
  color: #000000;
}

.city-options-list {
  border: 1px solid #dddddd;
  border-top: none;
  background: #ffffff;
  max-height: 250px;
  overflow-y: auto;
}

.city-option {
  padding: 16px 24px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.2s;
}
.city-option:hover {
  background-color: #f5f5f5;
}

/* Шаг 2: Список лабораторий */
.city-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #dfdfdf;
  padding-bottom: 16px;
}

.city-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 18px;
  font-weight: 500;
  color: #000000;
}

.change-city-btn {
  background: none;
  border: none;
  font-size: 16px;
  color: #000000;
  opacity: 0.5;
  text-decoration: underline;
  cursor: pointer;
}
.change-city-btn:hover {
  opacity: 0.8;
}

.promo-alert-card {
  background-color: #e8f5ee;
  border-radius: 0;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.promo-alert-title {
  font-size: 18px;
  font-weight: 500;
  color: #1a8a4a;
  margin: 0;
}

.promo-alert-desc {
  font-size: 15px;
  color: #1a8a4a;
  margin: 0;
  line-height: 1.45;
}

.labs-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.lab-card {
  border: 1px solid #dfdfdf;
  background-color: #ffffff;
  cursor: pointer;
  transition: border-color 0.2s, box-shadow 0.2s;
  display: flex;
  flex-direction: column;
}
.lab-card:hover {
  border-color: #000000;
}

.lab-card--active {
  border-color: #000000;
}

.lab-card-content {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.lab-card-badge {
  display: inline-block;
  font-size: 13px;
  font-weight: 500;
  color: #0f5e1a;
  background: #f1fff3;
  padding: 2px 8px;
  border-radius: 100px;
  width: fit-content;
}

.lab-card-name {
  font-size: 21px;
  font-weight: 400;
  color: #000000;
  margin: 0;
}

.lab-card-schedule {
  display: flex;
  flex-direction: column;
  gap: 4px;
  font-size: 15px;
  color: #000000;
  opacity: 0.6;
}

.lab-card-schedule .schedule-row {
  display: flex;
}

.lab-card-schedule .schedule-days {
  width: 80px;
}

.select-lab-btn {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 61px;
  background-color: #000000;
  color: #ffffff;
  border: none;
  padding: 0 24px;
  font-size: 17px;
  font-family: 'Roboto', sans-serif;
  cursor: pointer;
  transition: opacity 0.2s;
}
.select-lab-btn:hover {
  opacity: 0.9;
}

/* Мобильная кнопка на карте */
.mobile-map-trigger-btn {
  display: none;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 72px;
  background-color: #000000;
  color: #ffffff;
  border: none;
  padding: 0 24px;
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  cursor: pointer;
  margin-top: 24px;
}

/* КАРТА CONTAINER */
.map-view-container {
  flex: 1;
  background-color: #f0f3f8;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.map-svg {
  width: 100%;
  height: 100%;
  display: block;
}

.map-svg--moscow {
  transition: viewBox 0.4s ease-in-out;
}

.map-city-marker {
  cursor: pointer;
}

.map-city-marker circle {
  transition: transform 0.2s, fill 0.2s;
}

.map-city-marker:hover circle {
  fill: #ff0000;
}

.marker-pulse {
  animation: pulse 2s infinite;
}

.map-city-label {
  font-family: 'Roboto', sans-serif;
  font-size: 12px;
  font-weight: 500;
  fill: #333333;
  pointer-events: none;
}

.map-lab-marker {
  cursor: pointer;
}

.map-lab-marker circle, .map-lab-marker rect {
  transition: r 0.2s, fill 0.2s, transform 0.2s;
}

.map-lab-marker:hover circle {
  fill: #ff0000;
}

.map-lab-marker--detailed {
  z-index: 100;
}

@keyframes pulse {
  0% { r: 6; opacity: 1; }
  50% { r: 12; opacity: 0.4; }
  100% { r: 6; opacity: 1; }
}

/* MOBILE BOTTOM SHEET */
.mobile-lab-sheet {
  display: none;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  background: #ffffff;
  box-shadow: 0 -4px 24px rgba(0, 0, 0, 0.1);
  z-index: 200;
  transform: translateY(100%);
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.mobile-lab-sheet--open {
  transform: translateY(0);
}

.mobile-sheet-content {
  padding: 32px 24px 24px 24px;
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.close-sheet-btn {
  position: absolute;
  top: 16px;
  right: 16px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.mobile-sheet-title {
  font-size: 21px;
  font-weight: 500;
  color: #000000;
  margin: 0;
  font-family: 'Roboto', sans-serif;
  max-width: 90%;
}

.mobile-sheet-schedule {
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 16px;
  color: #000000;
  opacity: 0.6;
}

.mobile-sheet-schedule .schedule-row {
  display: flex;
}

.mobile-sheet-schedule .schedule-days {
  width: 80px;
}

.mobile-select-confirm-btn {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 61px;
  background-color: #000000;
  color: #ffffff;
  border: none;
  padding: 0 24px;
  font-size: 18px;
  font-family: 'Roboto', sans-serif;
  cursor: pointer;
  margin-top: 8px;
}

/* ───────────────────── RESPONSIVE (MOBILE АДАПТАЦИЯ) ───────────────────── */
@media (max-width: 900px) {
  
  .desktop-only {
    display: none !important;
  }
  .mobile-only {
    display: block !important;
  }

  /* Поток главной страницы */
  .page-body {
    flex-direction: column;
    padding-bottom: 96px; /* Зазор под фиксированную кнопку Продолжить */
  }

  .content-container {
    flex-direction: column;
  }

  .left-col {
    padding: 32px 16px; /* Отступы по бокам 16px на мобильных */
    gap: 48px;
  }

  /* Товары как отдельные белые карточки */
  .products-section {
    background: transparent;
    border: none;
    gap: 16px;
  }

  .product-row {
    flex-direction: column;
    background: #ffffff;
    border: 1px solid #dfdfdf;
    padding: 32px 24px 24px 24px;
    gap: 16px;
  }

  .product-row--added-border {
    border-color: #000000; /* Подсветка границы выбранного на мобильном */
  }

  .product-info {
    padding: 0;
  }

  .product-name {
    font-size: 24px;
    line-height: 1.25;
    margin-bottom: 8px;
  }

  .product-desc {
    font-size: 16px;
    line-height: 1.45;
    margin-bottom: 0;
  }

  /* Правая колонка переезжает вниз за левой колонкой */
  .right-col {
    width: 100%;
    position: static;
    height: auto;
    border-left: none;
    border-top: 1px solid #dfdfdf;
    background-color: #f5f5f5;
    overflow: visible;
  }

  .mobile-summary-title {
    padding: 48px 16px 8px 16px;
    margin: 0;
  }

  /* Переопределение отступов сводки на мобильном */
  .summary-block {
    padding: 24px 16px;
    background-color: #ffffff;
  }

  .promo-row {
    background-color: #ffffff;
  }

  .total-inner {
    padding: 32px 16px;
  }

  /* Кнопка Продолжить фиксирована в самом низу экрана */
  .continue-btn-wrapper {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #ffffff;
    border-top: 1px solid #dfdfdf;
    z-index: 999;
  }

  .continue-btn {
    height: 72px;
  }

  /* Экран выбора лаборатории */
  .map-selector-body {
    flex-direction: column;
    height: calc(100vh - 72px);
    overflow: hidden;
  }

  .map-sidebar {
    width: 100%;
    height: 100%;
    padding: 40px 16px;
    overflow-y: auto;
  }

  .map-sidebar--hidden {
    display: none;
  }

  .mobile-map-trigger-btn {
    display: flex;
  }

  .map-view-container {
    display: none;
    width: 100%;
    height: 100%;
  }

  .map-view-container--visible {
    display: flex;
  }

  .mobile-lab-sheet {
    display: block;
  }

  .section-title {
    font-size: 32px;
  }

  .form-row-two {
    flex-direction: column;
    gap: 24px;
  }

  .field-label--md {
    font-size: 18px;
  }
}
</style>
