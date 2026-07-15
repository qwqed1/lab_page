<template>
  <div class="page-container site-sidebar-layout">
    <SiteSidebar
      @register="redirectToCart"
      @about="$router.push('/')"
    />

    <!-- Right Column: Quiz App -->
    <main class="content-container quiz-page-content">
      <!-- Mobile Top Navigation Bar -->
      <div class="mobile-top-bar">
        <HomeBackLink />
        <span class="mobile-top-title">Квиз</span>
      </div>

      <header class="header-bar desktop-only">
        <HomeBackLink />
      </header>

      <div class="card-container">
        <Transition name="fade" mode="out-in">
          
          <!-- STATE: INTRO -->
          <div v-if="step === 'intro'" class="quiz-card-wrapper intro-state">
            <div class="glass-card main-card">
              <div class="main-card-inner">
                <h1 class="card-title">Нужно ли мне сдать тест на аллергию?</h1>
                <p class="card-subtitle">
                  Не уверены в том, что тест подойдёт вам? Пройдите тест на ~5 минут и сделайте выбор
                </p>
              </div>
            </div>
            
            <button class="action-btn next-btn" @click="startQuiz">
              <span class="btn-text">Начать тест</span>
              <!-- Arrow SVG -->
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="btn-arrow">
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
              </svg>
            </button>
          </div>

          <!-- STATE: QUIZ -->
          <div v-else-if="step === 'quiz'" class="quiz-card-wrapper quiz-state">
            <div class="options-header">
              <button class="back-prev-btn" @click="prevQuestion">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;">
                  <line x1="19" y1="12" x2="5" y2="12"></line>
                  <polyline points="12 19 5 12 12 5"></polyline>
                </svg>
                <span>Вернуться назад</span>
              </button>
            </div>

            <div class="glass-card question-card">
              <div class="question-info">
                <span class="question-counter">{{ currentQuestionIndex + 1 }}/{{ questions.length }}</span>
                <h2 class="question-text">{{ currentQuestion.text }}</h2>
              </div>
            </div>

            <div class="options-list">
              <div 
                v-for="(option, idx) in currentQuestion.options" 
                :key="idx" 
                class="option-row"
                :class="{ 'selected': answers[currentQuestionIndex] === idx }"
                @click="selectOption(idx)"
              >
                <div class="option-checkbox">
                  <div class="option-checkbox-inner"></div>
                </div>
                <span class="option-label">{{ option }}</span>
              </div>
            </div>
          </div>

          <!-- STATE: RESULT -->
          <div v-else-if="step === 'result'" class="quiz-card-wrapper result-state">
            <div class="glass-card result-card">
              <div class="result-content">
                <span class="result-badge">Результат</span>
                <div class="result-details">
                  <h2 class="result-title">{{ getResultTitle }}</h2>
                  <p class="result-subtitle">
                    {{ getResultSubtitle }}
                  </p>
                </div>
              </div>
            </div>

            <button class="action-btn submit-btn" @click="redirectToCart">
              <span class="btn-text">Записаться на тест</span>
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="btn-arrow inverted-arrow">
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
              </svg>
            </button>
          </div>

        </Transition>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from '#app'

const router = useRouter()

const step = ref('intro')
const currentQuestionIndex = ref(0)

const questions = [
  {
    text: 'Испытываете ли вы зуд в носу или глазах в весенне-летний период?',
    options: ['Очень часто', 'Иногда', 'Редко', 'Никогда', 'Не знаю']
  },
  {
    text: 'Как часто вы чихаете без причины?',
    options: ['Постоянно', 'Часто', 'Редко', 'Метко', 'Не знаю']
  },
  {
    text: 'Появляется ли у вас кожная сыпь после употребления определенных продуктов?',
    options: ['Да, постоянно', 'Бывает иногда', 'Очень редко', 'Никогда не замечал', 'Не уверен']
  },
  {
    text: 'Беспокоит ли вас заложенность носа по утрам без простудных симптомов?',
    options: ['Да, почти каждое утро', 'Периодически', 'Очень редко', 'Никогда', 'Сложно сказать']
  },
  {
    text: 'Бывает ли у вас сухой приступообразный кашель ночью или после физической нагрузки?',
    options: ['Часто бывает', 'Иногда беспокоит', 'Редко', 'Никогда', 'Не знаю']
  },
  {
    text: 'Замечали ли вы появление насморка или слезотечения после контакта с животными?',
    options: ['Да, выраженная реакция', 'Есть легкое раздражение', 'Редко', 'Никакой реакции', 'У меня нет контакта с животными']
  },
  {
    text: 'Усиливаются ли симптомы (насморк, кашель) во время уборки квартиры?',
    options: ['Да, очень сильно', 'Немного усиливаются', 'Редко замечаю', 'Никогда', 'Не знаю']
  },
  {
    text: 'Есть ли у кого-то из ваших близких родственников диагностированная аллергия?',
    options: ['Да, у нескольких', 'Да, у одного из родителей', 'Только подозрения', 'Нет ни у кого', 'Не знаю семейный анамнез']
  },
  {
    text: 'Была ли у вас когда-либо реакция на прием лекарственных препаратов?',
    options: ['Да, сильная реакция', 'Была легкая сыпь', 'Нет, никогда', 'Не принимаю лекарств', 'Не знаю']
  },
  {
    text: 'Возникает ли сильный отек, покраснение или зуд после укусов насекомых?',
    options: ['Да, держится долго', 'Умеренная реакция', 'Обычная реакция', 'Никогда не кусали', 'Не замечал']
  },
  {
    text: 'Бывает ли у вас тяжесть в животе или кожные высыпания после орехов, меда или молока?',
    options: ['Да, выраженная реакция', 'Бывает иногда', 'Очень редко', 'Никогда', 'Не знаю']
  },
  {
    text: 'Как долго продолжаются ваши симптомы насморка или слезотечения без признаков ОРВИ?',
    options: ['Более 2 недель', 'Около 1 недели', 'Несколько дней', 'Проходят за день', 'Симптомов нет']
  }
]

