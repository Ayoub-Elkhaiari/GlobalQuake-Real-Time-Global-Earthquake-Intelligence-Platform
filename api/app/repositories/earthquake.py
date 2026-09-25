from datetime import datetime
from sqlalchemy import text
from sqlalchemy.orm import Session
BASE='''SELECT e.event_id,e.event_time,e.magnitude,e.magnitude_type,e.place,e.longitude,e.latitude,e.depth_km,e.alert,e.tsunami,e.felt,e.significance,e.event_type,e.event_url,c.iso_alpha3 AS country_code,c.country_name FROM raw.earthquake_events e LEFT JOIN reference.countries c ON ST_Contains(c.geometry,e.location)'''
def search(db:Session,page:int,page_size:int,filters:dict):
 where=[];params={}
 for key,col,op in [('min_magnitude','e.magnitude','>='),('max_magnitude','e.magnitude','<='),('min_depth','e.depth_km','>='),('max_depth','e.depth_km','<='),('start_time','e.event_time','>='),('end_time','e.event_time','<=')]:
  if filters.get(key) is not None: where.append(f'{col} {op} :{key}');params[key]=filters[key]
 for key,col in [('country','c.iso_alpha3'),('alert','e.alert'),('event_type','e.event_type')]:
  if filters.get(key):where.append(f'{col} = :{key}');params[key]=filters[key]
 if filters.get('tsunami') is not None:where.append('e.tsunami = :tsunami');params['tsunami']=int(filters['tsunami'])
 clause=' WHERE '+' AND '.join(where) if where else ''
 total=db.execute(text('SELECT count(*) FROM ('+BASE+clause+') x'),params).scalar_one()
 params.update(limit=page_size,offset=(page-1)*page_size)
 return [dict(row) for row in db.execute(text(BASE+clause+' ORDER BY e.event_time DESC LIMIT :limit OFFSET :offset'),params).mappings()],total
def get_one(db,event_id): return db.execute(text(BASE+' WHERE e.event_id=:event_id'),{'event_id':event_id}).mappings().first()
def nearby(db,lat,lon,radius_km,limit):
 q=BASE+' WHERE ST_DWithin(e.location::geography,ST_SetSRID(ST_MakePoint(:lon,:lat),4326)::geography,:radius) ORDER BY ST_Distance(e.location::geography,ST_SetSRID(ST_MakePoint(:lon,:lat),4326)::geography) LIMIT :limit'
 return [dict(x) for x in db.execute(text(q),{'lat':lat,'lon':lon,'radius':radius_km*1000,'limit':limit}).mappings()]
