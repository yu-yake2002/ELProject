# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define m1 = Character("林枫")
define f1 = Character("白芷") #白芷 黑龙江绥化2015级工管学生 与男主林枫相识 ai
define f2 = Character("半夏") #半夏 云南双柏2016级法学 自卑 认为自己配不上男主 die
define m2 = Character("万叶") #万叶 有钱 15 计金 衡水复读
define m3 = Character("江波") #江波 JB 计拔 纸上谈兵的情感专家
define m4 = Character("钟嵘") #钟嵘 搞笑 见到白芷之后就不会搞笑了

$ choice = [-1, -1, -1]

label before_main_menu:
    $ renpy.movie_cutscene("../video/startMovie.mpg")
    return

# 游戏在此开始。

label start:
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。
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
    jump chapter6Start
label chapter6End:
    jump chapter7Start
label chapter7End:
    jump chapter8Start
label chapter8End:
    jump chapter9Start
label chapter9End:
    jump chapter10Start
label chapter10End:
    jump chapter11Start
label chapter11End:
    jump chapter12Start
label chapter12End:
    jump chapter13Start
label chapter13End:
    jump chapter14Start
label chapter14End:
    jump chapter15Start
label chapter15End:
    jump chapter16Start
label chapter16End:
    jump chapter17Start
label chapter17End:
    jump chapter18Start
label chapter18End:
    jump chapter19Start
label chapter19End:
    jump chapter20Start
label chapter20End:
    jump chapter21Start
label chapter21End:
    return
