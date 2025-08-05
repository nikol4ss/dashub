from django.db import models
from django.contrib.auth.models import User


class Dialect(models.TextChoices):
    POSTGRESQL = "postgresql", "PostgreSQL"
    MYSQL = "mysql", "MySQL"
    MARIADB = "mariadb", "MariaDB"
    MSSQL = "mssql", "Microsoft SQL Server"
    ORACLE = "oracle", "Oracle"
    SQLITE = "sqlite", "SQLite"


class DatabaseConnection(models.Model):
    # Defines the database connection model, linking the user and detailing connection parameters.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="connections")
    name = models.CharField(max_length=50)
    database = models.CharField(max_length=50)
    dialect = models.CharField(
        max_length=20, choices=Dialect.choices, default=Dialect.POSTGRESQL
    )
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    port = models.IntegerField()

    def __str__(self):
        return self.name
