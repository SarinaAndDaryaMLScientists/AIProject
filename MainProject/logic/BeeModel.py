from abc import ABC, abstractmethod
import networkx as nx




class BeeModel(ABC, object):
    def __init__(self, bee_clr, x, y):
        self.clr = bee_clr
        self.x = x
        self.y = y

    @abstractmethod
    def move(self, xprev, yprev, newx, newy):
        pass

    @abstractmethod
    def place(self, x, y):
        pass


class QueenBeeModel(BeeModel, object):
    def __init__(self, bee_clr, x, y):
        BeeModel.__init__(self, bee_clr, x, y)

    def move(self, xprv, yprv, xn, yn):
        pass

    def place(self, x, y):
        pass


class BeetleBee(BeeModel, object):
    # purple bees which can walk through one space.
    def __init__(self, bee_clr, x, y):
        BeeModel.__init__(self, bee_clr, x, y)

    def move(self, xprev, yprev, xn, yn):
        pass

    def place(self, x, y):
        pass


class GrassShopperBee(BeeModel, object):
    # can move 2 spaces
    def __init__(self, bee_clr, x, y):
        BeeModel.__init__(self, bee_clr, x, y)

    def move(self, xprev, yprev, xn, yn):
        pass

    def place(self, x, y):
        pass


class SpiderBee(BeeModel, object):
    # can move 3 spaces
    def __init__(self, bee_clr, x, y):
        BeeModel.__init__(self, bee_clr, x, y)

    def move(self, xprev, yprev, xn, yn):
        pass

    def place(self, x, y):
        pass


class SoldierAntBee(BeeModel, object):
    # can move literally anywhere based on some circumstances
    def __init__(self, bee_clr, x, y):
        BeeModel.__init__(self, bee_clr, x, y)

    def move(self, xprev, yprev, xn, yn):
        pass

    def place(self, x, y):
        pass
