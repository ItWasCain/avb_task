from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'УКОРАЧИВАТЕЛЬ'
    description: str = 'Сервис для укорачивания ссылок'
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str = "db"
    postgres_port: str = "5432"

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"

    class Config:
        env_file = ".env"
        env_prefix = "POSTGRES_"  # Автоматически добавляет префикс к переменным
        extra = "ignore"


settings = Settings()
