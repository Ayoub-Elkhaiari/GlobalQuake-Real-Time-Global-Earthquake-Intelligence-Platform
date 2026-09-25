from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from .config import settings
from .database import SessionLocal
from .routers import countries,earthquakes,statistics,websocket
app=FastAPI(title='GlobalQuake API',version='1.0.0',description='Real-time global earthquake intelligence API')
app.add_middleware(CORSMiddleware,allow_origins=[x.strip() for x in settings.cors_origins.split(',')],allow_credentials=True,allow_methods=['GET'],allow_headers=['*'])
app.include_router(earthquakes.router);app.include_router(countries.router);app.include_router(statistics.router);app.include_router(websocket.router)
@app.get('/health',tags=['Health'])
def health():return {'status':'ok','service':'globalquake-api'}
@app.get('/ready',tags=['Health'])
def ready():
 try:
  with SessionLocal() as db:db.execute(text('SELECT 1'))
  return {'status':'ready'}
 except Exception as exc:return {'status':'not_ready','detail':str(exc)}
