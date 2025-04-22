from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'УКОРАЧИВАТЕЛЬ'
    description: str = 'Сервис для укорачивания ссылок'
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()
