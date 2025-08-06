import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

import { toast } from 'vue-sonner'

export function cn(...inputs: ClassValue[]) {
  // Combines and merges multiple class names into a single optimized string.
  return twMerge(clsx(inputs))
}

export function toastError(err: any) {
  // Displays error messages from an API response using toasts and throws the error.
  const data = err.response?.data

  if (data && typeof data === 'object') {
    Object.entries(data).forEach(([_, messages]) => {
      if (Array.isArray(messages)) {
        messages.forEach(msg => toast.error(String(msg)))
      } else {
        toast.error(String(messages))
      }
    })
  } else {
    toast.error(err.message || String(err))
  }

  throw err
}
