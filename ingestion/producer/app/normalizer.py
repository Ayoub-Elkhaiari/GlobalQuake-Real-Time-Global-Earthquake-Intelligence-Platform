from datetime import UTC, datetime
from typing import Any

def _timestamp(value: Any) -> str | None:
    return datetime.fromtimestamp(value / 1000, tz=UTC).isoformat().replace("+00:00", "Z") if value is not None else None

def normalize(feature: dict[str, Any]) -> dict[str, Any]:
    props, geometry = feature.get("properties", {}), feature.get("geometry", {})
    coordinates = geometry.get("coordinates") or []
    if len(coordinates) < 3 or not feature.get("id"):
        raise ValueError("Feature requires id and [longitude, latitude, depth] coordinates")
    event = {
        "event_id": feature["id"], "event_time": _timestamp(props.get("time")),
        "updated_time": _timestamp(props.get("updated")), "magnitude": props.get("mag"),
        "magnitude_type": props.get("magType"), "place": props.get("place"),
        "longitude": coordinates[0], "latitude": coordinates[1], "depth_km": coordinates[2],
        "felt": props.get("felt"), "cdi": props.get("cdi"), "mmi": props.get("mmi"), "alert": props.get("alert"),
        "status": props.get("status"), "tsunami": props.get("tsunami"), "significance": props.get("sig"),
        "network": props.get("net"), "event_code": props.get("code"), "event_type": props.get("type"),
        "station_count": props.get("nst"), "distance_minimum": props.get("dmin"), "rms": props.get("rms"),
        "azimuthal_gap": props.get("gap"), "location_source": props.get("locationSource"),
        "magnitude_source": props.get("magSource"), "event_url": props.get("url"),
        "api_detail_url": props.get("detail"), "ids": props.get("ids"), "sources": props.get("sources"),
        "types": props.get("types"), "products": props.get("products"), "raw_payload": feature,
    }
    if event["event_time"] is None or not -90 <= event["latitude"] <= 90 or not -180 <= event["longitude"] <= 180:
        raise ValueError("Invalid event timestamp or coordinates")
    return event
