<script setup>
import { ref, computed, onMounted, onUnmounted, watch, nextTick } from 'vue'

// Modal states
const showDemoModal = ref(false)
const showSearchModal = ref(false)
const showQuizModal = ref(false)
const showRegisterModal = ref(false)

// Search State
const searchQuery = ref('')
const searchResult = ref(null)
const mockAllergens = [
  'Пыльца березы', 'Шерсть кошки', 'Шерсть собаки', 'Арахис', 
  'Молоко коровье', 'Яичный белок', 'Клещ домашней пыли', 
  'Пшеничная мука', 'Глютен', 'Полынь', 'Альфа-лактальбумин',
  'Креветки', 'Томаты', 'Шоколад', 'Пыльца ольхи', 'Яд осы'
]

const handleSearch = () => {
  if (!searchQuery.value.trim()) {
    searchResult.value = null
    return
  }
  const query = searchQuery.value.toLowerCase()
  const found = mockAllergens.filter(a => a.toLowerCase().includes(query))
  if (found.length > 0) {
    searchResult.value = {
      success: true,
      items: found
    }
  } else {
    searchResult.value = {
      success: false,
      message: 'Аллерген не найден в базе, но наш тест проверяет более 300 показателей. Скорее всего, он там есть!'
    }
  }
}

// Quiz State
const quizStep = ref(0) // 0: intro, 1-3: questions, 4: result
const quizAnswers = ref([])
const quizQuestions = [
  { text: 'Испытываете ли вы зуд, насморк или слезотечение без простуды?', category: 'symptoms' },
  { text: 'Бывают ли у вас высыпания на коже после еды или контакта с животными?', category: 'skin' },
  { text: 'Есть ли у ваших близких родственников подтвержденная аллергия?', category: 'heredity' }
]

const startQuiz = () => {
  quizStep.value = 1
  quizAnswers.value = []
}

const answerQuiz = (answer) => {
  quizAnswers.value.push(answer)
  if (quizStep.value < quizQuestions.length) {
    quizStep.value++
  } else {
    quizStep.value = 4 // show result
  }
}

const getQuizRecommendation = () => {
  const yesCount = quizAnswers.value.filter(a => a === 'yes').length
  if (yesCount === 3) {
    return 'У вас высокая вероятность аллергических реакций. Рекомендуем пройти полный многокомпонентный тест на 300+ аллергенов для точной диагностики.'
  } else if (yesCount >= 1) {
    return 'У вас наблюдаются некоторые признаки предрасположенности к аллергии. Рекомендуем проконсультироваться с аллергологом ALEX LAB и сдать направленный тест.'
  } else {
    return 'Симптомы аллергии минимальны. Однако, если вы хотите убедиться в безопасности для здоровья или планируете завести питомца, превентивный тест не будет лишним.'
  }
}

const resetQuiz = () => {
  quizStep.value = 0
  quizAnswers.value = []
}

// 21 Slides Definition (Extracted directly from Figma bridged mockup)
const currentSlideIndex = ref(0)
const scrollContainer = ref(null)

const videoA = ref(null)
const videoB = ref(null)
const activeVideoElement = ref('A') // 'A' or 'B'
let videoRequestId = 0
const isSlideTransitioning = ref(false)
const navigationMode = ref('scroll')
const videoBackgroundReady = ref(true)
const contentReadySlideIndex = ref(0)

const navigateToExternal = (url) => {
  window.location.href = url
}

const openCart = () => navigateTo('/cart')

const slides = ref([
  { id: 'slide-1',  label: '', title: 'Тест на аллергию ALEX² — один анализ, который даёт ответы', subtitle: '', direction: 'down', video: '/videos/scroll/forward/scr1.mp4',  reverseVideo: '/videos/scroll/reverse/scrr1.mp4' },
  { id: 'slide-2',  label: '', title: 'Почему ALEX2?', subtitle: '', direction: 'down', video: '/videos/scroll/forward/scr2.mp4',  reverseVideo: '/videos/scroll/reverse/scrr2.mp4' },
  
  // Advantages
  { id: 'slide-3',  step: '1', totalSteps: '5', label: 'Преимущества', title: 'Всё за один сеанс', subtitle: 'За одно исследование аллергочип проверяет реакцию организма сразу на 300 различных веществ: пыльцу деревьев и трав, домашнюю пыль, плесень, шерсть животных, продукты питания (молоко, яйца, орехи, рыбу, морепродукты, злаки, фрукты и овощи), а также яды пчёл и ос, латекс и многое другое.', direction: 'down', video: '/videos/scroll/forward/scr3.mp4',  reverseVideo: '/videos/scroll/reverse/scrr3-fixed.mp4' },
  { id: 'slide-4',  step: '2', totalSteps: '5', label: 'Преимущества', title: 'Точечный результат', subtitle: 'В природе многие растения и продукты содержат похожие белки. Из-за этого стандартные анализы нередко показывают «лишние» реакции — организм как будто реагирует на десятки всего, хотя настоящий виновник один. ALEX² отличает истинную аллергию от таких совпадений.', direction: 'right', video: '/videos/scroll/forward/scr4.mp4', reverseVideo: '/videos/scroll/reverse/scrr4.mp4' },
  { id: 'slide-5',  step: '3', totalSteps: '5', label: 'Преимущества', title: 'Отчёт и консультация', subtitle: 'Мы не бросаем человека с непонятными результатами — расшифруем и объясним человеческим языком.', direction: 'right', video: '/videos/scroll/forward/scr4-5.mp4', reverseVideo: '/videos/scroll/reverse/scrr4-5.mp4' },
  { id: 'slide-6',  step: '4', totalSteps: '5', label: 'Преимущества', title: 'Без диет и отмены лекарств', subtitle: 'Анализ можно сдавать на фоне приёма антигистаминных, гормонов и без голодания перед анализом. Специальной подготовки не нужно — достаточно не есть 3 часа до сдачи.', direction: 'right', video: '/videos/scroll/forward/scr5.mp4', reverseVideo: '/videos/scroll/reverse/scrr5.mp4' },
  { id: 'slide-7',  step: '5', totalSteps: '5', label: 'Преимущества', title: 'Подходит детям', subtitle: 'Тест можно сдавать с шести месяцев, а для анализа требуется совсем мало крови.', direction: 'right', video: '/videos/scroll/forward/scr6.mp4', reverseVideo: '/videos/scroll/reverse/scrr6.mp4' },
  
  // The short scr7 transition moves from the last advantage into the results intro.
  { id: 'slide-8',  label: 'О результатах', title: 'Что вы получите по итогам теста на аллергию', subtitle: '', direction: 'down', video: '/videos/scroll/forward/scr7.mp4', reverseVideo: '/videos/scroll/reverse/scrr7.mp4', holdVideo: true },
  
  // Results Steps
  { id: 'slide-9',  step: '1', totalSteps: '3', label: 'О результатах', title: 'Аллерго-паспорт', subtitle: 'Список из 300 аллергенов, которые будут разделены по группам и уровням опасности.', direction: 'down', video: '/videos/scroll/forward/scr8.mp4',  reverseVideo: '/videos/scroll/reverse/scrr8.mp4' },
  { id: 'slide-10', step: '2', totalSteps: '3', label: 'О результатах', title: 'Рекомендации по аллергенам', subtitle: 'Список из 300 аллергенов, которые будут разделены по группам и уровням опасности.', direction: 'right', video: '/videos/scroll/forward/scr9.mp4', reverseVideo: '/videos/scroll/reverse/scrr9.mp4' },
  { id: 'slide-11', step: '3', totalSteps: '3', label: 'О результатах', badge: 'Опционально', title: 'Консультация', subtitle: 'Список из 300 аллергенов, которые будут разделены по группам и уровням опасности.', direction: 'right', video: '/videos/scroll/forward/scr10.mp4', reverseVideo: '/videos/scroll/reverse/scrr10.mp4' },
  
  // Stories Intro
  { id: 'slide-12', label: 'Истории людей', title: 'Истории людей', subtitle: '', direction: 'down', video: '/videos/scroll/forward/scr11.mp4', reverseVideo: '/videos/scroll/reverse/scrr11.mp4' },
  
  // Stories Tabs
  { id: 'slide-13', label: 'Истории людей', type: 'story', activeTab: 'Misha',      direction: 'down',  video: '', reverseVideo: '', holdVideo: true },
  { id: 'slide-14', label: 'Истории людей', type: 'story', activeTab: 'Alexandra', direction: 'right', video: '/videos/scroll/forward/scr12.mp4', reverseVideo: '/videos/scroll/reverse/scrr12.mp4' },
  { id: 'slide-15', label: 'Истории людей', type: 'story', activeTab: 'Pasha',      direction: 'right', video: '/videos/scroll/forward/scr13.mp4', reverseVideo: '/videos/scroll/reverse/scrr13.mp4' },
  
  // FAQ
  { id: 'slide-16', label: 'FAQ', type: 'faq', title: 'FAQ', subtitle: '', direction: 'down', video: '/videos/scroll/forward/scr14.mp4', reverseVideo: '/videos/scroll/reverse/scrr14.mp4' },
  
  // Blog
  { id: 'slide-17', label: 'Блог про аллергию', type: 'blog', title: 'Блог про аллергию', subtitle: '', direction: 'down', video: '', reverseVideo: '' },
  
  // How to сдавать Steps
  { id: 'slide-18', step: '1', totalSteps: '3', label: 'Как сдать тест', title: 'Запишитесь на тест через наш сайт', subtitle: 'А если хотите получить дополнительно консультацию бесплатно — выберите сдачу теста в лабораториях ALEX', direction: 'down', video: '', reverseVideo: '' },
  { id: 'slide-19', step: '2', totalSteps: '3', label: 'Как сдать тест', title: 'Сдайте кровь в выбранной лаборатории', subtitle: 'Важно: За 4 часа до сдачи крови нужно не кушать. Кровь берут из вены.', direction: 'right', video: '', reverseVideo: '' },
  { id: 'slide-20', step: '3', totalSteps: '3', label: 'Как сдать тест', title: 'Отслеживайте результат в личном кабинете и на электронной почте', subtitle: 'В личном кабинете показываем статусы — туда же придёт результат. Дополнительно всё дублируем на почту.', direction: 'right', video: '', reverseVideo: '' },
  
  // Contacts
  { id: 'slide-21', label: 'Контакты', type: 'contacts', title: 'Контакты', subtitle: '', direction: 'down', video: '', reverseVideo: '' }
])

