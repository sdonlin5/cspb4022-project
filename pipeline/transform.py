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

def find_diff(subset_list, primary_list):
    output = []
    for i in subset_list:
        if i not in primary_list:
                output.append(i)
    return output


#def transform_play(raw_pbp,''' raw_participation, raw_charting''') -> pl.
def transform_play(raw_pbp, raw_charting, raw_participation) -> pl.LazyFrame:

    pbp_cols = ['game_id', 'play_id', 'yards_gained', 'rush_attempt', 'rush_touchdown', 'run_location', 'run_gap', 'pass_attempt', 'complete_pass','pass_touchdown', 'interception', 'air_yards', 'yards_after_catch','pass_location', 'qb_kneel', 'qb_spike', 'qb_dropback', 'qb_scramble', 'sack', 'penalty', 'aborted_play', 'special_teams_play']

    charting_cols = ['nflverse_game_id', 'nflverse_play_id', 'qb_location', 'is_drop', 'is_play_action', 'is_screen_pass', 'is_qb_sneak', 'is_trick_play', 'is_throw_away', 'n_pass_rushers', 'n_blitzers']
    
    participation_cols = ['nflverse_game_id', 'play_id', 'offense_positions', 'route', 'was_pressure', 'defenders_in_box', 'defense_man_zone_type', 'defense_coverage_type']


    # select subset of columns for play table
    pbp = raw_pbp.select(pbp_cols).filter(
         (pl.col('penalty') == 0) &
         (pl.col('aborted_play') == 0) & 
         (pl.col('special_teams_play') == 0)
         ).with_columns(
              pl.col('play_id').cast(pl.Int32)
              )
    
    charting = raw_charting.select(charting_cols).with_columns(
         pl.col('nflverse_play_id').cast(pl.Int32)
         )

    participation = raw_participation.select(participation_cols).with_columns(
         pl.col('play_id').cast(pl.Int32)
    )

    print('pbp schema: ', pbp.schema, '\n\n')
    print('charting schema: ', charting.schema, '\n\n')
    print('participation schema: ', participation.schema, "\n\n")

    joined = (pbp.join(
                charting, 
                left_on = ['game_id', 'play_id'],
                right_on = ['nflverse_game_id', 'nflverse_play_id'],
                how = 'left')
                .join(
                   participation, 
                   left_on = ['game_id', 'play_id'],
                   right_on = ['nflverse_game_id', 'play_id'],
                   how = 'left')
                )
    
    # boolean columns
    bool_cols = ['rush_attempt', 'rush_touchdown', 'pass_attempt', 
                 'complete_pass','pass_touchdown', 'interception', 'qb_kneel', 
                 'qb_spike', 'qb_dropback', 'qb_scramble', 'sack']
    
    name_map = {'is_play_action': 'play_action',
                'is_screen_pass': 'screen_pass',
                'is_qb_sneak': 'qb_sneak',
                'is_trick_play': 'trick_play'
                }
    
    result = joined.with_columns(
        # cast booleans
        pl.col(bool_cols).cast(pl.Boolean),

        # extract positions
        num_rb=(pl.col('offense_positions').str.count_matches('RB') + 
                pl.col('offense_positions').str.count_matches('FB'))
                .cast(pl.Int32),
        num_te=(pl.col('offense_positions').str.count_matches('TE'))
                .cast(pl.Int32),
        num_wr= (pl.col('offense_positions').str.count_matches('WR'))
                .cast(pl.Int32)
    ).rename(name_map).drop(
         ['offense_positions', 'penalty', 'aborted_play',
          'special_teams_play',])
    return result
