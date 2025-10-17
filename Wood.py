import zhong_zhi


def run(way, pe=Entities.Grass):
	for i in way:
		zhong_zhi.shou_huo()
		x = get_pos_x()
		y = get_pos_y()
		if (x + y) % 2:
			zhong_zhi.dan_1(Entities.Tree)
		else:
			zhong_zhi.dan_1(pe)
		move(i)


if __name__ == "__main__":
	import route
	way = route.route()
	while True:
		run(way)
