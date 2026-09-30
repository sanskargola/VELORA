from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = 'StockVision API'
    debug: bool = True
    database_url: str = 'sqlite:///./stockvision.db'
    secret_key: str = 'change-me-in-production'
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = 60 * 24
    refresh_token_expire_minutes: int = 60 * 24 * 7
    cors_origins: str = '*'

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()
