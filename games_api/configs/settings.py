from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """
    Configuraçoes gerais usadas na aplicação
    """

    API_VERSION: str = Field(default='/api/v0')
    DB_URL: str = Field(
        default='postgresql+asyncpg://gamesapi:gamesapi@localhost/gamesapi'
    )

    class Config:
        case_sensitive = True


settings: Settings = Settings()
