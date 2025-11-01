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

    if not utils.plough(utils.cycle()):
        go.to()
    run(utils.cycle(), 10 * utils.K)
