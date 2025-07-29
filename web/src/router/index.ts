import { createRouter, createWebHistory } from 'vue-router'
import { jwtDecode } from 'jwt-decode'

import Login from '@/pages/auth/Login.vue'
import Signup from '@/pages/auth/Signup.vue'
import MainLayout from '@/pages/layout/MainLayout.vue'

const routes = [
  { path: '/login/', name: 'Login', component: Login, meta: { title: 'Dashub - Login' } },
  { path: '/signup/', name: 'Signup', component: Signup },
  { path: '/dashboard/', name: 'Dashboard', component: MainLayout, meta: { requiresAuth: true } }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, _from, next) => {
  const token = localStorage.getItem('access_token')

  if (to.path === '/login/' && token) {
    return next('/dashboard/')
  }

  if (to.meta.requiresAuth) {
    if (!token) return next('/login/')

    try {
      const decoded = jwtDecode<{ exp: number }>(token)
      if (Date.now() >= decoded.exp * 1000) {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        return next('/login/')
      }
    } catch {
      return next('/login/')
    }
  }

  next()
})

export default router
