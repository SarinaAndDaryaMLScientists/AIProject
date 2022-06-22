import enum

import numpy as np

# print("hi")
# from Phase2MinMax.MinMaxImple import MinMaxAlgorithm1232
from Phase2MinMax.BoardThings import BoardThings

row = 4
col = 4
insectType = np.zeros((13, 13))

class BeeKind(enum.Enum):
    QueenBee = 1
    Ant = 2
    Spider = 3
    Grasshopper = 4
    Beetle = 5


print("debug")


# minMax = MinMaxAlgorithm1232()


def neighbor_points(x, y):
    res = []
    if x % 2 == 1:
        if y % 2 == 0:
            res = [[x - 1, y], [x + 1, y], [x - 1, y - 1], [x, y - 1],
                   [x - 1, y + 1], [x, y + 1]]
        else:
            res = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1], [x + 1, y + 1], [x + 1, y - 1]]
    else:
        if y % 2 == 1:
            res = [[x, y + 1], [x + 1, y + 1], [x - 1, y], [x + 1, y], [x, y - 1], [x + 1, y - 1]]
        else:
            res = [[x, y + 1], [x - 1, y + 1], [x - 1, y], [x + 1, y], [x, y - 1], [x - 1, y - 1]]

    return res


def findHumanScore(board1):
    counter = 0
    for i in range(0, row):
        for j in range(0, col):
            if board1[i][j] == 11:
                for u in neighbor_points(i, j):
                    print(u)
                    # # print(a, b)
                    # if 0 <= a < row and 0 <= b < col:
                    #     if board1[a][b] != 0 and board1[a][b] > 10:
                    #         counter = counter + 1
                return counter


# 11 0 0
def findAIScore(board1):
    counter = 0
    for i in range(0, row):
        for j in range(0, col):
            if board1[i][j] == 1:
                for a, b in neighbor_points(i, j):
                    if 0 <= a < row and 0 <= b < col:
                        if board1[a][b] != 0 and board1[a][b] < 10:
                            counter = counter + 1
                return counter


def getMaterialScore(board1):
    humanScore = findHumanScore(board1)
    AIScore = findAIScore(board1)
    return humanScore, AIScore


def hasAtLeastOneNeighbor(board1, i, j):
    for a, b in neighbor_points(i, j):
        if 0 <= a < row and 0 <= b < col:
            print(i, j)
            if board1[a][b] != 0:
                return True
    return False


def allNeighborsAreTheSameColor(i, j, color):
    for a, b in neighbor_points(i, j):
        if colors[a][b] != color:
            return False
        return True


class AIAgent(object):
    def getAllAvailablePlacements(self, board1):
        res = []
        for i in range(0, row):
            for j in range(0, col):
                if hasAtLeastOneNeighbor(board1, i, j) and allNeighborsAreTheSameColor(board1, i, j):
                    res.append(('insert', i, j))
        return res

    def getAllAvailableMovements(self, board):
        # todo
        return []

    def __init__(self):
        self.materialScore = 0
        self.is_queen_placed = False
        self.remainingPieces = {
            BeeKind.QueenBee: 1, BeeKind.Spider: 2, BeeKind.Ant: 3, BeeKind.Grasshopper: 3,
            BeeKind.Beetle: 2
        }
        self.usedPieces = {

        }

    def evaluate(self, board, maximizingClr):
        humanScore, ourScore = getMaterialScore(board)
        if maximizingClr == 'W':
            return humanScore - ourScore
        else:
            return ourScore - humanScore

    def gameResult(self, board):
        pass

    def makeChoice(self, board):
        print("ai is making choice")
        choice = self.minMaxAlgorithmMakeChoice(board)
        if choice[0] == 'insert':
            board[choice[1]][choice[2]] = getNumber(choice[3])
        else:
            board[choice[3]][choice[4]] = board[choice[1]][choice[2]]
            board[choice[1]][choice[2]] = 0
        print(board)

    def minMaxAlgorithmMakeChoice(self, board):

        # return insert or move if insert return beeType, position if move return the place to start move and the
        # place to end move.
        validMovesAndPlaces = self.getAvailableMovesAndPlaces(board)
        print(validMovesAndPlaces)
        return 'insert', 1, 1, 'q'
        return 'move', 0, 0, 1, 1

    def getAvailableMovesAndPlaces(self, board):
        return self.getAllAvailablePlacements(board) + self.getAllAvailableMovements(board)


