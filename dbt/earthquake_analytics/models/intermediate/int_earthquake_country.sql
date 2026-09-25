select e.*,c.iso_alpha3 as country_code,c.country_name,c.region,c.subregion from {{ ref('stg_earthquake_events') }} e left join {{ ref('stg_countries') }} c on st_contains(c.geometry,e.location)