const getSlideClass = (index) => {
  if (index === currentSlideIndex.value) {
    return 'active'
  }
  if (index > currentSlideIndex.value) {
    const slide = slides.value[index]
    return slide.direction === 'right' ? 'future-right' : 'future-down'
  }
  if (index < currentSlideIndex.value) {
    const nextSlide = slides.value[index + 1]
    return nextSlide.direction === 'right' ? 'past-left' : 'past-up'
  }
  return ''
}

const navigateToSlideIndex = (index, mode = 'direct') => {
  const targetIndex = Math.max(0, Math.min(index, slides.value.length - 1))
  if (targetIndex === currentSlideIndex.value) return

  navigationMode.value = mode
  currentSlideIndex.value = targetIndex
}

const goToSlideById = (id) => {
  const idx = slides.value.findIndex(s => s.id === id)
  if (idx !== -1) navigateToSlideIndex(idx, 'direct')
}

const goToPersistentStep = (step) => {
  const group = persistentStepGroup.value
  if (!group) return

  const firstSlideIndex = group.type === 'advantages' ? 2 : 8
  navigateToSlideIndex(firstSlideIndex + step - 1, 'direct')
}

const menuItems = [
  { label: 'Преимущества', slideId: 'slide-3' },
  { label: 'О результатах', slideId: 'slide-9' },
  { label: 'Истории людей', slideId: 'slide-13' },
  { label: 'FAQ', slideId: 'slide-16' },
  { label: 'Блог про аллергию', slideId: 'slide-17' },
  { label: 'Как сдать тест', slideId: 'slide-18' }
]

const activeMenuIndex = computed(() => {
  const idx = currentSlideIndex.value
  if (idx >= 2 && idx <= 6) return 0 // Преимущества
  if (idx >= 7 && idx <= 10) return 1 // О результатах
  if (idx >= 11 && idx <= 14) return 2 // Истории людей
  if (idx === 15) return 3 // FAQ
  if (idx === 16) return 4 // Блог про аллергию
  if (idx >= 17 && idx <= 19) return 5 // Как сдать тест
  if (idx === 20) return 0 // Final Figma frame keeps the full list with the first item selected
  return -1
})

const showMenu = computed(() => {
  return activeMenuIndex.value !== -1
})

const showSmokeCloud = computed(() => {
  const idx = currentSlideIndex.value

  // Decorative layers enter together with the content. This prevents a cloud
  // from the destination section appearing over the previous video frame.
  return contentReadySlideIndex.value === idx
    && ((idx >= 2 && idx <= 10) || (idx >= 12 && idx <= 14))
})

const isResultsSection = computed(() => {
  const idx = currentSlideIndex.value
  return idx >= 7 && idx <= 10
})

const resultsCloudVariant = computed(() => {
  const idx = currentSlideIndex.value

  if (idx >= 8 && idx <= 10) return 'results-cloud-primary'
  return ''
})

const isStoriesSection = computed(() => {
  const idx = currentSlideIndex.value
  return idx >= 12 && idx <= 14
})

const storyCloudVariant = computed(() => {
  const variants = ['story-cloud-misha', 'story-cloud-alexandra', 'story-cloud-pasha']
  return variants[currentSlideIndex.value - 12] || ''
})

const persistentStepGroup = computed(() => {
  const idx = currentSlideIndex.value

  if (idx >= 2 && idx <= 6) {
    return { type: 'advantages', total: 5, current: idx - 1 }
  }

  if (idx >= 8 && idx <= 10) {
    return { type: 'results', total: 3, current: idx - 7 }
  }

  return null
})

const isVideoBackgroundVisible = computed(() => {
  const slide = slides.value[currentSlideIndex.value]
  return videoBackgroundReady.value && Boolean(slide?.video || slide?.holdVideo)
})

