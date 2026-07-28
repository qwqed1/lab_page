<script setup>
const props = defineProps({
  doctorMode: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['register', 'about', 'close', 'materials'])
const router = useRouter()

const sidebarAssets = Object.freeze({
  logo: '/assets/figma-alex-logo.svg',
  cta: '/assets/figma-cta-arrow.svg',
  search: '/assets/figma-search-icon.svg',
  demo: '/assets/figma-demo-icon.svg',
  profile: '/assets/figma-profile-icon.svg',
  about: '/assets/figma-about-icon.svg',
  materials: '/assets/figma-doctor-materials-icon.svg'
})

const goTo = (path) => router.push(path)

const openAudienceContent = () => {
  if (props.doctorMode) {
    emit('materials')
    closeMobileMenu()
    return
  }

  goTo('/quiz')
}

const closeMobileMenu = () => {
  emit('close')
}

const openMobileAbout = () => {
  emit('about')
  closeMobileMenu()
}
</script>

<template>
  <aside class="sidebar-container site-sidebar" aria-label="Навигация по сайту">
    <div id="card-promo" class="promo-card">
      <div class="promo-content">
        <img
          :src="sidebarAssets.logo"
          alt="ALEX Allergy Xplorer"
          class="promo-banner-img"
          width="392"
          height="142"
          decoding="sync"
          fetchpriority="high"
        />
        <p class="promo-text">
          Многокомпонентный анализ крови, который за один забор крови проверяет более 300 аллергенов, выявляя истинные причины реакции.
        </p>
        <button class="mobile-supplier-link" type="button" @click="openMobileAbout">
          О поставщике ALEX LAB
        </button>
      </div>

      <button id="btn-register" class="promo-button" type="button" @click="emit('register')">
        <span class="promo-button-text">Записаться на тест на аллергию</span>
        <span class="promo-button-icon" aria-hidden="true">
          <img :src="sidebarAssets.cta" alt="" width="32" height="32" decoding="sync" />
        </span>
      </button>
    </div>

    <div class="cards-row">
      <div
        id="card-search"
        class="sub-card"
        role="button"
        tabindex="0"
        @click="goTo('/search')"
        @keydown.enter="goTo('/search')"
        @keydown.space.prevent="goTo('/search')"
      >
        <div class="card-icon-wrapper">
          <img :src="sidebarAssets.search" alt="" width="42" height="42" decoding="sync" />
        </div>
        <div class="card-text-group">
          <h3 class="card-title">
            <span class="desktop-sidebar-label">Поиск аллергенов</span>
            <span class="mobile-sidebar-label">Список аллергенов</span>
          </h3>
          <p class="card-subtitle">Убедитесь, что тест покажет, что вам нужно</p>
        </div>
      </div>

      <div
        id="card-demo"
        class="sub-card"
        role="button"
        tabindex="0"
        @click="goTo('/demo-result')"
        @keydown.enter="goTo('/demo-result')"
        @keydown.space.prevent="goTo('/demo-result')"
      >
        <div class="card-icon-wrapper">
          <img :src="sidebarAssets.demo" alt="" width="42" height="42" decoding="sync" />
        </div>
        <div class="card-text-group">
          <h3 class="card-title">
            <span class="desktop-sidebar-label">Посмотреть<br />демо-результат</span>
            <span class="mobile-sidebar-label">Посмотреть демо-результат</span>
          </h3>
          <p class="card-subtitle">Объясняем результаты<br />на человеческом языке</p>
        </div>
      </div>
    </div>

    <div
      :id="doctorMode ? 'row-doctor-materials' : 'row-quiz'"
      class="sidebar-row-card"
      role="button"
      tabindex="0"
      @click="openAudienceContent"
      @keydown.enter="openAudienceContent"
      @keydown.space.prevent="openAudienceContent"
    >
      <div class="row-left-content">
        <template v-if="doctorMode">
          <span class="row-icon-icon" aria-hidden="true">
            <img :src="sidebarAssets.materials" alt="" width="24" height="24" decoding="sync" />
          </span>
          <span class="row-text">Материалы для врачей</span>
        </template>
        <template v-else>
          <span class="tag-badge">~5 минут</span>
          <span class="row-text">КВИЗ: Нужен ли вам тест на аллергены?</span>
        </template>
      </div>
    </div>

    <div
      id="row-profile"
      class="sidebar-row-card"
      role="button"
      tabindex="0"
      @click="goTo('/personal-account')"
      @keydown.enter="goTo('/personal-account')"
      @keydown.space.prevent="goTo('/personal-account')"
    >
      <div class="row-left-content">
        <span class="row-icon-icon sidebar-profile-icon" aria-hidden="true">
          <img :src="sidebarAssets.profile" alt="" width="24" height="24" decoding="sync" />
        </span>
        <span class="row-text">Личный кабинет</span>
      </div>
    </div>

    <div
      id="row-about"
      class="sidebar-row-card"
      role="button"
      tabindex="0"
      @click="emit('about')"
      @keydown.enter="emit('about')"
      @keydown.space.prevent="emit('about')"
    >
      <div class="row-left-content">
        <span class="row-text">
          <span class="desktop-sidebar-label">Лаборатория ALEX LAB</span>
          <span class="mobile-sidebar-label">О поставщике ALEX LAB</span>
        </span>
      </div>
      <span class="row-icon-icon" aria-hidden="true">
        <img :src="sidebarAssets.about" alt="" width="24" height="24" decoding="sync" />
      </span>
    </div>

    <button class="mobile-close-row" type="button" @click="closeMobileMenu">
      <span class="mobile-close-icon" aria-hidden="true"></span>
      <span>Закрыть</span>
    </button>
  </aside>
</template>
