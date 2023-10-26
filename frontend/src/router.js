import { createRouter, createWebHistory } from 'vue-router'
import { session } from './data/session'
import { users } from './data/users'
import { getScrollContainer, scrollTo } from './utils/scrollContainer'

let defaultRoute = window.default_route
if (defaultRoute?.includes('{{')) {
  defaultRoute = '/'
}

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/pages/Login.vue'),
  },
  {
    path: '/project',
    name: 'Project',
    component: () => import('@/pages/Project.vue'),
  },
  {
    path: '/project_detail/:id',
    name: 'ProjectDetail',
    component: () => import('@/pages/ProjectDetail.vue'),
  },
  {
    path: '/stage_detail/:id',
    name: 'StageDetail',
    component: () => import('@/pages/StageDetail.vue'),
  },
  {
    path: '/property_detail/:id',
    name: 'PropertyDetail',
    component: () => import('@/pages/PropertyDetail.vue'),
  },
  {
    path: '/my_reservation/:id',
    name: 'MyReservation',
    component: () => import('@/pages/MyReservation.vue'),
  },
  {
    path: '/eoi_detail/',
    name: 'EoiDetail',
    component: () => import('@/pages/EoiDetail.vue'),
  },
  {
    path: '/eoi_edit/',
    name: 'EOIedit',
    component: () => import('@/pages/EoiEdit.vue'),
  },
  {
    path: '/priority_stock/',
    name: 'PriorityStock',
    component: () => import('@/pages/PriorityStock.vue'),
  },
  {
    path: '/my_allocation/',
    name: 'MyAllocation',
    component: () => import('@/pages/MyAllocation.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/s'),  // Route change to salesportal
  routes,
})


let scrollPositions = {}
function saveAndRestoreScrollPosition(to, from) {
  let scrollContainer = getScrollContainer()
  if (scrollContainer) {
    scrollPositions[from.path] = scrollContainer.scrollTop
  }
  if (scrollPositions[to.path] !== undefined && to.path !== from.path) {
    setTimeout(() => {
      scrollTo({ top: scrollPositions[to.path] })
    }, 0)
  }
}

router.beforeEach(async (to, from, next) => {
  saveAndRestoreScrollPosition(to, from)
  let isLoggedIn = session.isLoggedIn
  try {
    await users.promise
  } catch (error) {
    isLoggedIn = false
  }

  if (to.name === 'Login' && isLoggedIn) {
    next({ name: 'Home' })
  } else if (to.name !== 'Login' && !isLoggedIn) {
    next({ name: 'Login' })
  } else {
    next()
  }
})


export default router
