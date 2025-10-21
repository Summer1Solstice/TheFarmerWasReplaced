from direction import *
def to(x=0, y=0):
    if get_pos_x() < x:
        while get_pos_x() != x:
            move(right)
    else:
        while get_pos_x() != x:
            move(left)

    if get_pos_y() < y:
        while get_pos_y() != y:
            move(up)
    else:
        while get_pos_y() != y:
            move(down)


if __name__ == "__main__":
    to()
    