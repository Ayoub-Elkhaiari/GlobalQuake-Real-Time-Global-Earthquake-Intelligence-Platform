from sqlalchemy import text
from sqlalchemy.orm import Session
def global_statistics(db:Session):
 q='''SELECT count(*) FILTER (WHERE event_time >= now()-interval '24 hours') last_24_hours,count(*) FILTER (WHERE event_time >= now()-interval '7 days') last_7_days,count(*) FILTER (WHERE event_time >= now()-interval '30 days') last_30_days,max(magnitude) largest_magnitude,avg(magnitude) average_magnitude,avg(depth_km) average_depth_km,count(*) FILTER (WHERE tsunami=1) tsunami_events,count(*) FILTER (WHERE felt IS NOT NULL AND felt>0) felt_event_count FROM raw.earthquake_events'''
 return dict(db.execute(text(q)).mappings().one())
def grouped(db,kind):
 if kind=='countries': q="SELECT coalesce(c.country_name,'Unmapped') AS label,count(*) AS value FROM raw.earthquake_events e LEFT JOIN reference.countries c ON ST_Contains(c.geometry,e.location) GROUP BY 1 ORDER BY 2 DESC LIMIT 15"
 elif kind=='magnitude': q="SELECT CASE WHEN magnitude < 2 THEN '<2' WHEN magnitude < 4 THEN '2–3.9' WHEN magnitude < 6 THEN '4–5.9' ELSE '6+' END label,count(*) value FROM raw.earthquake_events GROUP BY 1 ORDER BY 1"
 else:q="SELECT date_trunc('day',event_time) AS label,count(*) AS value FROM raw.earthquake_events WHERE event_time >= now()-interval '30 days' GROUP BY 1 ORDER BY 1"
 return [dict(x) for x in db.execute(text(q)).mappings()]
