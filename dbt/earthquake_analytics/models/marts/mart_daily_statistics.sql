select event_date,count(*) event_count,avg(magnitude) average_magnitude,max(magnitude) largest_magnitude,count(*) filter(where tsunami=1) tsunami_events from {{ ref('fct_earthquakes') }} group by 1
