# 胡萝卜种植、收获
# 种: Entities.Carrot
# 收: Items.Carrot
import utils


def run(way, target):
    area = get_world_size() ** 2
    while num_items(Items.Carrot) < target and utils.cost(Entities.Carrot, area):
        for i in way:
            utils.shou_huo()
            utils.dan_1(Entities.Carrot)
            move(i)


if __name__ == "__main__":
    import route

    run(route.cycle())
