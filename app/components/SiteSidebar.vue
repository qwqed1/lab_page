<script setup>
const emit = defineEmits(['register', 'about'])
const router = useRouter()

const sidebarAssets = Object.freeze({
  logo: '/assets/figma-alex-logo.svg',
  cta: '/assets/figma-cta-arrow.svg',
  search: '/assets/figma-search-icon.svg',
  demo: '/assets/figma-demo-icon.svg',
  profile: '/assets/figma-profile-icon.svg',
  about: '/assets/figma-about-icon.svg'
})

const goTo = (path) => router.push(path)

const closeMobileMenu = () => {
  // The Figma mobile home is the navigation surface itself. "Close" reveals
  // the existing slide deck without changing the desktop sidebar behaviour.
  document.documentElement.classList.add('mobile-home-menu-closed')
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
        <span class="mobile-row-arrow" aria-hidden="true">
          <img :src="sidebarAssets.about" alt="" width="24" height="24" />
        </span>
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
        <span class="mobile-row-arrow" aria-hidden="true">
          <img :src="sidebarAssets.about" alt="" width="24" height="24" />
        </span>
      </div>
    </div>

    <div
      id="row-quiz"
      class="sidebar-row-card"
      role="button"
      tabindex="0"
      @click="goTo('/quiz')"
      @keydown.enter="goTo('/quiz')"
      @keydown.space.prevent="goTo('/quiz')"
    >
      <div class="row-left-content">
        <span class="tag-badge">~5 минут</span>
        <span class="row-text">
          <span class="desktop-sidebar-label">КВИЗ: Нужен ли вам тест на аллергены?</span>
          <span class="mobile-sidebar-label">Нужен ли вам тест на аллергены?</span>
        </span>
      </div>
      <span class="mobile-row-arrow" aria-hidden="true">
        <img :src="sidebarAssets.about" alt="" width="24" height="24" />
      </span>
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
      <span class="mobile-row-arrow" aria-hidden="true">
        <img :src="sidebarAssets.about" alt="" width="24" height="24" />
      </span>
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

    <button class="mobile-doctors-row" type="button" @click="goTo('/personal-account/doctor/login')">
      <img src="/assets/figma-doctors-icon.svg" alt="" width="24" height="24" />
      <span>Для врачей</span>
      <span class="mobile-row-arrow" aria-hidden="true">
        <img :src="sidebarAssets.about" alt="" width="24" height="24" />
      </span>
    </button>

    <button class="mobile-close-row" type="button" @click="closeMobileMenu">
      <span class="mobile-close-icon" aria-hidden="true"></span>
      <span>Закрыть</span>
    </button>
  </aside>
</template>
