from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    db_url: str = Field('postgresql://user:12345678@localhost:5432/database-2')
    
settings = Settings()