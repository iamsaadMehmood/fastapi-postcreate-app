from pydantic import BaseSettings


class Settings(BaseSettings):
    access_token_expire_minutes: int
    algorithm: str
    refresh_token_expire_days: int
    secret_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        fields = {
            'access_token_expire_minutes': {'env': 'AUTH_ACCESS_TOKEN_EXPIRE_MINUTES'},
            'algorithm': {'env': 'AUTH_ALGORITHM'},
            'refresh_token_expire_days': {'env': 'AUTH_REFRESH_TOKEN_EXPIRE_DAYS'},
            'secret_key': {'env': 'AUTH_SECRET_KEY'},
        }
