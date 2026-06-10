from dataclasses import dataclass
import os

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    port: int
    user: str
    password: str
    database: str | None = None


def _get_required_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value == "":
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def _get_int_env(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None or value == "":
        return default
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"Environment variable {name} must be an integer") from exc


def get_mysql_config(database: str | None = None) -> DatabaseConfig:
    return DatabaseConfig(
        host=_get_required_env("MYSQL_HOST"),
        port=_get_int_env("MYSQL_PORT", 3306),
        user=_get_required_env("MYSQL_USER"),
        password=_get_required_env("MYSQL_PASSWORD"),
        database=database or os.getenv("MYSQL_DATABASE"),
    )


def get_postgres_config(database: str | None = None) -> DatabaseConfig:
    return DatabaseConfig(
        host=_get_required_env("POSTGRES_HOST"),
        port=_get_int_env("POSTGRES_PORT", 5432),
        user=_get_required_env("POSTGRES_USER"),
        password=_get_required_env("POSTGRES_PASSWORD"),
        database=database or os.getenv("POSTGRES_DATABASE"),
    )
