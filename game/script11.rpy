label chapter11Start:
    "我答应了白芷，和她一起回到了绥化，同时以“以后再说”打发了半夏。"
    scene bg airport
    "我和白芷买好了机票。不过我察觉到事情的不对劲，于是便提前来到机场值机。"
    show phone wechat
    m1 "我已经值机完了。"
    f1 "你的座位号是多少？我想和你坐在一起。"
    m1 "不太好吧。飞机上万一有认识的人传闲话该怎么办啊。"
    f1 "什么，有认识的人，那样更好了！我倒是更希望让别人传一传我们的闲话！"
    m1 "好吧。不过你能不能和我坐在一起，那就要看你的运气了！我不会给你看我的座位号的！"
    f1 "诶？喂！"
    "在机场休息室等待，实在感到无聊，便发了一条动态："
    "终于可以回家了！上次喝酒输给你们了，但是这一次我肯定会把你们喝趴下！"
    "附图为一张自己和机票的合影。"
    "咦，有人立刻给我点赞了！是半夏！可是她又立刻把赞取消了。"
    show baizhi far bright
    "白芷拿着一张票，兴致勃勃地来到了我面前。"
    f1 "弱诶，拜托，你很弱诶！说着不告诉我座位号，却把自己的票发在了自己的动态里让我看，没想到你还有这样的一面~"
    m1 "你，你说什么？"
    "我立马回去查看自己发的动态。"
    show phone wechat
    "我竟然忘了给自己的座位信息打上马赛克！"
    hide phone
    m1 "好吧，输给你了！"
    "在完成一系列手续后，我和白芷成功地登机。"
    hide baizhi
    scene bg plane
    m1 "飞机上有这么多座位，我怎么偏偏就和她坐在一起呢？太尴尬了啊。。。"
    show baizhi near angry
    "两人坐在了座位上，每个座位局促的空间让两个人的距离更近了。"
    f1 "你去年为什么没有参加南星计划啊？怎么，南大不值得你宣传吗，看不起南大？还有，你去年这个时候怎么没回母校看一看？"
    f1 "不会因为我是南星计划的负责人而逃避我吧！"
    "我彻底被这一套组合拳打蒙了。必须想出一个能够让自己保命的回答啊！"
    menu:
        "去年寒假很忙":
            m1 "没有！去年寒假我真的很忙！小课程的论文剩一大堆，根本没时间忙这个啊！"
            $ val1 += 2
        "寒假怎么过，那是我的自由":
            m1 "用你管？你怎么什么都想管啊？我自己想干什么是我的自由！"
            $ val1 += 0
        "我今年不是来陪你了吗":
            m1 "别生气啊，我今年不是来陪你了吗？去年的事情就让他过去吧。"
            $ val1 += 5
    f1 "那你在忙什么活动？不会是那个助力双柏的活动吧？你和半夏从那个时候就有接触了？"
    m1 "和你没关系啊？我爸妈都没问我这些，你为什么要一再过问？"
    "乘客A" "小伙子，你这是啥子态度哟？女朋友关心你，你还对你女朋友这样？"
    m1 "不是，我。。。"
    "乘客B" "弄啥子哟？小姑娘噻，我跟你说，你在爱情里千万不要这么卑微啊！一定要问个明白！"
    hide baizhi
    "白芷的脸也红了起来，她看我急得说不出话来，连忙解释"
    f1 "其实，我和他暂时还不是情侣关系啦。。。"
    "乘客B" "暂时不是？这么说很快就是了嘛？小姑娘我跟你说，拍拖之前一定要擦亮眼睛，不要被人骗了！要是他一会再这样对你，你就来找我，我来劝他！"
    m1 "好奇怪啊，这不是去绥化的飞机吗？怎么没有一个人说东北话？停停停，现在不是管这个的时候！"
    m1 "唉，跳进黄河也洗不清了！"
    "乘客A" "你怎么还叹上气了？快点去给你女朋友道歉！"
    "嗐，只能硬着头皮上了。"
    m1 "我。。。。。。我。。。。。。我错了！我以后一定改正！一定会对她好的！"
    show baizhi near happy
    "白芷听到这番话，虽然知道我是迫于无奈，但是心中也满是温暖，脸上露出了笑容。"
    hide baizhi
    "从南京到绥化的飞机只有三个小时，但我感觉好像过了三个世纪一般。"
    m1 "啊~好困……"
    scene bg black
    with dissolve
    jump chapter11End