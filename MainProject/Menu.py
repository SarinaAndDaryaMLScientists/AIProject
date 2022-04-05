import main3
from tkinter import *
import networkx as nx
import enum
import numpy as np
import matplotlib.pyplot as plt
import anothertest.graphHashmap as ghashdict

from MainProject.logic.BeeModel import *
from MainProject.logic.Bee import *


def get_num(x, y):
    return ghashdict.inv_map[x, y]


row = 8
col = 8
yellowQueenPlaced = False
blueQueenPlaced = False
counter = 1
arr = np.zeros((row, col), dtype=int)
takenHomes = {}
colors_arr = {}


def initfirst():
    clrarrcnt = 0
    for i1 in range(0, 8):
        for j1 in range(0, 8):
            colors_arr[get_num(i1, j1)] = '?'
            clrarrcnt = clrarrcnt + 1
    for i in range(0, row):
        for j in range(0, col):
            takenHomes[get_num(i, j)] = False


yellowbees = {
    BeeKind.QueenBee: 1, BeeKind.Spider: 2, BeeKind.Ant: 3, BeeKind.Grasshopper: 3,
    BeeKind.Beetle: 2
}
bluebees = {
    BeeKind.QueenBee: 1, BeeKind.Spider: 2, BeeKind.Ant: 3, BeeKind.Grasshopper: 3,
    BeeKind.Beetle: 2
}
moves = []
# print(arr)

tk = Tk()

# UI ELEMENT
xAxisInput = Text(tk, height=2, width=2, bg="light yellow")

yAxisInput = Text(tk, height=2, width=2, bg="light yellow")
xmvfirst = Text(tk, height=2, width=2, bg="light blue")
xmvsecond = Text(tk, height=2, width=2, bg="light blue")
ymvfirst = Text(tk, height=2, width=2, bg="light blue")
ymvsecond = Text(tk, height=2, width=2, bg="light blue")

beeSelectBtn = Text(tk, height=2, width=2, bg="light yellow")
grid = main3.HexagonalGrid(tk, scale=50, grid_width=8, grid_height=8)

turn = False
g = nx.Graph()
clr = 'yellow'
mv_cnt = 0


def neighbor_points(x, y):
    res = [[x - 1, y], [x + 1, y], [x - 1, y - 1], [x, y - 1],
           [x - 1, y + 1], [x, y + 1]]
    return res


def validate_beekind(BeeKind1):
    global clr
    if clr == 'yellow':
        if BeeKind1 == BeeKind.QueenBee:
            for k, v in yellowbees.items():
                if k == BeeKind.QueenBee:
                    v = v - 1
                    del yellowbees[k]
                    if v >= 0:
                        yellowbees[k] = v
                        return True
                    else:
                        return False
        elif BeeKind1 == BeeKind.Beetle:
            for k, v in yellowbees.items():
                if k == BeeKind.Beetle:
                    v = v - 1
                    del yellowbees[k]
                    if v >= 0:
                        yellowbees[k] = v
                    else:
                        return False
                    return True
        elif BeeKind1 == BeeKind.Ant:
            for k, v in yellowbees.items():
                if k == BeeKind.Beetle:
                    v = v - 1
                    del yellowbees[k]
                    if v >= 0:
                        yellowbees[k] = v
                    else:
                        return False
                    return True
        elif BeeKind1 == BeeKind.Spider:
            for k, v in yellowbees.items():
                if k == BeeKind.Spider:
                    v = v - 1
                    del yellowbees[k]
                    if v >= 0:
                        yellowbees[k] = v
                    else:
                        return False
                    return True
        elif BeeKind1 == BeeKind.Grasshopper:
            for k, v in yellowbees.items():
                if k == BeeKind.Grasshopper:
                    v = v - 1
                    del yellowbees[k]
                    if v >= 0:
                        yellowbees[k] = v
                    else:
                        return False
                    return True
    else:
        if BeeKind1 == BeeKind.QueenBee:
            for k, v in bluebees.items():
                if k == BeeKind.QueenBee:
                    v = v - 1
                    del bluebees[k]
                    if v >= 0:
                        bluebees[k] = v
                    else:
                        return False
                    return True
        elif BeeKind1 == BeeKind.Beetle:
            for k, v in bluebees.items():
                if k == BeeKind.Beetle:
                    v = v - 1
                    del bluebees[k]
                    if v >= 0:
                        bluebees[k] = v
                    else:
                        return False
                    return True
        elif BeeKind1 == BeeKind.Ant:
            for k, v in bluebees.items():
                if k == BeeKind.Beetle:
                    v = v - 1
                    del bluebees[k]
                    if v >= 0:
                        bluebees[k] = v
                    else:
                        return False
                    return True
        elif BeeKind1 == BeeKind.Spider:
            for k, v in bluebees.items():
                if k == BeeKind.Spider:
                    v = v - 1
                    del bluebees[k]
                    if v >= 0:
                        bluebees[k] = v
                    else:
                        return False
                    return True
        elif BeeKind1 == BeeKind.Grasshopper:
            for k, v in bluebees.items():
                if k == BeeKind.Grasshopper:
                    v = v - 1
                    del bluebees[k]
                    if v >= 0:
                        bluebees[k] = v
                    else:
                        return False
                    return True


