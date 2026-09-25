from pydantic import BaseModel
class GlobalStatistics(BaseModel):
 last_24_hours:int;last_7_days:int;last_30_days:int;largest_magnitude:float|None;average_magnitude:float|None;average_depth_km:float|None;tsunami_events:int;felt_event_count:int
