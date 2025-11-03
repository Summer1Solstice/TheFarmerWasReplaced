# 仙人掌种植、收获
# 种: Entities.Cactus
# 收: Items.Cactus
from directions import *
import utils
import go

_Entitie = Entities.Cactus
_Item = Items.Cactus
side = get_world_size()


def run(way):
    for _ in way:
        plant(_Entitie)
        move(_)
    flag = True
    while flag:
        flag = False
        for i in way:
            x = get_pos_x()
            y = get_pos_y()
            if measure() < measure(left) and x != 0:
                flag = True
                swap(left)
            if measure() < measure(down) and y != 0:
                flag = True
                swap(down)
            if measure() > measure(right) and x != side - 1:
                flag = True
                swap(right)
            if measure() > measure(up) and y != side - 1:
                flag = True
                swap(up)
            move(i)
        if not flag:
            utils._harvest()
            go.to()
    return _Item


def main():
    way = utils.cycle()
    for i in way:
        utils._till()
        move(i)
    run(way)


if __name__ == "__main__":
    main()