def validate_x_y(x, y):
    if 0 <= x <= 8 and 0 <= y <= 8:
        return True
    else:
        return False


def validate(BeeKind1, clr, x, y):
    return validate_beekind(BeeKind1) and validate_x_y(x, y)
    # validates Beekind based on color.


def add_all_neighbors_to_graph(x, y):
    global g  # the graph that i'm using in this project.
    a = get_num(x, y)
    g.add_node(a)
    if x > 0:
        b = get_num(x - 1, y)
        if takenHomes[b]:
            g.add_edge(a, b)
    if x < 7:
        b = get_num(x + 1, y)
        if takenHomes[b]:
            g.add_edge(a, b)
    if x > 0 and y > 0:
        b = get_num(x - 1, y - 1)
        if takenHomes[b]:
            g.add_edge(a, b)
    if y > 0:
        b = get_num(x, y - 1)
        if takenHomes[b]:
            g.add_edge(a, b)
    if x > 0 and y < 7:
        b = get_num(x - 1, y + 1)
        if takenHomes[b]:
            g.add_edge(a, b)
    if y < 7:
        b = get_num(x, y + 1)
        if takenHomes[b]:
            g.add_edge(a, b)


def noSameClrNeighbor(x, y):
    if x > 0 and takenHomes[get_num(x - 1, y)] and not (colors_arr[get_num(x - 1, y)] == clr):
        return False
    if x < 7 and takenHomes[get_num(x + 1, y)] and not (colors_arr[get_num(x + 1, y)] == clr):
        return False
    if x > 0 and y > 0 and takenHomes[get_num(x - 1, y - 1)] and not (colors_arr[get_num(x - 1, y - 1)] == clr):
        return False
    if y > 0 and takenHomes[get_num(x, y - 1)] and not (colors_arr[get_num(x, y - 1)] == clr):
        return False
    if x > 0 and y < 7 and takenHomes[get_num(x - 1, y + 1)] and not (colors_arr[get_num(x - 1, y + 1)] == clr):
        return False
    if y < 7 and takenHomes[get_num(x, y + 1)] and not (colors_arr[get_num(x, y + 1)]):
        return False
    return True


