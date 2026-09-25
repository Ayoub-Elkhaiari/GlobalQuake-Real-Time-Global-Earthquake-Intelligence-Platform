# Architecture

The streaming and orchestration paths are separated. The producer polls USGS at a configured, respectful interval with timeout and exponential retry. It normalizes only stable fields while retaining the original feature. Invalid source features are sent to the DLQ. The consumer validates, performs a Postgres transaction, then commits its Kafka offset. This gives at-least-once delivery with idempotent event writes.

Airflow runs only scheduled dbt, data quality, and manually-triggered bounded historical queries. It is not a streaming scheduler. The current WebSocket endpoint polls persisted newest events to keep the API stateless and avoid a second distributed messaging bridge; for multi-instance production deployment, replace it with a shared notification channel (e.g., Postgres `NOTIFY` or Redis pub/sub).
