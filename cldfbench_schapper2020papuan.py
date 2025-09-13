import pathlib

import pyglottography


class Dataset(pyglottography.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "schapper2020papuan"
