# 草、收获
# 种: 草地、Entities.Grass
# 收: Items.Hay
import utils

_Entitie = Entities.Grass
_Item = Items.Hay


def run(way, target):
    while True:
        for i in way:
            utils._harvest()
            move(i)
        if utils.quit(_Item, target):
            return _Item


def main():
    way = utils.cycle()
    clear()
    run(way, None)


def main_multi():
    if not utils.UAVx32():
        return False
    clear()
    way = utils.line()

    def work():
        return run(way, None)

    utils.Assign(work)


if __name__ == "__main__":
    main()
