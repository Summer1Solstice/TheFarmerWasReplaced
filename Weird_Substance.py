from directions import *
import utils
import go


def run(way):
    clear()
    for y in range(utils.side):
        if not y % 2:
            for x in range(utils.side):
                if y % 4 == 0 and x % 3 == 0:
                    plant(Entities.Tree)
                    use_item(Items.Weird_Substance)
                elif y % 4 == 2 and x % 3 == 1:
                    plant(Entities.Tree)
                    use_item(Items.Weird_Substance)
                move(right)
        else:
            move(up)
            move(up)
    go.to()
    for i in way:
        utils._harvest()
        move(i)
    return Items.Weird_Substance


if __name__ == "__main__":
    run(utils.zigzag_X())
