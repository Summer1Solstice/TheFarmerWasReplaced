import go
def run(way):
    go.to()
    for i in way:
        if get_ground_type() != Grounds.Soil:
            till()
        elif can_harvest():
            harvest()
        move(i)


if __name__ == "__main__":
    import route

    run(route.cycle())
