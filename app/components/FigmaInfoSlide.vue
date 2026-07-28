<script setup>
const props = defineProps({
  slide: {
    type: Object,
    required: true
  },
  doctorMode: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['action', 'navigate'])

const openFaqIndex = ref(-1)

const patientFaqItems = [
  { question: 'Это больно?', answer: 'Забор крови из вены производится тонкой иглой, процедура быстрая и практически безболезненная.' },
  { question: 'Сколько аллергенов в тесте?', answer: 'Аллергочип ALEX2 проверяет более 300 аллергенов одновременно.' },
  { question: 'Через сколько будет результат?', answer: 'Готовность — через 4–7 рабочих дней.' },
  { question: 'У вас есть сертификаты?', answer: 'Да, тест ALEX2 сертифицирован и признан во всем мире.' }
]

const doctorFaqItems = [
  patientFaqItems[0],
  patientFaqItems[1],
  {
    question: 'Нужно ли сдавать на тощак?',
    answer: 'Нет. Анализ можно сдавать без голодания и специальной подготовки.'
  },
  patientFaqItems[3]
]

const faqItems = computed(() => (
  props.doctorMode ? doctorFaqItems : patientFaqItems
))

const blogCards = [
  {
    title: 'Я уволил джуна, нанял AI-агента, через месяц нанял джуна обратно',
    description: 'Про оптимизацию, которая выстрелила — но не так, как я думал'
  },
  {
    title: 'Я уволил джуна, нанял AI-агента, через месяц нанял джуна обратно',
    description: 'Про оптимизацию, которая выстрелила — но не так, как я думал'
  }
]

const howToAsset = computed(() => props.slide.step === '1'
  ? '/assets/figma-howto-step-1.png'
  : `/assets/${props.slide.step}.png`)

const toggleFaq = (index) => {
  openFaqIndex.value = openFaqIndex.value === index ? -1 : index
}
</script>

<template>
  <section v-if="slide.type === 'faq'" class="figma-exact-info-slide exact-faq-slide">
    <div class="exact-faq-list">
      <div
        v-for="(item, index) in faqItems"
        :key="item.question"
        class="exact-faq-item"
        :class="{ open: openFaqIndex === index }"
      >
        <button class="exact-faq-question" type="button" @click="toggleFaq(index)">
          <span>{{ item.question }}</span>
          <img
            src="/assets/figma-faq-chevron.svg"
            alt=""
            class="exact-faq-chevron"
          >
        </button>
        <p v-if="openFaqIndex === index" class="exact-faq-answer">{{ item.answer }}</p>
      </div>
    </div>

    <button class="exact-bottom-link" type="button" @click="emit('action')">
      <span>Все вопросы</span>
      <img src="/assets/figma-faq-link-arrow.svg" alt="">
    </button>
  </section>

  <section v-else-if="slide.type === 'blog'" class="figma-exact-info-slide exact-blog-slide">
    <h2 class="exact-section-title">Блог про аллергию</h2>

    <div class="exact-blog-grid">
      <article v-for="(card, index) in blogCards" :key="index" class="exact-blog-card">
        <div class="exact-blog-cover">
          <img src="/assets/figma-allergy-block.png" alt="">
          <div class="exact-blog-tags">
            <span>~16 минут</span>
            <span>Наука</span>
          </div>
        </div>

        <div class="exact-blog-author">
          <img src="/assets/figma-blog-author.png" alt="Александра Ковальчук">
          <div>
            <p class="exact-blog-author-name">Александра Ковальчук</p>
            <p class="exact-blog-author-role">Профессор МГУ</p>
          </div>
        </div>

        <div class="exact-blog-copy">
          <h3 class="exact-blog-card-title">{{ card.title }}</h3>
          <p class="exact-blog-description">{{ card.description }}</p>
        </div>
      </article>
    </div>

    <button class="exact-bottom-link" type="button" @click="emit('action')">
      <span>Все материалы</span>
      <img src="/assets/figma-faq-link-arrow.svg" alt="">
    </button>
  </section>

  <section
    v-else
    class="figma-exact-info-slide exact-howto-slide"
    :class="`exact-howto-step-${slide.step}`"
  >
    <h2 class="exact-section-title">Как сдать тест: подготовка и процесс</h2>

    <img class="exact-howto-image" :src="howToAsset" alt="">

    <div class="exact-howto-copy">
      <div class="exact-step-indicator" aria-label="Шаги">
        <button
          v-for="number in 3"
          :key="number"
          type="button"
          :class="{ active: Number(slide.step) === number }"
          :aria-label="`Перейти к шагу ${number}`"
          @click="emit('navigate', `slide-${17 + number}`)"
        >
          <i>{{ number }}</i>
        </button>
      </div>

      <div class="exact-howto-text">
        <h3 v-if="slide.step === '3'">
          Отслеживайте результат<br>в личном кабинете и на электронной почте
        </h3>
        <h3 v-else>{{ slide.title }}</h3>
        <p>{{ slide.subtitle }}</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.figma-exact-info-slide {
  --ux: min(calc(100cqw / 1243), calc(100cqh / 1080));
  --uy: calc(100cqh / 1080);
  --ui: min(var(--ux), var(--uy));
  position: absolute;
  inset: 0;
  container-type: size;
  overflow: hidden;
  color: #000;
  font-family: Helvetica, Arial, sans-serif;
}

button {
  font: inherit;
}

.exact-section-title {
  position: absolute;
  left: calc(64 * var(--ux));
  top: calc(326 * var(--uy));
  width: calc(1115 * var(--ux));
  margin: 0;
  font-size: 42px;
  font-weight: 400;
  line-height: 49px;
}

.exact-bottom-link {
  position: absolute;
  left: calc(64 * var(--ux));
  bottom: calc(64 * var(--uy));
  width: calc(1117 * var(--ux));
  min-height: 35px;
  padding: calc(24 * var(--ui)) 0 0 0;
  border: none;
  background: transparent;
  display: inline-flex;
  align-items: center;
  justify-content: flex-start;
  gap: 12px;
  color: #000;
  font-size: 24px;
  font-weight: 400;
  line-height: 1;
  text-align: left;
  cursor: pointer;
}

.exact-bottom-link::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 1px;
  background: rgba(0, 0, 0, 0.2);
}

