# 木材种植、收获
# 种: Entities.Wood
# 收: Items.Wood

import utils


def run(way, target):
    while True:
        for i in way:
            utils.shou_huo()
            x = get_pos_x()
            y = get_pos_y()
            if (x + y) % 2:
                utils.dan_1(Entities.Tree)
            else:
                utils.dan_1(Entities.Grass)
            move(i)
        if target != None and num_items(Items.Wood) >= target:
            return False


if __name__ == "__main__":
    
    import go

    if not utils.plough(utils.cycle()):
        go.to()
    run(utils.cycle(), 10 * utils.K)
