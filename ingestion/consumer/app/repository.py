import json
from confluent_kafka import Message
from psycopg.types.json import Json
from .database import connection
from .validator import EarthquakeEvent

COLUMNS='event_id,event_time,updated_time,magnitude,magnitude_type,place,longitude,latitude,depth_km,felt,cdi,mmi,alert,status,tsunami,significance,network,event_code,event_type,station_count,distance_minimum,rms,azimuthal_gap,location_source,magnitude_source,event_url,api_detail_url,ids,sources,types,products,raw_payload,kafka_topic,kafka_partition,kafka_offset'
JSON_COLUMNS = {'products', 'raw_payload'}

def persist(event:EarthquakeEvent,message:Message)->bool:
 data=event.model_dump()
 values=[
   Json(data.get(c)) if c in JSON_COLUMNS and data.get(c) is not None else data.get(c)
   for c in COLUMNS.split(',') if c not in {'kafka_topic','kafka_partition','kafka_offset'}
 ]+[message.topic(),message.partition(),message.offset()]
 placeholders=','.join(['%s']*len(values))
 updates=','.join(f'{c}=EXCLUDED.{c}' for c in COLUMNS.split(',') if c not in {'event_id','event_time'}) + ', location=EXCLUDED.location, updated_at=now()'
 sql=f'''INSERT INTO raw.earthquake_events ({COLUMNS},location) VALUES ({placeholders},ST_SetSRID(ST_MakePoint(%s,%s),4326)) ON CONFLICT (event_id) DO UPDATE SET {updates} WHERE EXCLUDED.updated_time > raw.earthquake_events.updated_time RETURNING event_id'''
 values += [event.longitude,event.latitude]
 with connection() as conn:
  with conn.cursor() as cur: cur.execute(sql,values); return cur.fetchone() is not None