<script setup>
// Composition API setup
</script>

<template>
  <div class="page-wrapper">
    <div class="content-container">
      
      <!-- Text Group (Frame 36) -->
      <div class="text-group">
        <h1 class="error-title">Ошибка 404</h1>
        <p class="error-subtitle">Вы попали на сайт ALEX2, но мы не смогли найти именно то, что вы искали</p>
      </div>

      <!-- Menu Items (Frame 40) -->
      <div class="menu-group">
        
        <!-- Button 1: Вернуться на главную (Black with backdrop blur) -->
        <NuxtLink to="/" class="menu-item menu-item-black">
          <span>Вернуться на главную</span>
          <svg class="item-icon-svg white" viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10" />
            <path d="M10 8l4 4-4 4" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </NuxtLink>

        <!-- Button 2: Блог (White) -->
        <NuxtLink to="/blog" class="menu-item menu-item-white">
          <span>Блог</span>
          <svg class="item-icon-svg black" viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10" />
            <path d="M10 8l4 4-4 4" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </NuxtLink>

        <!-- Button 3: Личный кабинет (White) -->
        <NuxtLink to="/personal-account" class="menu-item menu-item-white">
          <span>Личный кабинет</span>
          <svg class="item-icon-svg black" viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10" />
            <path d="M10 8l4 4-4 4" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </NuxtLink>

        <!-- Button 4: Корзина (White) -->
        <NuxtLink to="/cart" class="menu-item menu-item-white">
          <span>Корзина</span>
          <svg class="item-icon-svg black" viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10" />
            <path d="M10 8l4 4-4 4" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </NuxtLink>

      </div>

    </div>
  </div>
</template>

<style scoped>
:root {
  --color-white: #ffffff;
  --color-black: #000000;
  --color-border: #dfdfdf;
  --color-overlay: rgba(0, 0, 0, 0.4);
  --transition-speed: 0.25s;
}

/* Page Container */
.page-wrapper {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: url('/assets/bg-404.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  padding: 24px;
  font-family: 'Roboto', sans-serif;
}

/* Dark Overlay */
.page-wrapper::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: var(--color-overlay, rgba(0, 0, 0, 0.4));
  z-index: 1;
}

/* Content Container (Frame 37) */
.content-container {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 64px;
  width: 100%;
  max-width: 414px;
  text-align: center;
}

/* Text Group (Frame 36) */
.text-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  color: var(--color-white, #ffffff);
  width: 100%;
}

.error-title {
  font-size: 42px;
  font-weight: 400;
  line-height: 1.16;
}

.error-subtitle {
  font-size: 21px;
  font-weight: 400;
  line-height: 1.33;
  max-width: 400px;
}

/* Menu Group (Frame 40) */
.menu-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%;
}

/* Menu Item Link */
.menu-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 72px;
  padding: 0 24px;
  text-decoration: none;
  font-size: 21px;
  font-weight: 400;
  transition: background-color var(--transition-speed, 0.25s) ease, border-color var(--transition-speed, 0.25s) ease, transform 0.15s ease;
  user-select: none;
}

.menu-item:active {
  transform: scale(0.98);
}

/* Black Button (Вернуться на главную) */
.menu-item-black {
  background-color: var(--color-black, #000000);
  color: var(--color-white, #ffffff);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
}

.menu-item-black:hover {
  background-color: #222222;
}

/* White Buttons (Блог, Личный кабинет, Корзина) */
.menu-item-white {
  background-color: var(--color-white, #ffffff);
  color: var(--color-black, #000000);
  border: 1px solid var(--color-border, #dfdfdf);
}

.menu-item-white:hover {
  background-color: #f5f5f5;
  border-color: #cccccc;
}

/* SVG Inline Icon */
.item-icon-svg {
  width: 24px;
  height: 24px;
  stroke-width: 2px;
  fill: none;
}

.item-icon-svg.white {
  stroke: var(--color-white, #ffffff);
}

.item-icon-svg.black {
  stroke: var(--color-black, #000000);
}

/* Responsive / Mobile View (Viewport <= 767px) */
@media (max-width: 767px) {
  .content-container {
    max-width: 388px;
  }

  .error-subtitle {
    font-size: 20px;
    line-height: 1.25;
  }

  .menu-group {
    gap: 0;
  }

  .menu-item {
    height: 66px;
    padding: 0 24px;
    font-size: 18px;
  }

  /* White items border adjustment for stacked layout */
  .menu-item-white {
    border-top: none;
    border-left: 1px solid var(--color-border, #dfdfdf);
    border-right: 1px solid var(--color-border, #dfdfdf);
    border-bottom: 1px solid var(--color-border, #dfdfdf);
  }

  /* Restoring top border for the first white item if it follows the black item */
  .menu-item-black + .menu-item-white {
    border-top: 1px solid var(--color-border, #dfdfdf);
  }
}
</style>
