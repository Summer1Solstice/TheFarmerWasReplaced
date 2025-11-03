# 木材种植、收获
# 种: Entities.Tree
# 收: Items.Wood

import utils

_Entitie = Entities.Tree
_Item = Items.Wood


def run(way, target):
    while True:
        for i in way:
            utils._harvest()
            x = get_pos_x()
            y = get_pos_y()
            if (x + y) % 2:
                utils._plant(_Entitie)
            else:
                utils._plant(Entities.Grass)
            move(i)
        if utils.out(_Item, target):
            return _Item


def main():
    clear()
    way = utils.cycle()
    for i in way:
        utils._till()
        move(i)
    run(way, None)


if __name__ == "__main__":
    main()
