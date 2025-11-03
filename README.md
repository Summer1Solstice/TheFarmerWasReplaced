# TheFarmerWasReplaced
The Farmer Was Replaced and .py

## 介绍
steam游戏《The Farmer Was Replaced》
玩游戏的Python脚本

- [x] 重写
- [x] main 改成 test，综合simulate_。
## 备忘
- 除非必要run函数，不使用无限循环，单次运行。
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