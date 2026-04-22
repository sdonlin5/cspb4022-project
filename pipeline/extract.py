''' 
Functions to load data and convert to polars lazyframe. 
'''

import nflreadpy as nfl
import polars as pl


def extract_pbp(seasons: list = None) -> pl.LazyFrame:
    ''' Extract play by play data from NFLverse, default = 2025 season '''
    if seasons:
        return nfl.load_pbp(seasons).lazy()
    else:
        return nfl.load_pbp().lazy()


def extract_schedules(seasons: list = None) -> pl.LazyFrame:
    ''' Extract schedule data from NFLverse, default = 2025 season'''
    if seasons: 
        return nfl.load_schedules(seasons).lazy()
    else: 
        return nfl.load_schedules().lazy()


def extract_participation(seasons: list = None) -> pl.LazyFrame:
    ''' Extract player participation data from NFLverse default = 2025 season '''
    if seasons:
        return nfl.load_participation(seasons).lazy()
    else:
        return nfl.load_participation().lazy()


def extract_charting(seasons: list = None) -> pl.LazyFrame:
    ''' Extract charting data from NFLverse, default = 2025 season, if no list. Data avialable from 2022 ''' 
    if seasons:
        # only pass available seasons (from 2022)
        available_seasons = [s for s in seasons if s >= 2022]
        return nfl.load_ftn_charting(available_seasons).lazy()
    else:
        return nfl.load_ftn_charting().lazy()
