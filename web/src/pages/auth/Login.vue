<script setup lang="ts">
import LoginForm from '@/components/LoginForm.vue';
import ToggleTheme from '@/components/ToggleTheme.vue';
</script>

<template>
  <div class="relative flex flex-col items-center justify-center">
    <div class="fixed top-4 right-4 z-50 flex items-center gap-4"><ToggleTheme /></div>
    <img src="@/assets/dashub.svg" class="h-24 transition-all dark:invert" alt="Dashub Logo" />
    <LoginForm />
  </div>
</template>
