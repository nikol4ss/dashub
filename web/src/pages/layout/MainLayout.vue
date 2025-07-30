<script setup lang="ts">
import AppSidebar from '@/components/layout/AppSidebar.vue'
import ToggleTheme from '@/components/shared/ToggleTheme.vue'

import { Toaster } from 'vue-sonner'
import { Separator } from '@/components/ui/separator'
import {
    Breadcrumb,
    BreadcrumbItem,
    BreadcrumbLink,
    BreadcrumbList,
    BreadcrumbPage,
    BreadcrumbSeparator,
} from '@/components/ui/breadcrumb'

import {
    SidebarInset,
    SidebarProvider,
    SidebarTrigger,
} from '@/components/ui/sidebar'

import {
    AlertDialog,
    AlertDialogAction,
    AlertDialogCancel,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogTitle,
} from '@/components/ui/alert-dialog'

import { onMounted, onUnmounted, ref } from 'vue'
import { jwtDecode } from 'jwt-decode'
import { getCentral } from '@/services/api'
import { logout } from '@/services/api'

const description = 'A sidebar that collapses to icons.'
const iframeHeight = '800px'
const containerClass = 'w-full h-full'

defineExpose({
    description,
    iframeHeight,
    containerClass,
})

const centralData = ref<any>(null)
const backClicked = ref(false)

function handlePopState() {
    backClicked.value = true
}

onMounted(() => {
    window.addEventListener('popstate', handlePopState)
})

onUnmounted(() => {
    window.removeEventListener('popstate', handlePopState)
})

onMounted(async () => {
    const token = localStorage.getItem('access_token')
    if (!token) return

    try {
        const decoded = jwtDecode<{ exp: number }>(token)
        if (Date.now() >= decoded.exp * 1000) {
            localStorage.removeItem('access_token')
            localStorage.removeItem('refresh_token')
            return
        }

        centralData.value = await getCentral()
    } catch (err) {
        console.log('Erro ao carregar central:', err)
    }
})
</script>

<template>
    <Toaster richColors theme="dark" position="bottom-center" />
    <SidebarProvider>
        <AppSidebar />
        <SidebarInset>
            <header
                class="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-[[data-collapsible=icon]]/sidebar-wrapper:h-12">
                <div class="flex items-center gap-2 px-4">
                    <SidebarTrigger class="-ml-1" />
                    <Separator orientation="vertical" class="mr-2 h-4" />
                    <Breadcrumb>
                        <BreadcrumbList>
                            <BreadcrumbItem class="hidden md:block">
                                <BreadcrumbLink href="#">
                                    Building Your Application
                                </BreadcrumbLink>
                            </BreadcrumbItem>
                            <BreadcrumbSeparator class="hidden md:block" />
                            <BreadcrumbItem>
                                <BreadcrumbPage>Data Fetching</BreadcrumbPage>
                            </BreadcrumbItem>
                        </BreadcrumbList>
                    </Breadcrumb>
                    <div class="fixed top-4 right-4 z-50 flex items-center gap-4">
                        <ToggleTheme />
                    </div>
                </div>
            </header>
            <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
                <div class="grid auto-rows-min gap-4 md:grid-cols-3">
                    <div class="aspect-video rounded-xl bg-muted/50" />
                    <div class="aspect-video rounded-xl bg-muted/50" />
                    <div class="aspect-video rounded-xl bg-muted/50" />
                </div>
                <div class="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min" />
            </div>
        </SidebarInset>
        <AlertDialog :open="backClicked">
            <AlertDialogContent>
                <AlertDialogHeader>
                    <AlertDialogTitle>Are you sure you want to log out?</AlertDialogTitle>
                    <AlertDialogDescription>
                        If you log out, your current session will be terminated, and you will need to authenticate
                        again
                        to access
                        your account. Logging out also allows you to switch between different user accounts
                        securely.
                    </AlertDialogDescription>
                </AlertDialogHeader>
                <AlertDialogFooter>
                    <AlertDialogCancel @click="backClicked = false">Cancel</AlertDialogCancel>
                    <AlertDialogAction @click="logout">Continue</AlertDialogAction>
                </AlertDialogFooter>
            </AlertDialogContent>
        </AlertDialog>

    </SidebarProvider>
</template>
