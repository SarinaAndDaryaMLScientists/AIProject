# Darya Taghva
import main3
from tkinter import *
from tkinter import messagebox

# from Phase2MinMax.FinalMinMaxAlgorithmForHiveGame import FinalMinMaxAlgorithmForHiveGame
from logic.Player import Player
import networkx as nx
import numpy as np

p1 = Player("yellow")
p2 = Player("blue")
move_count = 1
move_count_map = np.zeros((13, 13))

tk = Tk()
grid = main3.HexagonalGrid(tk, scale=50, grid_width=8, grid_height=8)
xAxisInput = Text(tk, height=2, width=2, bg="light yellow")
yAxisInput = Text(tk, height=2, width=2, bg="light yellow")
xmvfirst = Text(tk, height=2, width=2, bg="light blue")
xmvsecond = Text(tk, height=2, width=2, bg="light blue")
ymvfirst = Text(tk, height=2, width=2, bg="light blue")
ymvsecond = Text(tk, height=2, width=2, bg="light blue")
typeTxt = Text(tk, height=2, width=2, bg="light yellow")

turn = False
mv_cnt = 0
board_size = 8
game_graph = nx.Graph()
valid_moves = set()
is_taken = []
game_page = []

aiPlayer = Player()


def get_peice_value(bee_type):
    if bee_type == 'Q':
        return 50
    elif bee_type == 'A':
        return 30
    elif bee_type == 'S':
        return 10
    return 20


def pieces_value():
    global game_page
    score = 0
    for i in range(board_size):
        for j in range(board_size):
            for a in game_page[i][j]:
                ai_piece = 1
                if a.color == 'blue':
                    ai_piece = -1
                score += ai_piece * get_peice_value(a.bee_type)
    return score


def huristicValue(): #todo
    return pieces_value()


insect_types = ['Q', 'A', 'S', 'G', 'B']


def get_all_insert_moves():
    ls = []
    for i in range(board_size):
        for j in range(board_size):
            for insect_type in insect_types:
                if is_valid_insert(i, j, insect_type):
                    ls.append(('insert', i, j, insect_type))
    return ls


def get_all_movements():
    ls = []
    for x1 in range(board_size):
        for y1 in range(board_size):
            if is_taken[x1][y1] and game_page[x1][y1][len(game_page[x1][y1]) - 1].color == get_current_player().color:
                for x2 in range(board_size):
                    for y2 in range(board_size):
                        if is_valid_move(x1, y1, x2, y2):
                            ls.append(('move', x1, y1, x2, y2))


def get_all_moves():
    return get_all_insert_moves() + get_all_movements()


def do_move(mv):
    if mv[0] == 'insert':
        logical_insert(mv[1], mv[1], mv[3])
    else:
        change_place_on_board(mv[1], mv[2], mv[3], mv[4], False)


def undo_move(mv):
    if mv[0] == 'insert':
        logical_remove(mv[1], mv[2])
    else:
        change_place_on_board(mv[3], mv[4], mv[1], mv[2], False)


def minmax(depth):
    if depth == 7:
        return huristicValue()
    global game_page
    moves = get_all_moves()
    score = 'nan'
    mx = 0
    for mv in moves:
        do_move(mv)
        currScore = minmax(depth + 1)
        undo_move(mv)
        if score == 'nan':
            score = currScore
        if depth % 2 == 0:
            score = max(score, currScore)
        else:
            score = min(score, currScore)
    return score


def check_game_finished():
    for x in range(board_size):
        for y in range(board_size):
            for a in game_page[x][y]:
                if a.bee_type == 'Q':
                    # print("game finished ", x, y)
                    flag = True
                    for x1, y1 in neighbor_points(x, y):
                        if not is_taken[x1][y1]:
                            flag = False
                    if flag:
                        print("game Over")
                        if a.color == "yellow":
                            messagebox.showerror("", "Game Over. blue wins ")
                        else:
                            messagebox.showerror("", "Game Over. yellow wins ")


def is_inside(x, y):
    x = int(x)
    y = int(y)
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
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


def check_queen_placed(a):
    if a == 1:
        return p1.is_queen_placed
    return p2.is_queen_placed


def is_valid_type(insect_type):
    if insect_type == 'Q' or insect_type == 'B' or insect_type == 'G' or insect_type == 'S' or insect_type == 'A':
        if has_enough_number_of_this_kind(insect_type):
            if move_count == 7 and insect_type != 'Q':
                return check_queen_placed(1)
            if move_count == 8 and insect_type != 'Q':
                return check_queen_placed(2)
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
    return board_size * x + y


