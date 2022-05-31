# Sarina Nemati
# Darya Taghva
# this is the main code which has been refactored.
import main3
from tkinter import *
from tkinter import messagebox
from MainProject.logic.Player import Player
import networkx as nx
import sets

p1 = Player("yellow")
p2 = Player("blue")
move_count = 1
arr_move_cnt = []
movecount_map = {}
# UI ELEMENTS

tk = Tk()
grid = main3.HexagonalGrid(tk, scale=50, grid_width=8, grid_height=8)
xAxisInput = Text(tk, height=2, width=2, bg="light yellow")
yAxisInput = Text(tk, height=2, width=2, bg="light yellow")
xmvfirst = Text(tk, height=2, width=2, bg="light blue")
xmvsecond = Text(tk, height=2, width=2, bg="light blue")
ymvfirst = Text(tk, height=2, width=2, bg="light blue")
ymvsecond = Text(tk, height=2, width=2, bg="light blue")
typeTxt = Text(tk, height=2, width=2, bg="light yellow")

#
turn = True
mv_cnt = 0

game_graph = nx.Graph()
valid_moves = set()
is_taken = []
game_page = []


def init_game_logic():
    global game_page
    global is_taken
    game_page = [[[] for j in range(8)] for i in range(8)]
    is_taken = [[False for j in range(8)] for i in range(8)]

    # print("is taken")
    # print(is_taken)


def _is_valid_x_and_y(x, y):
    try:
        x = int(x)
        y = int(y)
        if 0 <= x <= 7 and 0 <= y <= 7:
            return True
        return False
    except ValueError:
        messagebox.showerror("TYPE CASTING", "type casting of x and y failed")
        return False


def get_current_player():
    if turn:
        return p1
    return p2


def has_enough_number_of_this_kind(type1):
    p = get_current_player()
    if p.has_enough_piece(type1):
        return True
    return False


def checkQueenPlaced(a):
    if a == 1:
        return p1.is_queen_placed
    return p2.is_queen_placed


def _is_valid_type(insect_type):
    if insect_type == 'Q' or insect_type == 'B' or insect_type == 'G' or insect_type == 'S' or insect_type == 'A':
        if has_enough_number_of_this_kind(insect_type):
            if move_count == 7 and insect_type is not 'Q':
                return checkQueenPlaced(1)
            if move_count == 8 and insect_type is not 'Q':
                return checkQueenPlaced(2)
            return True

    return False


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


def get_num(x, y):
    x = int(x)
    y = int(y)
    return 2 * x + 5 * y + 1


def graph_is_connected_connection_check(x, y):
    global is_taken
    global move_count
    global game_graph
    if move_count == 1:
        return True
    for [u, v] in neighbor_points(x, y):
        if 0 <= u < 8 and 0 <= v < 8:
            if is_taken[u][v]:
                return True
    print("graph connection problem")
    messagebox.showerror("graph connection problem")
    return False


def graph_is_connected_color_check(x, y):
    curr_clr = get_current_player().color
    global game_page
    for [u, v] in neighbor_points(x, y):
        if _is_valid_x_and_y(u, v):
            if is_taken[u][v]:
                # print(game_page[u][v])
                # print(u, v)
                if game_page[u][v][len(game_page[u][v]) - 1].color != curr_clr:
                    # print(game_page[u][v][len(game_page[u][v]) - 1].color)
                    # print(u, v)
                    # print(game_page[u][v][0].color)
                    # print(len(game_page[u][v]) - 1)
                    # print(curr_clr)
                    return False
    return True


def getLeftIndex(x, y):
    return [x - 1, y]


def getRightIndex(x, y):
    return [x + 1, y]


def getLeftUpIndex(x, y):
    if x % 2 == 1:
        if y % 2 == 0:
            return [x - 1, y - 1]
        else:
            return [x, y - 1]
    else:
        if y % 2 == 1:
            return [x, y - 1]
        else:
            return [x - 1, y - 1]


def getRightUpIndex(x, y):
    if x % 2 == 1:
        if y % 2 == 0:
            return [x, y - 1]
        else:
            return [x + 1, y - 1]
    else:
        if y % 2 == 1:
            return [x + 1, y - 1]
        else:
            return [x, y - 1]


