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

side = get_world_size()
area = side * side

K = 1000
M = 1000000
B = 1000000000

cycle = route.cycle()
zigzag_Y = route.zigzag_Y()
zigzag_X = route.zigzag_X()

# clear()
plough.run(cycle)
do_a_flip()

while True:
    if zhong_zhi.cost(Entities.Pumpkin, area):
        Pumpkin.run(cycle)
    elif zhong_zhi.cost(Entities.Carrot, area):
        Carrot.run(cycle)
    elif Wood.run(cycle):
        pass
    else:
        Hay.run(cycle)
        plough.run(cycle)
