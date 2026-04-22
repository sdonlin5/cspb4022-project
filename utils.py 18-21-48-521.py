import os 
from dotenv import load_dotenv
from pathlib import Path

def get_dimension_path():
    # Loads the environment variable for the dimension definitions
    load_dotenv()
    path = Path(str(os.getenv('DIMENSIONS_DIR')))
    return path


def load_dimensions():
    # Returns a dictionary of columns to be used with the data loaded as key
    # Ex. { play-by-play : ['play_id', 'game_id', 'down', 'distance'...] }
    dir = len(str(path)) + 1
    dimension_dict = {}

    for file in path.glob('*.txt'): 
        key = str(file)[dir:-4]
        dimension_dict[key] = [
            line for line in file.read_text().splitlines()
            if line.strip() and not line.startswith('#')
        ]
    return dimension_dict