def getLeftDownIndex(x, y):
    if x % 2 == 1:
        if y % 2 == 0:
            return [x - 1, y + 1]
        else:
            return [x, y + 1]
    else:
        if y % 2 == 1:
            return [x, y + 1]
        else:
            return [x - 1, y + 1]


def getRightDownIndex(x, y):
    if x % 2 == 1:
        if y % 2 == 0:
            return [x, y + 1]
        else:
            return [x + 1, y + 1]
    else:
        if y % 2 == 1:
            return [x + 1, y + 1]
        else:
            return [x, y + 1]


def is_valid_insert(x, y, insect_type):
    global valid_moves
    global move_count

    try:
        if not _is_valid_x_and_y(x, y):
            print("error in x & y")
            messagebox.showerror("", "X&Y ERR")
            return False

        x = int(x)
        y = int(y)
        if not _is_valid_type(insect_type):
            print("type is not valid")
            messagebox.showerror("", "TYPE VALIDATION FAILED SUCCESSFULLY")
            return False
        # print(is_taken)
        if is_taken[x][y]:
            print("this house is taken")
            messagebox.showerror("Taken Error", "THIS HOUSE IS TAKEN")
            return False
        if not graph_is_connected_connection_check(x, y):
            messagebox.showerror("GRAPH", "CONNECTION PROBLEM OR COLOR PROBLEM")
            # messagebox.showerror("graph is not connected")
            print("graph is not connected")
            return False
        if move_count > 2 and not graph_is_connected_color_check(x, y):
            messagebox.showerror("", "color check failed!")
            print("color check failed ")
            return False
        return True

    except ValueError:
        print("error caught")
        return False


def _graphical_insert(x, y, insect_type):
    current_clr = 'blue'
    if turn:
        current_clr = 'yellow'

    grid.setCell(x, y, txt=insect_type, fill=current_clr)
    arr_move_cnt[x][y] = move_count
    messagebox.showinfo("GRAPHICAL INSERT COMPLETED!")
    print("graphical insert completed")


class Logical_Hexagon(object):
    def __init__(self, bee_type, color):
        self.bee_type = bee_type
        self.color = color


def _logical_insert(x, y, insect_type):
    global is_taken
    color = get_current_player().color
    global game_page
    game_page[x][y].append(Logical_Hexagon(insect_type, color))
    #
    # [] [Logical_Hex]
    #
    # print(x, y)
    # print(len(game_page[x][y]))
    # print(game_page[x][y][0].color)
    p = get_current_player()
    p.use_one_piece(insect_type)
    is_taken[x][y] = True


def insert_on_board(x, y, bee_type):
    _graphical_insert(x, y, bee_type)
    _logical_insert(x, y, bee_type)


def insert_piece():
    global turn
    if turn:
        print("wait for your turn")
        return
    global xAxisInput
    global yAxisInput
    global typeTxt
    # global turn
    global move_count
    global movecount_map
    x = xAxisInput.get("1.0", "end-1c")
    y = yAxisInput.get("1.0", "end-1c")
    type = typeTxt.get("1.0", "end-1c")
    # print(x, y, type)
    if not is_valid_insert(x, y, type):
        return

    x = int(x)
    y = int(y)
    insert_on_board(x, y, type)
    turn = not turn
    movecount_map[x, y] = move_count
    move_count = move_count + 1


def get_direction_index(n, x, y):
    if n == 0:
        return getLeftDownIndex(x, y)
    elif n == 1:
        return getRightDownIndex(x, y)
    elif n == 2:
        return getLeftIndex(x, y)
    elif n == 3:
        return getRightIndex(x, y)
    elif n == 4:
        return getLeftUpIndex(x, y)
    elif n == 5:
        return getRightUpIndex(x, y)


def current_place_is_valid(x1, y1):
    if not _is_valid_x_and_y(x1, y1):
        return False
    if not is_taken[x1][y1]:
        return False
    if game_page[x1][y1][len(game_page[x1][y1]) - 1].color != get_current_player().color:
        return False
    return True


def other_place_is_valid(x2, y2):
    if not _is_valid_x_and_y(x2, y2):
        return False
    if is_taken[x2][y2]:
        return False
    return True


indexArrCnt = 0
check_grasshopper = []