const CONTENT_EXIT_DURATION = 650
const CONTENT_REVEAL_PROGRESS = 0.25
const VIDEO_LAYER_CROSSFADE_DURATION = 160
const VIDEO_CONTAINER_FADE_DURATION = 450
const WHEEL_GESTURE_RESET_DURATION = 90
const RESULTS_INTRO_DURATION = 2000
const STORIES_INTRO_DURATION = 2000
let wheelGestureActive = false
let wheelGestureResetTimer = 0
let contentExitTimer = 0
let resultsIntroTimer = 0
let storiesIntroTimer = 0
let shouldAutoAdvanceStoriesIntro = false
let slideTransitionId = 0
let cancelEarlyContentReveal = () => {}
const exitingContentSlideIndex = ref(-1)

const revealSlideContent = (index) => {
  if (currentSlideIndex.value !== index) return

  contentReadySlideIndex.value = index

  if (index === 11 && shouldAutoAdvanceStoriesIntro) {
    window.clearTimeout(storiesIntroTimer)
    storiesIntroTimer = window.setTimeout(() => {
      if (currentSlideIndex.value !== 11 || contentReadySlideIndex.value !== 11) return
      shouldAutoAdvanceStoriesIntro = false
      animateOutgoingContent(11)

      storiesIntroTimer = window.setTimeout(() => {
        if (currentSlideIndex.value !== 11) return
        navigateToSlideIndex(12, 'auto')
      }, CONTENT_EXIT_DURATION)
    }, STORIES_INTRO_DURATION)
  }
}

const animateOutgoingContent = (index) => {
  window.clearTimeout(contentExitTimer)
  exitingContentSlideIndex.value = index
  contentExitTimer = window.setTimeout(() => {
    if (exitingContentSlideIndex.value === index) exitingContentSlideIndex.value = -1
  }, CONTENT_EXIT_DURATION)
}

const goNext = () => {
  if (isSlideTransitioning.value) return

  if (currentSlideIndex.value < slides.value.length - 1) {
    navigateToSlideIndex(currentSlideIndex.value + 1, 'scroll')
  }
}

const goPrev = () => {
  if (isSlideTransitioning.value) return

  if (currentSlideIndex.value > 0) {
    navigateToSlideIndex(currentSlideIndex.value - 1, 'scroll')
  }
}

const handleWheel = (e) => {
  e.preventDefault()
  window.clearTimeout(wheelGestureResetTimer)
  wheelGestureResetTimer = window.setTimeout(() => {
    wheelGestureActive = false
  }, WHEEL_GESTURE_RESET_DURATION)

  if (wheelGestureActive || Math.abs(e.deltaY) <= 30) return
  wheelGestureActive = true

  if (e.deltaY > 30) {
    goNext()
  } else if (e.deltaY < -30) {
    goPrev()
  }
}

const handleKeydown = (e) => {
  if (e.repeat) return

  switch (e.key) {
    case 'ArrowDown':
    case 'PageDown':
    case ' ':
      e.preventDefault()
      goNext()
      break
    case 'ArrowUp':
    case 'PageUp':
      e.preventDefault()
      goPrev()
      break
    case 'Home':
      e.preventDefault()
      navigateToSlideIndex(0, 'direct')
      break
    case 'End':
      e.preventDefault()
      navigateToSlideIndex(slides.value.length - 1, 'direct')
      break
  }
}

let touchStartY = 0
const handleTouchStart = (e) => {
  touchStartY = e.touches[0].clientY
}

const handleTouchEnd = (e) => {
  const touchEndY = e.changedTouches[0].clientY
  const diff = touchStartY - touchEndY

  if (Math.abs(diff) > 50) {
    if (diff > 0) goNext()
    else goPrev()
  }
}

const getStoryBefore = (tab) => {
  if (tab === 'Misha') {
    return [
      'Неуверенность в аллергии, вроде есть, а вроде и нет',
      'Боится выходить из дома',
      'При аллергии просто замирает в страхе'
    ]
  } else if (tab === 'Alexandra') {
    return [
      'Постоянный насморк без простуды весной и летом',
      'Не понимала, на какое именно растение реакция',
      'Горсти антигистаминных наугад'
    ]
  } else {
    return [
      'Пищевая аллергия',
      'Исключал почти все продукты, боясь приступов',
      'Постоянные ограничения и стресс при походах в рестораны'
    ]
  }
}

const getStoryAfter = (tab) => {
  if (tab === 'Misha') {
    return [
      'Точно знает, на что аллергия',
      'Знает, в какие конкретно недели пик цветения',
      'Пьёт конкретные таблетки'
    ]
  } else if (tab === 'Alexandra') {
    return [
      'Исключила из рациона яблоки и орехи (перекрестная реакция на березу)',
      'Подготовилась к сезону пыления заранее'
    ]
  } else {
    return [
      'Выявил точные белковые аллергены',
      'Понял, какие продукты безопасны при термообработке',
      'Вернул разнообразие в диету'
    ]
  }
}



const getAbsoluteVideoUrl = (src) => {
  if (!src || typeof window === 'undefined') return ''

  try {
    return new URL(src, window.location.origin).href
  } catch {
    return src
  }
}

const waitForAnimationFrames = (count = 1) => new Promise((resolve) => {
  const waitForNextFrame = () => {
    if (count <= 0) {
      resolve()
      return
    }

    count--
    requestAnimationFrame(waitForNextFrame)
  }

  waitForNextFrame()
})

const waitForVideoFrame = (video) => new Promise((resolve, reject) => {
  let settled = false
  let frameCallbackId = 0

  const cleanup = () => {
    window.clearTimeout(timeoutId)

    if (frameCallbackId && typeof video.cancelVideoFrameCallback === 'function') {
      video.cancelVideoFrameCallback(frameCallbackId)
    }
  }
  const finish = async () => {
    if (settled) return
    settled = true
    cleanup()
    // requestVideoFrameCallback fires when a decoded frame is submitted to the
    // compositor. Keep the current layer visible for two more paints so the new
    // texture is actually on screen before changing the layer order.
    await waitForAnimationFrames(2)
    resolve()
  }
  const timeoutId = window.setTimeout(() => {
    if (settled) return
    settled = true
    cleanup()
    reject(new Error('Timed out waiting for a decoded video frame'))
  }, 5000)

  if (typeof video.requestVideoFrameCallback === 'function') {
    frameCallbackId = video.requestVideoFrameCallback(finish)
    return
  }

  finish()
})

const waitUntilVideoCanPlay = (video) => new Promise((resolve, reject) => {
  if (video.readyState >= HTMLMediaElement.HAVE_CURRENT_DATA) {
    resolve()
    return
  }

  const onReady = () => {
    cleanup()
    resolve()
  }
  const onError = () => {
    cleanup()
    reject(video.error || new Error('Video loading failed'))
  }
  const cleanup = () => {
    window.clearTimeout(timeoutId)
    video.removeEventListener('loadeddata', onReady)
    video.removeEventListener('error', onError)
  }

  const timeoutId = window.setTimeout(() => {
    cleanup()
    reject(new Error('Video loading timed out'))
  }, 10000)

  video.addEventListener('loadeddata', onReady, { once: true })
  video.addEventListener('error', onError, { once: true })
})

