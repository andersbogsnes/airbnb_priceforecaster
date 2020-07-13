import pathlib

BASE_PATH = pathlib.Path(__file__).parents[2]
DATA_PATH = BASE_PATH / "data"

RAW_DATA_PATH = DATA_PATH / "raw"
INTERIM_DATA_PATH = DATA_PATH / "interim"
PROCESSED_DATA_PATH = BASE_PATH / "processed"
