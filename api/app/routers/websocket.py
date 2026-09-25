import asyncio
from fastapi import APIRouter,WebSocket,WebSocketDisconnect
from sqlalchemy import text
from ..database import SessionLocal
router=APIRouter(tags=['Live events'])
@router.websocket('/ws/earthquakes')
async def live_events(websocket:WebSocket):
 await websocket.accept();last_id=None
 try:
  while True:
   with SessionLocal() as db:
    event=db.execute(text('SELECT event_id,event_time,magnitude,place,longitude,latitude,depth_km FROM raw.earthquake_events ORDER BY ingested_at DESC LIMIT 1')).mappings().first()
   if event and event['event_id']!=last_id: await websocket.send_json({'type':'earthquake.created','event':dict(event)});last_id=event['event_id']
   await asyncio.sleep(5)
 except WebSocketDisconnect: pass
