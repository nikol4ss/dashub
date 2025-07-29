import { reactive } from 'vue'

export type SignupForm = {
  first_name: string
  last_name: string
  username: string
  email: string
  password: string
}

export const form = reactive<SignupForm>({
  first_name: "",
  last_name: "",
  username: "",
  email: "",
  password: "",
})
