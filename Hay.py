# 草、收获
# 种: 草地、Entities.Grass
# 收: Items.Hay

import utils
import go

_Entitie = Entities.Grass
_Item = Items.Hay


def run(way, target):
    while True:
        for i in way:
            utils._harvest()
            move(i)
        if utils.out(_Item,target):
            return _Item


def main():
    way = utils.cycle()
    clear()
    run(way, None)


if __name__ == "__main__":
    main()
