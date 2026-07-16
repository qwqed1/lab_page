<script setup>
const props = defineProps({
  slide: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['action', 'navigate'])

const openFaqIndex = ref(-1)

const faqItems = [
  { question: 'Это больно?', answer: 'Забор крови из вены производится тонкой иглой, процедура быстрая и практически безболезненная.' },
  { question: 'Сколько аллергенов в тесте?', answer: 'Аллергочип ALEX2 проверяет более 300 аллергенов одновременно.' },
  { question: 'Через сколько будет результат?', answer: 'Готовность — через 4–7 рабочих дней.' },
  { question: 'У вас есть сертификаты?', answer: 'Да, тест ALEX2 сертифицирован и признан во всем мире.' }
]

const blogCards = [
  'Cursor представила модель Composer 2.5 — в тестах она сопоставима c Opus 4.7 и GPT-5.5, но стоит примерно в 10 раз дешевле Как сдать тест: подготовка и процесс',
  'Cursor представила модель Composer 2.5 — в тестах она сопоставима c Opus 4.7 и GPT-5.5, но стоит примерно в 10 раз дешевле'
]

const howToAsset = computed(() => `/assets/figma-howto-step-${props.slide.step}.png`)

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
      <article v-for="(description, index) in blogCards" :key="index" class="exact-blog-card">
        <div class="exact-blog-cover">
          <img src="/assets/figma-blog-cover.png" alt="">
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

        <p class="exact-blog-description">{{ description }}</p>
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
  font-family: 'Roboto', Arial, sans-serif;
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
  font-size: clamp(28px, calc(42 * var(--ui)), 42px);
  font-weight: 400;
  line-height: 1.1667;
}

.exact-bottom-link {
  position: absolute;
  left: calc(64 * var(--ux));
  bottom: calc(64 * var(--uy));
  width: calc(1117 * var(--ux));
  height: calc(49 * var(--ui));
  min-height: 35px;
  padding: calc(24 * var(--ui)) 0 0;
  border: 0;
  border-top: 1px solid rgba(0, 0, 0, 0.2);
  background: transparent;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  color: #000;
  font-size: clamp(17px, calc(24 * var(--ui)), 24px);
  font-weight: 400;
  line-height: 1;
  text-align: left;
  cursor: pointer;
}

.exact-bottom-link img {
  width: calc(24 * var(--ui));
  height: calc(24 * var(--ui));
  min-width: 19px;
  min-height: 19px;
}

/* FAQ — node 39:2029 */
.exact-faq-list {
  position: absolute;
  left: calc(64 * var(--ux));
  /* Leave a full row of breathing room above the "All questions" divider.
     The list grows upward when an answer opens, so its last item never
     crosses that divider. */
  bottom: calc(64 * var(--uy) + 49 * var(--ui) + 52px);
  width: calc(1117 * var(--ux));
  display: flex;
  flex-direction: column;
  gap: calc(32 * var(--uy));
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
  font-size: clamp(17px, calc(24 * var(--ui)), 24px);
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
  font-size: clamp(14px, calc(18 * var(--ui)), 18px);
  font-weight: 400;
  line-height: 1;
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
  aspect-ratio: 552 / 335;
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
  font-size: clamp(13px, calc(16 * var(--ui)), 16px);
  line-height: 1.1875;
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
  font-size: clamp(14px, calc(18 * var(--ui)), 18px);
  line-height: 1;
}

.exact-blog-author-role {
  color: rgba(0, 0, 0, 0.5);
  font-size: clamp(13px, calc(16 * var(--ui)), 16px);
  line-height: 1.1875;
}

.exact-blog-description {
  margin: calc(24 * var(--ui)) 0 0;
  font-size: clamp(15px, calc(21 * var(--ui)), 21px);
  font-weight: 400;
  line-height: 1.03;
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
  font-size: clamp(17px, calc(24 * var(--ui)), 24px);
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
  font-size: clamp(22px, calc(32 * var(--ui)), 32px);
  line-height: 1.1875;
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
  font-size: clamp(15px, calc(21 * var(--ui)), 21px);
  line-height: 1.03;
}

@media (max-width: 700px) {
  .exact-section-title {
    font-size: clamp(24px, calc(42 * var(--ui)), 42px);
  }

  .exact-blog-grid {
    grid-template-columns: 1fr;
  }

  .exact-blog-card:nth-child(2) {
    display: none;
  }

  .exact-blog-description {
    max-width: 90%;
  }
}

</style>