const answers = ref(Array(questions.length).fill(null))

const currentQuestion = computed(() => questions[currentQuestionIndex.value])

const getResultTitle = computed(() => {
  const positiveAnswersCount = answers.value.filter(ans => ans !== null && ans <= 1).length
  if (positiveAnswersCount >= 6) {
    return 'Лучше всего пройти тест в ближайшее время'
  } else if (positiveAnswersCount >= 3) {
    return 'Рекомендуется пройти профилактический тест'
  } else {
    return 'У вас низкий риск проявления аллергии'
  }
})

const getResultSubtitle = computed(() => {
  const positiveAnswersCount = answers.value.filter(ans => ans !== null && ans <= 1).length
  if (positiveAnswersCount >= 6) {
    return 'Ваши ответы в большинстве своём означают, что у вас высокий риск аллергии. Чтобы точно в этом убедиться — сдайте тест'
  } else if (positiveAnswersCount >= 3) {
    return 'У вас присутствуют некоторые симптомы, характерные для аллергических реакций. Рекомендуется сдать тест для исключения рисков.'
  } else {
    return 'Ваши симптомы маловероятно связаны с аллергией, однако для полной уверенности вы всегда можете пройти обследование.'
  }
})

const startQuiz = () => {
  step.value = 'quiz'
  currentQuestionIndex.value = 0
  answers.value = Array(questions.length).fill(null)
}

const resetQuiz = () => {
  step.value = 'intro'
  currentQuestionIndex.value = 0
  answers.value = Array(questions.length).fill(null)
}

const selectOption = (idx) => {
  answers.value[currentQuestionIndex.value] = idx
  setTimeout(() => {
    if (currentQuestionIndex.value < questions.length - 1) {
      currentQuestionIndex.value++
    } else {
      step.value = 'result'
    }
  }, 250)
}

const prevQuestion = () => {
  if (currentQuestionIndex.value > 0) {
    currentQuestionIndex.value--
  } else {
    step.value = 'intro'
  }
}

const redirectToProfile = () => {
  router.push('/personal-account')
}

const redirectToCart = () => {
  navigateTo('/cart')
}
</script>

<style scoped>
.quiz-page-content {
  display: flex;
  flex-direction: column;
  height: 100vh;
  position: relative;
  overflow: hidden;
  background-color: var(--bg-page);
}

.active-row-card {
  background-color: #f0f0f0 !important;
}

/* Header Bar (Frame 290) */
.header-bar {
  height: 72px;
  border-bottom: 1px solid var(--border-color-grey);
  background: var(--bg-card-white);
  padding: 24px 32px;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  z-index: 10;
}

.back-home-btn {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 18px;
  color: var(--text-black);
  font-weight: 400;
  padding: 4px 8px;
  border-radius: 4px;
  transition: background 0.2s ease;
}

.back-home-btn:hover {
  background: rgba(0, 0, 0, 0.05);
}

/* Centered cards container */
.card-container {
  flex: 1;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 120px 40px 40px 40px;
  overflow-y: auto;
}

@media (min-width: 1600px) {
  .card-container {
    justify-content: flex-start;
    padding-left: 298px; /* Match Figma exact gap */
    padding-right: 268px; /* Match Figma exact gap */
  }
}

.quiz-card-wrapper {
  width: 677px;
  display: flex;
  flex-direction: column;
  gap: 0; /* Match exact figma layout combining card + button */
}

/* Glass Card styling */
.glass-card {
  background: var(--bg-card-white);
  border: 1px solid var(--border-color-grey);
  backdrop-filter: blur(50px);
  padding: 32px;
}

