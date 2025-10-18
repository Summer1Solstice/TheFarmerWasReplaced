import route
def run(way):
	clear()
	for i in way:
		till()
		move(i)
if __name__ == "__main__":
	run(route.cycle())