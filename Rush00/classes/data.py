import random
from typing import Dict, List

from classes.map import Monster
from classes.map import Map
from classes.moviemon import Moviemon
from my_funcs.get_started import *
from Rush00.settings.game_data import *


class Data:
    def __init__(self):
        self.map = None
        self.captured: List[str] = []
        self.pos: list = START_PNT
        self.size: tuple = GRID_SIZE
        self.moviballs: int = START_BAL
        self.moviemons: Dict[str, Moviemon] = {}

    def dump(self):
        return {
            "pos": self.pos,
            "captured": self.captured,
            "map": self.map,
            "moviemons": self.moviemons,
            "moviballs": self.moviballs
        }

    def get_random_movie(self) -> Monster:
        return self.map.monsteur

    def get_movie(self, name):
        return self.map.get_movie(name)

    @staticmethod
    def load(settings):
        data = Data()
        data.pos = settings["pos"]
        data.moviballs = settings["moviballs"]
        data.moviemons = settings["moviemons"]
        data.captured = settings["captured"]
        data.map = settings["map"]

    @staticmethod
    def load_default_settings():
        data = Data()
        data.moviemons = get_info()
        data.map = Map(data.moviemons)
        data.captured = data.map.get_captured()
        return data

    def get_strength(self) -> int:
        if self.captured is not None:
            return 1
        else:
            return sum(self.map.get_captured())

