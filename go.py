from direction import *


def to(x=0, y=0):
    if get_pos_x() < x:
        while get_pos_x() != x:
            if not move(right):
                return False
    else:
        while get_pos_x() != x:
            if not move(left):
                return False

    if get_pos_y() < y:
        while get_pos_y() != y:
            if not move(up):
                return False
    else:
        while get_pos_y() != y:
            if not move(down):
                return False


def edge(x=None, y=None):
    if x == None:
        x = get_pos_x()
        if y == up:
            y = get_world_size() - 1
        elif y == down:
            y = 0
    elif y == None:
        y = get_pos_y()
        if x == right:
            x = get_world_size() - 1
        elif x == left:
            x = 0
    to(x, y)


if __name__ == "__main__":
    to()