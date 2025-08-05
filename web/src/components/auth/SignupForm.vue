<script setup lang="ts">
import 'vue-sonner/style.css'

import { Toaster } from 'vue-sonner'

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'

import { modelSignup } from '@/models'
import { formSignup } from '@/services/api'


function handleSubmit() {
  formSignup(modelSignup)
}
</script>

<template>
  <Toaster richColors theme="dark" />
  <form @submit.prevent="handleSubmit" class="flex flex-col gap-6 max-w-sm mx-auto">

    <div class="flex flex-col items-center gap-2 text-center">
      <h1 class="text-2xl font-bold">
        Register a new account
      </h1>
      <p class="text-muted-foreground text-sm">
        Enter your information to create an account
      </p>
    </div>

    <div class="grid gap-6">
      <div class="grid grid-cols-2 gap-4">

        <div class="grid gap-3">
          <Label for="first-name">First name</Label>
          <Input id="first-name" v-model="modelSignup.first_name" placeholder="Max" required />
        </div>
        <div class="grid gap-3">
          <Label for="last-name">Last name</Label>
          <Input id="last-name" v-model="modelSignup.last_name" placeholder="Robinson" required />
        </div>
      </div>

      <div class="grid gap-3">
        <Label for="username">Username</Label>
        <Input id="username" v-model="modelSignup.username" placeholder="max123" required />
      </div>

      <div class="grid gap-3">
        <Label for="email">Email</Label>
        <Input id="email" type="email" v-model="modelSignup.email" placeholder="m@example.com" required />
      </div>

      <div class="grid gap-3">
        <Label for="password">Password</Label>
        <Input id="password" type="password" v-model="modelSignup.password" required />
      </div>

      <Button type="submit" class="w-full cursor-pointer">
        Create an account
      </Button>
    </div>

    <div class="text-center text-sm">
      Already have an account?
      <a href="/login/" class="underline underline-offset-4">Sign in</a>
    </div>
  </form>
</template>
