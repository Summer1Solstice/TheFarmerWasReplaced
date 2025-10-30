# 草、收获
# 种: 草地、Entities.Grass
# 收: Items.Hay

import utils
import go


def run(way, target=50000000):
    if num_items(Items.Hay) >= target:
        return False
    clear()
    go.to()
    while True:
        for i in way:
            utils.shou_huo()
            move(i)
        if num_items(Items.Hay) >= target:
            break


if __name__ == "__main__":
    import route

    run(route.cycle())
