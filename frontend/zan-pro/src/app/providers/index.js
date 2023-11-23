import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../../pages/ui/HomeView/home.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('')
    }
  ]
})

export default router