const seekVideo = (video, time) => new Promise((resolve, reject) => {
  const targetTime = Math.max(0, Math.min(time, Number.isFinite(video.duration) ? video.duration : time))
  if (Math.abs(video.currentTime - targetTime) < 0.02) {
    resolve()
    return
  }

  let settled = false
  const finish = () => {
    if (settled) return
    settled = true
    window.clearTimeout(timeoutId)
    video.removeEventListener('seeked', finish)
    resolve()
  }
  const timeoutId = window.setTimeout(() => {
    if (settled) return
    settled = true
    video.removeEventListener('seeked', finish)
    reject(new Error('Video seek timed out'))
  }, 2500)
  video.addEventListener('seeked', finish, { once: true })
  video.currentTime = targetTime
})

const waitUntilVideoEnds = (video) => new Promise((resolve, reject) => {
  if (video.ended) {
    resolve()
    return
  }

  const cleanup = () => {
    window.clearTimeout(timeoutId)
    video.removeEventListener('ended', onEnded)
    video.removeEventListener('error', onError)
  }
  const onEnded = () => {
    cleanup()
    resolve()
  }
  const onError = () => {
    cleanup()
    reject(video.error || new Error('Video playback failed'))
  }
  const timeoutId = window.setTimeout(() => {
    cleanup()
    reject(new Error('Timed out waiting for the final video frame'))
  }, 1500)

  video.addEventListener('ended', onEnded, { once: true })
  video.addEventListener('error', onError, { once: true })
})

const configureVideoElement = (video) => {
  video.muted = true
  video.defaultMuted = true
  video.playsInline = true
  video.disablePictureInPicture = true
}

const revealContentAtVideoProgress = (video, slideIndex, requestId, reveal) => {
  cancelEarlyContentReveal()

  const duration = Number.isFinite(video.duration) ? video.duration : 0
  if (duration <= 0) {
    reveal()
    return
  }

  const targetTime = duration * CONTENT_REVEAL_PROGRESS
  let frameCallbackId = 0
  let fallbackTimer = 0
  let cancelled = false

  const cleanup = () => {
    window.clearTimeout(fallbackTimer)
    if (frameCallbackId && typeof video.cancelVideoFrameCallback === 'function') {
      video.cancelVideoFrameCallback(frameCallbackId)
    }
  }
  const checkProgress = (_now, metadata) => {
    if (cancelled || requestId !== videoRequestId || currentSlideIndex.value !== slideIndex) {
      cleanup()
      return
    }

    const mediaTime = metadata?.mediaTime ?? video.currentTime
    if (mediaTime >= targetTime || video.ended) {
      cleanup()
      reveal()
      return
    }

    if (typeof video.requestVideoFrameCallback === 'function') {
      frameCallbackId = video.requestVideoFrameCallback(checkProgress)
    } else {
      fallbackTimer = window.setTimeout(checkProgress, 50)
    }
  }

  cancelEarlyContentReveal = () => {
    cancelled = true
    cleanup()
  }
  checkProgress()
}

const preloadUpcomingVideo = () => {
  const inactiveEl = activeVideoElement.value === 'A' ? videoB.value : videoA.value
  if (!inactiveEl) return

  let nextSrc = ''

  // Keep the reverse clip for the current slide hot in the inactive layer.
  // This removes the decoding pause when a user scrolls back immediately.
  const currentSlide = slides.value[currentSlideIndex.value]
  if (currentSlideIndex.value > 0 && currentSlide?.reverseVideo) {
    nextSrc = currentSlide.reverseVideo
  } else {
    for (let index = currentSlideIndex.value + 1; index < slides.value.length; index++) {
      const nextSlide = slides.value[index]
      if (nextSlide.video) {
        nextSrc = nextSlide.video
        break
      }
      if (!nextSlide.holdVideo) break
    }
  }

  if (!nextSrc || inactiveEl.src === getAbsoluteVideoUrl(nextSrc)) return

  inactiveEl.pause()
  configureVideoElement(inactiveEl)
  inactiveEl.src = nextSrc
  inactiveEl.load()
}

const finishVideoLayerSwap = async (outgoingEl, requestId, { preload = false } = {}) => {
  // Keep the old frame untouched until the opacity crossfade is complete.
  // Reusing it earlier can flash the next preloaded clip on screen.
  await nextTick()
  await waitForAnimationFrames(2)
  await new Promise(resolve => window.setTimeout(resolve, VIDEO_LAYER_CROSSFADE_DURATION))

  if (requestId !== videoRequestId) return

  outgoingEl.pause()
  if (preload) preloadUpcomingVideo()
}

const getSlideBackgroundSource = (slideIndex) => {
  const slide = slides.value[slideIndex]
  if (!slide) return ''
  if (slide.video) return slide.video
  if (!slide.holdVideo) return ''

  for (let index = slideIndex - 1; index >= 0; index--) {
    if (slides.value[index]?.video) return slides.value[index].video
    if (!slides.value[index]?.holdVideo) break
  }

  return ''
}

const settleWithoutVideo = async (requestId) => {
  videoBackgroundReady.value = false
  videoA.value?.pause()
  videoB.value?.pause()
  await new Promise(resolve => window.setTimeout(resolve, VIDEO_CONTAINER_FADE_DURATION))
  if (requestId !== videoRequestId) return
}

const settleOnSlideFrame = async (src, requestId) => {
  if (!src || requestId !== videoRequestId) return

  const activeEl = activeVideoElement.value === 'A' ? videoA.value : videoB.value
  const stillEl = activeVideoElement.value === 'A' ? videoB.value : videoA.value
  if (!activeEl || !stillEl) return

  try {
    stillEl.pause()
    configureVideoElement(stillEl)

    if (stillEl.src !== getAbsoluteVideoUrl(src)) {
      stillEl.src = src
      stillEl.load()
    }

    await waitUntilVideoCanPlay(stillEl)
    if (requestId !== videoRequestId) return

    await seekVideo(stillEl, Math.max(0, stillEl.duration - (1 / 30)))
    if (requestId !== videoRequestId) return

    // A paused, fully covered video may be compositor-culled and never receive
    // requestVideoFrameCallback. Play its last frame underneath the current
    // opaque layer, then switch only after that frame has actually completed.
    const finalFrameReady = waitForVideoFrame(stillEl)
    const videoEnded = waitUntilVideoEnds(stillEl)
    await stillEl.play()
    await Promise.all([finalFrameReady, videoEnded])
    stillEl.pause()
    if (requestId !== videoRequestId) return

    videoBackgroundReady.value = true
    activeVideoElement.value = activeVideoElement.value === 'A' ? 'B' : 'A'
    await finishVideoLayerSwap(activeEl, requestId, { preload: true })
  } catch (error) {
    if (requestId === videoRequestId) {
      console.warn('Failed to settle destination video frame:', error)
      await settleWithoutVideo(requestId)
    }
  }
}

