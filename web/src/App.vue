<script setup lang="ts">
import { Toaster } from '@/components/ui/sonner'
import 'vue-sonner/style.css'  
</script>

<template>
  <Toaster class="pointer-events-auto" />
  <router-view />
</template>
