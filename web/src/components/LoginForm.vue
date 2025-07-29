<script setup lang="ts">
import { useRouter } from 'vue-router'
import { Toaster } from 'vue-sonner'
import { toast } from 'vue-sonner'
import { cn } from '@/lib/utils'

import type { HTMLAttributes } from 'vue'
import { ref } from 'vue'

import api from '@/lib/utils'

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'


const props = defineProps<{
  class?: HTMLAttributes['class']
}>()

const router = useRouter()
const username = ref('')
const password = ref('')

const login = async () => {
  try {
    const response = await api.post('/token/', {
      username: username.value,
      password: password.value,
    })

    const { access, refresh } = response.data
    localStorage.setItem('access_token', access)
    localStorage.setItem('refresh_token', refresh)

    router.push('/dashboard/')
  } catch (error) {
    toast.warning("Login failed")
  }
}
</script>



<template>
  <Toaster richColors />
  <form :class="cn('flex flex-col gap-6 max-w-sm mx-auto', props.class)" @submit.prevent="login">
    <div class="flex flex-col items-center gap-2 text-center">
      <h1 class="text-2xl font-bold">Login to your account</h1>
      <p class="text-muted-foreground text-sm text-balance">
        Enter your email below to login to your account
      </p>
    </div>

    <div class="grid gap-6">
      <div class="grid gap-3">
        <Label for="Username">Username</Label>
        <Input id="username" type="username" placeholder="max123" required v-model="username" />
      </div>
      <div class="grid gap-3">
        <div class="flex items-center">
          <Label for="password">Password</Label>
          <a href="#" class="ml-auto text-sm underline-offset-4 hover:underline">
            Forgot your password?
          </a>
        </div>
        <Input id="password" type="password" required v-model="password" />
      </div>

      <Button type="submit" class-name="w-full">Access your account</Button>
    </div>

    <div class="text-center text-sm">
      Don't have an account?
      <a href="/signup/" class="underline underline-offset-4">Sign up</a>
    </div>
  </form>
</template>
