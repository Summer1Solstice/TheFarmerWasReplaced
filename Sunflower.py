# 向日葵种植、收获
# 种: Entities.Sunflower
# 收: Items.Power

import utils
import go


def run(way):
    map = {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: []}
    for i in way:
        utils.dan_1(Entities.Sunflower)
        x, y = get_pos_x(), get_pos_y()
        map[measure()].append((x, y))
        move(i)

    for i in range(15, 6, -1):
        if not len(map[i]):
            continue
        for j in map[i]:
            x = j[0]
            y = j[1]
            go.to(x, y)
            utils.shou_huo()
    go.to()
    return Items.Power


if __name__ == "__main__":
    
    
    if not utils.plough(utils.cycle()):        
        go.to()
    utils.loop(run, utils.cycle(), 10 * utils.K)