def whole_board_is_checked():
    global check_grasshopper
    for i in range(0, 8):
        for j in range(0, 8):
            if check_grasshopper[i][j] == [False]:
                return False
    return True


def reinitGrasshopper():
    indexArrCnt = 0
    check_grasshopper = []
    for i in range(0, 8):
        for j in range(0, 8):
            check_grasshopper[i][j] = [False]
    return False


def find_grassshoper(x1, y1, x2, y2):
    global indexArrCnt
    global check_grasshopper

    if whole_board_is_checked():
        reinitGrasshopper()

    a = getLeftDownIndex(x1, y1)
    if _is_valid_x_and_y(a[0], a[1]):
        check_grasshopper[a[0], a[1]] = [True]
        if not is_taken[a[0]][a[1]]:
            if [x2, y2] == a:
                reinitGrasshopper()
                return True
    find_grassshoper(a[0], a[1], x2, y2)

    b = getRightDownIndex(x1, y1)
    if _is_valid_x_and_y(b[0], b[1]):
        check_grasshopper[b[0]][b[1]] = [True]
        if not is_taken[b[0]][b[1]]:
            if [x2, y2] == b:
                reinitGrasshopper()
                return True
    find_grassshoper(b[0], b[1], x2, y2)
    c = getRightIndex(x1, y1)
    if _is_valid_x_and_y(c[0], c[1]):
        check_grasshopper[c[0][c[1]]] = [True]
        if not is_taken[c[0]][c[1]]:
            if [x2, y2] == c:
                reinitGrasshopper()
                return True
    find_grassshoper(c[0], c[1], x2, y2)
    d = getLeftIndex(x1, y1)
    if _is_valid_x_and_y(d[0], d[1]):
        check_grasshopper[d[0][d[1]]] = [True]
        if not is_taken[d[0]][d[1]]:
            if [x2, y2] == d:
                reinitGrasshopper()
                return True
    find_grassshoper(d[0], d[1], x2, y2)
    e = getLeftUpIndex(x1, y1)
    if _is_valid_x_and_y(e[0], e[1]):
        check_grasshopper[e[0]][e[1]] = [True]
        if not is_taken[e[0]][e[1]]:
            if [x2, y2] == e:
                reinitGrasshopper()
                return True
    find_grassshoper(e[0], e[1], x2, y2)

    f = getRightUpIndex(x1, y1)
    if _is_valid_x_and_y(f[0], f[1]):
        check_grasshopper[f[0]][f[1]] = [True]
        if not is_taken[f[0]][f[1]]:
            if [x2, y2] == e:
                reinitGrasshopper()
                return True


def type_movement_possible_for_specific_bee(x1, y1, x2, y2):
    global game_page
    current_bee_kind = game_page[x1][y1][len(game_page[x1][y1]) - 1].bee_kind
    if current_bee_kind == 'Q' or 'B':
        a = getLeftDownIndex(x1, y1)
        b = getRightDownIndex(x1, y1)
        c = getLeftIndex(x1, y1)
        d = getRightIndex(x1, y1)
        e = getLeftUpIndex(x1, y1)
        f = getRightUpIndex(x1, y1)
        if [x2, y2] == a or [x2, y2] == b or [x2, y2] == c or [x2, y2] == d or [x2, y2] == e or [x2, y2] == f:
            if current_bee_kind == 'B':
                return True
            return is_taken[x1][y1] and not is_taken[x2][y2]
        return False
    elif current_bee_kind == 'A':
        return True
    elif current_bee_kind == 'S':
        a = getLeftDownIndex(x1, y1)
        a = getLeftDownIndex(a[0], a[1])
        a = getLeftDownIndex(a[0], a[1])
        b = getRightDownIndex(x1, y1)
        b = getRightDownIndex(b[0], b[1])
        b = getRightDownIndex(b[0], b[1])
        c = getLeftIndex(x1, y1)
        c = getLeftIndex(c[0], c[1])
        c = getLeftIndex(c[0], c[1])
        d = getRightIndex(x1, y1)
        d = getRightIndex(d[0], d[1])
        d = getRightIndex(d[0], d[1])
        e = getLeftUpIndex(x1, y1)
        e = getLeftUpIndex(e[0], e[1])
        e = getLeftUpIndex(e[0], e[1])
        f = getRightUpIndex(x1, y1)
        f = getRightUpIndex(f[0], f[1])
        f = getRightUpIndex(f[0], f[1])
        if [x2, y2] == a or [x2, y2] == b or [x2, y2] == c or [x2, y2] == d or [x2, y2] == e or [x2, y2] == f:
            return True
        elif current_bee_kind == 'G':
            while_flag = True
            indexArrCnt = 0
            while while_flag:
                b = find_grassshoper(x1, y1, x2, y2)
                if not b:
                    break


