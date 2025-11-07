# 胡萝卜种植、收获
# 种: Entities.Carrot
# 收: Items.Carrot
import utils

_Entitie = Entities.Carrot
_Item = Items.Carrot


def run(way, target):
    while utils.cost(_Entitie):
        for i in way:
            utils._harvest()
            utils._plant(_Entitie)
            move(i)
        if utils.quit(_Item, target):
            return _Item


def main():
    clear()
    way = utils.cycle()
    utils._till_all(way)
    run(way, None)


def main_multi():
    if not utils.UAVx32():
        return False
    clear()
    way = utils.line()
    utils._till_multi()
    utils.Watering = True


    def work():
        return run(way, None)

    utils.Assign(work)


if __name__ == "__main__":
    if utils.cost(_Entitie):
        main()
