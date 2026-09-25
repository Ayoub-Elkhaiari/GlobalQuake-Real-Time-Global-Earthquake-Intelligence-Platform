CREATE TABLE IF NOT EXISTS raw.earthquake_events (
 event_id TEXT PRIMARY KEY, event_time TIMESTAMPTZ NOT NULL, updated_time TIMESTAMPTZ,
 magnitude DOUBLE PRECISION, magnitude_type TEXT, place TEXT, longitude DOUBLE PRECISION NOT NULL,
 latitude DOUBLE PRECISION NOT NULL, depth_km DOUBLE PRECISION, felt INTEGER, cdi DOUBLE PRECISION,
 mmi DOUBLE PRECISION, alert TEXT, status TEXT, tsunami SMALLINT, significance INTEGER, network TEXT,
 event_code TEXT, event_type TEXT, station_count INTEGER, distance_minimum DOUBLE PRECISION,
 rms DOUBLE PRECISION, azimuthal_gap DOUBLE PRECISION, location_source TEXT, magnitude_source TEXT,
 event_url TEXT, api_detail_url TEXT, ids TEXT, sources TEXT, types TEXT, products JSONB,
 raw_payload JSONB NOT NULL, location geometry(Point,4326) NOT NULL, kafka_topic TEXT,
 kafka_partition INTEGER, kafka_offset BIGINT, ingested_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 CONSTRAINT valid_latitude CHECK (latitude BETWEEN -90 AND 90),
 CONSTRAINT valid_longitude CHECK (longitude BETWEEN -180 AND 180)
);
CREATE INDEX IF NOT EXISTS idx_eq_event_time ON raw.earthquake_events(event_time DESC);
CREATE INDEX IF NOT EXISTS idx_eq_magnitude ON raw.earthquake_events(magnitude);
CREATE INDEX IF NOT EXISTS idx_eq_depth ON raw.earthquake_events(depth_km);
CREATE INDEX IF NOT EXISTS idx_eq_location ON raw.earthquake_events USING GIST(location);
CREATE INDEX IF NOT EXISTS idx_eq_place ON raw.earthquake_events USING GIN(place gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_eq_alert ON raw.earthquake_events(alert);
CREATE TABLE IF NOT EXISTS reference.countries (
 country_id BIGSERIAL PRIMARY KEY, iso_alpha2 CHAR(2) UNIQUE, iso_alpha3 CHAR(3) UNIQUE NOT NULL,
 country_name TEXT NOT NULL, region TEXT, subregion TEXT, geometry geometry(MultiPolygon,4326) NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_countries_geometry ON reference.countries USING GIST(geometry);
