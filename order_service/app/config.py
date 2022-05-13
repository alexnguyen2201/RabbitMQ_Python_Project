import secrets
import datetime

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    DATABASE_URL = "mysql+mysqlconnector://test:test@localhost:3306/food"  # noqa

    def past_week(self):
        return datetime.datetime.utcnow() - datetime.timedelta(weeks=1)

    def current_time(self):
        return (datetime.datetime.utcnow() +
                datetime.timedelta(hours=7))

    class Config:
        case_sensitive = True


settings = Settings()
