# todo when we want to insert there might be a slight chance that we have to insert for 2 nodes and
# todo and we don't know if the NODE is empty or NOT.
#ex: NW insertion, the next line could be neighbor with our North neighbor, How to Find that out?
class BeeKeeper:
    def __init__(self):
        self.n = None
        self.ne = None
        self.se = None
        self.s = None
        self.sw = None
        self.nw = None

    def insertNorth(self, b):
        if not self._has_neighborN():
            self.n = b
            b.s = self
        else:
            print("this node has neighbor")

    def insertNE(self, b):
        if not self._hasNeighborNE():
            self.ne = b
            b.sw = self
        else:
            print("this node has neighbor")

    def insertSE(self, b):
        if not self._hasNeighborSE():
            self.se = b
            b.nw = self
        else:
            print("this node has neighbor")

    def insertS(self, b):
        self.s = b
        b.n = self

    def insertSW(self, b):
        self.sw = b
        b.ne = self

    def insertNW(self, b):
        self.nw = b
        b.se = self

    def _has_neighborN(self):
        return self.n is not None

    def _hasNeighborNE(self):
        return self.ne is not None

    def _hasNeighborSE(self):
        return self.se is not None

    def _hasNeighborS(self):
        return self.s is not None

    def _hasNeighborSW(self):
        return self.sw is not None

    def _hasNeighborNW(self):
        return self.nw is not None
