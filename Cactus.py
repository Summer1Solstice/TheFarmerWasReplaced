# 仙人掌种植、收获
# 种: Entities.Cactus
# 收: Items.Cactus
from direction import *
import utils
import go


def run(way):
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


if __name__ == "__main__":
    
        import go

    if not utils.plough(utils.cycle()):        
        go.to()
    utils.loop(run, utils.cycle(), 10 * utils.K)
