import os
from dataclasses import dataclass, field

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class AsyncPostgresSettings:
    """Configurate data for database connection"""

    db_user: str = field(default_factory=lambda: 'postgres')
    db_pass: str = field(default_factory=lambda: 'postgres')
    db_host: str = field(default_factory=lambda: 'localhost')
    db_port: int = field(default_factory=lambda: 5432)
    db_name: str = field(default_factory=lambda: 'postgres')
    db_driver: str = field(default_factory=lambda: 'postgresql+asyncpg')

    @property
    def db_url(self) -> str:
        return (
            f'{self.db_driver}://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}'
        )


async_postgres_settings = AsyncPostgresSettings(
    db_user=os.environ.get('DB_USER'),
    db_pass=os.environ.get('DB_PASS'),
    db_host=os.environ.get('DB_HOST'),
    db_port=os.environ.get('DB_PORT'),
    db_name=os.environ.get('DB_NAME')
)
