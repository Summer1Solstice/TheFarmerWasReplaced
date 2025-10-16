import zhong_zhi	#单一种植、草木头种植、浇水
import xiang_ri_kui	#向日葵种植、收获
import route		#环回寻路
import go			#前往指定坐标
from const import *	#转换地图方向为屏幕方向
side = get_world_size()



array = route.route()
#change_hat(Hats.Dinosaur_Hat)
go.to()
while True:
	xiang_ri_kui.run(array)