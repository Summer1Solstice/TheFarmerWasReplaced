from direction import *
import zhong_zhi
import go

def run(way):
    side=get_world_size()
    area = side ** 2
    while num_items(Items.Cactus) < area and zhong_zhi.cost(Entities.Cactus, area):
        for _ in way:
            plant(Entities.Cactus)
            move(_)
        flag = True
        while flag:
            flag = False
            for i in way:
                x = get_pos_x()
                y = get_pos_y()
                if measure() < measure(left) and x != 0:
                    flag = True
                    swap(left)
                if measure() < measure(down) and y != 0:
                    flag = True
                    swap(down)
                if measure() > measure(right) and x != side - 1:
                    flag = True
                    swap(right)
                if measure() > measure(up) and y != side - 1:
                    flag = True
                    swap(up)
                move(i)
            if not flag:
                zhong_zhi.shou_huo()
                go.to()
