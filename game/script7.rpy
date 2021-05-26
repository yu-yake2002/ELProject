label chapter7Start:
    play music "../audio/chapter7.mp3"
    scene bg classroom
    "2016年12月"
    "我终于明白了转专业的痛苦。我所要复习的科目是别人复习科目的二倍。我每天泡图书馆里面，忙得焦头烂额。"
    "白芷曾经邀请过我一同学习，但是都被我拒绝了。她觉得奇怪，于是又找到了万叶。"
    scene bg xian i
    show baizhi near sad
    f1 "我那天交待给你的事情，完成了吗？"
    hide baizhi
    show wanye far upset
    m2 "我……我……"
    "万叶想了又想，但确实是不知道。他醉酒的时间内失去了记忆，忘记了进入宿舍之后所发生的事情。"
    m2 "额，我肯定说了！我向你保证！"
    hide wanye
    show baizhi near angry
    f1 "哼，你这个废物！我要主动出击！"
    hide baizhi
    scene bg xian ii inner
    "半夏也是这么想的。她也决定约我一起出去学习交流感情。"
    scene bg xian ii roof
    play sound "../audio/message.mp3"
    show phone wechat
    f1 "最近有时间吗，林枫？期末考试要到了，这学期专业课不少，我有点紧张呢。"
    f1 "你能陪我一起学习吗？就这周六吧，我在图书馆二层靠窗的座上等你。一定要来哦！"
    scene bg xian ii inner
    play sound "../audio/message.mp3"
    show phone wechat
    f2 "林枫哥哥，我有几道微积分还是不会呢QwQ，能给我讲一讲吗？哥哥最好啦~"
    f2 "就定在这周六吧，我在图书馆二层靠窗的座上等你。等你嗷^_^"
    "简直就像在做梦一样啊。两个人同时和我约在同一个时间，同一个地点见面。"
    m1 "这两个人是不是约好了？算了，多一个不多，少一个不少，我都答应下来吧。"
    stop music fadeout 1.0
    scene bg library outlook
    "2016年12月17日星期六"
    "本着不能让女生等待的原则，我早早便来到了约好的地方等候，开始了自己的复习。"
    f1 "今天也是好天气呢，一想到要和林枫一起学习，我的心情就好激动！"
    "半夏正好从另一边向图书馆走过去。"
    f1 "咦，怎么是她？要是她看到我们俩一起学习捣乱，今天的计划可就泡汤了！"
    scene bg library inner
    image baizhiFollowbanxia = HBox(
        "images/baizhi/baizhi near calm.png",
        "images/banxia/banxia front curious.png",
    )
    show baizhiFollowbanxia
    "两人一前一后，走进了图书馆。白芷跟在后面，发现她的行进路线和她完全一样。两个人就这样谁都不理谁，一起往上走。气氛很是尴尬。"
    "上到二楼，二人便都能看到在窗户边上学习的林枫。"
    "白芷和半夏像是看到了救星一样。"
    "半夏向我招了招手，便向我跑了过来。"
    "白芷看到这一幕彻底慌了。自己的劳动果实要被他人无情地窃取！这她哪里忍得了！"
    "于是……两个女生在图书馆里飞奔着向我冲过来。"
    hide baizhiFollowbanxia
    "首先跑到的是半夏。半夏一个箭步，冲到了林枫旁边的沙发椅上，坐了下来。"
    "白芷可是急坏了，她内心急得快要哭出来。"
    m1 "别着急，慢慢走！"
    show baizhi near cry
    play sound "../audio/hit.mp3"
    f1 "我知道！不用你管！她说完之后，没有注意到脚下的电源线，直接摔倒在了林枫的前面。"
    hide baizhi
    show banxia jk evil
    f2 "我的天哪？学姐你没事吧？你怎么这么着急？"
    hide banxia
    show baizhi near embarrassed
    f1 "哼，还不是因为你搞的？"
    hide baizhi
    "两个人的眼神对在了一起，杀气开始在我的周围弥漫。"
    show baizhi near embarrassed
    "此时的白芷，头发散乱，坐在了我的另一侧。我看她这个样子，便用手帮她整理头发。"
    m1 "你头发乱成什么样了！我帮你收拾一下。说着，他的双手便开始捋起头发。"
    show baizhi near happy
    "白芷激动极了。她悄悄转过头来，瞥了半夏一眼。"
    hide baizhi
    show banxia jk bored
    "半夏被眼前的一幕惊呆了。她是个要强的孩子。她可不允许自己在竞争中占下风。"
    f2 "林枫哥哥休息一下吧！我来帮白芷姐姐梳头发。女生梳头肯定要比男孩子好一些。"
    m1 "有道理啊，那交给你了！我先去学习了。"
    show banxia jk bright
    "于是，半夏从我手中接过了白芷的头发。半夏把脑袋别过去，她要开心死了。白芷则是面如死灰，时不时出现短暂的面目狰狞，十分痛苦。"
    hide banxia
    show baizhi far angry
    f1 "不要拧我头发！是不是公报私仇！"
    hide baizhi
    show banxia jk bright
    f2 "哼，给我老实点！"
    hide banxia
    "头发梳理完后，白芷和半夏坐在了我的两侧。半夏的位置明显离我要近许多。白芷便挪起了凳子，靠的离我更近一些。"
    "半夏假装在学习，实际上眼睛一直瞟着侧面。见此情景，她也把凳子挪近一些。"
    "半个小时之后，我还在学习，但是不知不觉间，旁边的两个凳子已经是紧挨着我。"
    m1 "呵欠！"
    "突然觉得自己好困。"
    "空调的温度是不是太高了啊！算了，时候也不早了，先睡一觉吧！"
    "困意使我瘫在椅子上睡着了。"
    
    jump chapter7End