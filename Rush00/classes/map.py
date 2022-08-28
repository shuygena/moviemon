import random
from Rush00.settings.game_data import *
from classes.moviemon import Moviemon


class Monster:
    def __init__(self,
                 row,
                 column,
                 value):
        self.row = row
        self.column = column
        self.value = value
        self.caught = 0

    def __float__(self):
        return self.value


class Map:
    def __init__(self,
                 moviemons):
        self.map = self.init_map()
        self.pos = START_PNT
        self.mons = self.link_mons(moviemons, self.map)

    def get_captured(self) -> [Monster]:
        result = []
        for i in self.mons:
            if i.caught != 0:
                result.append(i)
        return result

    def monsteur(self):
        random.choice([i for i, x in enumerate(self.mons) if x.caught == 0])

    @staticmethod
    def link_mons(mons, mmap) -> [Monster]:
        monsters = []
        i = 0
        for line in mmap:
            column = line.index(2)
            monsters.append(Monster(i, column, random.choice(list(mons))))
            i += 1
        return monsters

    @staticmethod
    def init_map():
        mmap = [[0 for _ in range(10)] for _ in range(10)]
        for i in mmap:
            yy = random.randrange(0, 9)
            i[yy] = 2
            if i[9 - yy] != 2:
                i[9 - yy] = 3
        return mmap
        