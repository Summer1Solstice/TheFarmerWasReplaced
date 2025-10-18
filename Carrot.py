# 胡萝卜种植、收获
# 种: Entities.Carrot
# 收: Items.Carrot
import zhong_zhi


def run(way):
    while True:
        for i in way:
            zhong_zhi.shou_huo()
            zhong_zhi.dan_1(Entities.Carrot)
            move(i)
    return False


if __name__ == "__main__":
    import route

    run(route.cycle())
