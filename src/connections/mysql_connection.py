from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine, URL

from src.config.config_loader import DatabaseConfig, get_mysql_config


def create_mysql_engine(
    database: str | None = None,
    config: DatabaseConfig | None = None,
    echo: bool = False,
) -> Engine:
    db_config = config or get_mysql_config(database)
    url = URL.create(
        drivername="mysql+pymysql",
        username=db_config.user,
        password=db_config.password,
        host=db_config.host,
        port=db_config.port,
        database=db_config.database,
    )
    return create_engine(url, echo=echo, pool_pre_ping=True)


def test_mysql_connection(
    database: str | None = None,
    config: DatabaseConfig | None = None,
) -> bool:
    engine = create_mysql_engine(database=database, config=config)
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    engine.dispose()
    return True