def onSubmitMove():
    global clr
    beeKindStr = beeSelectBtn.get("1.0", "end-1c")
    beeKind = 'N'
    # print(beeKindStr)
    if beeKindStr == 'Q':
        beeKind = BeeKind.QueenBee
    elif beeKindStr == 'B':
        beeKind = BeeKind.Beetle
    elif beeKindStr == 'G':
        beeKind = BeeKind.Grasshopper
    elif beeKindStr == 'S':
        beeKind = BeeKind.Spider
    elif beeKindStr == 'A':
        beeKind = BeeKind.Ant

    x = xAxisInput.get("1.0", "end-1c")
    y = yAxisInput.get("1.0", "end-1c")
    print(x, y)
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
    global counter
    global yellowQueenPlaced
    global blueQueenPlaced
    if mv_cnt == 0:
        if validate(beeKind, clr, x, y):
            if beeKind == BeeKind.QueenBee:
                if clr == 'yellow':
                    yellowQueenPlaced = True
                else:
                    blueQueenPlaced = True
            print("first move place it wherever you want")
            grid.setCell(x, y, txt=beeKindStr, fill=clr)
            mv_cnt = mv_cnt + 1
            for q in neighbor_points(x, y):
                if not takenHomes[get_num(x, y)]:
                    moves.append([q[0], q[1]])
                g.add_node(get_num(x, y))
            add_all_neighbors_to_graph(x, y)
            takenHomes[get_num(x, y)] = True
            colors_arr[get_num(x, y)] = clr
            if clr == 'yellow':
                clr = 'blue'
            else:
                clr = 'yellow'
            # print(moves)
        else:
            print("unable to validate beekind, Make sure that you placed the right bee")
    else:
        if mv_cnt == 7:
            if not yellowQueenPlaced:
                if not (beeKind == BeeKind.QueenBee):
                    print("you should place your queen at this move!")
                    return

        if mv_cnt == 8:
            if not blueQueenPlaced:
                if not (beeKind == BeeKind.QueenBee):
                    print("you should place your queen at this move!")
                    return
        if mv_cnt == 1:
            print(moves) #todo delete
            if validate(beeKind, clr, x, y):
                if not takenHomes[get_num(x, y)] and [x, y] in moves:
                    grid.setCell(x, y, txt=beeKindStr, fill=clr)
                    for q in neighbor_points(x, y):
                        if not takenHomes[get_num(x, y)]:
                            moves.append([q[0], q[1]])
                    if [x, y] in moves:
                        moves.remove([x, y])
                    mv_cnt = mv_cnt + 1
                    takenHomes[get_num(x, y)] = True
                    print("success")
                    colors_arr[get_num(x, y)] = clr
                    if clr == 'yellow':
                        clr = 'blue'
                    else:
                        clr = 'yellow'
                    return
        else:
            print(noSameClrNeighbor(x, y))
            if validate(beeKind, clr, x, y) and noSameClrNeighbor(x, y):
                if not takenHomes[get_num(x, y)] and [x, y] in moves:
                    grid.setCell(x, y, txt=beeKindStr, fill=clr)
                    for q in neighbor_points(x, y):
                        if not takenHomes[get_num(x, y)]:
                            moves.append([q[0], q[1]])
                    if [x, y] in moves:
                        moves.remove([x, y])
                    mv_cnt = mv_cnt + 1
                    takenHomes[get_num(x, y)] = True
                    print("success")
                    if clr == 'yellow':
                        clr = 'blue'
                    else:
                        clr = 'yellow'
                    return

        print("failed! line 271")

    # Here the turns change


def onMove(args):
    pass


if __name__ == '__main__':
    initfirst();
    grid.grid(row=0, column=0, padx=0, pady=0)
    btn = Button(tk, height=2, text='Create new bee', bg='#66ff66', command=onSubmitMove)
    btn2 = Button(tk, height=2, text="edit bee place", bg='#66ff66', command=onMove)
    xAxisInput.grid(row=10, column=10)
    yAxisInput.grid(row=10, column=9)
    beeSelectBtn.grid(row=10, column=8)
    xmvfirst.grid(row=10, column=6)
    ymvfirst.grid(row=10, column=5)
    xmvsecond.grid(row=10, column=4)
    ymvsecond.grid(row=10, column=3)

    btn.grid(row=10, column=7)
    btn2.grid(row=10, column=2)

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
