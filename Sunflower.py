# 向日葵种植、收获
# 种: Entities.Sunflower
# 收: Items.Power

import zhong_zhi
import go


def run(array):
    map = {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: []}
    for i in array:
        zhong_zhi.dan_1(Entities.Sunflower)
        move(i)
    for i in array:
        x = get_pos_x()
        y = get_pos_y()
        map[measure()].append((x, y))
        move(i)
    for i in range(15, 6, -1):
        if not len(map[i]):
            continue
        for j in map[i]:
            x = j[0]
            y = j[1]
            go.to(x, y)
            zhong_zhi.shou_huo()
    go.to()


if __name__ == "__main__":
    go.to()
    import route

    way = route.cycle()
    while True:
        run(way)
