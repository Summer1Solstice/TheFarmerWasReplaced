# 南瓜种植、收获
# 种: Entities.Pumpkin
# 收: Items.Pumpkin

import go
import utils

_Entitie = Entities.Pumpkin
_Item = Items.Pumpkin


def run(way):
    if not utils.cost(_Entitie):
        return False
    for i in way:
        utils._plant(_Entitie)
        move(i)
    array = []
    for i in way:
        x = get_pos_x()
        y = get_pos_y()
        if utils._plant(_Entitie) or not can_harvest():
            array.append((x, y))
        move(i)

    while len(array) > 64:
        temp = []
        for i in array:
            x = i[0]
            y = i[1]
            go.to(x, y)
            if utils._plant(_Entitie) or not can_harvest():
                temp.append(i)
        array = temp

    for i in array:
        x = i[0]
        y = i[1]
        go.to(x, y)
        while True:
            if get_entity_type() == Entities.Dead_Pumpkin:
                utils._plant(_Entitie)
            if not can_harvest():
                use_item(Items.Fertilizer)
            else:
                break

    utils._harvest()
    go.to()
    return _Item


def main():
    clear()
    way = utils.cycle()
    for i in way:
        utils._till()
        move(i)
    run(way)


if __name__ == "__main__":
    main()
