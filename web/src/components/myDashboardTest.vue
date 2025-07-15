<template>
  <div class="p-4">
    <h1 class="text-xl font-bold">Dashboard Funcionando!</h1>
    <p class="text-gray-500">Teste de componente Vue.</p>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'


console.log("testetstet");

onMounted(async () => {
    const res = await fetch('/api/ping');
    const data = await res.json();
    console.log(data) // deve mostrar { pong: true } no console do navegador
})
</script>
