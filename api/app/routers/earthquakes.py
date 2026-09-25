from datetime import datetime
from fastapi import APIRouter,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from ..database import get_db
from ..repositories.earthquake import get_one,nearby,search
from ..schemas.earthquake import Earthquake,EarthquakePage
router=APIRouter(prefix='/api/v1/earthquakes',tags=['Earthquakes'])
@router.get('',response_model=EarthquakePage)
def list_earthquakes(page:int=Query(1,ge=1),page_size:int=Query(100,ge=1,le=500),min_magnitude:float|None=None,max_magnitude:float|None=None,start_time:datetime|None=None,end_time:datetime|None=None,min_depth:float|None=None,max_depth:float|None=None,country:str|None=None,alert:str|None=None,tsunami:bool|None=None,event_type:str|None=None,db:Session=Depends(get_db)):
 items,total=search(db,page,page_size,locals());return {'items':items,'page':page,'page_size':page_size,'total':total}
@router.get('/nearby',response_model=list[Earthquake])
def nearby_search(lat:float=Query(ge=-90,le=90),lon:float=Query(ge=-180,le=180),radius_km:float=Query(ge=.1,le=20000),limit:int=Query(100,ge=1,le=500),db:Session=Depends(get_db)): return nearby(db,lat,lon,radius_km,limit)
@router.get('/{event_id}',response_model=Earthquake)
def earthquake(event_id:str,db:Session=Depends(get_db)):
 event=get_one(db,event_id)
 if not event:raise HTTPException(404,'Earthquake not found')
 return event