.exact-bottom-link img {
  width: calc(24 * var(--ui));
  height: calc(24 * var(--ui));
  min-width: 19px;
  min-height: 19px;
}

.exact-faq-list {
  position: absolute;
  left: calc(64 * var(--ux));
  right: calc(64 * var(--ux));
  /* Leave a full row of breathing room above the "All questions" divider.
     The list grows upward when an answer opens, so its last item never
     crosses that divider. */
  bottom: calc(64 * var(--uy) + 49 * var(--ui) + 52px);
  width: auto;
  display: flex;
  flex-direction: column;
  gap: calc(32 * var(--uy));
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.exact-faq-list::-webkit-scrollbar {
  display: none;
  width: 0;
  height: 0;
}

.exact-faq-item {
  width: 100%;
  flex-shrink: 0;
}

.exact-faq-question {
  width: 100%;
  height: calc(24 * var(--uy));
  min-height: 20px;
  padding: 0;
  border: 0;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #000;
  font-size: 24px;
  font-weight: 400;
  line-height: 1;
  text-align: left;
  cursor: pointer;
}

.exact-faq-chevron {
  width: calc(24 * var(--ui));
  height: calc(24 * var(--ui));
  min-width: 19px;
  min-height: 19px;
  transition: transform 180ms ease;
}

.exact-faq-item.open .exact-faq-chevron {
  transform: rotate(180deg);
}

.exact-faq-answer {
  width: min(calc(718 * var(--ux)), 100%);
  margin: calc(12 * var(--ui)) 0 0;
  color: rgba(0, 0, 0, 0.6);
  font-size: 18px;
  font-weight: 400;
  line-height: 21px;
}

/* Blog — node 39:2204 */
.exact-blog-grid {
  position: absolute;
  left: calc(64 * var(--ux));
  top: calc(398 * var(--uy));
  width: calc(1116 * var(--ux));
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: calc(12 * var(--ui));
}

.exact-blog-card {
  min-width: 0;
}

.exact-blog-cover {
  position: relative;
  width: 100%;
  aspect-ratio: 987 / 494;
  overflow: hidden;
  background: rgba(0, 0, 0, 0.09);
}

.exact-blog-cover > img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.exact-blog-tags {
  position: absolute;
  left: calc(16 * var(--ui));
  top: calc(16 * var(--ui));
  display: flex;
  gap: calc(4 * var(--ui));
}

.exact-blog-tags span {
  min-height: calc(35 * var(--ui));
  padding: calc(8 * var(--ui)) calc(12 * var(--ui));
  border-radius: calc(10 * var(--ui));
  background: #f2f2f2;
  display: inline-flex;
  align-items: center;
  font-size: 16px;
  line-height: 19px;
  white-space: nowrap;
}

.exact-blog-author {
  height: calc(48 * var(--ui));
  margin-top: calc(24 * var(--ui));
  display: flex;
  align-items: center;
  gap: calc(12 * var(--ui));
}

.exact-blog-author > img {
  width: calc(48 * var(--ui));
  height: calc(48 * var(--ui));
  border-radius: calc(10 * var(--ui));
}

.exact-blog-author > div {
  display: flex;
  flex-direction: column;
  gap: calc(6 * var(--ui));
}

.exact-blog-author p {
  margin: 0;
}

.exact-blog-author-name {
  font-size: 18px;
  line-height: 21px;
}

.exact-blog-author-role {
  color: rgba(0, 0, 0, 0.5);
  font-size: 16px;
  line-height: 19px;
}

.exact-blog-copy {
  margin-top: calc(24 * var(--ui));
  display: flex;
  flex-direction: column;
  gap: calc(12 * var(--ui));
}

.exact-blog-card-title,
.exact-blog-description {
  margin: 0;
  font-weight: 400;
}

.exact-blog-card-title {
  font-size: 21px;
  line-height: 24px;
}

.exact-blog-description {
  font-size: 16px;
  line-height: 19px;
}

/* How to — nodes 39:2396, 39:2561 and 39:2726 */
.exact-howto-image {
  position: absolute;
  left: calc(64 * var(--ux));
  top: calc(412 * var(--uy));
  width: calc(627 * var(--ui));
  height: calc(360 * var(--ui));
  display: block;
  object-fit: cover;
}

.exact-howto-copy {
  position: absolute;
  left: calc(64 * var(--ux));
  top: calc(793.5 * var(--uy));
  width: calc(491 * var(--ui));
  display: flex;
  flex-direction: column;
  gap: calc(21 * var(--ui));
}

.exact-howto-step-2 .exact-howto-copy {
  left: calc(64.5 * var(--ux));
  width: calc(412 * var(--ui));
}

.exact-howto-step-3 .exact-howto-copy {
  width: calc(415 * var(--ui));
}

.exact-step-indicator {
  width: calc(144 * var(--ui));
  height: calc(48 * var(--ui));
  display: flex;
}

.exact-step-indicator > button {
  width: calc(48 * var(--ui));
  height: calc(48 * var(--ui));
  display: grid;
  place-items: center;
  opacity: 0.3;
  padding: 0;
  border: 0;
  background: transparent;
  cursor: pointer;
}

.exact-faq-slide .exact-bottom-link {
  right: calc(64 * var(--ux));
  width: auto;
}

.exact-step-indicator > button.active {
  opacity: 1;
}

.exact-step-indicator i {
  width: calc(38 * var(--ui));
  height: calc(38 * var(--ui));
  border: calc(2 * var(--ui)) solid #000;
  border-radius: 50%;
  display: grid;
  place-items: center;
  color: #000;
  font-size: 24px;
  font-style: normal;
  font-weight: 400;
  line-height: 1;
}

.exact-howto-text {
  display: flex;
  flex-direction: column;
  gap: calc(12 * var(--ui));
}

.exact-howto-text h3,
.exact-howto-text p {
  margin: 0;
  font-weight: 400;
}

.exact-howto-text h3 {
  font-size: 32px;
  line-height: 38px;
}

.exact-howto-step-1 .exact-howto-text h3 {
  width: calc(365 * var(--ui));
}

.exact-howto-step-2 .exact-howto-text h3 {
  width: calc(412 * var(--ui));
}

.exact-howto-step-3 .exact-howto-text h3 {
  width: calc(698 * var(--ui));
}

.exact-howto-text p {
  color: rgba(0, 0, 0, 0.8);
  font-size: 21px;
  line-height: 24px;
}

@media (max-width: 700px) {
  .figma-exact-info-slide {
    --mu: calc(100cqw / 420);
  }

  .exact-section-title {
    left: calc(16 * var(--mu));
    top: calc(100cqh - 611 * var(--mu));
    width: calc(388 * var(--mu));
    font-size: 32px;
    line-height: 38px;
  }

  .exact-blog-grid {
    left: calc(16 * var(--mu));
    top: calc(100cqh - 552 * var(--mu));
    width: calc(388 * var(--mu));
    grid-template-columns: 1fr;
    gap: 0;
  }

  .exact-blog-card:nth-child(2) {
    display: none;
  }

  .exact-blog-cover {
    width: calc(388 * var(--mu));
    height: auto;
    aspect-ratio: 987 / 494;
  }

  .exact-blog-tags {
    left: calc(6 * var(--mu));
    top: calc(6 * var(--mu));
    gap: calc(4 * var(--mu));
  }

  .exact-blog-tags span {
    min-height: calc(32 * var(--mu));
    padding: calc(8 * var(--mu)) calc(12 * var(--mu));
    border-radius: calc(8 * var(--mu));
    font-size: 14px;
    line-height: 16px;
  }

  .exact-blog-author {
    height: calc(48 * var(--mu));
    margin-top: calc(16 * var(--mu));
    gap: calc(12 * var(--mu));
  }

  .exact-blog-author > img {
    width: calc(48 * var(--mu));
    height: calc(48 * var(--mu));
    border-radius: calc(8 * var(--mu));
  }

  .exact-blog-author > div {
    gap: calc(2 * var(--mu));
  }

  .exact-blog-author-name {
    font-size: 16px;
    line-height: 19px;
  }

  .exact-blog-author-role {
    font-size: 14px;
    line-height: 16px;
  }

  .exact-blog-copy {
    margin-top: calc(16 * var(--mu));
    gap: calc(12 * var(--mu));
  }

  .exact-blog-card-title {
    width: calc(345 * var(--mu));
    font-size: 21px;
    line-height: 24px;
  }

  .exact-blog-description {
    width: calc(388 * var(--mu));
    max-width: none;
    font-size: 16px;
    line-height: 19px;
  }

  .exact-faq-list {
    left: calc(16 * var(--mu));
    right: calc(16 * var(--mu));
    top: auto;
    bottom: calc(170 * var(--mu));
    gap: calc(24 * var(--mu));
  }

  .exact-faq-question {
    height: calc(24 * var(--mu));
    min-height: calc(24 * var(--mu));
    font-size: 20px;
    line-height: 24px;
  }

  .exact-faq-chevron {
    width: calc(24 * var(--mu));
    height: calc(24 * var(--mu));
    min-width: 0;
    min-height: 0;
  }

  .exact-faq-answer {
    width: calc(388 * var(--mu));
    margin-top: calc(12 * var(--mu));
    font-size: 18px;
    line-height: 21px;
  }

  .exact-faq-item.open {
    margin-bottom: calc(-8 * var(--mu));
  }

  .exact-bottom-link,
  .exact-faq-slide .exact-bottom-link {
    left: calc(16 * var(--mu));
    right: calc(16 * var(--mu));
    bottom: calc(98 * var(--mu));
    width: calc(388 * var(--mu));
    height: calc(40 * var(--mu));
    min-height: 0;
    padding-top: calc(24 * var(--mu));
    border-top: 1px solid rgba(0, 0, 0, 0.2);
    font-size: 18px;
    line-height: 22px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: calc(12 * var(--mu));
  }

  .exact-bottom-link img {
    width: calc(16 * var(--mu));
    height: calc(16 * var(--mu));
    min-width: 0;
    min-height: 0;
  }

  .exact-howto-image {
    left: calc(16 * var(--mu));
    top: calc(100cqh - 516 * var(--mu));
    width: calc(388 * var(--mu));
    height: calc(224 * var(--mu));
  }

  .exact-howto-copy,
  .exact-howto-step-2 .exact-howto-copy,
  .exact-howto-step-3 .exact-howto-copy {
    left: calc(16 * var(--mu));
    top: calc(100cqh - 271 * var(--mu));
    width: calc(388 * var(--mu));
    gap: calc(21 * var(--mu));
  }

  .exact-howto-step-3 .exact-howto-copy {
    top: calc(100cqh - 279 * var(--mu));
    gap: calc(16 * var(--mu));
  }

  .exact-step-indicator {
    width: calc(120 * var(--mu));
    height: calc(40 * var(--mu));
  }

  .exact-step-indicator > button {
    width: calc(40 * var(--mu));
    height: calc(40 * var(--mu));
  }

  .exact-step-indicator i {
    width: calc(32 * var(--mu));
    height: calc(32 * var(--mu));
    border-width: 1px;
    font-size: 20px;
  }

  .exact-howto-text {
    gap: calc(12 * var(--mu));
  }

  .exact-howto-step-3 .exact-howto-text {
    gap: calc(8 * var(--mu));
  }

  .exact-howto-text h3,
  .exact-howto-step-1 .exact-howto-text h3,
  .exact-howto-step-2 .exact-howto-text h3,
  .exact-howto-step-3 .exact-howto-text h3 {
    width: calc(388 * var(--mu));
    font-size: 24px;
    line-height: 28px;
  }

  .exact-howto-step-3 .exact-howto-text h3 {
    line-height: calc(27 * var(--mu));
  }

  .exact-howto-text p {
    width: calc(388 * var(--mu));
    font-size: 18px;
    line-height: 21px;
  }

  .exact-howto-step-3 .exact-howto-text p {
    line-height: calc(20 * var(--mu));
  }
}

@container (min-width: 701px) and (max-width: 1024px) {
  .exact-section-title {
    left: 32px;
    top: 180px;
    width: calc(100% - 64px);
    font-size: 32px;
    line-height: 38px;
  }

  /* FAQ Tablet Styles */
  .exact-faq-list {
    left: 32px;
    right: 32px;
    top: auto;
    bottom: 180px;
    width: auto;
    max-height: calc(100cqh - 420px);
    overflow-y: auto;
    gap: 18px;
  }

  .exact-faq-question {
    font-size: 21px;
    line-height: 24px;
  }

  .exact-faq-answer {
    width: 100%;
    max-width: 600px;
    font-size: 18px;
    line-height: 21px;
  }

  /* Blog Tablet Styles */
  .exact-blog-grid {
    left: 32px;
    top: 250px;
    width: calc(100% - 64px);
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 24px;
  }

  .exact-blog-tags span {
    font-size: 14px;
    line-height: 16px;
  }

  .exact-blog-author-name {
    font-size: 16px;
    line-height: 19px;
  }

  .exact-blog-author-role {
    font-size: 14px;
    line-height: 16px;
  }

  .exact-blog-card-title {
    font-size: 21px;
    line-height: 24px;
  }

  .exact-blog-description {
    font-size: 16px;
    line-height: 20px;
  }

  .exact-bottom-link,
  .exact-faq-slide .exact-bottom-link {
    left: 32px;
    right: 32px;
    bottom: 96px;
    width: calc(100% - 64px);
    border-top: 1px solid rgba(0, 0, 0, 0.2);
    padding-top: 24px;
    font-size: 18px;
    line-height: 22px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 12px;
  }

  /* How-to Tablet Styles */
  .exact-howto-image {
    left: 32px;
    top: 250px;
    width: min(calc(100% - 64px), 520px);
    height: auto;
    aspect-ratio: 627 / 360;
    max-height: 280px;
    object-fit: cover;
  }

  .exact-howto-copy,
  .exact-howto-step-2 .exact-howto-copy,
  .exact-howto-step-3 .exact-howto-copy {
    left: 32px;
    top: 560px;
    width: min(calc(100% - 64px), 520px);
    gap: 16px;
  }

  .exact-howto-step-3 .exact-howto-copy {
    top: 560px;
    gap: 14px;
  }

  .exact-step-indicator {
    width: 144px;
    height: 48px;
  }

  .exact-step-indicator > button {
    width: 48px;
    height: 48px;
  }

  .exact-step-indicator i {
    width: 38px;
    height: 38px;
    font-size: 24px;
  }

  .exact-howto-text {
    gap: 12px;
  }

  .exact-howto-text h3,
  .exact-howto-step-1 .exact-howto-text h3,
  .exact-howto-step-2 .exact-howto-text h3,
  .exact-howto-step-3 .exact-howto-text h3 {
    width: 100%;
    font-size: 24px;
    line-height: 28px;
  }

  .exact-howto-text p {
    width: 100%;
    font-size: 18px;
    line-height: 22px;
  }
}

/* The 1440px desktop layout is the typography reference. Wider desktop
   viewports may expand the composition, but must not enlarge its text. */
@media (min-width: 1025px) {
  .exact-section-title {
    font-size: 32px;
    line-height: 38px;
  }

  .exact-faq-question {
    font-size: 24px;
    line-height: 24px;
  }

  .exact-faq-answer {
    font-size: 18px;
    line-height: 21px;
  }

  .exact-bottom-link,
  .exact-faq-slide .exact-bottom-link {
    font-size: 18px;
    line-height: 22px;
  }

  .exact-blog-tags span {
    font-size: 14px;
    line-height: 16px;
  }

  .exact-blog-author-name {
    font-size: 16px;
    line-height: 19px;
  }

  .exact-blog-author-role {
    font-size: 14px;
    line-height: 16px;
  }

  .exact-blog-card-title {
    font-size: 21px;
    line-height: 24px;
  }

  .exact-blog-description {
    font-size: 16px;
    line-height: 20px;
  }
}

</style>
