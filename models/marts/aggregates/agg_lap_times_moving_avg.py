import pandas as pd

def model(dbt, session):
    dbt.config(packages=['pandas'])

    lap_times = dbt.ref('mrt_lap_times_years').to_pandas()

    lap_times['LAP_TIME_SECONDS'] = lap_times['LAP_TIME_MILLISECONDS']/1000
    lap_time_trends = lap_times.groupby(by='RACE_YEAR')['LAP_TIME_SECONDS'].mean().to_frame()
    lap_time_trends['LAP_MOVING_AVG_5_YEARS'] = lap_time_trends['LAP_TIME_SECONDS'].rolling(5).mean()
    lap_time_trends.reset_index(inplace=True)
    lap_time_trends.columns = lap_time_trends.columns.str.upper()

    return lap_time_trends.round(1)
