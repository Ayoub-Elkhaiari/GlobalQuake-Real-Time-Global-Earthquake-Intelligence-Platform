import json
from datetime import UTC, datetime
from confluent_kafka import Producer
from .config import settings
class EventProducer:
 def __init__(self): self.client = Producer({"bootstrap.servers": settings.kafka_broker, "enable.idempotence": True})
 def publish(self, event: dict) -> None:
  self.client.produce(settings.kafka_topic, key=event["event_id"], value=json.dumps(event, default=str)); self.client.flush(10)
 def dlq(self, payload: dict, error: Exception, source: str = "producer") -> None:
  envelope={"event_id":payload.get("id") or payload.get("event_id"),"error":str(error),"error_type":type(error).__name__,"timestamp":datetime.now(UTC).isoformat(),"original_payload":payload,"source":source}
  self.client.produce(settings.kafka_dlq_topic,key=envelope["event_id"],value=json.dumps(envelope,default=str));self.client.flush(10)
 def close(self): self.client.flush(10)