const playVideoShot = async (src, { playbackRate = 1, onPlaybackStarted, onComplete } = {}) => {
  if (!src) {
    onComplete?.()
    return
  }

  const requestId = ++videoRequestId
  const activeEl = activeVideoElement.value === 'A' ? videoA.value : videoB.value
  const incomingEl = activeVideoElement.value === 'A' ? videoB.value : videoA.value

  if (!activeEl || !incomingEl) {
    onComplete?.()
    return
  }

  const absoluteSrc = getAbsoluteVideoUrl(src)

  try {
    incomingEl.pause()
    configureVideoElement(incomingEl)

    if (incomingEl.src !== absoluteSrc) {
      incomingEl.src = src
      incomingEl.load()
    }

    await waitUntilVideoCanPlay(incomingEl)
    if (requestId !== videoRequestId) return

    await seekVideo(incomingEl, 0)
    if (requestId !== videoRequestId) return

    incomingEl.playbackRate = playbackRate
    await incomingEl.play()
    await waitForVideoFrame(incomingEl)
    if (requestId !== videoRequestId) return

    videoBackgroundReady.value = true
    activeVideoElement.value = activeVideoElement.value === 'A' ? 'B' : 'A'
    await finishVideoLayerSwap(activeEl, requestId, { preload: true })
    if (requestId !== videoRequestId) return

    onPlaybackStarted?.(incomingEl, requestId)

    const finishTransition = async () => {
      if (requestId !== videoRequestId) return
      await waitForAnimationFrames(2)
      if (requestId !== videoRequestId) return
      onComplete?.()
    }

    if (incomingEl.ended) finishTransition()
    else incomingEl.addEventListener('ended', finishTransition, { once: true })
  } catch (error) {
    if (requestId === videoRequestId) {
      console.warn('Failed to play next video shot:', error)
      const fallbackRequestId = ++videoRequestId
      await settleOnSlideFrame(src, fallbackRequestId)
      if (fallbackRequestId === videoRequestId) onComplete?.()
    }
  }
}

// Every numbered file is a transition into its slide. When moving back, play
// the matching reverse transition of the slide being left.
watch(currentSlideIndex, (newIndex, oldIndex) => {
  const transitionId = ++slideTransitionId
  const transitionStartedAt = performance.now()
  let transitionFinishing = false
  const slide = slides.value[newIndex]
  const oldSlide = slides.value[oldIndex]
  const goingBack = newIndex < oldIndex
  const isDirectJump = navigationMode.value === 'direct' && Math.abs(newIndex - oldIndex) > 1
  const destinationHasVideo = Boolean(slide?.video || slide?.holdVideo)
  const originHasVideo = Boolean(oldSlide?.video || oldSlide?.holdVideo)
  if (!destinationHasVideo || !originHasVideo) videoBackgroundReady.value = false
  isSlideTransitioning.value = true

  const isCurrentTransition = () => (
    transitionId === slideTransitionId
    && currentSlideIndex.value === newIndex
  )
  const waitForOutgoingContent = async () => {
    const remaining = CONTENT_EXIT_DURATION - (performance.now() - transitionStartedAt)
    if (remaining > 0) {
      await new Promise(resolve => window.setTimeout(resolve, remaining))
    }
  }
  const revealCurrentSlide = async () => {
    await waitForOutgoingContent()
    if (!isCurrentTransition()) return
    if (contentReadySlideIndex.value !== newIndex) revealSlideContent(newIndex)
    isSlideTransitioning.value = false
  }
  const finishCurrentTransition = async () => {
    if (transitionFinishing) return
    transitionFinishing = true
    await waitForOutgoingContent()
    if (!isCurrentTransition()) return
    await revealCurrentSlide()
  }
  const revealAtQuarter = (video, requestId) => {
    if (!isCurrentTransition()) return
    revealContentAtVideoProgress(video, newIndex, requestId, revealCurrentSlide)
  }

  cancelEarlyContentReveal()
  window.clearTimeout(resultsIntroTimer)
  window.clearTimeout(storiesIntroTimer)
  shouldAutoAdvanceStoriesIntro = newIndex === 11 && oldIndex === 10
  animateOutgoingContent(oldIndex)
  contentReadySlideIndex.value = -1

  if (newIndex === 7 && oldIndex === 6) {
    resultsIntroTimer = window.setTimeout(() => {
      if (!isCurrentTransition()) return
      navigateToSlideIndex(8, 'auto')
    }, RESULTS_INTRO_DURATION)
  }

  // A direct jump across several slides cannot use one adjacent reverse clip:
  // its final frame belongs to the wrong page. Play the destination animation
  // instead, or settle the exact held frame before revealing any content.
  if (isDirectJump) {
    if (slide.video) {
      playVideoShot(slide.video, {
        onPlaybackStarted: revealAtQuarter,
        onComplete: finishCurrentTransition
      })
    } else {
      const requestId = ++videoRequestId
      const backgroundSrc = getSlideBackgroundSource(newIndex)
      const settle = backgroundSrc
        ? settleOnSlideFrame(backgroundSrc, requestId)
        : settleWithoutVideo(requestId)
      settle.finally(finishCurrentTransition)
    }
    return
  }

  if (goingBack) {
    if (oldSlide?.reverseVideo) {
      playVideoShot(oldSlide.reverseVideo, {
        onComplete: finishCurrentTransition
      })
    } else {
      const requestId = ++videoRequestId
      const backgroundSrc = getSlideBackgroundSource(newIndex)
      const settle = backgroundSrc
        ? settleOnSlideFrame(backgroundSrc, requestId)
        : settleWithoutVideo(requestId)
      settle.finally(finishCurrentTransition)
    }
    return
  }

  if (slide.video) {
    playVideoShot(slide.video, {
      onPlaybackStarted: revealAtQuarter,
      onComplete: finishCurrentTransition
    })
  } else if (!slide.holdVideo) {
    const requestId = ++videoRequestId
    settleWithoutVideo(requestId).finally(finishCurrentTransition)
  } else {
    finishCurrentTransition()
  }
})

onMounted(() => {


  nextTick(() => {
    const container = scrollContainer.value
    if (!container) return

    container.addEventListener('wheel', handleWheel, { passive: false })
    container.addEventListener('touchstart', handleTouchStart, { passive: true })
    container.addEventListener('touchend', handleTouchEnd, { passive: true })
    window.addEventListener('keydown', handleKeydown)

    // Load initial video
    const slide = slides.value[currentSlideIndex.value]
    const initialSrc = slide ? slide.video : null
    if (initialSrc && videoA.value) {
      configureVideoElement(videoA.value)
      videoA.value.src = initialSrc
      videoA.value.load()
      videoA.value.play().catch(() => {})
      preloadUpcomingVideo()
    }
  })
})

onUnmounted(() => {
  const container = scrollContainer.value
  if (container) {
    container.removeEventListener('wheel', handleWheel)
    container.removeEventListener('touchstart', handleTouchStart)
    container.removeEventListener('touchend', handleTouchEnd)
  }
  window.removeEventListener('keydown', handleKeydown)

  if (videoA.value) videoA.value.pause()
  if (videoB.value) videoB.value.pause()
  window.clearTimeout(wheelGestureResetTimer)
  window.clearTimeout(contentExitTimer)
  cancelEarlyContentReveal()
  window.clearTimeout(resultsIntroTimer)
  window.clearTimeout(storiesIntroTimer)
  slideTransitionId++
  videoRequestId++
})
</script>

