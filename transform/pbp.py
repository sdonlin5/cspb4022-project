import polars as pl
import pandas as pd

def drop_cols(pbp_df: pl.DataFrame, drop_cols: list):
    new_df = pbp_df.drop(drop_cols)
    return new_df




