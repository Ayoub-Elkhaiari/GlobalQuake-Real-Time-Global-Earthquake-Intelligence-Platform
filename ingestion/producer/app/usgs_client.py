import asyncio
import httpx
from .config import settings
async def fetch_feed() -> list[dict]:
    for attempt in range(settings.retry_attempts):
        try:
            async with httpx.AsyncClient(timeout=settings.http_timeout_seconds) as client:
                response = await client.get(settings.usgs_feed_url)
                response.raise_for_status()
                return response.json().get("features", [])
        except (httpx.HTTPError, ValueError):
            if attempt == settings.retry_attempts - 1: raise
            await asyncio.sleep(settings.retry_backoff_seconds * (2 ** attempt))
    return []
