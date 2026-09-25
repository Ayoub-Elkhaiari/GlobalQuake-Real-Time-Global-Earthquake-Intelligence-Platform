select magnitude_band,count(*) event_count,avg(depth_km) average_depth_km from {{ ref('fct_earthquakes') }} group by 1
