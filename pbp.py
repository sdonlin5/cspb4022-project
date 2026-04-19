import nflreadpy as nfl
import utils as util
import polars as pl


def load_plays(seasons:list):
   # wrapper for load pbp function
   plays = nfl.load_pbp(seasons)
   return plays

def drop_play_cols(pbp_df: pl.DataFrame, drop_cols: list):
    # Drops columns from plays df based on list
    plays = pbp_df.drop(drop_cols)
    return plays

def get_play_cols(pbp_df: pl.DataFrame, cols: list): 
    # returns subset of pbp columns from list
    # used to get cols for tables
    
    df = pbp_df.select(cols)
    return df


