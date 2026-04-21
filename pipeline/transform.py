from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import polars as pl

def select_dimensions(raw_data: pl.DataFrame, cols: list) -> pl.DataFrame:
    ''' Select a subset of columns from a polars dataframe. '''
    from polars import col    
    output = raw_data.select(col(cols))
    return output

