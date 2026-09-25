from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
 model_config=SettingsConfigDict(env_file='.env',extra='ignore')
 database_url:str;redis_url:str='redis://redis:6379/0';cors_origins:str='http://localhost:3000';cache_ttl_seconds:int=30
settings=Settings()
