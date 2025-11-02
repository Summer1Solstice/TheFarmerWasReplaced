import utils
import go


def run(way):
    origin = (get_pos_x(), get_pos_y())
    for i in way:
        utils._till()
        utils._plant(Entities.Pumpkin)
        move(i)
    while utils.cost(Entities.Pumpkin, 36):
        for i in way:
            utils._plant(Entities.Pumpkin)
            move(i)

        array = []
        for i in way:
            x = get_pos_x()
            y = get_pos_y()
            if utils._plant(Entities.Pumpkin) or not can_harvest():
                array.append((x, y))
            move(i)

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
        go.to(origin[0], origin[1])
        if utils.out(Items.Pumpkin, 1 * utils.B):
            return Items.Pumpkin


if __name__ == "__main__":
    clear()
    utils.Watering = True
    array = []
    for x in [0, 7, 14, 21]:
        for y in [0, 7, 14, 21]:
            array.append((x, y))

    def foo():
        return run(utils.cycle(6))

    for _ in range(len(array)):
        x,y = array.pop()
        go.to(x,y)
        if not spawn_drone(foo):
            foo()
