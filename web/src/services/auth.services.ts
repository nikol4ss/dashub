import api from './api'
import router from '@/router'

import type { SignupForm, LoginForm, ResetPassword, ResetConfirm } from '@/models/auth.model'

import { toastError } from '@/lib/utils'
import { toast } from 'vue-sonner'
import { toRaw } from 'vue'


/**
 * Logs in the user by sending credentials to the backend.
 * - Posts login data to 'token/' endpoint.
 * - Stores access and refresh tokens in localStorage.
 * - Redirects to '/central/' on success.
 * - Displays backend validation errors via toast on failure.
 *
 * @param form LoginForm object with username and password.
 * @returns Promise resolving to navigation or void.
 */
export async function postLogin(form: LoginForm) {
  try {
    const { data } = await api.post('token/', toRaw(form))
    const { access, refresh } = data

    localStorage.setItem('access_token', access)
    localStorage.setItem('refresh_token', refresh)

    return router.push('/central/')
  } catch (err: any) {
    toastError(err)
  }
}

/**
 * Registers a new user.
 * - Sends signup form data to 'signup/' endpoint.
 * - Redirects to '/login/' on success.
 * - Shows validation errors from backend as toasts.
 *
 * @param form SignupForm object with user details.
 * @returns Promise resolving to navigation or void.
 */
export async function formSignup(form: SignupForm) {
  try {
    await api.post('signup/', toRaw(form))
    router.push('/login/')
  } catch (err: any) {
    toastError(err)
  }
}

/**
 * Initiates password reset process.
 * - Sends reset password form data to 'password_reset/' endpoint.
 * - Shows success toast on email sent.
 * - Displays backend errors as toasts on failure.
 *
 * @param form ResetPassword object with user email.
 * @throws Re-throws error after displaying messages.
 */
export async function postResetPassword(form: ResetPassword) {
  try {
    await api.post('password_reset/', toRaw(form))
    toast.success('Email sent to your mailbox')
  } catch (err: any) {
    toastError(err)
  }
}

/**
 * Confirms password reset with token and new password.
 * - Sends form data to 'password_reset/confirm/' endpoint.
 * - Redirects to '/login/' on success.
 * - Displays errors from backend as toasts.
 *
 * @param form ResetConfirm object with password and token.
 * @throws Re-throws error after displaying messages.
 */
export async function postResetConfirm(form: ResetConfirm) {
  try {
    await api.post('password_reset/confirm/', toRaw(form))
    router.push('/login/')
  } catch (err: any) {
    toastError(err)
  }
}

/**
 * Fetches data from the `central/` endpoint using the JWT access token.
 *
 * :Reads the access token from localStorage
 * :Sends a GET request with the Bearer token in the Authorization header
 * :LIf a new access token is returned, updates localStorage
 * :Displays a success toast with the `value` from the response
 * :On error, shows an error toast and rethrows the error
 *
 * @returns Response data from the backend
 * @throws Error if token is missing or the request fails
 */
export async function getCentral() {
  try {
    const token = localStorage.getItem('access_token')
    if (!token) throw new Error('No access token')

    const response = await api.get("central/", {
      headers: { Authorization: `Bearer ${token}` }
    })

    if (response.data?.access) {
      localStorage.setItem('access_token', response.data.access)
    }

    return response.data

  } catch(err: any) {
    toastError(err)
    throw err
  }
}


/**
 * Logs out the user.
 * - Removes tokens from localStorage.
 * - Redirects to login page.
 */
export function logout() {
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  router.push('/login/')
}
