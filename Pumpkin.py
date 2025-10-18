# 南瓜种植、收获
# 种: Entities.Pumpkin
# 收: Items.Pumpkin

import go
import zhong_zhi


def run(way):
    while True:
        for i in way:
            zhong_zhi.dan_1(Entities.Pumpkin)
            move(i)

        array = []
        for i in way:
            x = get_pos_x()
            y = get_pos_y()
            if get_entity_type() == Entities.Dead_Pumpkin:
                zhong_zhi.dan_1(Entities.Pumpkin)
                array.append((x, y))
            elif not can_harvest():
                array.append((x, y))
            move(i)

        while len(array) != 0:
            temp = []
            for i in array:
                x = i[0]
                y = i[1]
                go.to(x, y)
                if len(array) == 1:
                    zhong_zhi.fertilize()
                if get_entity_type() == Entities.Dead_Pumpkin:
                    zhong_zhi.dan_1(Entities.Pumpkin)
                    temp.append(i)
                elif not can_harvest():
                    temp.append(i)
            array = temp

        zhong_zhi.shou_huo()
        go.to()
    return False


if __name__ == "__main__":
    import route

    run(route.cycle())
