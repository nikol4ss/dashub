import { reactive } from 'vue'

export type SignupForm = {
  first_name: string
  last_name: string
  username: string
  email: string
  password: string
}

export type LoginForm = {
  username: string
  password: string
}

export type ResetPassword = {
  email: string
}

export type ResetConfirm = {
  password: string
  token: string
}

export const modelSignup = reactive<SignupForm>({
  first_name: "",
  last_name: "",
  username: "",
  email: "",
  password: "",
})

export const modelLogin = reactive<LoginForm>({
  username: "",
  password: "",
})

export const modelResetPassword = reactive<ResetPassword>({
  email: "",
})

