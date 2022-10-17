import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/account/',
      name: 'account',
      children : [
        {
          path:'login',
          name: 'login',
          component: () => import('../views/Login.vue')
        },
        {
          path:'register',
          name: 'register',
          component: () => import('../views/Register.vue')
        },
      ],
      // 
    }
  ]
})

export default router
