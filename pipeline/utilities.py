import os 
from dotenv import load_dotenv
from pathlib import Path

def get_dimension_path():
    # Loads the environment variable for the dimension definitions
    load_dotenv()
    path = Path(str(os.getenv('DIMENSIONS_DIR')))
    return path

def get_dimensions(source: str) -> list: 
    load_dotenv()
    #path = Path(str(os.getenv('DIMENSIONS_DIR')))
    file = Path(str(os.getenv('DIMENSIONS_DIR')), (source + ".txt"))
    #print(file)
    try:
        if file.exists():
           #print(f'Reading from: {file}') 
            output = [
                line for line in file.read_text().splitlines()
                if line.strip() and not line.startswith('#')
            ]
            #print(f'\n Found {len(output)} dimensions in {file}:\n')
            #print(output, '\n')
            return output
    except ValueError: 
        print(f'File not found: {file}')