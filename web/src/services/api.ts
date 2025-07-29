import api from '@/lib/utils'
import router from "@/router";
import { toast } from 'vue-sonner'
import { toRaw } from 'vue'
import type { SignupForm } from '@/models/userSignupForm';

export async function postLogin(username: string, password: string) {
    const response = api.post('/token/', {
        username,
        password,
    })

    const { access, refresh } = (await response).data
    localStorage.setItem('access_token', access)
    localStorage.setItem('refresh_token', refresh)

    router.push('/dashboard')
}


export function getDashboard(accessToken: any) {
    return api.get("dashboard/", {
        headers: { Authorization: `Bearer ${accessToken}`}
    })
}

export async function formSignup(form: SignupForm) {
  try {
    await api.post('/api/signup/', toRaw(form))

  } catch (err: any) {
    const data = err.response?.data

    if (data && typeof data === 'object') {
      Object.entries(data).forEach(([_, messages]) => {
        (messages as string[]).forEach(msg => {
          toast.warning(msg)
        })
      })
    } else {
      toast.error(err)
    }
  }
}