<template>
  <div class="page-container home-page-container site-sidebar-layout">
    <SiteSidebar
      @register="openCart"
      @about="goToSlideById('slide-1')"
    />

    <!-- Right Column: Content Container with Slide Deck -->
    <main class="content-container home-content" ref="scrollContainer">
      <Transition name="fade">
        <button
          v-if="currentSlideIndex === 0 && contentReadySlideIndex === 0"
          class="figma-doctors-button"
          type="button"
          disabled
        >
          <span>Для врачей</span>
          <img src="/assets/figma-doctors-icon.svg" alt="" />
        </button>
      </Transition>

      <!-- Persistent Right Menu overlay -->
      <div class="figma-right-menu" :class="{ visible: showMenu }">
        <div 
          v-for="(item, idx) in menuItems" 
          :key="item.label" 
          class="figma-menu-item"
          :class="{ active: idx === activeMenuIndex }"
          @click="goToSlideById(item.slideId)"
        >
          {{ item.label }}
        </div>
      </div>

      <!-- Fixed Video Background Layer -->
      <div
        class="video-bg-container"
        :class="{ 'no-video': !isVideoBackgroundVisible, 'story-video': isStoriesSection }"
        aria-hidden="true"
      >
        <video 
          ref="videoA" 
          class="bg-video" 
          :class="{ active: activeVideoElement === 'A' }"
          muted 
          playsinline 
          preload="auto"
        ></video>
        <video 
          ref="videoB" 
          class="bg-video" 
          :class="{ active: activeVideoElement === 'B' }"
          muted 
          playsinline 
          preload="auto"
        ></video>
        <div class="video-overlay"></div>
      </div>

      <!-- Static Smoke Cloud (Fixed, transitions opacity, does not slide) -->
      <div
        class="figma-smoke-cloud-fixed"
        :class="[
          {
            visible: showSmokeCloud,
            'results-cloud': isResultsSection,
            'story-cloud': isStoriesSection
          },
          resultsCloudVariant,
          storyCloudVariant
        ]"
      ></div>

      <!-- Persistent pagination stays mounted while text slides change -->
      <Transition name="persistent-steps">
        <div
          v-if="persistentStepGroup && contentReadySlideIndex === currentSlideIndex"
          class="persistent-step-indicator"
          :class="`persistent-step-indicator--${persistentStepGroup.type}`"
        >
          <button
            v-for="i in persistentStepGroup.total"
            :key="i"
            type="button"
            class="figma-step-circle"
            :class="{ active: i === persistentStepGroup.current }"
            :aria-label="`Перейти к шагу ${i}`"
            @click="goToPersistentStep(i)"
          >
            {{ i }}
          </button>
        </div>
      </Transition>

      <!-- Slides Deck -->
      <div class="slides-deck-container">
        <div
          v-for="(slide, index) in slides"
          :key="slide.id"
          class="slide-layer"
          :class="[getSlideClass(index), { 'content-exiting': index === exitingContentSlideIndex }]"
          :data-direction="slide.direction"
          :data-has-video="!!(slide.video || slide.holdVideo)"
          :data-content-ready="index === contentReadySlideIndex"
        >
          <!-- Slide 1: Hero -->
          <template v-if="slide.id === 'slide-1'">
            <div class="figma-scroll-icon">
              <img class="scroll-mouse" src="/assets/figma-mouse.svg" alt="" />
              <img class="scroll-chevron scroll-chevron-1" src="/assets/figma-scroll-chevron-1.svg" alt="" />
              <img class="scroll-chevron scroll-chevron-2" src="/assets/figma-scroll-chevron-2.svg" alt="" />
              <img class="scroll-chevron scroll-chevron-3" src="/assets/figma-scroll-chevron-3.svg" alt="" />
            </div>
            <h1 class="figma-hero-title">
              Тест на аллергию ALEX² — один анализ, который даёт ответы
            </h1>
          </template>

          <!-- Slide 2: Why ALEX2 Intro -->
          <template v-else-if="slide.id === 'slide-2'">
            <h2 id="slide-2-title" class="figma-intro-title white">
              Почему ALEX2?
            </h2>
          </template>

          <!-- Advantages detail slides (Slide 3 to 7) -->
          <template v-else-if="slide.label === 'Преимущества'">
            <div class="figma-content-wrapper">
              <div class="figma-step-block advantages-pos text-only">
                <!-- Text stack -->
                <div class="figma-step-text-stack">
                  <h2 class="figma-slide-title-inline">{{ slide.title }}</h2>
                  <p class="figma-slide-desc-inline">{{ slide.subtitle }}</p>
                </div>
              </div>
            </div>
          </template>

          <!-- Results Intro (Slide 8) -->
          <template v-else-if="slide.id === 'slide-8'">
            <h2 class="figma-intro-title">
              Что вы получите <br>по итогам теста на аллергию
            </h2>
          </template>

          <!-- Results Steps (Slide 9 to 11) -->
          <template v-else-if="slide.label === 'О результатах' && slide.step">
            <div class="figma-content-wrapper results-wrapper">
              <div class="figma-step-block results-pos text-only">
                <!-- Text stack -->
                <div class="figma-step-text-stack">
                  <div class="figma-result-title-row">
                    <h2 class="figma-slide-title-inline">{{ slide.title }}</h2>
                    <span v-if="slide.badge" class="figma-badge">{{ slide.badge }}</span>
                  </div>
                  <p class="figma-slide-desc-inline">{{ slide.subtitle }}</p>
                </div>
              </div>
            </div>
          </template>

          <!-- Stories Intro (Slide 12) -->
          <template v-else-if="slide.id === 'slide-12'">
            <h2 class="figma-intro-title">
              {{ slide.title }}
            </h2>
          </template>

          <!-- Stories Detail (Slide 13 to 15) -->
          <template v-else-if="slide.type === 'story'">
            <div class="figma-content-wrapper story-wrapper">
              <div class="figma-story-body">
                <!-- Tab Bar -->
                <div class="figma-story-tabs">
                  <button class="figma-tab-btn" :class="{ active: slide.activeTab === 'Misha' }" @click="goToSlideById('slide-13')">Миша</button>
                  <button class="figma-tab-btn" :class="{ active: slide.activeTab === 'Alexandra' }" @click="goToSlideById('slide-14')">Александра</button>
                  <button class="figma-tab-btn" :class="{ active: slide.activeTab === 'Pasha' }" @click="goToSlideById('slide-15')">Паша</button>
                </div>

                <!-- Stories Details content list -->
                <div class="figma-story-content">
                  <!-- After ALEX2 (Header & List) -->
                  <div class="story-block-after">
                    <h3 class="story-block-title green">После теста ALEX2</h3>
                    <ul class="story-bullets">
                      <li v-for="item in getStoryAfter(slide.activeTab)" :key="item">{{ item }}</li>
                    </ul>
                  </div>

                  <!-- Before (Header & List) -->
                  <div class="story-block-before">
                    <h3 class="story-block-title">До</h3>
                    <ul class="story-bullets gray">
                      <li v-for="item in getStoryBefore(slide.activeTab)" :key="item">{{ item }}</li>
                    </ul>
                  </div>
                </div>
              </div>

              <!-- Horizontal divider and Read More -->
              <div class="figma-story-footer">
                <div class="story-footer-divider"></div>
                <div class="story-read-more" @click="showDemoModal = true">
                  <span>Читать подробнее</span>
                  <img class="read-more-arrow" src="/assets/figma-story-read-more.svg" alt="" />
                </div>
              </div>
            </div>
          </template>

          <!-- Figma-exact FAQ, Blog and How-to frames (nodes 39:2029–39:2726) -->
          <template v-else-if="['slide-16', 'slide-17', 'slide-18', 'slide-19', 'slide-20'].includes(slide.id)">
            <FigmaInfoSlide
              :slide="slide"
              @action="showDemoModal = true"
              @navigate="goToSlideById"
            />
          </template>

          <!-- FAQ (Slide 16) -->
          <template v-else-if="slide.type === 'faq'">
            <div class="figma-content-wrapper faq-wrapper">
              <span class="figma-category-label">{{ slide.label }}</span>
              
              <div class="figma-faq-list">
                <div class="figma-faq-item">
                  <h4 class="figma-faq-q">Это больно?</h4>
                  <p class="figma-faq-a">Забор крови из вены производится тонкой иглой, процедура быстрая и практически безболезненная.</p>
                </div>
                <div class="figma-faq-item">
                  <h4 class="figma-faq-q">Сколько аллергенов в тесте?</h4>
                  <p class="figma-faq-a">Аллергочип ALEX2 проверяет более 300 аллергенов одновременно.</p>
                </div>
                <div class="figma-faq-item">
                  <h4 class="figma-faq-q">Через сколько будет результат?</h4>
                  <p class="figma-faq-a">Готовность — через 4–7 рабочих дней.</p>
                </div>
                <div class="figma-faq-item">
                  <h4 class="figma-faq-q">У вас есть сертификаты?</h4>
                  <p class="figma-faq-a">Да, тест ALEX2 сертифицирован и признан во всем мире.</p>
                </div>
              </div>
              
              <button class="figma-faq-all-btn" @click="showDemoModal = true">Все вопросы</button>
            </div>
          </template>

          <!-- Blog (Slide 17) -->
          <template v-else-if="slide.type === 'blog'">
            <div class="figma-content-wrapper blog-wrapper">
              <span class="figma-category-label">{{ slide.label }}</span>
              
              <div class="figma-blog-list">
                <!-- Blog Card 1 -->
                <div class="figma-blog-card">
                  <div class="blog-meta">~16 минут • Наука</div>
                  <h3 class="blog-title">Как сдать тест: подготовка и процесс</h3>
                  <div class="blog-author">
                    <p class="author-name">Александра Ковальчук</p>
                    <p class="author-title">Профессор МГУ</p>
                  </div>
                  <p class="blog-desc">Cursor представила модель Composer 2.5 — в тестах она сопоставима c Opus 4.7 и GPT-5.5, но стоит примерно в 10 раз дешевле </p>
                </div>

                <!-- Blog Card 2 -->
                <div class="figma-blog-card">
                  <div class="blog-meta">~16 минут • Наука</div>
                  <h3 class="blog-title">Как сдать тест: подготовка и процесс</h3>
                  <div class="blog-author">
                    <p class="author-name">Александра Ковальчук</p>
                    <p class="author-title">Профессор МГУ</p>
                  </div>
                  <p class="blog-desc">Cursor представила модель Composer 2.5 — в тестах она сопоставима c Opus 4.7 и GPT-5.5, но стоит примерно в 10 раз дешевле </p>
                </div>
              </div>

              <button class="figma-blog-all-btn" @click="showDemoModal = true">Все материалы</button>
            </div>
          </template>

          <!-- How to сдавать Steps (Slide 18 to 20) -->
          <template v-else-if="slide.label === 'Как сдать тест'">
            <div class="figma-content-wrapper howto-wrapper">
              <h2 class="figma-section-title">Как сдать тест: подготовка и процесс</h2>
              <div class="figma-step-block howto-pos">
                <!-- Step circles indicator -->
                <div class="figma-step-indicator">
                  <div 
                    v-for="i in 3" 
                    :key="i"
                    class="figma-step-circle"
                    :class="{ active: i === parseInt(slide.step) }"
                  >
                    {{ i }}
                  </div>
                </div>
                <!-- Text stack -->
                <div class="figma-step-text-stack">
                  <h2 class="figma-slide-title-inline">{{ slide.title }}</h2>
                  <p class="figma-slide-desc-inline">{{ slide.subtitle }}</p>
                </div>
              </div>
            </div>
          </template>

          <!-- Contacts (Slide 21) -->
          <template v-else-if="slide.type === 'contacts'">
            <FigmaContactsSlide
              @register="openCart"
              @quiz="showQuizModal = true; goToSlideById('slide-1')"
              @navigate="goToSlideById"
            />
          </template>
        </div>
      </div>
    </main>
  </div>

  <!-- ==========================================================================
       MODALS & OVERLAYS (Preserved from original)
       ========================================================================== -->

  <!-- Modal: Demo Results -->
  <Transition name="fade">
    <div class="modal-overlay" v-if="showDemoModal" @click.self="showDemoModal = false">
      <div class="modal-card">
        <button class="modal-close-btn" @click="showDemoModal = false">&times;</button>
        <h3 class="modal-title">Пример результатов теста</h3>
        <p class="modal-desc">Здесь показано, как выглядит расшифровка теста на 300+ аллергенов на понятном языке.</p>
        
        <div class="demo-results-list">
          <div class="demo-result-item high">
            <span class="allergen-name">Пыльца березы (t3)</span>
            <span class="allergen-level">Высокий уровень (45.2 kU/l)</span>
            <div class="level-bar"><div class="fill" style="width: 90%; background: #ff4d4f;"></div></div>
          </div>
          <div class="demo-result-item medium">
            <span class="allergen-name">Шерсть кошки (e1)</span>
            <span class="allergen-level">Средний уровень (12.4 kU/l)</span>
            <div class="level-bar"><div class="fill" style="width: 50%; background: #faad14;"></div></div>
          </div>
          <div class="demo-result-item low">
            <span class="allergen-name">Арахис (f13)</span>
            <span class="allergen-level">Следовые реакции (0.2 kU/l)</span>
            <div class="level-bar"><div class="fill" style="width: 5%; background: #52c41a;"></div></div>
          </div>
        </div>
        <p style="font-size: 14px; color: #666; margin-top: 15px; line-height: 1.4;">
          * Полный отчет включает рекомендации аллерголога, разбор перекрестных реакций и карту диеты.
        </p>
      </div>
    </div>
  </Transition>

  <!-- Modal: Search Allergens -->
  <Transition name="fade">
    <div class="modal-overlay" v-if="showSearchModal" @click.self="showSearchModal = false">
      <div class="modal-card">
        <button class="modal-close-btn" @click="showSearchModal = false">&times;</button>
        <h3 class="modal-title">Проверить аллерген</h3>
        <p class="modal-desc">Введите название продукта, растения или животного, чтобы узнать, входит ли он в наш тест.</p>
        
        <div style="display: flex; gap: 10px; margin-top: 15px; margin-bottom: 15px;">
          <input 
            type="text" 
            v-model="searchQuery" 
            @input="handleSearch"
            placeholder="Например: береза, кошка, яйцо" 
            style="flex: 1; padding: 12px 16px; border: 1px solid #dfdfdf; border-radius: 8px; font-size: 16px; outline: none;"
          />
        </div>

        <div v-if="searchResult" class="search-results-box">
          <div v-if="searchResult.success" style="color: #52c41a; font-weight: 500;">
            <p style="margin-bottom: 8px;">✓ Да, эти показатели проверяются в тесте:</p>
            <ul style="list-style: inside; color: #333; font-weight: normal; margin-left: 10px;">
              <li v-for="item in searchResult.items" :key="item">{{ item }}</li>
            </ul>
          </div>
          <div v-else style="color: #ff4d4f;">
            {{ searchResult.message }}
          </div>
        </div>
        <div v-else style="color: #999; font-size: 14px; text-align: center; padding: 10px 0;">
          Начните вводить название...
        </div>
      </div>
    </div>
  </Transition>

  <!-- Modal: Interactive Quiz -->
  <Transition name="fade">
    <div class="modal-overlay" v-if="showQuizModal" @click.self="showQuizModal = false">
      <div class="modal-card">
        <button class="modal-close-btn" @click="showQuizModal = false">&times;</button>
        <h3 class="modal-title">Нужен ли вам тест?</h3>
        
        <!-- Quiz Steps -->
        <div v-if="quizStep === 0" style="text-align: center; padding: 15px 0;">
          <p class="modal-desc">Ответьте на 3 простых вопроса, чтобы узнать, рекомендуется ли вам обследование на аллергены.</p>
          <button @click="startQuiz" class="quiz-btn-primary" style="margin-top: 15px;">Начать квиз</button>
        </div>

        <div v-else-if="quizStep >= 1 && quizStep <= 3" style="padding: 15px 0;">
          <div style="font-size: 14px; color: #999; margin-bottom: 10px;">Вопрос {{ quizStep }} из 3</div>
          <p style="font-size: 18px; font-weight: 500; line-height: 1.4; margin-bottom: 20px;">
            {{ quizQuestions[quizStep - 1].text }}
          </p>
          <div style="display: flex; gap: 12px;">
            <button @click="answerQuiz('yes')" class="quiz-btn-choice">Да</button>
            <button @click="answerQuiz('no')" class="quiz-btn-choice outline">Нет</button>
          </div>
        </div>

        <div v-else-if="quizStep === 4" style="text-align: center; padding: 15px 0;">
          <h4 style="font-size: 20px; font-weight: bold; color: #52c41a; margin-bottom: 15px;">Результат квиза</h4>
          <p style="font-size: 16px; line-height: 1.6; color: #333; margin-bottom: 20px;">
            {{ getQuizRecommendation() }}
          </p>
          <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 15px;">
            <button @click="showQuizModal = false; showDemoModal = true" class="quiz-btn-primary">Посмотреть демо-отчет</button>
            <div style="display: flex; gap: 12px;">
              <button @click="resetQuiz" class="quiz-btn-choice outline" style="flex: 1;">Пройти заново</button>
              <button @click="showQuizModal = false; openCart()" class="quiz-btn-choice" style="flex: 1;">Записаться на тест</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Transition>

  <!-- Modal: Registration -->
  <Transition name="fade">
    <div class="modal-overlay" v-if="showRegisterModal" @click.self="showRegisterModal = false">
      <div class="modal-card">
        <button class="modal-close-btn" @click="showRegisterModal = false">&times;</button>
        <h3 class="modal-title">Запись на тест</h3>
        <p class="modal-desc">Оставьте ваши контакты, администратор ALEX LAB свяжется с вами для подбора даты забора крови.</p>
        
        <form @submit.prevent="alert('Заявка успешно отправлена! Наш администратор свяжется с вами в течение 15 минут.'); showRegisterModal = false" style="display: flex; flex-direction: column; gap: 16px; margin-top: 15px;">
          <div style="display: flex; flex-direction: column; gap: 6px;">
            <label style="font-size: 14px; font-weight: 500; color: #666;">Ваше имя</label>
            <input type="text" required placeholder="Иван Иванов" style="padding: 12px; border: 1px solid #dfdfdf; border-radius: 8px; font-size: 16px;" />
          </div>
          <div style="display: flex; flex-direction: column; gap: 6px;">
            <label style="font-size: 14px; font-weight: 500; color: #666;">Номер телефона</label>
            <input type="tel" required placeholder="+7 (999) 999-99-99" style="padding: 12px; border: 1px solid #dfdfdf; border-radius: 8px; font-size: 16px;" />
          </div>
          <button type="submit" class="quiz-btn-primary" style="margin-top: 10px;">Отправить заявку</button>
        </form>
      </div>
    </div>
  </Transition>
