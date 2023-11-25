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
      path: '/employment',
      name: 'employment',
      component: () => import('../../pages/ui/EmploymentView/employment.vue')
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import('../../pages/ui/ContactView/contact.vue')

    }
  ]
})

export default router
