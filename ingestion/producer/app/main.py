import asyncio, logging, signal
from .config import settings
from .kafka_producer import EventProducer
from .normalizer import normalize
from .usgs_client import fetch_feed
running=True
logging.basicConfig(level=settings.log_level, format='%(asctime)s %(levelname)s producer %(message)s')
def stop(*_):
 global running; running=False
async def run():
 producer=EventProducer()
 try:
  while running:
   try:
    features=await fetch_feed(); published=0
    for feature in features:
     try: producer.publish(normalize(feature)); published+=1
     except Exception as exc: logging.exception('event rejected'); producer.dlq(feature,exc)
    logging.info('feed processed fetched=%s published=%s',len(features),published)
   except Exception: logging.exception('feed polling failed')
   await asyncio.sleep(settings.usgs_poll_interval_seconds)
 finally: producer.close()
if __name__=='__main__':
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop);asyncio.run(run())
