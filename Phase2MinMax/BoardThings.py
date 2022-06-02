# from MainProject.Phase1 import findHumanScore
from Phase2MinMax.MinMaxFunctionForHiveSimpleImplementation import *


def isMoveAblePiece(u):
    return True # todo


def get_available_moves(u):
    return [] #todo



class BoardThings():
    def getGameResults(self, board1):
        if findAIScore(board1) == 6:
            if findHumanScore(board1) == 6:
                return 0
            else:
                return -1
        return 1

    def getMoves(self, board, maximizingColor):
        # tamame mohre hayi k hastan tamame harkatashoon.
        selections = []
        moves = []
        for i in range(0, row):
            for j in range(0, col):
                if hasAtLeastOneNeighbor(board, i, j):
                    if allNeighborsAreTheSameColor(i, j, maximizingColor):
                        selections.append(('select', i, j))
        if maximizingColor == humanPlayer.color:
            for u in humanPlayer.usedPieces:
                if isMoveAblePiece(u):  # todo
                    moves.append(get_available_moves(u))
        else:
            for u in AI.usedPieces:
                if isMoveAblePiece(u):
                    moves.append(get_available_moves(u))  # todo
        return moves