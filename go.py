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


def edge(side):
    if side == up:
        return to(get_pos_x(), get_world_size() - 1)
    if side == down:
        return to(get_pos_x(), 0)
    if side == left:
        return to(0, get_pos_y())
    if side == right:
        return to(get_world_size() - 1, get_pos_y())
    return False

if __name__ == "__main__":
    to()
