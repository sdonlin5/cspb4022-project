import nflreadpy as nfl
import polars as pl



def pbp(seasons: list = None) -> pl.DataFrame:
    # Extract play by play data from NFLverse
    # Default = 2025 season, if no list
    if seasons: 
        return nfl.load_pbp(seasons)
    else: 
        return nfl.load_pbp()

def schedules(seasons: list = None) -> pl.DataFrame: 
    # Extract schedule data from NFLverse
    # Default = 2025 season, if no list
    if seasons: 
        return nfl.load_schedules(seasons)
    else: 
        return nfl.load_schedules()

def participation(seasons: list = None) -> pl.DataFrame: 
    # Extract player participation data from NFLverse
    # Default = 2025 season, if no list
    if seasons: 
        return nfl.load_participation(seasons)
    else: 
        return nfl.load_participation()

def chart(seasons: list = None) -> pl.DataFrame:
    # Extract charting data from NFLverse
    # Default = 2025 season, if no list
    # Data avialable from 2022
    if seasons: 
        # only pass available seasons (from 2022)
        available_seasons = [s for s in seasons if s >= 2022]
        return nfl.load_ftn_charting(available_seasons)
    else: 
        return nfl.load_ftn_charting()

