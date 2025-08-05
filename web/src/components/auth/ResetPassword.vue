<script setup lang="ts">
import { onMounted, reactive, type HTMLAttributes } from 'vue'

import { Toaster } from 'vue-sonner'

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'

import { cn } from '@/lib/utils'
import { postResetConfirm } from '@/services/api'
import { useRoute } from 'vue-router'
import type { ResetConfirm } from '@/models'


const props = defineProps<{
    class?: HTMLAttributes['class']
}>()


const route = useRoute()
const token = route.query.token as string

const modelResetConfirm = reactive<ResetConfirm>({
    password: '',
    token: token || ''
})

function handleResetConfirm() {
    postResetConfirm(modelResetConfirm)
}

onMounted(() => {
    modelResetConfirm.token = String(route.query.token || '')
})
</script>

<template>
    <Toaster richColors theme="dark" />
    <form :class="cn('flex flex-col gap-6 max-w-sm mx-auto', props.class)" @submit.prevent="handleResetConfirm">
        <div class="flex flex-col items-center gap-2 text-center">
            <h1 class="text-2xl font-bold">Reset Password</h1>
            <p class="text-muted-foreground text-sm text-balance">
                Please choose a secure new password
            </p>
        </div>
        <div class="grid gap-6">
            <div class="grid gap-3">
                <Label for="password">New Password</Label>
                <Input id="password" type="password" required v-model="modelResetConfirm.password" />
            </div>
            <Button type="submit" class-name="w-full">Update Password</Button>
        </div>
    </form>
</template>
