from const import *


def run(way):
    while True:
        for i in way:
            if not move(i):
                change_hat(Hats.Brown_Hat)
                change_hat(Hats.Dinosaur_Hat)
                move(i)

if __name__ == '__main__':
    import route
    way = route.cycle()
    change_hat(Hats.Dinosaur_Hat)
    run(way)