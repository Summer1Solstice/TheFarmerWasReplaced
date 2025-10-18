from const import *  # 转换地图方向为屏幕方向
import zhong_zhi  # 种植、收获、浇水
import route  # 环回寻路
import go  # 前往指定坐标
import plough  # 耕地
import Hay  # 草
import Wood  # 木材种植、收获
import Carrot  # 胡萝卜种植、收获
import Pumpkin  # 南瓜种植、收获
import Bone  # 骨、贪吃蛇
import Sunflower  # 向日葵种植、收获

side = get_world_size()
array = route.zigzag_Y()

# change_hat(Hats.Dinosaur_Hat)
go.to()
Hay.run(array)
