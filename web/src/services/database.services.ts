import api from './api'

import type { DatabaseConnection } from '@/models/database.model'

import { toastStatus } from '@/lib/utils'
import { toRaw } from 'vue'
import { toast } from 'vue-sonner'


/**
 * Sends database connection data to the backend.
 * - Posts to 'db/connect/' endpoint with connection credentials.
 * - Logs response data and status to the console.
 * - Displays backend errors as toasts on failure.
 *
 * @param form postDBconnection object with required fields (e.g. host, port, user).
 * @throws Re-throws error after displaying messages.
 */
export async function postDBconnection(form: DatabaseConnection) {
  try {
    await api.post('db/connect/', toRaw(form))
    toast.success("Database connection insertion done")
  } catch (err: any) {
      toastStatus(err)
  }
}
