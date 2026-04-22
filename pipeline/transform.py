from __future__ import annotations
from typing import TYPE_CHECKING
from pathlib import Path
import os 
from dotenv import load_dotenv

if TYPE_CHECKING:
    import polars as pl
    from pathlib import Path


def load_cols(source_name: str) -> list:
    ''' 
    Searches data definition directory and returns columns required from .txt file as a list. 

    Ex. load_cols('pbp') searches definition files and returns columns required from 'pbp' dataframe
    '''
    load_dotenv()
    file = Path(str(os.getenv('DIMENSIONS_DIR')), source_name+".txt")

    if file.exists():
        cols = [line for line in file.read_text().splitlines()
                if line.strip() and not line.startswith('#')
                ]    
    return cols

def select_dimensions(raw_data: pl.LazyFrame, cols: list) -> pl.LazyFrame:
    ''' Select a subset of columns from a polars dataframe. '''
    output = raw_data.select(cols)
    return output


def transform_play(raw_pbp, raw_participation, raw_charting) -> pl.LazyFrame:
    ''' Cre '''
    
    pbp = raw_pbp.select([ 'game_id', 'play_id', 'yds_gained', 'rush_attempt', 'rush_touchdown', 'run_location', 'run_gap', 'pass_attempt', 'complete_pass', 'pass_touchdown', 'interception', 'air_yards', 'yards_after_catch','pass_location', 'qb_kneel', 'qb_spike', 'qb_dropback', 'qb_scramble', 'sack'
        ])
    
    charting = raw_charting.select(['nflverse_game_id', 'qb_location', 'is_drop', 'play_action', 'screen_pass', 'qb_sneak', 'trick_play', 'n_pass_rushers', 'n_blitzers'])

    participation = raw_participation.select(['nflverse_game_id', 'offense_positions', 'route', 'was_pressure', 'defenders_in_box', 'defense_man_zone_type', 'defense_coverage_type'])    
    
    result = (pbp.join(charting, left_on = 'game_id', 
                        right_on = 'nflverse_game_id', how = 'left').join(
                            participation, left_on = 'game_id', 
                            right_on = 'nflverse_game_id',how = 'left'
                            ))
    return result 


def merge_situation(pbp_lf, charting_lf) -> pl.LazyFrame: 
    ''' Merges data for situation table. '''

    pbp = pbp_lf.select(['game_id', 'play_id', 'game_id', 'posteam', 'yardline_100', 'quarter_seconds_remaining', 'down', 'goal_to_go', 'ydstogo'
        ])
    
    charting = charting_lf.select(['nflverse_game_id','starting_hash'])

    result = (pbp.join(charting, left_on = 'game_id', 
                       right_on = 'nflverse_game_id', how = 'left'
                       ))
    return result




def clean_pbp(raw_pbp: pl.LazyFrame, raw_participation: pl.LazyFrame,
                   raw_charting: pl.LazyFame):
    path = './data/dimension_definitions/pbp.txt'
    cols = load_cols(path)
    pbp_df = select_dimensions(raw_pbp, cols) # selects the column


    path = './data/dimension_definitions/pbp.txt'
    cols = load_cols(path)
    pbp_df = select_dimensions(raw_pbp, cols) # selects the columns

    return pbp_df

    


