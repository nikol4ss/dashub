import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'
import axios from 'axios'


const api = axios.create({
  baseURL: '/api/',
})

/**
 * Axios request interceptor that adds the JWT token
 * in the Authorization header for Bearer authentication.
 * Fetches the token from localStorage.
 *
 * @param {import('axios').AxiosRequestConfig} config Request configuration
 * @returns {import('axios').AxiosRequestConfig} Configuration modified with token
 */
api.interceptors.request.use(config => {

  const token = localStorage.getItem('access_token')

  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

/**
 * Axios response interceptor to handle authorization errors.
 * If the response status is 401 or 403, removes tokens from localStorage.
 *
 * @param {import('axios').AxiosResponse} response - Successful response
 * @returns {import('axios').AxiosResponse} The response, unchanged
 *
 * @param {any} error - Error object from axios
 * @returns {Promise<any>} Rejected promise with the error
 */
api.interceptors.response.use(
  response => response,
  error => {
    if (error.response && (error.response.status === 401 || error.response.status === 403)) {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
    }

    return Promise.reject(error)
  }
)

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export default api

