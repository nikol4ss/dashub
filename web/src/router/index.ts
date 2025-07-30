import { createRouter, createWebHistory } from 'vue-router'
import { jwtDecode } from 'jwt-decode'

import Login from '@/pages/auth/Login.vue'
import Signup from '@/pages/auth/Signup.vue'
import MainLayout from '@/pages/layout/MainLayout.vue'

const routes = [
  { path: '/login/', name: 'Login', component: Login, meta: { title: 'Dashub - Login' } },
  { path: '/signup/', name: 'Signup', component: Signup },
  { path: '/central/', name: 'Central', component: MainLayout, meta: { requiresAuth: true } }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})
/**
 * Vue Router navigation guard to protect routes requiring authentication.
 *
 * Workflow:
 * :Checks if JWT token exists and is valid in localStorage.
 * :If token is missing or invalid, redirects to /login.
 * :Decodes token safely; if decoding fails, clears tokens and redirects.
 * :Checks token expiration; if expired, clears tokens and redirects.
 * :Prevents authenticated users from accessing /login by redirecting to /central.
 * :Allows navigation if authenticated and route is permitted.
 *
 * @param {import('vue-router').RouteLocationNormalized} to - Target route object
 * @param {import('vue-router').RouteLocationNormalized} _from - Current route (unused)
 * @param {(path?: string) => void} next - Function to resolve navigation
 */
router.beforeEach((to, _from, next) => {
  const token = localStorage.getItem('access_token')

  if (!token || token === 'undefined' || token === 'null') {
    if (to.meta.requiresAuth) return next('/login/')
    return next()
  }

  let decoded: { exp?: number } | null = null

  try {
    decoded = jwtDecode<{ exp: number }>(token)
    
  } catch {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    return next('/login/')
  }

  if (!decoded.exp || Date.now() >= decoded.exp * 1000) {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    return next('/login/')
  }

  if (to.path === '/login/') {
    return next('/central/')
  }

  return next()
})

export default router
