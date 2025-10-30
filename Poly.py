import go
import zhong_zhi


def run(way,pe=Entities.Grass):
    PolyMap = {}
    while True:
        for i in way:
            coord = (get_pos_x(), get_pos_y())
            if coord in PolyMap:
                poly = PolyMap.pop(coord)
            else:
                poly = pe
            zhong_zhi.shou_huo()
            zhong_zhi.dan_1(poly)
            if get_companion() != None:
                poly, coord = get_companion()
                PolyMap[coord] = poly
            move(i)


if __name__ == "__main__":
    import route
    import plough

    cycle = route.cycle()
    if get_ground_type() == Grounds.Grassland:
        plough.run(cycle)
    else:
        go.to()

    run(cycle)
