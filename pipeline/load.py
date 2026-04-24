import os
from dotenv import load_dotenv
import polars as pl


def load_data(data: pl.DataFrame, table_name: str) -> None:
    ''' Loads polars dataframe to postgres database '''
    database_url = os.getenv('LOAD_URL')

    if not database_url:
        raise ValueError('DATABASE_URL environment variable not set.')
    
    data.write_database(
        table_name,
        connection=database_url, 
        if_table_exists='append',
        engine='adbc'
    )


