from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ALGORITHM_CRYPT: str
    SECRET_TOKEN_KEY: str
    ACCESS_TOKEN_DURATION: int
    URL_DB: str

    model_config = SettingsConfigDict(env_file=".env")