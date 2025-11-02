# 仙人掌种植、收获, 多无人机版
# 种: Entities.Cactus
# 收: Items.Cactus
from directions import *
import utils
import go


def sort(XorY):
    if XorY == "X":
        XorY = (right, left)
    elif XorY == "Y":
        XorY = (up, down)
    for i in range(utils.side - 1, 0, -1):
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


def run():
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
    return Items.Cactus


if __name__ == "__main__":

    def foo():
        for _ in range(utils.side):
            utils._till()
            utils._plant(Entities.Cactus)
            move(up)

    for _ in range(max_drones()):
        if not spawn_drone(foo):
            foo()
        move(right)
    run()
