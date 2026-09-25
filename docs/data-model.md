# Data model

`raw.earthquake_events` uses USGS `event_id` as the primary key. All timestamps are `TIMESTAMPTZ` and location is `geometry(Point, 4326)`. `raw_payload` preserves the unmodified USGS feature. A conflict update applies only if `EXCLUDED.updated_time` is newer than the stored source update time, so stale feed observations do not overwrite corrected records.

Country attribution is a spatial `ST_Contains` join with `reference.countries`. Country columns are nullable because ocean, border, and disputed-region events do not necessarily have reliable membership.
