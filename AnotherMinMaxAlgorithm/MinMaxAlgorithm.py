import random
import numpy as np

from Phase2MinMax.MinMaxFunctionForHiveSimpleImplementation import BoardThings


def huristic(board, color): #todo todo todo warning:
    #Dore queen tarafe moghabel por she bedoon inke dore queen ma por she.
    #tedade kasayi ke dor queen AI an - tedad kasaii ke dor queen oonykian.
    pass
class MinMaxAlgorithm():
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
