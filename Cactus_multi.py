# 仙人掌种植、收获, 多无人机版
# 种: Entities.Cactus
# 收: Items.Cactus
from directions import *
import utils
import go

_Entitie = Entities.Cactus
_Item = Items.Cactus
side = get_world_size()


def sort(XorY):
    if XorY == "X":
        XorY = (right, left)
    elif XorY == "Y":
        XorY = (up, down)
    for i in range(side - 1, 0, -1):
        flag = False
        for _ in range(i):
            if measure() > measure(XorY[0]):
                swap(XorY[0])
                flag = True
            move(XorY[0])
        go.edge(XorY[1])
        if not flag:
            break
    return True


def sort_X():
    return sort("X")


def sort_Y():
    return sort("Y")


def _plant():
    for _ in range(side):
        utils._till()
        utils._plant(_Entitie)
        move(up)


def run():
    go.to()
    for _ in range(max_drones()):
        if not spawn_drone(_plant):
            _plant()
        move(right)
    go.to()
    move_val = up
    for fn in [sort_X, sort_Y]:
        for _ in range(max_drones()):
            if not spawn_drone(fn):
                fn()
            move(move_val)
        while True:
            if num_drones() == 1:
                break
        move_val = right

    utils._harvest()
    return _Item


if __name__ == "__main__":

    while True:
        run()
        if utils.out(_Item, 1 * utils.B):
            break
