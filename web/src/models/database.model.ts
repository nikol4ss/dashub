import { reactive } from 'vue'

export type Dialect = 'postgresql' | 'mysql' | 'mariadb' | 'mssql' | 'oracle' | 'sqlite'

export type DatabaseConnection = {
  name: string
  database: string
  dialect: Dialect | ""
  username: string
  password: string
  host: string
  port: number | null
}

export const modelDatabaseConnection = reactive<DatabaseConnection>({
  name: "",
  database: "",
  dialect: "",
  username: "",
  password: "",
  host: "",
  port: null,
})
