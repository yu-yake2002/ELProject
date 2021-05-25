label chapter16Start:
    scene bg kunming station
    "尊敬的旅客，感谢您乘坐本次列车。本次列车到达终点站昆明站。"
    scene bg kunming scenary
    "昆明是一个有着悠久历史、灿烂文化、光荣革命传统的历史文化名城，先辈们在追求进步、幸福、独立、自由的曲折历程中给我们留下了浩淼博大、光辉灿烂而又独具地方特色和民族特色的历史文化。"
    m1 "昆明真是给人一种心旷神怡的感觉！"
    show banxia far happy
    f2 "别着急啊！这里还不是我们的终点站。我们的目标是星辰大海。。啊不。。云南双柏！"
    m1 "可是这里真的好漂亮！半夏，咱们还能在这里待多久？换句话说，下一趟车是什么时候？"
    show banxia far calm
    f2 "40分钟？"
    m1 "蛤？"
    scene bg kunming station
    "我再次被半夏拽进了火车站。"
    m1 "不是我说你，你没少来过这里，可是我是第一次来啊？好说歹说也是客人，是不是？下次再经过昆明一定要带我逛一逛！"
    show banxia far calm
    f2 "好，好的。不过。。说实话我还从来没去过昆明的任何一个地方，除了火车站和客运站。"
    f2 "我的父母倒是一直在这里工作，但是却被人拖欠工资。我讨厌这个城市。"
    m1 "对，对不起。我不应该提起这件事的。"
    show banxia far calm
    f2 "没事的，是我太过情绪用事了。"
    hide banxia
    scene bg bus station
    "我们来到了昆明市客运站，在客车还有两分钟就要出发的时候终于上了车。"
    show banxia far bright
    f2 "你晕车吗？如果你晕车的话，我这里有晕车药，先吃点吧。"
    m1 "我不可能晕车！堂堂男子汉，这点痛苦还挺不住了？"
    f2 "云南的地形与黑龙江可是不同。黑龙江平原居多，但云南的道路很多都是山路。像我们这样的本地居民都花了很长一段时间才适应呢！晕车了一定要及时告诉我！"
    hide banxia
    scene bg bus inner
    "客车开动了。我用两个小时的车程证明了来到这里为了不出洋相必须听半夏的话。"
    "路人a" "你看旁边的这位同学，才开了一个小时的山路就晕车了，真的太逊了。"
    "路人b" "这个人就是逊啦！"
    m1 "才不是呢！我只是中午饭吃多了！绝对不是晕车！"
    "路人c" "哪有吃这么饱到山路上来吐的啊！下次注意吧！"
    "我这才想起来，刚才吃饭的时候，半夏确实没有吃多少，却是自己在狼吞虎咽。"
    "真是尴尬极了，我现在只想钻到凳子底下呆着。"
    show banxia far happy
    "大概下午三点，楚雄客运站终于到了。我像喝了酒一样，摇摇晃晃地走着。半夏在后面偷笑，但很快就被我发现了。"
    m1 "笑什么笑！再笑我打你啊！"
    "林枫说着，作出挥拳的姿势。不过由于平衡不稳，他重重地摔在了地上。"
    m1 "诶呦！"
    "半夏笑得更开心了。"
    hide banxia
    "接下来是一段更加曲折的路程。现在他们距离双柏只剩下最后一步了。"
    "我坐在车里，看着比他的脸还大的树叶，倒吸了一口凉气。"
    "我还第一次看见了长在树上的香蕉、成片的、让人直流口水的芒果。"
    m1 "这次我怎么没有晕车？哦，原来是刚才吃的东西我都吐出去了，那没事了。不过我好饿啊！"
    scene bg shuangbai scenary
    "双柏县是云南省楚雄自治州下辖县，位于云南省中部，楚雄州南部，哀牢山脉以东，金沙江与红河水系分水岭南侧，荣获2019年“中国天然氧吧”创建地区称号。"
    "一下车，那种沁人心脾的感觉更加浓烈了。我在自己的家乡很难闻到这样清新的空气。或许这里的空气净化方式能够给我一点经验。"
    m1 "支教什么时候开始啊？"
    show banxia near calm
    f2 "如果我没算错的话，应该是后天。"
    m1 "那有没有推荐的旅馆啊。"
    f2 "怎么突然提到旅馆？"
    menu:
        "关于旅馆……"
        "半夏有什么推荐呢":
            $ val2 += 10
            m1 "也是啊。半夏有没有什么推荐？"
            jump nxt16
        "（露出同样疑惑的表情）":
            $ val2 += 5
            m1 "我露出同样疑惑的表情"
            jump nxt16
        "难道住你家吗？":
            m1 "不住旅馆住哪里？难道住你家吗？"
            jump nxt16
label nxt16:
    show banxia near happy
    f2 "我的意思当然是在我家住啦！我总是和我的父母提起你，他们现在都想见见你呢！"
    m1 "既然你的父母要见见我，那我就恭敬不如从命了。我现在去买点礼物。"
    f2 "不用不用。我爸妈说，你就是最好的礼物了！"
    m1 "啊？啊！"
    f2 "诶嘿！"
    f2 "诶嘿是什么意思啊！"
    hide banxia
    jump chapter16End