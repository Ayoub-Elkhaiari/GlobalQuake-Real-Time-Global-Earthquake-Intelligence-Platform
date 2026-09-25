import json,logging,signal
from datetime import UTC,datetime
from confluent_kafka import Consumer,Producer
from .config import settings
from .repository import persist
from .validator import EarthquakeEvent
running=True
logging.basicConfig(level=settings.log_level,format='%(asctime)s %(levelname)s consumer %(message)s')
def stop(*_):
 global running;running=False
def dlq(producer,payload,error):
 body={'event_id':payload.get('event_id'),'error':str(error),'error_type':type(error).__name__,'timestamp':datetime.now(UTC).isoformat(),'original_payload':payload,'source':'consumer'}
 producer.produce(settings.kafka_dlq_topic,key=body['event_id'],value=json.dumps(body,default=str));producer.flush(10)
def main():
 consumer=Consumer({'bootstrap.servers':settings.kafka_broker,'group.id':settings.kafka_consumer_group,'enable.auto.commit':False,'auto.offset.reset':'earliest'})
 producer=Producer({'bootstrap.servers':settings.kafka_broker});consumer.subscribe([settings.kafka_topic])
 try:
  while running:
   message=consumer.poll(1)
   if message is None: continue
   if message.error(): logging.error('kafka error %s',message.error());continue
   payload={}
   try:
    payload=json.loads(message.value()); changed=persist(EarthquakeEvent.model_validate(payload),message); consumer.commit(message=message,asynchronous=False);logging.info('persisted event_id=%s changed=%s',payload['event_id'],changed)
   except Exception as exc:
    logging.exception('message failed');dlq(producer,payload,exc);consumer.commit(message=message,asynchronous=False)
 finally: consumer.close();producer.flush(10)
if __name__=='__main__':
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop);main()
