import go
import utils


def run(way,pe=Entities.Carrot):
    PolyMap = {}
    while True:
        for i in way:
            coord = (get_pos_x(), get_pos_y())
            if coord in PolyMap:
                poly = PolyMap.pop(coord)
            else:
                poly = pe
            utils.shou_huo()
            utils.dan_1(poly)
            if get_companion() != None:
                poly, coord = get_companion()
                PolyMap[coord] = poly
            else:
                do_a_flip()
            move(i)


if __name__ == "__main__":
    cycle = utils.zigzag_X()
    if not utils.plough(cycle):
        go.to()

    run(cycle)
