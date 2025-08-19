import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

import { toast } from 'vue-sonner'

export function cn(...inputs: ClassValue[]) {
  // Combines and merges multiple class names into a single optimized string.
  return twMerge(clsx(inputs))
}

function displayObject(data: any, typeToast: string) {
    if (data && typeof data === 'object') {
      Object.entries(data).forEach(([_, messages]) => {
        if (Array.isArray(messages)) {
          if (typeToast == "success") {
            messages.forEach(msg => toast.success(String(msg)))
          } else if (typeToast == "warning"){
            messages.forEach(msg => toast.warning(String(msg)))
          } else if (typeToast == "error") {
            messages.forEach(msg => toast.error(String(msg)))
          } else if (typeToast == "info") {
            messages.forEach(msg => toast.info(String(msg)))
          }
        } else {
          toast.error(String(messages))
        }
      })
    }
}

export function toastStatus(error: any) {
  const code = error.response?.status
  const data = error.response?.data

  if (code >= 200 && code < 300) {
    displayObject(data, "success")
  } else if (code >= 400 && code < 500) {
    displayObject(data, "warning")
  } else if (code >= 500 && code < 600) {
    displayObject(data, "error")
  }
}
