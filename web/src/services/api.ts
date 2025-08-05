import api from '@/lib/utils'
import router from "@/router";

import type { SignupForm, LoginForm, ResetPassword, ResetConfirm, DBconnection } from '@/models';

import { toast } from 'vue-sonner'
import { toRaw } from 'vue'


/**
 * Handles user login and JWT authentication.
 *
 * :Sends login credentials to the backend (`token/` endpoint)
 * :Stores the access and refresh tokens in localStorage
 * :Redirects to `/central/` on successful authentication
 * :Displays backend validation errors via toast on failure
 *
 * @param form Object containing the login form data
 * @returns Promise<void> Redirects on success or shows error messages
 */
export async function postLogin(form: LoginForm) {
  try {
    const { data } = await api.post('token/', toRaw(form))
    const { access, refresh } = data

    localStorage.setItem('access_token', access)
    localStorage.setItem('refresh_token', refresh)

    return router.push('/central/')

  } catch (err: any) {
    const data = err.response?.data

    if (data && typeof data === 'object') {
      Object.entries(data).forEach(([_, messages]) => {
        if (Array.isArray(messages)) {
          messages.forEach(msg => toast.error(msg))
        } else {
          toast.warning(String(messages))
        }
      })
    } else {
      toast.error(err.message || 'Error')
    }
  }
}

/**
 * Sends user signup data to the backend and handles response.
 *
 * :Submits the form to the `signup/` endpoint
 * :On success, redirects to the login page (`/login/`)
 * :On error, displays validation messages returned by the backend
 *
 * @param form Object containing the signup form data
 * @returns Promise<void> Redirects on success or displays error toasts
 */
export async function formSignup(form: SignupForm) {
  try {
    await api.post('signup/', toRaw(form))
    router.push('/login/')

  } catch (err: any) {
    const data = err.response?.data

    if (data && typeof data === 'object') {
      Object.entries(data).forEach(([_, messages]) => {
        (messages as string[]).forEach(msg => {
          toast.warning(String(msg))
        })
      })
    } else {
      toast.error(err)
    }
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
    toast.error(err.message || 'Error retrieving data from the control panel')
    throw err
  }
}

/**
 * Sends a POST request to `password_reset/` with form data to initiate password reset.
 *
 * :On success, shows a toast indicating the reset email was sent.
 * :On failure, shows error messages from API response or a generic error toast.
 * :Throws the error after displaying the messages.
 *
 * @param {ResetPassword} form - Data object containing the user's email
 * @throws {any} Re-throws the caught error for further handling
 */
export async function postResetPassword(form: ResetPassword) {
  try {
    await api.post("password_reset/", toRaw(form))
    toast.success("Email sent to your mailbox")
  } catch (err: any) {
    const data = err.response?.data

    if (data && typeof data === 'object') {
      Object.entries(data).forEach(([_, messages]) => {
        (messages as string[]).forEach(msg => {
          toast.error(String(msg))
        })
      })
    } else {
      toast.error(err)
    }
    throw err
  }
}

/**
 * Sends a POST request to `password_reset/confirm/` with form data.
 *
 * :On success, redirects user to the login page.
 * :On failure, shows error messages from API response or a generic error toast.
 * :Throws the error after displaying the messages.
 *
 * @param {ResetConfirm} form - Data object for reset confirmation
 * @throws {any} Re-throws the caught error for further handling
 */
export async function postResetConfirm(form: ResetConfirm) {
  try {
    await api.post("password_reset/confirm/", toRaw(form))
    router.push('/login/')
  } catch(err: any) {
    const data = err.response?.data

    if (data && typeof data === 'object') {
      Object.entries(data).forEach(([_, messages]) => {
        (messages as string[]).forEach(msg => {
          toast.error(String(msg))
        })
      })
    } else {
      toast.error(err)
    }
    throw err
  }
}

export function logout() {
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  router.push('/login/')
}

export async function postDBconnection(form: DBconnection) {
  try {
    const response = await api.post("db/connect/", toRaw(form))
    console.log(response.data);
    console.log(response.status);
  } catch (err: any) {
    const data = err.response?.data

    if (data && typeof data === 'object') {
      Object.entries(data).forEach(([_, messages]) => {
        (messages as string[]).forEach(msg => {
          toast.error(String(msg))
        })
      })
    } else {
      toast.error(err)
    }
    throw err
  }
}
