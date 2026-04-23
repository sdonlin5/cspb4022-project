''' 
Functions to load data and convert to polars lazyframe. 
'''
import nflreadpy as nfl
import polars as pl
#from .utilities import get_dimensions

def extract_pbp(seasons: list = None) -> pl.LazyFrame:
    ''' Extract play by play data from NFLverse, default = 2025 season '''
    if seasons:
        df = nfl.load_pbp(seasons)
    else: 
        df = nfl.load_pbp()
    return df.lazy()

def extract_schedules(seasons: list = None) -> pl.LazyFrame:
    ''' Extract schedule data from NFLverse, default = 2025 season'''
    if seasons:
        df = nfl.load_schedules(seasons)
    else: 
        df = nfl.load_schedules()
    return df.lazy()

def extract_participation(seasons: list = None) -> pl.LazyFrame:
    ''' Extract player participation data from NFLverse default = 2025 season
    Available from 2016'''
    if seasons:
        available_seasons = [s for s in seasons if s >= 2016]
        df = nfl.load_participation(available_seasons)
    else:
        df =  nfl.load_participation()
    return df.lazy()


def extract_charting(seasons: list = None) -> pl.LazyFrame:
    ''' Extract charting data from NFLverse, default = 2025 season, if no list. Data avialable from 2022 ''' 
    if seasons:
        # only pass available seasons (from 2022)
        available_seasons = [s for s in seasons if s >= 2022]
        df = nfl.load_ftn_charting(available_seasons)
    else:
        df = nfl.load_ftn_charting()
    return df.lazy()