def getNumber(insectType):
    if insectType == 'q':  # queen bee
        return 1
    if insectType == 'a':  # soldier ant
        return 2
    if insectType == 's':  # spider
        return 3
    if insectType == 'g':  # grasshopper
        return 4
    if insectType == 'b':  # beetle
        return 5


class InteractiveHumanPlayer(object):
    def __init__(self):
        self.color = 'black'
        self.materialScore = 0
        self.is_queen_placed = False
        self.remainingPieces = {
            BeeKind.QueenBee: 1, BeeKind.Spider: 2, BeeKind.Ant: 3, BeeKind.Grasshopper: 3,
            BeeKind.Beetle: 2
        }
        self.usedPieces = {

        }

    def makeChoice(self, board):
        kindPlay = input("please enter your move type: m for move p for placement")
        if kindPlay == 'p':
            insectType = input("please enter the kind of insect you wish to place")
            x = int(input("please enter location x of your insect"))
            y = int(input("please enter y location of your insect"))
            board[x][y] = getNumber(insectType) + 10

            print(board)
        else:
            print("move is not implemented yet, please wait")


humanPlayer = InteractiveHumanPlayer()
AI = AIAgent()
colors = np.zeros((row, col))
boardMain = np.zeros((row, col))
turn = True


def getIndex(board, param):
    for i in range(row):
        for j in range(col):
            if board[i][j] == param:
                return i, j
    return -1, -1


def countValidNeighbors(board, x, y):
    counter = 0
    for i, j in neighbor_points(x, y):
        if 0 <= i <= row and 0 <= j <= col:
            if board[i][j] != 0:
                counter = counter + 1
    return counter


def getGameResult(board):
    x, y = getIndex(board, 11)
    x1, y1 = getIndex(board, 1)
    if x1 == -1 or x == -1:
        return 0  # har 2 taraf malake hashoono nazashtan.
    if countValidNeighbors(board, x, y) == 6:
        return 1
    elif countValidNeighbors(board, x1, y1) == 6:
        return -1
    return 0


if __name__ == '__main__':
    while True:
        # 1 = WE WON -1 AI 0 HANOOZ TAMOOM NASHODE -3 MOSAVI -5Hameja por shode vli dor malake ha khalie.
        gameFinished = getGameResult(boardMain)
        if gameFinished != 0:
            print("game finished")
            print(gameFinished)
            break
        if turn:
            AI.makeChoice(boardMain)
        else:
            humanPlayer.makeChoice(boardMain)
        turn = not turn
import random
# from BoardThings import *


def huristic(board, color):  # todo todo todo warning:
    # Dore queen tarafe moghabel por she bedoon inke dore queen ma por she.
    # tedade kasayi ke dor queen AI an - tedad kasaii ke dor queen oonykian.
    pass


class MinMaxAlgorithm1232:
    def __init__(self):

        self.parent = {}

    def minMax(self, board, depth, alpha, beta, maximizingPlayer, maximizingColor):
        b = BoardThings()
        gameResult = b.getGameResults(board)
        if gameResult != 0:
            return gameResult
        if depth == 0:
            return huristic(board, maximizingColor)
        moves = b.getMoves(board, maximizingColor)
        bestMove = random.choice(moves)
        inf = 10000
        if maximizingPlayer:
            maxEvl = -inf
            for mv in moves:
                b.makeMove(mv, board)
                ceval = self.minMax(board, depth - 1, alpha, beta, False, maximizingColor)[1]
                b.undoMove(mv, board)
                if ceval > maxEvl:
                    maxEvl = ceval
                    bestMove = mv
                alpha = max(alpha, ceval)
                if beta <= alpha:
                    break
            return bestMove, maxEvl

        else:
            minEval = inf
            for mv in moves:
                b.makeMove(mv, board)
                ceval = self.minMax(board, depth - 1, alpha, beta, True, maximizingColor)[1]
                b.undoMove(mv, board)
                if ceval < minEval:
                    minEval = ceval
                    bestMove = mv
                beta = min(beta, minEval)
                if beta <= alpha:
                    break
                return bestMove, minEval


minMax = MinMaxAlgorithm1232()