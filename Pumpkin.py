# 南瓜种植、收获
# 种: Entities.Pumpkin
# 收: Items.Pumpkin

import go
import zhong_zhi


def run(way):
    for i in way:
        zhong_zhi.shou_huo()
        zhong_zhi.dan_1(Entities.Pumpkin)
        move(i)

    array = []
    for i in way:
        x = get_pos_x()
        y = get_pos_y()
        if zhong_zhi.dan_1(Entities.Pumpkin) or not can_harvest():
            array.append((x, y))
        move(i)

    while len(array) > 36:
        temp = []
        for i in array:
            x = i[0]
            y = i[1]
            go.to(x, y)
            if zhong_zhi.dan_1(Entities.Pumpkin) or not can_harvest():
                temp.append(i)
        array = temp

    for i in array:
        x = i[0]
        y = i[1]
        go.to(x, y)
        while True:
            if get_entity_type() == Entities.Dead_Pumpkin:
                zhong_zhi.dan_1(Entities.Pumpkin)
            if not can_harvest():
                use_item(Items.Fertilizer)
            else:
                break

    zhong_zhi.shou_huo()
    go.to()


if __name__ == "__main__":
    import route

    run(route.cycle())
