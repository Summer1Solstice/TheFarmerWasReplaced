# TheFarmerWasReplaced
The Farmer Was Replaced and .py

## 介绍
steam游戏《The Farmer Was Replaced》
玩游戏的Python脚本
## 脚本
无特别说明，为单无人机版本。
多无人机版本只有32的版本。

    __builtins__.py          补充多无人机函数  
    Bone.py                  遍历农场的贪吃蛇  
    Cactus_multi.py          仙人掌多无人机  
    Cactus.py                仙人掌单无人机  
    Carrot.py                胡萝卜，单、32无人机  
    constants.py             将东南西北转为上下左右方向，数字单位K、M、B的常量  
    go.py                    移动无人机到指定坐标，移动到地图边缘  
    gold_dfs.py              迷宫；转载  
    Hay.py                   草，单、32无人机  
    Poly.py                  混合种植  
    Pumpkin_multi.py         南瓜多无人机  
    Pumpkin.py               南瓜，单无人机  
    route.py                 路径生成  
    snake_v2.py              贪吃蛇；转载  
    Sunflower_multi.py       向日葵多无人机  
    Sunflower.py             向日葵单无人机  
    TEST.py                  模拟测试  
    utils.py                 通用函数库  
    Weird_Substance.py       奇异物质  
    Wood.py                  树，单、32无人机  
## 时长
单次运行时长

    Cactus_multi             1分6.41秒  
    Cactus                   25分56.8秒  
    Pumpkin_multi            13.64秒  
    Pumpkin                  3分46秒  
    Sunflower_multi          42.38秒
    Sunflower                6分49.36秒  


## 备忘
- 除非必要,run函数不使用无限循环，单次运行。
- 路径生成尽量完成环回
- main函数包含，清场、耕地。
- run函数包含，种植、收获。
### 模板
```Python
_Item = 
_Entitie =
def run(way):
    for i in way:
        plant()
        move
    收获前
    收获
    Return _Item

def main():
    clear()
    way = 路径
    耕地（）
    run(way)
```