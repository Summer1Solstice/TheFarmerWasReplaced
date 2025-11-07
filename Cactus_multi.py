# 仙人掌种植、收获, 多无人机版
# 种: Entities.Cactus
# 收: Items.Cactus
from constants import *
import utils
import go

_Entitie = Entities.Cactus
_Item = Items.Cactus


def sort(XorY):
    for i in range(get_world_size() - 1, 0, -1):
        flag = False
        for _ in range(i):
            if measure() > measure(XorY[0]):
                swap(XorY[0])
                flag = True
            move(XorY[0])
        for _ in range(i):
            if measure() < measure(XorY[1]):
                swap(XorY[1])
                flag = True
            move(XorY[1])
        if not flag:
            break
    return True


def sort_X():
    return sort((right, left))


def sort_Y():
    return sort((up, down))


def run():
    utils._plant_multi(_Entitie)
    go.to()
    utils.Assign(sort_X, up)
    utils.Assign(sort_Y)
    utils._harvest()


def main():
    if not utils.UAVx32():
        return False
    clear()
    utils._till_multi()
    go.to()
    run()


if __name__ == "__main__":
    if utils.cost(_Entitie):
        main()
