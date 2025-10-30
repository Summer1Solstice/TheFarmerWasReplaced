# 向日葵种植、收获
# 种: Entities.Sunflower
# 收: Items.Power

import utils
import go


def run(way, target):
    area = get_world_size() ** 2
    while num_items(Items.Power) < target and utils.cost(Entities.Sunflower, area):
        map = {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: []}
        for i in way:
            utils.dan_1(Entities.Sunflower)
            move(i)
        for i in way:
            x = get_pos_x()
            y = get_pos_y()
            if measure() == 15:
                utils.shou_huo()
            else:
                map[measure()].append((x, y))
            move(i)
        for i in range(14, 6, -1):
            if not len(map[i]):
                continue
            for j in map[i]:
                x = j[0]
                y = j[1]
                go.to(x, y)
                utils.shou_huo()
        go.to()


if __name__ == "__main__":
    import route
    import plough

    plough.run(route.cycle())
    go.to()
    run(route.cycle(), 100 * utils.K)
