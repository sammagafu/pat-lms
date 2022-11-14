import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BaseView from '@/views/BaseView.vue'
import BaseViewAdmin from '@/views/BaseViewAdmin.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '',
      component: BaseViewAdmin,
      name:'views',
      children : [
        {
          path : '',
          name : 'home',
          component : HomeView
        },
        {
          path:'/courses/',
          children : [
            {
              path:'',
              name:'course-list',
              component : () => import('@/views/courses/CourseList.vue')
            },
            {
              path:'mycourses',
              name:'my-course-list',
              component : () => import('@/views/courses/TuitorsCourse.vue')
            },
            {
              path:'mycourses/:slug',
              name:'my-course-detail',
              component : () => import('@/views/courses/TuitorsCourseDetail.vue')
            },
            {
              path:'create',
              name:'course-create',
              component : () => import('@/views/courses/CourseCreate.vue')
            },
          ]
        },
      ]
    },
    {
      path: '/account/',
      component : BaseView,
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
    },
  
  ]
})

export default router
