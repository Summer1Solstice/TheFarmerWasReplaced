from A import *
def run(route_list):
	clear()
	for i in route_list:
		till()
		move(i)
if __name__ == "__main__":
	import route
	run(route.route())