def graph_is_connected_connection_check(x, y):
    global is_taken
    global move_count
    if move_count == 1:
        return True
    for [u, v] in neighbor_points(x, y):
        if 0 <= u < board_size and 0 <= v < board_size:
            if is_taken[u][v]:
                return True
    print("graph connection problem")
    messagebox.showerror("graph connection problem")
    return False


def graph_is_connected_color_check(x, y):
    curr_clr = get_current_player().color
    global game_page
    for [u, v] in neighbor_points(x, y):
        if is_inside(u, v):
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


def get_neighbor_index(x, y, t):
    if t == 0:
        return [x - 1, y]
    elif t == 1:
        return [x + 1, y]
    elif t == 2:
        if y % 2 == 0:
            return [x - 1, y - 1]
        else:
            return [x, y - 1]
    elif t == 3:
        if y % 2 == 0:
            return [x, y - 1]
        else:
            return [x + 1, y - 1]
    elif t == 4:
        if y % 2 == 0:
            return [x - 1, y + 1]
        else:
            return [x, y + 1]
    else:
        if y % 2 == 0:
            return [x, y + 1]
        else:
            return [x + 1, y + 1]


def is_valid_insert(x, y, insect_type):
    global valid_moves
    global move_count

    try:
        if not is_inside(x, y):
            print("error in x & y")
            messagebox.showerror("", "X&Y ERR")
            return False

        x = int(x)
        y = int(y)
        if not is_valid_type(insect_type):
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


def graphical_insert(x, y, insect_type):
    current_clr = 'blue'
    if turn:
        current_clr = 'yellow'
    grid.setCell(x, y, txt=insect_type, fill=current_clr)
    print("graphical insert completed")


class LogicalHexagon(object):
    def __init__(self, bee_type, color):
        self.bee_type = bee_type
        self.color = color


def logical_insert(x, y, insect_type):
    global is_taken
    global game_page
    p = get_current_player()
    game_page[x][y].append(LogicalHexagon(insect_type, p.color))
    p.use_one_piece(insect_type)
    is_taken[x][y] = True
    global game_graph
    game_graph.add_node(get_num(x, y))
    for a, b in neighbor_points(x, y):
        if is_taken[a][b]:
            game_graph.add_edge(get_num(x, y), get_num(a, b))


def insert_on_board(x, y, bee_type):
    graphical_insert(x, y, bee_type)
    logical_insert(x, y, bee_type)


def insert_piece():
    global turn
    # if turn:
    #     print("wait for your turn")
    #     return
    global xAxisInput
    global yAxisInput
    global typeTxt
    # global turn
    global move_count
    global move_count_map
    x = xAxisInput.get("1.0", "end-1c")
    y = yAxisInput.get("1.0", "end-1c")
    type = typeTxt.get("1.0", "end-1c")
    type, y, x = input().split()
    print(x, y, type)
    # print(x, y, type)
    if not is_valid_insert(x, y, type):
        return

    x = int(x)
    y = int(y)
    insert_on_board(x, y, type)
    check_game_finished()
    turn = not turn
    move_count = move_count + 1
    AI_move()


def current_place_is_valid(x1, y1):
    if not is_inside(x1, y1):
        print('x, y problem')
        return False
    if not is_taken[x1][y1]:
        print("is not taken")
        return False
    if game_page[x1][y1][len(game_page[x1][y1]) - 1].color != get_current_player().color:
        print("not color")
        return False
    return True


def other_place_is_valid(x2, y2):
    if not is_inside(x2, y2):
        return False
    if is_taken[x2][y2]:
        return False
    return True


def type_movement_possible_for_specific_bee(x1, y1, x2, y2):
    global game_page
    current_bee_type = game_page[x1][y1][len(game_page[x1][y1]) - 1].bee_type
    if current_bee_type == 'Q' or current_bee_type == 'B':
        print("Q or B")
        for nx1, ny1 in neighbor_points(x1, y1):
            if nx1 == x2 and ny1 == y2:
                return True
        return False
    elif current_bee_type == 'A':
        return True
    elif current_bee_type == 'S':
        for nx1, ny1 in neighbor_points(x1, y1):
            if not is_taken[nx1][ny1]:
                for nx2, ny2 in neighbor_points(nx1, ny1):
                    if not is_taken[nx2][ny2]:
                        for nx3, ny3 in neighbor_points(nx2, ny2):
                            if not is_taken[nx3][ny3]:
                                if nx3 == x2 and ny3 == y2:
                                    return True
        return False
    elif current_bee_type == 'G':
        for t in range(6):
            a = get_neighbor_index(x1, y1, t)
            while is_inside(a[0], a[1]) and is_taken[a[0]][a[1]]:
                a = get_neighbor_index(x1, y1, t)
            if a[0] == x2 and a[1] == y2:
                return True
        return False
    else:
        return False