def remove_hexagon_from_screen(n):
    # n is the number of the haxagon.
    # there is 8 because there is 6 edges, 1 color, 1 text
    for i in range(8 * n, 8 * n + 8):
        grid.delete(i)


def safe_to_remove_node(x1, y1):
    global game_graph
    cpygrph = game_graph.copy()
    cpygrph.remove_node(get_num(x1, y1))
    if nx.is_connected(cpygrph):
        return True
    return False


def safe_to_insert_node(x2, y2):
    global game_graph
    cpygrph = game_graph.copy()
    cpygrph.add_node(get_num(x2, y2))
    for [u, v] in neighbor_points(x2, y2):
        if is_taken[u][v]:
            cpygrph.add_edge(get_num(x2, y2), get_num(u, v))
    return nx.is_connected(cpygrph)


def _valid_change(x1, y1, x2, y2):
    if not type_movement_possible_for_specific_bee(x1, y1, x2, y2):
        return False  # this means that if bee is queen can it move to that place? or ...
    if not safe_to_remove_node(x1, y1):
        return False
    if not safe_to_insert_node(x2, y2):
        return False
    return True


def is_valid_move(x1, x2, y1, y2):
    try:
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if not current_place_is_valid(x1, y1):
            return False
        if not other_place_is_valid(x2, y2):
            return False
        if not _valid_change(x1, y1, x2, y2):
            return False
        return True
    except ValueError:
        return False


def change_place_on_board(x1, y1, x2, y2):
    global is_taken
    global arr_move_cnt
    remove_hexagon_from_screen(arr_move_cnt[x1][y1])
    grid.setCell(x2, y2)
    is_taken[x1][y1] = False
    is_taken[x2][y2] = True


def move_piece():
    global turn
    if turn:
        print("wait for your own turn")
        return
    global xmvfirst
    global xmvsecond
    global ymvfirst
    global ymvsecond
    x1 = xmvfirst.get("1.0", "end-1c")
    x2 = xmvsecond.get("1.0", "end-1c")
    y1 = ymvfirst.get("1.0", "end-1c")
    y2 = ymvsecond.get("1.0", "end-1c")
    if not is_valid_move(x1, x2, y1, y2):
        return
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    change_place_on_board(x1, y1, x2, y2)
    global move_count
    turn = not turn
    move_count = move_count + 1


def make_board():
    global xAxisInput
    global yAxisInput
    global typeTxt
    global xmvfirst
    global xmvsecond
    global ymvfirst
    global ymvsecond
    global grid
    xAxisInput = Text(tk, height=2, width=2, bg="light yellow")
    yAxisInput = Text(tk, height=2, width=2, bg="light yellow")
    xmvfirst = Text(tk, height=2, width=2, bg="light blue")
    xmvsecond = Text(tk, height=2, width=2, bg="light blue")
    ymvfirst = Text(tk, height=2, width=2, bg="light blue")
    ymvsecond = Text(tk, height=2, width=2, bg="light blue")
    typeTxt = Text(tk, height=2, width=2, bg="light yellow")
    grid.grid(row=0, column=0, padx=0, pady=0)
    btn = Button(tk, height=2, text='Create new bee', bg='#66ff66', command=insert_piece)
    btn2 = Button(tk, height=2, text="edit bee place", bg='#66ff66', command=move_piece)
    xAxisInput.grid(row=10, column=10)
    yAxisInput.grid(row=10, column=9)
    typeTxt.grid(row=10, column=8)
    xmvfirst.grid(row=10, column=6)
    ymvfirst.grid(row=10, column=5)
    xmvsecond.grid(row=10, column=4)
    ymvsecond.grid(row=10, column=3)

    btn.grid(row=10, column=7)
    btn2.grid(row=10, column=2)


if __name__ == '__main__':
    make_board()
    init_game_logic()
    tk.mainloop()