</template>

<style scoped>
/* Modal and Interactive Component Styles scoped here to avoid cluttering main.css */

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-card {
  background: white;
  border-radius: 20px;
  width: 90%;
  max-width: 500px;
  padding: 32px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.15);
  position: relative;
  border: 1px solid #f0f0f0;
}

.modal-close-btn {
  position: absolute;
  top: 20px;
  right: 24px;
  background: transparent;
  border: none;
  font-size: 28px;
  cursor: pointer;
  color: #999;
  transition: color 0.2s ease;
}

.modal-close-btn:hover {
  color: #333;
}

.modal-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 12px;
}

.modal-desc {
  font-size: 16px;
  color: #666;
  line-height: 1.5;
  margin-bottom: 16px;
}

/* Demo results graphic inside modal */
.demo-results-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 20px;
}

.demo-result-item {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.allergen-name {
  font-weight: bold;
  font-size: 16px;
}

.allergen-level {
  font-size: 14px;
  color: #666;
}

.level-bar {
  width: 100%;
  height: 8px;
  background: #f0f0f0;
  border-radius: 4px;
  overflow: hidden;
}

.level-bar .fill {
  height: 100%;
  border-radius: 4px;
  transition: width 1s ease;
}

/* Search Box style */
.search-results-box {
  background: #f9f9f9;
  border: 1px dashed #dfdfdf;
  border-radius: 8px;
  padding: 16px;
  margin-top: 15px;
  font-size: 15px;
  line-height: 1.5;
}

/* Quiz button styles */
.quiz-btn-primary {
  width: 100%;
  background: black;
  color: white;
  border: 1px solid black;
  padding: 14px;
  font-size: 16px;
  font-weight: 500;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.quiz-btn-primary:hover {
  background: #333;
  border-color: #333;
}

.quiz-btn-choice {
  flex: 1;
  padding: 12px;
  font-size: 16px;
  font-weight: 500;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
  background: black;
  color: white;
  border: 1px solid black;
  text-align: center;
}

.quiz-btn-choice:hover {
  background: #333;
  border-color: #333;
}

.quiz-btn-choice.outline {
  background: transparent;
  color: black;
  border: 1px solid black;
}

.quiz-btn-choice.outline:hover {
  background: #f5f5f5;
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
</style>
