from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
 model_config=SettingsConfigDict(env_file='.env',extra='ignore')
 kafka_broker:str; kafka_topic:str='earthquake.events.v1'; kafka_dlq_topic:str='earthquake.dlq.v1'; kafka_consumer_group:str='earthquake-postgres-writer-v1'; database_url:str; log_level:str='INFO'
settings=Settings()
