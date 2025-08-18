<script setup lang="ts">
import { ref, type Component } from 'vue'
import { ChevronsUpDown, Plus } from 'lucide-vue-next'

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'

import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"

import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
} from '@/components/ui/sheet'

import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from '@/components/ui/sidebar'

import { postDBconnection } from '@/services/database.services'
import { modelDatabaseConnection, type Dialect } from '@/models/database.model'

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { ScrollArea } from '@/components/ui/scroll-area'

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

const dialects: Dialect[] = ['mariadb', 'postgresql', 'mysql', 'mssql', 'sqlite', 'oracle']

function handleDBconnection(): void {
  postDBconnection(modelDatabaseConnection)
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
          <ScrollArea class="h-full rounded-md border ">
            <SheetHeader>
              <SheetTitle>Configure Database Connection</SheetTitle>
              <SheetDescription>
                Please fill in all required fields carefully and accurately. Correct information ensures a stable
                database
                connection and proper application functioning.
              </SheetDescription>
              <hr class="mt-3">
              <form @submit.prevent="handleDBconnection" class="flex flex-col gap-6 max-w-sm mx-auto">
                <div class="grid gap-3 mt-3">
                  <Label for="name-workspace">Name Workspace</Label>
                  <Input id="name-workspace" v-model="modelDatabaseConnection.name" placeholder="Connection name"
                    required />
                </div>

                <hr>

                <div class="grid gap-3">
                  <Label>DBMS Dialect</Label>
                  <Select v-model="modelDatabaseConnection.dialect">
                    <SelectTrigger class="w-full">
                      <SelectValue placeholder="Select a DBMS" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectGroup>
                        <SelectItem v-for="dialect in dialects" :key="dialect" :value="dialect">
                          {{ dialect }}
                        </SelectItem>
                      </SelectGroup>
                    </SelectContent>
                  </Select>
                </div>

                <div class="grid gap-3">
                  <Label for="name-database">Database</Label>
                  <Input id="name-database" v-model="modelDatabaseConnection.database" placeholder="Database Name"
                    required />
                </div>

                <div class="grid gap-6">

                  <div class="grid grid-cols-2 gap-4">
                    <div class="grid gap-3">
                      <Label for="username">Username</Label>
                      <Input id="username" v-model="modelDatabaseConnection.username" placeholder="User credential"
                        required />
                    </div>
                    <div class="grid gap-3">
                      <Label for="password">Password</Label>
                      <Input id="password" type="password" v-model="modelDatabaseConnection.password" required />
                    </div>
                  </div>
                  <div class="grid grid-cols-2 gap-4">
                    <div class="grid gap-3">
                      <Label for="host">Host</Label>
                      <Input id="host" v-model="modelDatabaseConnection.host" placeholder="Host/IP" required />
                    </div>
                    <div class="grid gap-3">
                      <Label for="port">Port</Label>
                      <Input id="port" v-model="modelDatabaseConnection.port" placeholder="1234" required />
                    </div>
                  </div>

                  <hr>

                  <Button type="submit" class="w-full cursor-pointer">
                    Create Connection
                  </Button>
                </div>
              </form>
            </SheetHeader>
          </ScrollArea>
        </SheetContent>
      </Sheet>
    </SidebarMenuItem>
  </SidebarMenu>
</template>
