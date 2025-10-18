import go
def run(way):
	change_hat(Hats.Dinosaur_Hat)
	go.to()
	while True:
		for i in way:
			if not move(i):
				change_hat(Hats.Brown_Hat)
				change_hat(Hats.Dinosaur_Hat)
				move(i)


if __name__ == "__main__":
	import route

	run(route.cycle())
