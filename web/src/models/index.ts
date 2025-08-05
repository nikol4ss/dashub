import { reactive } from 'vue'

type Dialect = 'postgresql' | 'mysql' | 'mariadb' | 'mssql' | 'oracle' | 'sqlite'

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

export type DBconnection = {
  name: string
  database: string
  dialect: Dialect | ""
  username: string
  password: string
  host: string
  port: number
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

export const modelDBconnection = reactive<DBconnection>({
  name: "",
  database: "",
  dialect: "",
  username: "",
  password: "",
  host: "",
  port: 0,
})
