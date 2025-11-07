from constants import *
import utils
import go

_Entitie = Entities.Pumpkin
_Item = Items.Pumpkin


def run(way, target):
    origin = (get_pos_x(), get_pos_y())
    for _ in way:
        utils._till()
        move(_)
    while utils.cost(_Entitie, 36):
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
        go.to(origin[0], origin[1])
        if utils.quit(_Item, target):
            return _Item


def main():
    if not utils.UAVx32():
        return False
    clear()
    utils.Watering = True
    array = [
        (0, 7),
        (0, 14),
        (0, 21),
        (7, 21),
        (7, 14),
        (7, 7),
        (14, 7),
        (14, 14),
        (14, 21),
        (21, 21),
        (21, 14),
        (21, 7),
        (21, 0),
        (14, 0),
        (7, 0),
        (0, 0),
    ]
    way = utils.cycle(6)
    target = 1 * M

    def work():
        return run(way, target)

    for i in array:
        go.to(i[0], i[1])
        if not spawn_drone(work):
            work()


if __name__ == "__main__":
    if utils.cost(_Entitie):
        main()
