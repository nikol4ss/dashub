<script setup lang="ts">
import { ref, type HTMLAttributes } from 'vue'

import { Toaster } from 'vue-sonner'
import { LoaderCircle } from 'lucide-vue-next'

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'

import { cn } from '@/lib/utils'
import { modelLogin, modelResetPassword } from '@/models'
import { postLogin, postResetPassword } from '@/services/api'

import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from '@/components/ui/sheet'


const isResetting = ref(false)
const props = defineProps<{
  class?: HTMLAttributes['class']
}>()

async function handleResetPassword() {
  isResetting.value = true
  try {
    await postResetPassword(modelResetPassword)
  } finally {
    isResetting.value = false
  }
}

function handleSubmit() {
  postLogin(modelLogin)
}
</script>

<template>
  <BounceLoader :loading="true" color="#3b82f6" size="40px" />
  <Toaster richColors theme="dark" />
  <form :class="cn('flex flex-col gap-6 max-w-sm mx-auto', props.class)" @submit.prevent="handleSubmit">
    <div class="flex flex-col items-center gap-2 text-center">
      <h1 class="text-2xl font-bold">Login to your account</h1>
      <p class="text-muted-foreground text-sm text-balance">
        Enter your email below to login to your account
      </p>
    </div>

    <div class="grid gap-6">
      <div class="grid gap-3">
        <Label for="Username">Username</Label>
        <Input id="username" type="username" required v-model="modelLogin.username" />
      </div>
      <div class="grid gap-3">
        <div class="flex items-center">
          <Label for="password">Password</Label>
          <a href="#" class="ml-auto text-sm underline-offset-4 hover:underline">
            <Sheet>
              <SheetTrigger class="hover:underline cursor-pointer">Forgot your password?</SheetTrigger>
              <SheetContent>
                <SheetHeader>
                  <SheetTitle>Email address to receive reset code</SheetTitle>
                  <SheetDescription>
                    Check your email for a verification message. It contains a link to reset your password.
                  </SheetDescription>
                  <hr class="mt-3">
                  <form @submit.prevent="handleResetPassword">
                    <Input id="email" class="mt-3" type="email" required v-model="modelResetPassword.email"
                      placeholder="m@example.com" />
                    <Button type="submit" class="mt-4 w-full" :disabled="isResetting">
                      <LoaderCircle v-if="isResetting" class="size-4 animate-spin" />
                      <span>
                        {{ isResetting ? "Sending" : "Send recovery email" }}
                      </span>
                    </Button>
                  </form>
                </SheetHeader>
              </SheetContent>
            </Sheet>
          </a>
        </div>
        <Input id="password" type="password" required v-model="modelLogin.password" />
      </div>

      <Button type="submit" class-name="w-full">Access your account</Button>
    </div>

    <div class="text-center text-sm">
      Don't have an account?
      <a href="/signup/" class="underline underline-offset-4">Sign up</a>
    </div>
  </form>
</template>
