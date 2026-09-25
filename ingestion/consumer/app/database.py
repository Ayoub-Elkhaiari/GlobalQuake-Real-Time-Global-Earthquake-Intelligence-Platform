import psycopg
from psycopg.rows import dict_row
from .config import settings
def connection(): return psycopg.connect(settings.database_url.replace('postgresql+psycopg://','postgresql://'),row_factory=dict_row)
