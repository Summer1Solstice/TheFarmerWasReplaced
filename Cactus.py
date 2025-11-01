# 仙人掌种植、收获
# 种: Entities.Cactus
# 收: Items.Cactus
from directions import *
import utils
import go


def v1(way):
    for _ in way:
        plant(Entities.Cactus)
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
            if measure() > measure(right) and x != utils.side - 1:
                flag = True
                swap(right)
            if measure() > measure(up) and y != utils.side - 1:
                flag = True
                swap(up)
            move(i)
        if not flag:
            utils.shou_huo()
            go.to()
    return Items.Cactus


def v2(way):  # 耗时比v1长，v了个什么玩意
    go.to()
    for i in way:
        plant(Entities.Cactus)
        move(i)
    go.to()
    # set_execution_speed(1)
    for _ in range(utils.side):  # x
        for i in range(utils.side - 1, 0, -1):
            flag = False
            for _ in range(i):
                if measure() > measure(right):
                    swap(right)
                    flag = True
                move(right)
            go.edge(left)
            if not flag:
                break
        move(up)

    for _ in range(utils.side):  # y
        for i in range(utils.side - 1, 0, -1):
            flag = False
            for _ in range(i):
                if measure() > measure(up):
                    swap(up)
                    flag = True
                move(up)
            go.edge(down)
            if not flag:
                break
        move(right)
    utils.shou_huo()
    return Items.Cactus


def run(way):
    return v1(way)


if __name__ == "__main__":
    # set_world_size(6)
    utils.update()
    if not utils.plough(utils.cycle()):
        go.to()
    run(utils.cycle())
    # utils.loop(run, utils.cycle(), 10 * utils.K)
