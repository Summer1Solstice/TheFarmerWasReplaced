# 胡萝卜种植、收获
# 种: Entities.Carrot
# 收: Items.Carrot
import utils


def run(way, target):
    while num_items(Items.Carrot) < target and utils.cost(Entities.Carrot, utils.area):
        for i in way:
            utils._harvest()
            utils._plant(Entities.Carrot)
            move(i)


if __name__ == "__main__":
    import go

    if not utils.plough(utils.cycle()):
        go.to()
    run(utils.cycle(), 10 * utils.K)
