import asyncio
from database.db import create_tables, drop_all
from pipeline.extract import (
    extract_pbp, 
    extract_participation, 
    extract_charting, 
    extract_schedules
)
from pipeline.transform import (
    transform_play, 
    transform_schedule, 
    transform_situation 
)
from pipeline.load import load_data

async def main() -> None:

    print("Clearing database.")
    await drop_all()
    
    print("Initializing database tables...")
    await create_tables()

    # Get data from nflverse 
    print("Extracting NFLverse data...")
    raw_charting = extract_charting()
    raw_pbp = extract_pbp()
    raw_schedule = extract_schedules()
    raw_participation = extract_participation()

    # generate lazy execution plans 
    print("Transforming data...")
    play_plan = transform_play(raw_pbp, raw_charting, raw_participation)
    situation_plan = transform_situation(raw_pbp, raw_charting)
    schedule_plan = transform_schedule(raw_schedule)

    # materialize dataframes
    print("Materializing DataFrames for loading...")
    play = play_plan.collect()
    situation = situation_plan.collect()
    schedule = schedule_plan.collect()

    # write to database
    print("Loading play data to PostgreSQL database...")
    load_data(play, 'play')
    print("Loading situation data to PostgreSQL database...")
    load_data(situation, 'situation')
    print("Loading schedule data to PostgreSQL database...")
    load_data(schedule, 'schedule')

    print("Data pipeline complete!")



if __name__ == '__main__':
    asyncio.run(main())


    