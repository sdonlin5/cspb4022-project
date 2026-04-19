import pandas as pd
from pathlib import Path

def file_to_list(file_path: str) -> list[str]:
    # reads lines from file and returns as a list
    # used to read in columns

    path = Path(file_path).expanduser()

    if path.exists():
        # read txt file line by line in the text file 
        output = [ 
            line for line in path.read_text().splitlines()
            # if line -> if there is a valid string
            # .strip() -> remove any whitespace and empty strings
            if line.strip() and not line.startswith('#')
            ]
    else: 
        raise FileNotFoundError

    return output
