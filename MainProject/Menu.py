import main3
from tkinter import *
import networkx as nx
import enum
import numpy as np
import matplotlib.pyplot as plt

row = 8
col = 8
arr = np.zeros((row, col), dtype=int)
whitebees = []
blackbees = []
moves = []
print(arr)

tk = Tk()

xAxisInput = Text(tk, height=2, width=2, bg="light yellow")

yAxisInput = Text(tk, height=2, width=2, bg="light yellow")
beeSelectBtn = Text(tk, height=2, width=2, bg="light yellow")
grid = main3.HexagonalGrid(tk, scale=50, grid_width=8, grid_height=8)

turn = False
gx = nx.Graph()
gy = nx.Graph()
clr = 'yellow'
mv_cnt = 0


def neighbor_points(x, y):

    res = [[x - 1, y, 'N'], [x + 1, y, 'N'], [x - 1, y - 1, 'N'], [x, y - 1, 'N'], [x - 1, y + 1, 'N'], [x, y + 1, 'N']]
    return res



def onSubmitMove():
    global clr
    beeKind = beeSelectBtn.get("1.0", "end-1c")
    x = xAxisInput.get("1.0", "end-1c")
    y = yAxisInput.get("1.0", "end-1c")
    try:
        x = int(x)
        if x > 7 or x < 0:
            raise ValueError("x is more than MAXX")
    except ValueError:
        print("x is not int")
        return
    try:
        y = int(y)
        if y > 7 or y < 0:
            raise ValueError("y is more than MAXY")
    except ValueError:
        print("y is not int")
        return
    global mv_cnt
    if mv_cnt == 0:
        print("first move place it wherever you want")
        grid.setCell(x, y, txt=beeKind, fill=clr)
        mv_cnt = mv_cnt + 1
        moves.append(neighbor_points(x, y))
        moves.append([x, y, 'T'])
        # print(moves)
    else:
        pass

    if clr == 'yellow':
        clr = 'blue'
    else:
        clr = 'yellow'


def drawGraph():
    nx.draw(gx)
    plt.show()
    nx.draw(gy)
    plt.show()


if __name__ == '__main__':
    grid.grid(row=0, column=0, padx=0, pady=0)
    btn = Button(tk, height=2, text='submit move', bg='#66ff66', command=onSubmitMove)
    xAxisInput.grid(row=10, column=10)
    yAxisInput.grid(row=10, column=9)
    beeSelectBtn.grid(row=10, column=8)
    btn.grid(row=10, column=7)

    tk.mainloop()

# todo set neighbors
# grid.setCell(2, 2, fill='green', txt='2,2')
# grid.setCell(2, 1, fill='gold', txt='2,1')
# grid.setCell(2, 3, fill='gold', txt='2,3')
# grid.setCell(3, 2, fill='gold', txt='3,2')
# grid.setCell(1, 2, fill='gold', txt='1,2')
# grid.setCell(2, 3, fill='gold', txt='2,3')
# grid.setCell(1, 3, fill='gold', txt='1, 3')
# grid.setCell(1, 1, txt='1,1', fill='gold')
# grid.setCell(0, 1, txt='0,1', fill = 'red')
# grid.setCell(1, 0, txt='1, 0', fill='red')
# grid.setCell(2, 0, txt='2, 0', fill = 'red')
