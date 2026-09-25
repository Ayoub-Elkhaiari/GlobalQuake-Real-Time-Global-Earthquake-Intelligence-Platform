select * from {{ ref('fct_earthquakes') }} where event_time_utc >= now() - interval '30 days'
