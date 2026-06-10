from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine, URL

from src.config.config_loader import DatabaseConfig, get_postgres_config


def create_postgres_engine(
    database: str | None = None,
    config: DatabaseConfig | None = None,
    echo: bool = False,
) -> Engine:
    db_config = config or get_postgres_config(database)
    url = URL.create(
        drivername="postgresql+psycopg2",
        username=db_config.user,
        password=db_config.password,
        host=db_config.host,
        port=db_config.port,
        database=db_config.database,
    )
    return create_engine(url, echo=echo, pool_pre_ping=True)


def test_postgres_connection(
    database: str | None = None,
    config: DatabaseConfig | None = None,
) -> bool:
    engine = create_postgres_engine(database=database, config=config)
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    engine.dispose()
    return True
