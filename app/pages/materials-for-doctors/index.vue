<script setup>
import { computed, ref } from 'vue'

useHead({
  title: 'Материалы для врачей — ALEX LAB'
})

const router = useRouter()
const query = ref('')

const materials = Object.freeze([
  { title: '№ Л041-01126-23/00345678', date: 'От 12.04.2022' },
  { title: 'Стандарт ISO', date: 'От 12.04.2024' },
  { title: 'Ежегодный аудит 2025', date: 'От 02.01.2025' },
  { title: '№ Л041-01126-23/00345678', date: 'От 12.04.2022' },
  { title: '№ Л041-01126-23/00345678', date: 'От 12.04.2022' },
  { title: 'Стандарт ISO', date: 'От 12.04.2024' },
  { title: 'Ежегодный аудит 2025', date: 'От 02.01.2025' },
  { title: 'Ежегодный аудит 2025', date: 'От 02.01.2025' },
  { title: 'Ежегодный аудит 2025', date: 'От 02.01.2025' }
])

const visibleMaterials = computed(() => {
  const normalizedQuery = query.value.trim().toLocaleLowerCase('ru')

  if (!normalizedQuery) {
    return materials
  }

  return materials.filter((material) => (
    material.title.toLocaleLowerCase('ru').includes(normalizedQuery) ||
    material.date.toLocaleLowerCase('ru').includes(normalizedQuery)
  ))
})

const goBack = () => {
  if (window.history.length > 1) {
    router.back()
    return
  }

  router.push('/')
}
</script>

<template>
  <main class="page-container site-sidebar-layout doctor-materials-page">
    <SiteSidebar
      class="doctor-materials-sidebar"
      :doctor-mode="true"
    />

    <section class="materials-shell" aria-labelledby="materials-title">
      <header class="materials-back-bar">
        <button class="materials-back-button" type="button" aria-label="Назад" @click="goBack">
          <img src="/assets/figma-demo-back.svg" alt="" width="24" height="24" />
          <span>Назад</span>
        </button>
      </header>

      <div class="materials-content">
        <h1 id="materials-title">Материалы для врачей</h1>

        <div class="materials-browser">
          <label class="materials-search">
            <span class="sr-only">Поиск по материалам</span>
            <input v-model="query" type="search" placeholder="Поиск" />
            <img src="/assets/figma-materials-search.svg" alt="" width="24" height="24" />
          </label>

          <div class="materials-list" aria-live="polite">
            <article
              v-for="(material, index) in visibleMaterials"
              :key="`${material.title}-${material.date}-${index}`"
              class="material-card"
            >
              <div class="material-copy">
                <h2>{{ material.title }}</h2>
                <p>{{ material.date }}</p>
              </div>

              <a
                class="material-download"
                href="/documents/elagin-demo-result.pdf"
                download
                :aria-label="`Скачать: ${material.title}`"
              >
                <img src="/assets/figma-materials-download.svg" alt="" width="24" height="24" />
              </a>
            </article>

            <p v-if="visibleMaterials.length === 0" class="materials-empty">
              Материалы не найдены
            </p>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<style scoped>
.doctor-materials-page {
  background: #f5f5f5;
}

.materials-shell {
  min-width: 0;
  height: 100dvh;
  overflow-x: hidden;
  overflow-y: auto;
  background: #f5f5f5;
}

.materials-back-bar {
  width: 100%;
  height: 72px;
  padding: 24px 32px;
  background: #ffffff;
  border: 1px solid #dfdfdf;
}

.materials-back-button {
  display: flex;
  align-items: center;
  gap: 8px;
  width: max-content;
  height: 24px;
  padding: 0;
  border: 0;
  background: transparent;
  color: #000000;
  cursor: pointer;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 17px;
  font-weight: 400;
  line-height: 24px;
}

.materials-back-button img {
  display: block;
  width: 24px;
  height: 24px;
}

.materials-content {
  width: 851px;
  padding: 64px;
}

.materials-content h1 {
  width: 723px;
  color: #000000;
  font-family: Roboto, Arial, sans-serif;
  font-size: 42px;
  font-weight: 400;
  line-height: 49px;
  letter-spacing: 0;
}

.materials-browser {
  width: 723px;
  margin-top: 64px;
}

.materials-search {
  position: relative;
  display: block;
  width: 100%;
  height: 61px;
  /* Figma uses a centred 1 px stroke; the half-pixel raster is equivalent
     to this 50% blend against the page background in CSS. */
  border-bottom: 1px solid rgba(101, 101, 101, 0.5);
}

.materials-search input {
  width: 100%;
  height: 60px;
  padding: 0 64px 0 24px;
  border: 0;
  outline: 0;
  background: transparent;
  color: rgba(0, 0, 0, 0.3);
  font-family: Roboto, Arial, sans-serif;
  font-size: 18px;
  font-weight: 400;
  line-height: normal;
  appearance: none;
}

.materials-search input::placeholder {
  color: rgba(0, 0, 0, 0.3);
  opacity: 1;
}

.materials-search input::-webkit-search-cancel-button {
  display: none;
}

.materials-search img {
  position: absolute;
  top: 18px;
  right: 24px;
  width: 24px;
  height: 24px;
  pointer-events: none;
}

.materials-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
  width: 100%;
  margin-top: 21px;
}

.material-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 94px;
  padding: 24px;
  background: #ffffff;
  border: 1px solid #dfdfdf;
  backdrop-filter: blur(4px);
}

.material-copy {
  display: flex;
  flex-direction: column;
  gap: 12px;
  height: 46px;
}

.material-copy h2 {
  color: #000000;
  font-family: Roboto, Arial, sans-serif;
  font-size: 21px;
  font-weight: 400;
  line-height: 15px;
  letter-spacing: 0;
}

.material-copy p {
  color: #000000;
  font-family: Roboto, Arial, sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 19px;
  letter-spacing: 0;
}

.material-download {
  display: flex;
  flex: 0 0 24px;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  color: #000000;
}

.material-download img {
  display: block;
  width: 24px;
  height: 24px;
}

.materials-empty {
  padding: 24px 0;
  font-size: 18px;
  color: rgba(0, 0, 0, 0.5);
}

.sr-only {
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

@media (max-width: 1024px) {
  .doctor-materials-page {
    display: block;
    width: 100%;
    height: auto;
    min-height: 100dvh;
    overflow: visible;
  }

  .doctor-materials-sidebar {
    display: none !important;
  }

  .materials-shell {
    width: 100%;
    height: auto;
    min-height: 100dvh;
    overflow: visible;
  }

  .materials-back-bar {
    height: 72px;
    padding: 24px 32px;
  }

  .materials-back-button span {
    display: none;
  }

  .materials-content {
    width: 100%;
    padding: 32px 16px 16px;
  }

  .materials-content h1 {
    width: 100%;
    font-size: 32px;
    line-height: 38px;
    white-space: nowrap;
  }

  .materials-browser {
    width: 100%;
    margin-top: 32px;
  }
}
</style>
