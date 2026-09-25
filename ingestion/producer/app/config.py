from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    kafka_broker: str
    kafka_topic: str = "earthquake.events.v1"
    kafka_dlq_topic: str = "earthquake.dlq.v1"
    usgs_feed_url: str
    usgs_poll_interval_seconds: int = 60
    http_timeout_seconds: float = 20
    retry_attempts: int = 4
    retry_backoff_seconds: float = 2
    log_level: str = "INFO"
settings = Settings()
