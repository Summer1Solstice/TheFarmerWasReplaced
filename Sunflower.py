# 向日葵种植、收获
# 种: Entities.Sunflower
# 收: Items.Power

import utils
import go

_Entitie = Entities.Sunflower
_Item = Items.Power


def run(way):
    if not utils.cost(_Entitie):
        return False
    map = {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: []}
    for i in way:
        utils._plant(_Entitie)
        x, y = get_pos_x(), get_pos_y()
        map[measure()].append((x, y))
        move(i)

    for i in range(15, 6, -1):
        if not len(map[i]):
            continue
        for j in map[i]:
            x = j[0]
            y = j[1]
            go.to(x, y)
            utils._harvest()
    go.to()
    return _Item


def main():
    clear()
    way = utils.cycle()
    utils._till_all(way)
    utils.loop(run, way, 1 * utils.M)


if __name__ == "__main__":
    if utils.cost(_Entitie):
        main()
