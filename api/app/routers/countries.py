from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from ..database import get_db
router=APIRouter(prefix='/api/v1/countries',tags=['Countries'])
@router.get('')
def countries(db:Session=Depends(get_db)):
 return [dict(x) for x in db.execute(text("SELECT iso_alpha3 country_code,country_name,region,subregion FROM reference.countries ORDER BY country_name")).mappings()]
@router.get('/{country_code}/statistics')
def country_statistics(country_code:str,db:Session=Depends(get_db)):
 q="""SELECT c.iso_alpha3 country_code,c.country_name,count(e.*) event_count,max(e.magnitude) largest_magnitude,avg(e.magnitude) average_magnitude,max(e.event_time) last_event,count(e.*) FILTER (WHERE e.tsunami=1) tsunami_events FROM reference.countries c LEFT JOIN raw.earthquake_events e ON ST_Contains(c.geometry,e.location) WHERE c.iso_alpha3=:code GROUP BY 1,2"""
 data=db.execute(text(q),{'code':country_code.upper()}).mappings().first()
 if not data:raise HTTPException(404,'Country not found')
 return dict(data)
