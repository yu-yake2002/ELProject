# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define j = Character("林枫")
define a = Character("白芷")
define d = Character("")

$ choice = [-1, -1, -1]

# 游戏在此开始。

label start:
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    show eileen happy
    jump chapter1Start

label chapter1End:
    jump chapter2Start

label chapter2End:
    jump chapter3Start

label chapter3End:
    jump chapter4Start

label chapter4End:
    jump chapter5Start

label chapter5End:
    return
