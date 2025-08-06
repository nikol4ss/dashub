import axios from 'axios'

const api = axios.create({
  baseURL: '/api/',
})

api.interceptors.request.use(config => {
    // Request interceptor: adds JWT token to the header
  const token = localStorage.getItem('access_token')
  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

api.interceptors.response.use(
    // Response interceptor: clear tokens if unauthorized (401/403)
  response => response,
  error => {
    const status = error.response?.status
    if (status === 401 || status === 403) {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
    }
    return Promise.reject(error)
  }
)

export default api
