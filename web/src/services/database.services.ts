import api from './api'

import type { DatabaseConnection } from '@/models/database.model'

import { toastError } from '@/lib/utils'
import { toRaw } from 'vue'

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
    const response = await api.post('db/connect/', toRaw(form))
    console.log(response.data)
    console.log(response.status)
  } catch (err: any) {
      toastError(err)
  }
}
