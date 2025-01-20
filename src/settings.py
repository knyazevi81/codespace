import os
import base64

from pydantic_settings import BaseSettings

def generate_random_base64_string(length: int) -> str:
    random_bytes = os.urandom(length)
    base64_string = base64.b64encode(random_bytes).decode('utf-8')
    return base64_string


class Settings(BaseSettings):
    SECRET_DOCS_PATH: str = generate_random_base64_string(10)
    BASE64_SECRET_CODE_KEY: str | None
    SECRET_KEY: str | None

    @property
    def SECRET_CODE_KEY(cls) -> bytes:
        return bytes(cls.BASE64_CODE_KEY, "utf-8")


settings = Settings()

