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
      path: '/contact',
      name: 'contact',
      component: () => import('../../pages/ui/ContactView/contact.vue')
    },
    {
      path: '/employment',
      name: 'employment',
      component: () => import('../../pages/ui/EmploymentView/employment.vue')
    },
    {
      path: '/employment/:slug',
      name: 'employmentDetails',
      component: () => import('../../pages/ui/EmpDetailsView/empDetails.vue'),
      props: true,
    },
    {
      path: '/:pathMatch(.*)*',
      component: () => import('../../pages/ui/404ErrorView/error404.vue'),
    },
    {
      path: '/error500',
      component: () => import('../../pages/ui/500ErrorView/error500.vue'),
    }
  ]
})

export default router
