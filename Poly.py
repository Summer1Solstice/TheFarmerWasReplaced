import utils


def run(way, pe=Entities.Bush):
    PolyMap = {}
    while True:
        for i in way:
            coord = (get_pos_x(), get_pos_y())
            if coord in PolyMap:
                poly = PolyMap.pop(coord)
            else:
                poly = pe
            utils._harvest()
            utils._plant(poly)
            if get_companion() != None:
                poly, coord = get_companion()
                PolyMap[coord] = poly
            else:
                do_a_flip()
            move(i)


def main():
    way = utils.zigzag_X()
    utils._till_all(way)
    run(way)


if __name__ == "__main__":
    main()
