# API

- `GET /health`, `GET /ready`
- `GET /api/v1/earthquakes` supports page, page_size, magnitude, depth, time, country, alert, tsunami, and event-type filters.
- `GET /api/v1/earthquakes/{event_id}` and `GET /api/v1/earthquakes/nearby?lat=&lon=&radius_km=`.
- `GET /api/v1/countries`, `GET /api/v1/countries/{country_code}/statistics`.
- `GET /api/v1/statistics/{global,countries,magnitude,timeline}`.
- `WS /ws/earthquakes` sends `earthquake.created` envelopes.

Interactive OpenAPI documentation is available at `/docs` and `/redoc`.
