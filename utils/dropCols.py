import pandas as pd
from pathlib import Path

def to_list(file_path: str) -> list[str]:
    # returns list from line separated .txt file

    path = Path(file_path).expanduser()
    if path.exists():
        output = [ 
            line for line in path.read_text().splitlines()
            # remove whitespace and empty lines
            # if line: if valid string then strip() 
            # ignore comments
            if line.strip() and not line.startswith('#') 
            ]
    else: 
        raise FileNotFoundError
    return output

def drop_cols(df: pd.DataFrame, file: str) -> pd.DataFrame:
    # takes line separated list of columns in .txt file to drop
    # returns dataframe
     
    cols = to_list(file) 
    return df.drop(columns=cols)
    
