# 向日葵种植、收获
# 种: Entities.Sunflower
# 收: Items.Power
from directions import *
import utils
import go

_Entitie = Entities.Sunflower
_Item = Items.Power
side = get_world_size()
map = {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: []}


def _plant():
    global map

    def foo():
        for _ in range(side):
            utils._plant(_Entitie)
            map[measure()].append((get_pos_x(), get_pos_y()))
            move(up)
        return map

    return utils.Assign(foo)

def _harvest(petal):
    global map
    def foo():
        for i in map[petal]:
            if i[0] == get_pos_x():
                go.to(i[0], i[1])
                utils._harvest()
        return True
    return utils.Assign(foo)
def run(way):
    global map
    _power = num_items(_Item)
    drone_list = _plant()
    # 合并map
    for i in range(len(drone_list) - 1, -1, -1):
        m = wait_for(drone_list[i])
        for j in m:
                map[j] += m[j]
    go.to()
    for i in range(7):
        do_a_flip()
    for i in range(15, 6, -1):
        _harvest(i)
        map[i] = []
    go.to()
    quick_print(num_items(_Item) - _power)
    return _Item


def mian():
    clear()
    way = utils.cycle()
    utils._till_multi()
    utils.loop(run, way, 1 * utils.M)


if __name__ == "__main__":
    mian()
