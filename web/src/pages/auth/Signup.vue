<script setup lang="ts">
import SignupForm from '@/components/SignupForm.vue';
import ToggleTheme from '@/components/ToggleTheme.vue';
</script>

<template>
  <div class="w-screen h-screen">
    <div class="grid min-h-screen lg:grid-cols-2">
      <div class="flex flex-col gap-4 p-6 md:p-10">

        <div class="flex justify-center md:justify-start">
          <div class="flex items-center justify-center text-primary-foreground">
            <img src="@/assets/dashub.svg" class="w-15 transition-all dark:invert" alt="Dashub Logo" />
          </div>
        </div>

        <div class="flex flex-1 items-center justify-center">
          <div class="fixed top-4 right-4 z-50 flex items-center gap-4">
            <ToggleTheme />
          </div>

          <div class="w-full max-w">
            <SignupForm />
          </div>
        </div>
      </div>

      <div class="relative bg-muted hidden lg:block">
        <img src="../../assets/placeholder.svg" alt="Image"
          class="absolute inset-0 w-full h-full object-cover dark:brightness-[0.2] dark:grayscale" />
      </div>
    </div>
  </div>
</template>
