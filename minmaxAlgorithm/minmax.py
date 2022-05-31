inf = 1000;

import numpy as np


def neighbor_points(x, y):
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


def get_childeren(x, y):
    res = []
    for [a, b] in neighbor_points(x, y):
        if 0 <= a <= 13 and b >= 0 and b <= 13:
            res.append((a, b))
    return res;


def theSituation(board):
    res = 0;
    for i in range(0, 12):
        for j in range(0, 12):
            if (board[i][j] == 1):
                if (i % 2 == 0 and j % 2 == 1):
                    res += 1
                else:
                    res -= 1
    return res


class MinMax():
    def minMax(self, board, depth, maximizingPlayer, x, y):
        if depth == 1:
            return theSituation(board)
        if maximizingPlayer:
            value = -inf;
            for a, b in get_childeren(x, y):
                value = max(value, self.minMax(board, depth - 1, False, a, b))
            return value;
        value = inf;
        for a, b in get_childeren(x, y):
            value = max(value, self.minMax(board, depth - 1, True, a, b))
        return value;


v = MinMax()
board1 = np.zeros((13, 13))
board1[1][1] = 1;
board1[2][4] = 1;
print(v.minMax(board1, 2, True, 10, 10))
