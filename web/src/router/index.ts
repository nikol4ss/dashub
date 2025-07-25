import { createRouter, createWebHistory } from 'vue-router'

import Login from '@/pages/auth/Login.vue'
import Signup from '@/pages/auth/Signup.vue'

const routes = [
  { path: '/login/', name: 'Login', component: Login, meta: { title: 'Dashub - Login' },},
  { path: '/signup/', name: 'Signup', component: Signup },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
