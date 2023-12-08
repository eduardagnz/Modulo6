from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    db_url: str = Field('sqlite:///db.sqlite3')
    
settings = Settings()