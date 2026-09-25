import json
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..repositories.statistics import global_statistics,grouped
from ..schemas.statistics import GlobalStatistics
router=APIRouter(prefix='/api/v1/statistics',tags=['Statistics'])
@router.get('/global',response_model=GlobalStatistics)
def global_stats(db:Session=Depends(get_db)): return global_statistics(db)
@router.get('/countries')
def country_stats(db:Session=Depends(get_db)): return grouped(db,'countries')
@router.get('/magnitude')
def magnitude_stats(db:Session=Depends(get_db)): return grouped(db,'magnitude')
@router.get('/timeline')
def timeline_stats(db:Session=Depends(get_db)): return grouped(db,'timeline')