.main-card {
  height: 538px;
  display: flex;
  align-items: flex-end;
}

.main-card-inner {
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: 100%;
}

.card-title {
  font-size: 32px;
  font-weight: 400;
  line-height: 1.2;
}

.card-subtitle {
  font-size: 18px;
  color: var(--text-muted);
  line-height: 1.4;
}

/* Action button at bottom */
.action-btn {
  height: 72px;
  width: 100%;
  background: var(--bg-card-white);
  border: 1px solid var(--border-color-grey);
  border-top: none;
  padding: 24px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background 0.2s ease, color 0.2s ease;
  backdrop-filter: blur(4px);
}

.action-btn:hover {
  background: rgba(240, 240, 240, 0.9);
}

.btn-text {
  font-size: 21px;
  font-weight: 400;
  color: var(--text-black);
}

.btn-arrow {
  width: 24px;
  height: 24px;
}

/* QUIZ STATE STYLES */
.options-header {
  height: 72px;
  background: var(--bg-card-white);
  border: 1px solid var(--border-color-grey);
  border-bottom: none;
  padding: 24px;
  display: flex;
  align-items: center;
  backdrop-filter: blur(4px);
}

.back-prev-btn {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 21px;
  color: var(--text-black);
  font-weight: 400;
  transition: transform 0.2s ease;
}

.back-prev-btn:hover {
  transform: translateX(-4px);
}

.question-card {
  min-height: 127px;
  border-bottom: 1px solid var(--border-color-grey);
  display: flex;
  align-items: flex-start;
}

.question-info {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.question-counter {
  font-size: 18px;
  color: var(--text-muted);
}

.question-text {
  font-size: 32px;
  font-weight: 400;
  line-height: 1.2;
}

.options-list {
  display: flex;
  flex-direction: column;
}

.option-row {
  height: 72px;
  background: var(--bg-card-white);
  border: 1px solid var(--border-color-grey);
  border-top: none;
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  transition: background 0.2s ease, border-color 0.2s ease;
  backdrop-filter: blur(4px);
}

.option-row:hover {
  background: rgba(245, 245, 245, 0.9);
}

.option-row.selected {
  background: rgba(151, 174, 150, 0.15);
  border-left: 4px solid #97ae96;
}

.option-checkbox {
  width: 24px;
  height: 24px;
  border: 2px solid var(--border-color-grey);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: border-color 0.2s ease;
}

.option-row.selected .option-checkbox {
  border-color: #97ae96;
}

.option-checkbox-inner {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: transparent;
  transition: background-color 0.2s ease;
}

.option-row.selected .option-checkbox-inner {
  background: #97ae96;
}

.option-label {
  font-size: 21px;
  color: var(--text-black);
  font-weight: 400;
}

/* RESULT STATE STYLES */
.result-card {
  height: 588px;
  display: flex;
  align-items: flex-end;
}

.result-content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  width: 100%;
}

.result-badge {
  font-size: 18px;
  color: var(--text-muted);
}

.result-details {
  display: flex;
  flex-direction: column;
  gap: 21px;
}

.result-title {
  font-size: 32px;
  font-weight: 400;
  line-height: 1.2;
}

.result-subtitle {
  font-size: 18px;
  color: var(--text-muted);
  line-height: 1.4;
}

.submit-btn {
  background: var(--text-black);
  border-color: var(--text-black);
}

.submit-btn:hover {
  background: #1a1a1a;
  border-color: #1a1a1a;
}

.submit-btn .btn-text {
  color: var(--bg-card-white);
}

.inverted-arrow {
  filter: invert(1);
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

/* RESPONSIVE DESIGN (MOBILE ADAPTATION) */
@media (max-width: 1024px) {
  .header-bar {
    display: none;
  }

  .back-home-btn span {
    display: none;
  }

  .card-container {
    padding: 41px 16px 16px 16px;
    align-items: flex-start;
  }

  .quiz-card-wrapper {
    width: 100%;
  }

  .main-card {
    height: auto;
    min-height: 400px;
    padding: 32px;
    align-items: center;
  }

  .card-title {
    font-size: 32px;
  }

  .card-subtitle {
    font-size: 18px;
  }

  .action-btn {
    height: 66px;
    padding: 21px 24px;
  }

  .question-card {
    height: auto;
    min-height: 120px;
    padding: 24px;
  }

  .question-text {
    font-size: 32px;
  }

  .option-label {
    font-size: 21px;
  }

  .option-row {
    height: 72px;
    padding: 24px;
  }

  .result-card {
    height: auto;
    min-height: 450px;
    padding: 32px;
  }

  .result-title {
    font-size: 32px;
  }

  .result-subtitle {
    font-size: 18px;
  }

  .submit-btn {
    height: 72px;
    padding: 24px;
  }
}
</style>