def remove_hexagon_from_screen(x, y):
    grid.setCell(x, y, fill='white')
    global game_graph
    game_graph.remove_node(get_num(x, y))


def safe_to_remove_node(x1, y1):
    global game_graph
    copy_graph = game_graph.copy()
    copy_graph.remove_node(get_num(x1, y1))
    if nx.is_connected(copy_graph):
        return True
    return False


def safe_to_insert_node(x2, y2):
    global game_graph
    copy_graph = game_graph.copy()
    copy_graph.add_node(get_num(x2, y2))
    for [u, v] in neighbor_points(x2, y2):
        if is_taken[u][v]:
            copy_graph.add_edge(get_num(x2, y2), get_num(u, v))
    return nx.is_connected(copy_graph)


def is_valid_change(x1, y1, x2, y2):
    if not type_movement_possible_for_specific_bee(x1, y1, x2, y2):
        return False  # this means that if bee is queen can it move to that place? or ...
    if not safe_to_remove_node(x1, y1):
        print('unsafe to remove')
        return False
    if not safe_to_insert_node(x2, y2):
        print("unsafe to insert")
        return False
    return True


def is_valid_move(x1, y1, x2, y2):
    try:
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if not current_place_is_valid(x1, y1):
            print("current bee invalid")
            return False
        if not other_place_is_valid(x2, y2):
            print("other bee invalid")
            return False
        if not is_valid_change(x1, y1, x2, y2):
            print("invalid change")
            return False
        return True
    except ValueError:
        return False


def logical_remove(x, y):

    global game_page
    t = game_page[x][y].pop().bee_type
    if len(game_page[x][y]) == 0:
        is_taken[x][y] = False
    get_current_player().return_one_piece(t)
    global game_graph
    game_graph.remove_node(get_num(x, y))


def change_place_on_board(x1, y1, x2, y2, graphical = True):
    global is_taken
    global game_page
    bee_type = game_page[x1][y1][len(game_page[x1][y1] - 1)]
    if graphical:
        remove_hexagon_from_screen(x1, y1)
        graphical_insert(x2, y2, bee_type)
    logical_remove(x1, y1)
    logical_insert(x2, y2, bee_type)


aiPlaying = False


def AI_move():
    global turn
    global move_count
    best_move = minmax()
    if best_move.move_type == 'insert':
        insert_on_board(best_move.x1, best_move.y1, best_move.piece_type)
    else:
        change_place_on_board(best_move.x1, best_move.y1, best_move.x2, best_move.y2)
    turn = not turn
    move_count = move_count + 1
    check_game_finished()


def move_piece():
    global aiPlaying
    if aiPlaying:
        print("AI is playing!")
        print("wait for your turn")
        return
    global turn
    global xmvfirst
    global xmvsecond
    global ymvfirst
    global ymvsecond
    x2 = xmvfirst.get("1.0", "end-1c")
    x1 = xmvsecond.get("1.0", "end-1c")
    y2 = ymvfirst.get("1.0", "end-1c")
    y1 = ymvsecond.get("1.0", "end-1c")
    y1, x1, y2, x2 = input().split()
    print("x1", x1, "y1", y1, "x2", x2, "y2", y2)
    if not is_valid_move(x1, y1, x2, y2):
        print("invalid move")
        return
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    change_place_on_board(x1, y1, x2, y2)
    global move_count
    turn = not turn
    move_count = move_count + 1
    check_game_finished()
    aiPlaying = True
    AI_move()
    aiPlaying = False


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


def init_game_logic():
    global game_page
    global is_taken
    game_page = [[[] for j in range(board_size)] for i in range(board_size)]
    is_taken = [[False for j in range(board_size)] for i in range(board_size)]

    # print("is taken")
    # print(is_taken)


if __name__ == '__main__':
    make_board()
    init_game_logic()
    tk.mainloop()
