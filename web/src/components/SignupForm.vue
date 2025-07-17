<script lang="ts">
export const description
  = 'A sign up form with first name, last name, email and password inside a card. There\'s an option to sign up with GitHub and a link to login if you already have an account'
export const iframeHeight = '600px'
export const containerClass = 'w-full h-screen flex items-center justify-center px-4'
</script>

<script setup lang="ts">
import 'vue-sonner/style.css'
import { toast } from 'vue-sonner'

import { Label } from '@/components/ui/label'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'

import axios from 'axios';
import { reactive } from 'vue';


const form = reactive({
  first_name: "",
  last_name: "",
  username: "",
  email: "",
  password: "",
})

async function formSignup() {
  try {
    const response = await axios.post('/api/signup/', form)
    toast.error("User Created", {
      description: response
    })

  } catch(err: unknown) {
    const error = err as any
    console.log(error)
    toast.error(error.response?.data || error.message, {
      description: 'Verifique os campos e tente novamente.'
    })
  }
}
</script>


<template>
  <form @submit.prevent="formSignup">
    <Card class="mx-auto max-w-sm">
      <CardHeader>
        <CardTitle class="text-xl">Sign Up</CardTitle>
        <CardDescription>
          Enter your information to create an account
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div class="grid gap-4">
          <div class="grid grid-cols-2 gap-4">
            <div class="grid gap-2">
              <Label for="first-name">First name</Label>
              <Input id="first-name" v-model="form.first_name" placeholder="Max" required />
            </div>
            <div class="grid gap-2">
              <Label for="last-name">Last name</Label>
              <Input id="last-name" v-model="form.last_name" placeholder="Robinson" required />
            </div>
          </div>
          <div class="grid gap-2">
              <Label for="first-name">Username</Label>
              <Input id="username" v-model="form.username" placeholder="max123" required />
            </div>
          <div class="grid gap-2">
            <Label for="email">Email</Label>
            <Input id="email" type="email" v-model="form.email" placeholder="m@example.com" required />
          </div>
          <div class="grid gap-2">
            <Label for="password">Password</Label>
            <Input id="password" type="password" v-model="form.password" required />
          </div>
          <Button type="submit" class="w-full">Create an account</Button>
        </div>
        <div class="mt-4 text-center text-sm">
          Already have an account?
          <a href="/login/" class="underline">Sign in</a>
        </div>
      </CardContent>
    </Card>
  </form>
</template>
