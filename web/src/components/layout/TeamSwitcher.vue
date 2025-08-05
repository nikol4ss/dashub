<script setup lang="ts">
import { ChevronsUpDown, Plus } from 'lucide-vue-next'

import { type Component, ref } from 'vue'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'

// import {
//   CircleDot
// } from 'lucide-vue-next'

import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
} from '@/components/ui/sheet'

import { postDBconnection } from '@/services/api'
import { modelDBconnection } from '@/models'

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'

import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from '@/components/ui/sidebar'

const props = defineProps<{
  teams: {
    name: string
    logo: Component
    status: string
  }[]
}>()

const { isMobile } = useSidebar()
const activeTeam = ref(props.teams[0])
const showSheet = ref(false)

function handleDBconnection() {
  postDBconnection(modelDBconnection)
}
</script>

<template>
  <SidebarMenu>
    <SidebarMenuItem>
      <DropdownMenu>
        <DropdownMenuTrigger as-child>
          <SidebarMenuButton size="lg"
            class="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground">
            <div
              class="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
              <component :is="activeTeam.logo" class="size-4" />
            </div>
            <div class="grid flex-1 text-left text-sm leading-tight">
              <span class="truncate font-medium">
                {{ activeTeam.name }}
              </span>
              <span class="truncate text-xs">{{ activeTeam.status }}</span>
            </div>
            <ChevronsUpDown class="ml-auto" />
          </SidebarMenuButton>
        </DropdownMenuTrigger>
        <DropdownMenuContent class="w-[--reka-dropdown-menu-trigger-width] min-w-56 rounded-lg" align="start"
          :side="isMobile ? 'bottom' : 'right'" :side-offset="4">
          <DropdownMenuLabel class="text-xs text-muted-foreground">
            Workspace
          </DropdownMenuLabel>
          <DropdownMenuItem v-for="(team, index) in teams" :key="team.name" class="gap-2 p-2"
            @click="activeTeam = team">
            <div class="flex size-6 items-center justify-center rounded-sm border">
              <component :is="team.logo" class="size-3.5 shrink-0" />
            </div>
            {{ team.name }}
            <DropdownMenuShortcut>⌘{{ index + 1 }}</DropdownMenuShortcut>
          </DropdownMenuItem>
          <DropdownMenuSeparator />
          <DropdownMenuItem @click.stop="showSheet = true" class="gap-2 p-2">
            <div class="flex size-6 items-center justify-center rounded-md border bg-transparent">
              <Plus class="size-4" />
            </div>
            <div class="font-medium text-muted-foreground">
              <span class="cursor-pointer">Add Database</span>
            </div>
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
      <Sheet v-model:open="showSheet">
        <SheetContent>
          <SheetHeader>
            <SheetTitle>Email address to receive reset code</SheetTitle>
            <SheetDescription>
              Check your email for a verification message.
            </SheetDescription>
            <hr class="mt-3">
            <form @submit.prevent="handleDBconnection">
              <Label for="password">Password</Label>
              <Input id="name" type="name" v-model="modelDBconnection.name" placeholder="m@example.com" required />


              <Button type="submit" class="w-full cursor-pointer">
                Create an account
              </Button>

            </form>
          </SheetHeader>
        </SheetContent>
      </Sheet>
    </SidebarMenuItem>
  </SidebarMenu>
</template>
