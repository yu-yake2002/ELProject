label chapter6Start:
    play music "../audio/chapter6.mp3"
    scene bg qinhuai river
    "万叶，白芷和其他计金班的同学走在秦淮河沿岸，感受着凉风的吹拂。他们一起合照，玩剧本杀，好不快活。"
    "万叶在剧本杀中和白芷分到了一个阵营里面。"
    show wanye near calm
    m2 "我告诉你我的底牌吧，我其实跟你是一伙的。"
    hide wanye
    "白芷看了看自己的剧情本，重重地点了点头。"
    "很快，两个人一起分享线索卡，在合作之下赢得了最终的胜利。"
    "街上的人逐渐少了起来，这一行人也作出了回去的打算。"
    show baizhi near calm
    "就在两人靠近地铁站的时候，白芷拍了拍万叶的后背。"
    f1 "现在还不算晚，我请你喝一杯去啊！有事相求。"
    "万叶大概已经能够猜出来白芷所求是为何事了，他纠结了好一会，最终还是跟着白芷去了附近的一家饭店。"
    "白芷的目的即将达到了。她想让万叶喝醉，再趁机让他把自己的心意转达给林枫。"
    hide baizhi
    "两人都已经很长时间没有喝酒了。两人喝得很醉，白芷看时机到了，便首先开口。"
    show baizhi near calm
    f1 "还记得那次我提起林枫吗？这次叫你来，是因为我是真的心急了！我看到半夏在林枫的旁边，我的心就不是滋味。"
    f1 "我和林枫从2008年就认识了，我从那时候，我就一直在等这一天！现在他上大学了，我终于有机会了，不能让那个人把我喜欢的人抢走！绝对不能！"
    hide baizhi
    show wanye near upset
    m2 "你这是什么意思？让我帮忙转达是吗？"
    hide wanye
    show baizhi near calm
    f1 "对！而且是今天！马上！如果你转达不到，我明天就说你趁我喝醉非礼我！你自己看着办!"
    hide baizhi
    show wanye near upset
    m2 "完了，上了贼船了这是！没办法，我只好答应你了！"
    hide wanye
    "白芷结完账后，便和万叶坐上了最后一班回南大仙林校区的地铁。万叶怕白芷喝醉耍酒疯，便给他买了一瓶农天山泉。"
    show baizhi near embarrassed
    f1 "这白开水怎么没味啊！"
    hide baizhi
    show wanye near upset
    m2 "完了！他这真是喝多了！"
    hide wanye
    scene bg dormitory night
    "两个人回到自己的宿舍已是凌晨一点。不幸的是，万叶的酒劲现在才上来，导致他没有立刻上楼，而是在外面闲逛。"
    show zhongrong far serious
    m4 "万叶现在还没回来！不会出事了吧！"
    hide zhongrong
    m1 "要不咱们出去找找他？"
    show jiangbo far shocked
    m3 "肯定是喝多了。咱们先发个信息看看。"
    hide jiangbo
    show phone wechat
    "我们试图联系万叶，但他始终没有回复。"
    hide phone
    play sound "../audio/door.mp3"
    "钟嵘心里一紧，边穿上衣服，打算出去找万叶。可是他刚打开宿舍门，便看到万叶躺在宿舍门口，口中不停地嘟囔着些什么。"
    "林枫和江波刚穿好衣服，也急匆匆地赶了过来。几个人合力把万叶抬了进来。"
    "万叶似乎忘了白芷交待给自己的任务，便开始回忆起自己在衡水中学学习的往事，从高一一直讲到高四（中间复读一年）"
    show zhongrong far serious
    m4 "你听到了吗？他刚才说的这一段里面起码有八个前女友！"
    hide zhongrong
    show jiangbo far shocked
    m3 "可不是呗！没录下来真是太可惜了。"
    hide jiangbo
    "随后，万叶又开始讲起了故事。"
    show wanye far pain
    m2 "我小的时候，是我们大庆的奶茶冠军。全市买奶茶最多的人就是我，没有之一。这些年，我在奶茶方面至少花了十万了。可我无论怎么喝就是不胖。钟嵘，你来气不？"
    "本来已经很生气的钟嵘听到后面这句话更生气了，钟嵘没有理他，自己回床上睡觉去了。万叶看自己的问题没有回复，瞬间愤怒起来。"
    play sound "../audio/hit.mp3"
    m2 "妈的，干死你！"
    "万叶说着便要上床去揍钟嵘，被我和江波生生拦了下来。"
    hide wanye
    "这个晚上便在万叶的醉酒狂暴之间度过了。可是，他最终也没有完成白芷交给他的任务。"
    stop music fadeout 1.0
    jump chapter6End