# 耕地
import go
def run(way):
    if get_ground_type() == Grounds.Soil:
        return False
    go.to()
    for i in way:
        if get_ground_type() != Grounds.Soil:
            till()
        elif can_harvest():
            harvest()
        move(i)
    return True


if __name__ == "__main__":
    import route

    run(route.cycle())
