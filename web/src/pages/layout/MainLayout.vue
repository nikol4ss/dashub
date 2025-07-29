<script setup lang="ts">
import AppSidebar from '@/components/layout/AppSidebar.vue'
import ToggleTheme from '@/components/shared/ToggleTheme.vue'

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

import { ref, onMounted } from 'vue'
import { getDashboard } from '@/services/api'

// Exportações de metadados
const description = 'A sidebar that collapses to icons.'
const iframeHeight = '800px'
const containerClass = 'w-full h-full'

defineExpose({
    description,
    iframeHeight,
    containerClass,
})

// Reatividade
const accessToken = 'seu_token_aqui'
const data = ref(null)

onMounted(() => {
    getDashboard(accessToken).then(res => {
        data.value = res.data
    })
})
</script>

<template>
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
    </SidebarProvider>
</template>
