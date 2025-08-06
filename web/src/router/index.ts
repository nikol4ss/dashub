import { createRouter, createWebHistory } from 'vue-router'
import { jwtDecode } from 'jwt-decode'

import Login from '@/pages/auth/Login.vue'
import Signup from '@/pages/auth/Signup.vue'
import ResetPassword from '@/pages/auth/ResetPassword.vue'
import Central from '@/pages/layout/Central.vue'

const routes = [
  { path: '/login/', name: 'Login', component: Login, meta: { title: 'Dashub - Login' } },
  { path: '/signup/', name: 'Signup', component: Signup },
  { path: '/password_reset/confirm', name: 'ResetPassword', component: ResetPassword },
  { path: '/central/', name: 'Central', component: Central, meta: { requiresAuth: true } },
]

/**
 * Checks if a JWT token is valid.
 * - Verifies token existence and format.
 * - Decodes token safely.
 * - Checks expiration timestamp.
 *
 * @param token JWT string or null
 * @returns boolean indicating if token is valid and not expired
 */
function isTokenValid(token: string | null): boolean {
  if (!token || token === 'undefined' || token === 'null') return false

  try {
    const decoded = jwtDecode<{ exp: number }>(token)
    if (!decoded.exp) return false

    // Compare expiration with current timestamp (ms)
    return Date.now() < decoded.exp * 1000
  } catch {
    return false
  }
}

const router = createRouter({
  history: createWebHistory(),
  routes,
})

/**
 * Navigation guard to protect routes that require authentication.
 * - Redirects unauthenticated users to /login.
 * - Removes invalid or expired tokens.
 * - Prevents authenticated users from accessing /login.
 */
router.beforeEach((to, _from, next) => {
  const token = localStorage.getItem('access_token')

  if (!isTokenValid(token)) {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')

    if (to.meta.requiresAuth) return next('/login/')
    return next()
  }

  if (to.path === '/login/') return next('/central/')

  next()
})

export default router
