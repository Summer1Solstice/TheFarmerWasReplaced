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
                utils._plant(Entities.Bush)
            move(i)
        if utils.quit(_Item, target):
            return _Item


def main():
    clear()
    way = utils.cycle()
    run(way, None)


def main_multi():
    if not utils.UAVx32():
        return False
    clear()
    way = utils.line()
    utils.Watering = True

    def work():
        return run(way, None)

    utils.Assign(work)


if __name__ == "__main__":
    if utils.cost(_Entitie):
        main()
