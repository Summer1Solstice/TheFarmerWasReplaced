# 胡萝卜种植、收获
# 种: Entities.Carrot
# 收: Items.Carrot
import utils

_Entitie = Entities.Carrot
_Item = Items.Carrot

def run(way,target):
    while utils.cost(_Entitie):
        for i in way:
            utils._harvest()
            utils._plant(_Entitie)
            move(i)
        if utils.out(_Item,target):
            return _Item
        
def main():
    clear()
    way = utils.cycle()
    for i in way:
        utils._till()
        move(i)
    run(way,None)

if __name__ == '__main__':
    main()