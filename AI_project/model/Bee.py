import enum


class BeeKind(enum.Enum):
    QueenBee = 0
    Cockroch = 1
    Malakh = 2
    Spider = 3
    Ant = 4


class BeeMove():
    @staticmethod
    def canMove(bekind, x1, y1, x2, y2):
        return False  # todo implement bee movement


class Bee:
    def __init__(self, beekind, color):
        self.beekind = beekind
        self.color = color

