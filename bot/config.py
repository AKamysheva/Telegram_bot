from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    HOST_DB: str
    PORT_DB: int
    OPENROUTER_API_KEY: str

    @property
    def database_url(self):
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.HOST_DB}:{self.PORT_DB}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(env_file="bot/.env")


settings = Settings()
