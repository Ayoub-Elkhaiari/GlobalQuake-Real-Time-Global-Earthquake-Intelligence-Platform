from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl, field_validator
from typing import Any
class EarthquakeEvent(BaseModel):
 event_id:str=Field(min_length=1); event_time:datetime; updated_time:datetime|None=None; magnitude:float|None=Field(default=None,ge=-2,le=10)
 magnitude_type:str|None=None; place:str|None=None; longitude:float=Field(ge=-180,le=180); latitude:float=Field(ge=-90,le=90); depth_km:float|None=Field(default=None,ge=0,le=1000)
 felt:int|None=None;cdi:float|None=None;mmi:float|None=None;alert:str|None=None;status:str|None=None;tsunami:int|None=None;significance:int|None=None;network:str|None=None;event_code:str|None=None;event_type:str|None=None;station_count:int|None=None;distance_minimum:float|None=None;rms:float|None=None;azimuthal_gap:float|None=None;location_source:str|None=None;magnitude_source:str|None=None;event_url:str|None=None;api_detail_url:str|None=None;ids:str|None=None;sources:str|None=None;types:str|None=None;products:dict[str,Any]|None=None;raw_payload:dict[str,Any]
 @field_validator('updated_time')
 @classmethod
 def update_not_before_event(cls,v,info):
  if v and info.data.get('event_time') and v < info.data['event_time']: raise ValueError('updated_time before event_time')
  return v
