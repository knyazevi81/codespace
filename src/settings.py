import os
import base64

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE64_SECRET_CODE_KEY: str | None
    SECRET_KEY: str | None

    @property
    def SECRET_CODE_KEY(cls) -> bytes:
        return bytes(cls.BASE64_CODE_KEY, "utf-8")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
