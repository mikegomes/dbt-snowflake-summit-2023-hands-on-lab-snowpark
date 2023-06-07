with
    lap_times as (
        select
            {{ dbt_utils.generate_surrogate_key(["race_id", "driver_id", "lap"]) }}
            as lap_times_id,
            race_id,
            driver_id,
            lap,
            driver_position,
            lap_time_formatted,
            official_laptime,
            lap_time_milliseconds
        from {{ ref("stg_lap_times") }}
    )

select *
from lap_times
