# 木材种植、收获
# 种: Entities.Wood
# 收: Items.Wood

import utils


def run(way, target):
    while True:
        for i in way:
            utils._harvest()
            x = get_pos_x()
            y = get_pos_y()
            if (x + y) % 2:
                utils._plant(Entities.Tree)
            else:
                utils._plant(Entities.Grass)
            move(i)
        if target != None and num_items(Items.Wood) >= target:
            return False


if __name__ == "__main__":
    
    import go

    for i in utils.cycle():
        utils._till()
        utils._plant(Entities.Cactus)
        move(i)
    go.to()
    run(utils.cycle(), 10 * utils.K)
