#草、收获
#种: 草地、Entities.Grass
#收: Items.Hay

from const import *
import zhong_zhi
def run(way):
	for i in way:
		zhong_zhi.shou_huo()
		move(i)

if __name__ == '__main__':
	import route
	way = route.cycle()
	while True:
		run(way)