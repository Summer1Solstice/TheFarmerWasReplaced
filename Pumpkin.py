# 南瓜种植、收获
# 种: Entities.Pumpkin
# 收: Items.Pumpkin

import go
import utils


def run(way):
    if not utils.cost(Entities.Pumpkin, utils.area):
        return False
    loop = 64
    if utils.area <= loop:
        utils.Watering = True
    else:
        loop = utils.area * 0.2
        if loop < 64:
            loop = 64
        for i in way:
            utils._harvest()
            utils._plant(Entities.Pumpkin)
            move(i)

    array = []
    for i in way:
        x = get_pos_x()
        y = get_pos_y()
        if utils._plant(Entities.Pumpkin) or not can_harvest():
            array.append((x, y))
        move(i)

    while len(array) > loop:
        temp = []
        for i in array:
            x = i[0]
            y = i[1]
            go.to(x, y)
            if utils._plant(Entities.Pumpkin) or not can_harvest():
                temp.append(i)
        array = temp

    for i in array:
        x = i[0]
        y = i[1]
        go.to(x, y)
        while True:
            if get_entity_type() == Entities.Dead_Pumpkin:
                utils._plant(Entities.Pumpkin)
            if not can_harvest():
                use_item(Items.Fertilizer)
            else:
                break

    utils._harvest()
    go.to()
    return Items.Pumpkin


if __name__ == "__main__":
    set_world_size(6)
    for i in utils.cycle():
        utils._till()
        utils._plant(Entities.Pumpkin)
        move(i)
    utils.loop(run, utils.cycle(), 10 * utils.K)
