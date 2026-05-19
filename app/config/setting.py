from dotenv import load_dotenv
import os
load_dotenv()


class Settings:
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = os.getenv("DB_PORT")
    SECRET_KEY = os.getenv("SECRET_KEY")
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379

    @property
    def PATH(self):
        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
