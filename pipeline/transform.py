from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import polars as pl
    from pathlib import Path


def load_cols(path: str) -> list:
    ''' Returns a dictionary of columns to be used with the data loaded as key. Ex. { play-by-play : ['play_id', 'game_id', 'down', 'distance'...] } '''
    from pathlib import Path
    file = Path(path).expanduser()
    if file.exists():
        cols = [line for line in file.read_text().splitlines()
                if line.strip() and not line.startswith('#')
                ]
    
    return cols

def select_dimensions(raw_data: pl.LazyFrame, cols: list) -> pl.LazyFrame:
    ''' Select a subset of columns from a polars dataframe. '''
    output = raw_data.select(cols)
    return output


def merge_play_data(pbp_lf, participation_lf, charting_lf) -> pl.LazyFrame:
    ''' Merges data for the play table '''
    pbp = pbp_lf.select([ 'game_id', 'play_id', 'yds_gained', 'rush_attempt', 'rush_touchdown', 'run_location', 'run_gap', 'pass_attempt', 'complete_pass', 'pass_touchdown', 'interception', 'air_yards', 'yards_after_catch','pass_location', 'qb_kneel', 'qb_spike', 'qb_dropback', 'qb_scramble', 'sack'
        ])
    
    charting = charting_lf.select(['nflverse_game_id', 'qb_location', 'is_drop', 'play_action', 'screen_pass', 'qb_sneak', 'trick_play', 'n_pass_rushers', 'n_blitzers'])

    participation = participation_lf.select(['nflverse_game_id', 'offense_positions', 'route', 'was_pressure', 'defenders_in_box', 'defense_man_zone_type', 'defense_coverage_type'])    
    
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


def transform_play(raw_pbp: pl.DataFrame):
    path = './data/dimension_definitions/pbp.txt'
    cols = load_cols(path)
    #pbp_df = select_dimensions(raw_pbp, cols) # selects the column
    pbp_lf = raw_pbp.lazy()
    




















    
    path = './data/dimension_definitions/pbp.txt'
    cols = load_cols(path)
    pbp_df = select_dimensions(raw_pbp, cols) # selects the columns

    return pbp_df

    


