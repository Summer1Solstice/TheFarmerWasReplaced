from direction import *  # 转换地图方向为屏幕方向
import zhong_zhi  # 种植、收获、浇水
import route  # 生成路径
import go  # 前往指定坐标
import plough  # 耕地
import Hay  # 草
import Wood  # 木材种植、收获
import Carrot  # 胡萝卜种植、收获
import Pumpkin  # 南瓜种植、收获
import Bone  # 骨、贪吃蛇
import Sunflower  # 向日葵种植、收获

K = 1000
M = 1000000
B = 1000000000

side = get_world_size()
area = side**2

cycle = route.cycle(10)
zigzag_Y = route.zigzag_Y()
zigzag_X = route.zigzag_X()

# clear()
plough.run(cycle)
do_a_flip()

while True:
    Hay.run(cycle)
    if zhong_zhi.cost(Entities.Pumpkin, area):
        Pumpkin.run(cycle)
    elif num_items(Items.Power) <= 10000 and zhong_zhi.cost(Entities.Sunflower, area):
        Sunflower.run(cycle)
    elif zhong_zhi.cost(Entities.Carrot, area):
        Carrot.run(cycle)
    elif Wood.run(cycle, 50 * M):
        pass
    else:
        Hay.run(cycle, 50 * M)
        plough.run(cycle)
