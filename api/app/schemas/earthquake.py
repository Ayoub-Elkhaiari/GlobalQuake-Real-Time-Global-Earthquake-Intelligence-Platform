from datetime import datetime
from pydantic import BaseModel
class Earthquake(BaseModel):
 event_id:str;event_time:datetime;magnitude:float|None; magnitude_type:str|None;place:str|None;longitude:float;latitude:float;depth_km:float|None;alert:str|None;tsunami:int|None;felt:int|None;significance:int|None;event_type:str|None;event_url:str|None;country_code:str|None=None;country_name:str|None=None
class EarthquakePage(BaseModel): items:list[Earthquake];page:int;page_size:int;total:int
