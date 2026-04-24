"""
人教版小学英语词库 (1-4年级)
包含单词和句子，用于听写练习
"""

# 词库结构：每个条目包含 english(英文), chinese(中文), type(word/sentence), grade(年级)

WORD_BANK = {
    "一年级": {
        "words": [
            # Unit 1 - 上册
            {"english": "book", "chinese": "书，书本"},
            {"english": "ruler", "chinese": "尺子"},
            {"english": "pencil", "chinese": "铅笔"},
            {"english": "schoolbag", "chinese": "书包"},
            {"english": "teacher", "chinese": "教师"},
            {"english": "I", "chinese": "我"},
            {"english": "have", "chinese": "有"},
            {"english": "a", "chinese": "一(个)"},
            {"english": "an", "chinese": "一(个)"},
            
            # Unit 2 - 上册
            {"english": "face", "chinese": "脸"},
            {"english": "ear", "chinese": "耳朵"},
            {"english": "eye", "chinese": "眼睛"},
            {"english": "nose", "chinese": "鼻子"},
            {"english": "mouth", "chinese": "嘴巴"},
            {"english": "this", "chinese": "这(个)"},
            {"english": "is", "chinese": "是"},
            {"english": "my", "chinese": "我的"},
            
            # Unit 3 - 上册
            {"english": "dog", "chinese": "狗"},
            {"english": "bird", "chinese": "鸟"},
            {"english": "tiger", "chinese": "老虎"},
            {"english": "monkey", "chinese": "猴子"},
            {"english": "cat", "chinese": "猫"},
            {"english": "what", "chinese": "什么"},
            {"english": "it", "chinese": "它"},
            
            # Unit 4 - 上册
            {"english": "one", "chinese": "一"},
            {"english": "two", "chinese": "二"},
            {"english": "three", "chinese": "三"},
            {"english": "four", "chinese": "四"},
            {"english": "five", "chinese": "五"},
            {"english": "six", "chinese": "六"},
            {"english": "seven", "chinese": "七"},
            {"english": "eight", "chinese": "八"},
            {"english": "nine", "chinese": "九"},
            {"english": "ten", "chinese": "十"},
            {"english": "how", "chinese": "多少"},
            {"english": "many", "chinese": "多的，许多的"},
            {"english": "are", "chinese": "是"},
            {"english": "there", "chinese": "(代替主语)"},
            
            # Unit 5 - 上册
            {"english": "black", "chinese": "黑色；黑色的"},
            {"english": "yellow", "chinese": "黄色；黄色的"},
            {"english": "blue", "chinese": "蓝色；蓝色的"},
            {"english": "red", "chinese": "红色；红色的"},
            {"english": "green", "chinese": "绿色；绿色的"},
            {"english": "colour", "chinese": "颜色"},
            
            # Unit 6 - 上册
            {"english": "apple", "chinese": "苹果"},
            {"english": "pear", "chinese": "梨"},
            {"english": "banana", "chinese": "香蕉"},
            {"english": "orange", "chinese": "柑橘；橙"},
            {"english": "do", "chinese": "(助动词)"},
            {"english": "you", "chinese": "你；你们"},
            {"english": "like", "chinese": "喜欢，喜爱"},
            {"english": "yes", "chinese": "是，是的"},
            {"english": "no", "chinese": "不，不是"},
            
            # Unit 1 - 下册
            {"english": "chair", "chinese": "椅子"},
            {"english": "desk", "chinese": "书桌，写字台"},
            {"english": "blackboard", "chinese": "黑板"},
            {"english": "on", "chinese": "在……上"},
            {"english": "under", "chinese": "在……下面；在……下方"},
            {"english": "in", "chinese": "在……里面"},
            {"english": "where", "chinese": "在哪里"},
            {"english": "the", "chinese": "放在名词前，特指人、事或物"},
            
            # Unit 2 - 下册
            {"english": "light", "chinese": "灯"},
            {"english": "bed", "chinese": "床"},
            {"english": "door", "chinese": "门；出入口"},
            {"english": "box", "chinese": "箱子；盒子"},
            {"english": "near", "chinese": "靠近，接近"},
            {"english": "behind", "chinese": "在……背后"},
            
            # Unit 3 - 下册
            {"english": "plane", "chinese": "飞机"},
            {"english": "ball", "chinese": "球"},
            {"english": "doll", "chinese": "玩偶，玩具娃娃"},
            {"english": "train", "chinese": "列车，火车"},
            {"english": "car", "chinese": "小汽车，轿车"},
            {"english": "bear", "chinese": "玩具熊；熊"},
            {"english": "can", "chinese": "可以；能够"},
            {"english": "sure", "chinese": "当然"},
            {"english": "sorry", "chinese": "对不起，抱歉"},
            
            # Unit 4 - 下册
            {"english": "rice", "chinese": "米饭；米"},
            {"english": "noodles", "chinese": "面条"},
            {"english": "vegetable", "chinese": "蔬菜"},
            {"english": "fish", "chinese": "鱼肉；鱼"},
            {"english": "chicken", "chinese": "鸡肉；鸡"},
            {"english": "egg", "chinese": "鸡蛋"},
            {"english": "hungry", "chinese": "饥饿的"},
            {"english": "want", "chinese": "要，想要"},
            {"english": "and", "chinese": "和"},
            
            # Unit 5 - 下册
            {"english": "juice", "chinese": "果汁；蔬菜汁"},
            {"english": "tea", "chinese": "茶；茶叶"},
            {"english": "milk", "chinese": "奶；牛奶"},
            {"english": "water", "chinese": "水"},
            {"english": "thirsty", "chinese": "口渴的"},
            {"english": "thanks", "chinese": "感谢"},
            
            # Unit 6 - 下册
            {"english": "shirt", "chinese": "衬衫"},
            {"english": "T-shirt", "chinese": "T恤衫；短袖圆领汗衫"},
            {"english": "skirt", "chinese": "裙子"},
            {"english": "dress", "chinese": "连衣裙；套裙"},
            {"english": "socks", "chinese": "短袜"},
            {"english": "shorts", "chinese": "短裤"},
            {"english": "your", "chinese": "你的；你们的"},
        ],
        "sentences": [
            # 基础介绍和拥有 (使用 Unit 1 词汇)
            {"english": "I have a book.", "chinese": "我有一本书。"},
            {"english": "I have a pencil.", "chinese": "我有一支铅笔。"},
            {"english": "This is my ruler.", "chinese": "这是我的尺子。"},
            {"english": "This is my schoolbag.", "chinese": "这是我的书包。"},
            
            # 身体部位介绍 (使用 Unit 2 词汇)
            {"english": "This is my face.", "chinese": "这是我的脸。"},
            {"english": "This is my nose.", "chinese": "这是我的鼻子。"},
            {"english": "I have two eyes.", "chinese": "我有两只眼睛。"},
            {"english": "I have two ears.", "chinese": "我有两只耳朵。"},
            
            # 动物识别 (使用 Unit 3 词汇)
            {"english": "What is it?", "chinese": "它是什么？"},
            {"english": "It is a cat.", "chinese": "它是一只猫。"},
            {"english": "It is a dog.", "chinese": "它是一只狗。"},
            {"english": "I have a bird.", "chinese": "我有一只鸟。"},
            
            # 数量询问 (使用 Unit 4 词汇)
            {"english": "How many cats?", "chinese": "有多少只猫？"},
            {"english": "There are three cats.", "chinese": "有三只猫。"},
            {"english": "I have five pencils.", "chinese": "我有五支铅笔。"},
            {"english": "How many books are there?", "chinese": "有多少本书？"},
            
            # 颜色描述 (使用 Unit 5 词汇)
            {"english": "It is red.", "chinese": "它是红色的。"},
            {"english": "I like blue.", "chinese": "我喜欢蓝色。"},
            {"english": "What colour is it?", "chinese": "它是什么颜色？"},
            {"english": "It is green.", "chinese": "它是绿色的。"},
            
            # 喜好表达 (使用 Unit 6 词汇)
            {"english": "Do you like apples?", "chinese": "你喜欢苹果吗？"},
            {"english": "Yes, I do.", "chinese": "是的，我喜欢。"},
            {"english": "No, I do not.", "chinese": "不，我不喜欢。"},
            {"english": "I like bananas.", "chinese": "我喜欢香蕉。"},
            {"english": "Do you like oranges?", "chinese": "你喜欢橙子吗？"},
            
            # 位置描述 (使用下册 Unit 1 词汇)
            {"english": "Where is the book?", "chinese": "书在哪里？"},
            {"english": "It is on the desk.", "chinese": "它在桌子上。"},
            {"english": "The pencil is in the box.", "chinese": "铅笔在盒子里。"},
            {"english": "The cat is under the chair.", "chinese": "猫在椅子下面。"},
            
            # 物品位置 (使用下册 Unit 2 词汇)
            {"english": "The ball is near the door.", "chinese": "球在门附近。"},
            {"english": "The dog is behind the box.", "chinese": "狗在盒子后面。"},
            {"english": "Where is my bed?", "chinese": "我的床在哪里？"},
            
            # 能力和请求 (使用下册 Unit 3 词汇)
            {"english": "I have a ball.", "chinese": "我有一个球。"},
            {"english": "Can I have the car?", "chinese": "我可以要那辆车吗？"},
            {"english": "Sure.", "chinese": "当然可以。"},
            {"english": "Sorry, I cannot.", "chinese": "对不起，我不能。"},
            
            # 食物和需求 (使用下册 Unit 4 词汇)
            {"english": "I am hungry.", "chinese": "我饿了。"},
            {"english": "I want rice.", "chinese": "我想要米饭。"},
            {"english": "I want fish and chicken.", "chinese": "我想要鱼肉和鸡肉。"},
            {"english": "Do you want noodles?", "chinese": "你想要面条吗？"},
            
            # 饮料和感受 (使用下册 Unit 5 词汇)
            {"english": "I am thirsty.", "chinese": "我渴了。"},
            {"english": "I want water.", "chinese": "我想要水。"},
            {"english": "Do you like milk?", "chinese": "你喜欢牛奶吗？"},
            {"english": "Thank you.", "chinese": "谢谢你。"},
            
            # 衣物描述 (使用下册 Unit 6 词汇)
            {"english": "This is my shirt.", "chinese": "这是我的衬衫。"},
            {"english": "I like your dress.", "chinese": "我喜欢你的连衣裙。"},
            {"english": "Where are my socks?", "chinese": "我的袜子在哪里？"},
            {"english": "Your shorts are on the bed.", "chinese": "你的短裤在床上。"},
        ]
    },
    "二年级": {
        "words": [
            # Unit 1 - 上册
            {"english": "father", "chinese": "父亲；爸爸"},
            {"english": "mother", "chinese": "母亲；妈妈"},
            {"english": "brother", "chinese": "兄；弟"},
            {"english": "sister", "chinese": "姐；妹"},
            {"english": "grandmother", "chinese": "(外)祖母"},
            {"english": "grandfather", "chinese": "(外)祖父"},
            {"english": "who", "chinese": "谁"},
            {"english": "he", "chinese": "他"},
            {"english": "she", "chinese": "她"},
            
            # Unit 2 - 上册
            {"english": "classmate", "chinese": "同班同学"},
            {"english": "friend", "chinese": "朋友"},
            {"english": "woman", "chinese": "女人"},
            {"english": "girl", "chinese": "女孩"},
            {"english": "man", "chinese": "男人"},
            {"english": "boy", "chinese": "男孩"},
            {"english": "look", "chinese": "看；瞧"},
            {"english": "his", "chinese": "他的"},
            {"english": "name", "chinese": "名字"},
            {"english": "her", "chinese": "她的"},
            {"english": "or", "chinese": "还是"},
            
            # Unit 3 - 上册
            {"english": "big", "chinese": "大的"},
            {"english": "tall", "chinese": "高的"},
            {"english": "pretty", "chinese": "漂亮的，可爱的"},
            {"english": "thin", "chinese": "瘦的"},
            {"english": "short", "chinese": "矮的"},
            {"english": "handsome", "chinese": "漂亮的，英俊的"},
            {"english": "new", "chinese": "新的"},
            {"english": "does", "chinese": "(助动词)"},
            
            # Unit 4 - 上册
            {"english": "bookshop", "chinese": "书店"},
            {"english": "zoo", "chinese": "动物园"},
            {"english": "school", "chinese": "学校"},
            {"english": "supermarket", "chinese": "超市"},
            {"english": "park", "chinese": "公园"},
            {"english": "hospital", "chinese": "医院"},
            {"english": "go", "chinese": "去"},
            {"english": "to", "chinese": "向，朝"},
            
            # Unit 5 - 上册
            {"english": "grass", "chinese": "草"},
            {"english": "tree", "chinese": "树"},
            {"english": "flower", "chinese": "花；花朵"},
            {"english": "boat", "chinese": "小船"},
            {"english": "lake", "chinese": "湖"},
            {"english": "hill", "chinese": "小山"},
            
            # Unit 6 - 上册
            {"english": "Christmas", "chinese": "圣诞节"},
            {"english": "Father Christmas", "chinese": "圣诞老人"},
            {"english": "Christmas tree", "chinese": "圣诞树"},
            {"english": "card", "chinese": "贺卡；明信片"},
            {"english": "present", "chinese": "礼物"},
            {"english": "New Year", "chinese": "新年"},
            {"english": "merry", "chinese": "高兴的；愉快的"},
            {"english": "too", "chinese": "也；又"},
            {"english": "here", "chinese": "这儿"},
            {"english": "for", "chinese": "(表示接受某事物或从某事物中获益的人)"},
            {"english": "thank", "chinese": "谢谢"},
            {"english": "happy", "chinese": "快乐的；幸福的"},
            
            # Unit 1 - 下册
            {"english": "play football", "chinese": "踢足球"},
            {"english": "fly a kite", "chinese": "放风筝"},
            {"english": "ride a bike", "chinese": "骑自行车"},
            {"english": "make a model plane", "chinese": "做飞机模型"},
            {"english": "swim", "chinese": "游泳"},
            {"english": "make a snowman", "chinese": "堆雪人"},
            {"english": "can't", "chinese": "不能，不会"},
            
            # Unit 2 - 下册
            {"english": "rainy", "chinese": "下雨的"},
            {"english": "cloudy", "chinese": "多云的"},
            {"english": "snowy", "chinese": "下雪的"},
            {"english": "windy", "chinese": "刮风的"},
            {"english": "sunny", "chinese": "晴朗的"},
            {"english": "umbrella", "chinese": "雨伞"},
            {"english": "weather", "chinese": "天气"},
            {"english": "wow", "chinese": "哇"},
            {"english": "let's", "chinese": "让我们……"},
            
            # Unit 3 - 下册
            {"english": "spring", "chinese": "春天"},
            {"english": "summer", "chinese": "夏天"},
            {"english": "autumn", "chinese": "秋天"},
            {"english": "winter", "chinese": "冬天"},
            {"english": "hot", "chinese": "炎热的"},
            {"english": "warm", "chinese": "温暖的"},
            {"english": "cool", "chinese": "凉爽的"},
            {"english": "cold", "chinese": "寒冷的"},
            {"english": "favourite", "chinese": "最喜欢的"},
            {"english": "season", "chinese": "季节"},
            
            # Unit 4 - 下册
            {"english": "eleven", "chinese": "十一"},
            {"english": "twelve", "chinese": "十二"},
            {"english": "twenty", "chinese": "二十"},
            {"english": "thirty", "chinese": "三十"},
            {"english": "forty", "chinese": "四十"},
            {"english": "fifty", "chinese": "五十"},
            {"english": "thirteen", "chinese": "十三"},
            {"english": "fourteen", "chinese": "十四"},
            {"english": "fifteen", "chinese": "十五"},
            {"english": "time", "chinese": "时间"},
            {"english": "playtime", "chinese": "游戏时间，课间休息时间"},
            
            # Unit 5 - 下册
            {"english": "get up", "chinese": "起床"},
            {"english": "eat breakfast", "chinese": "吃早饭"},
            {"english": "go to school", "chinese": "上学"},
            {"english": "eat lunch", "chinese": "吃午饭"},
            {"english": "go home", "chinese": "回家"},
            {"english": "eat dinner", "chinese": "吃晚饭"},
            {"english": "go to bed", "chinese": "上床，睡觉"},
            {"english": "when", "chinese": "什么时候，何时"},
            {"english": "every day", "chinese": "每天"},
            {"english": "at", "chinese": "在……点钟"},
            
            # Unit 6 - 下册
            {"english": "Sunday", "chinese": "星期天"},
            {"english": "Monday", "chinese": "星期一"},
            {"english": "Tuesday", "chinese": "星期二"},
            {"english": "Wednesday", "chinese": "星期三"},
            {"english": "Thursday", "chinese": "星期四"},
            {"english": "Friday", "chinese": "星期五"},
            {"english": "Saturday", "chinese": "星期六"},
            {"english": "today", "chinese": "今天"},
        ],
        "sentences": [
            # 家庭成员介绍 (使用 Unit 1 词汇)
            {"english": "This is my father.", "chinese": "这是我的爸爸。"},
            {"english": "This is my mother.", "chinese": "这是我的妈妈。"},
            {"english": "He is my brother.", "chinese": "他是我的弟弟/哥哥。"},
            {"english": "She is my sister.", "chinese": "她是我的妹妹/姐姐。"},
            {"english": "Who is he?", "chinese": "他是谁？"},
            {"english": "He is my grandfather.", "chinese": "他是我的祖父/外祖父。"},
            {"english": "Who is she?", "chinese": "她是谁？"},
            {"english": "She is my grandmother.", "chinese": "她是我的祖母/外祖母。"},
            
            # 朋友和人物 (使用 Unit 2 词汇)
            {"english": "This is my friend.", "chinese": "这是我的朋友。"},
            {"english": "He is my classmate.", "chinese": "他是我的同班同学。"},
            {"english": "What is his name?", "chinese": "他叫什么名字？"},
            {"english": "His name is Tom.", "chinese": "他的名字叫汤姆。"},
            {"english": "What is her name?", "chinese": "她叫什么名字？"},
            {"english": "Her name is Lily.", "chinese": "她的名字叫莉莉。"},
            {"english": "Is he a boy or a girl?", "chinese": "他是男孩还是女孩？"},
            {"english": "Look, she is a woman.", "chinese": "看，她是一位女士。"},
            
            # 人物描述 (使用 Unit 3 词汇)
            {"english": "He is tall.", "chinese": "他很高。"},
            {"english": "She is short.", "chinese": "她很矮。"},
            {"english": "My father is big.", "chinese": "我爸爸很高大。"},
            {"english": "My sister is pretty.", "chinese": "我妹妹/姐姐很漂亮。"},
            {"english": "He is handsome.", "chinese": "他很英俊。"},
            {"english": "She is thin.", "chinese": "她很瘦。"},
            {"english": "I have a new friend.", "chinese": "我有一个新朋友。"},
            
            # 地点 (使用 Unit 4 词汇)
            {"english": "Let's go to school.", "chinese": "让我们去学校吧。"},
            {"english": "I go to the park.", "chinese": "我去公园。"},
            {"english": "She goes to the zoo.", "chinese": "她去动物园。"},
            {"english": "We go to the supermarket.", "chinese": "我们去超市。"},
            {"english": "He goes to the bookshop.", "chinese": "他去书店。"},
            {"english": "My mother goes to the hospital.", "chinese": "我妈妈去医院。"},
            
            # 自然景物 (使用 Unit 5 词汇)
            {"english": "I can see a tree.", "chinese": "我能看见一棵树。"},
            {"english": "The grass is green.", "chinese": "草是绿色的。"},
            {"english": "There is a boat on the lake.", "chinese": "湖上有一艘船。"},
            {"english": "Look at the flowers.", "chinese": "看这些花。"},
            {"english": "I can see a hill.", "chinese": "我能看见一座小山。"},
            
            # 节日祝福 (使用 Unit 6 词汇)
            {"english": "Merry Christmas!", "chinese": "圣诞快乐！"},
            {"english": "Happy New Year!", "chinese": "新年快乐！"},
            {"english": "This is for you.", "chinese": "这是给你的。"},
            {"english": "Thank you!", "chinese": "谢谢你！"},
            {"english": "Here is a present.", "chinese": "这儿有一份礼物。"},
            {"english": "I have a card.", "chinese": "我有一张贺卡。"},
            {"english": "Look at the Christmas tree.", "chinese": "看这棵圣诞树。"},
            
            # 活动 (使用下册 Unit 1 词汇)
            {"english": "I can play football.", "chinese": "我会踢足球。"},
            {"english": "I can swim.", "chinese": "我会游泳。"},
            {"english": "I can ride a bike.", "chinese": "我会骑自行车。"},
            {"english": "I can fly a kite.", "chinese": "我会放风筝。"},
            {"english": "I can make a snowman.", "chinese": "我会堆雪人。"},
            {"english": "I can't make a model plane.", "chinese": "我不会做飞机模型。"},
            
            # 天气 (使用下册 Unit 2 词汇)
            {"english": "It is sunny today.", "chinese": "今天是晴天。"},
            {"english": "It is rainy.", "chinese": "下雨了。"},
            {"english": "It is cloudy.", "chinese": "多云。"},
            {"english": "It is windy.", "chinese": "刮风了。"},
            {"english": "It is snowy.", "chinese": "下雪了。"},
            {"english": "What is the weather like?", "chinese": "天气怎么样？"},
            {"english": "I have an umbrella.", "chinese": "我有一把雨伞。"},
            
            # 季节 (使用下册 Unit 3 词汇)
            {"english": "I like spring.", "chinese": "我喜欢春天。"},
            {"english": "Summer is hot.", "chinese": "夏天很热。"},
            {"english": "Autumn is cool.", "chinese": "秋天很凉爽。"},
            {"english": "Winter is cold.", "chinese": "冬天很冷。"},
            {"english": "Spring is warm.", "chinese": "春天很温暖。"},
            {"english": "What is your favourite season?", "chinese": "你最喜欢的季节是什么？"},
            
            # 时间和数字 (使用下册 Unit 4 词汇)
            {"english": "What time is it?", "chinese": "现在几点了？"},
            {"english": "It is eleven o'clock.", "chinese": "现在是十一点。"},
            {"english": "I have twelve books.", "chinese": "我有十二本书。"},
            {"english": "It is playtime.", "chinese": "现在是游戏时间。"},
            
            # 日常作息 (使用下册 Unit 5 词汇)
            {"english": "I get up at seven.", "chinese": "我七点起床。"},
            {"english": "I eat breakfast at eight.", "chinese": "我八点吃早饭。"},
            {"english": "I go to school every day.", "chinese": "我每天上学。"},
            {"english": "I eat lunch at twelve.", "chinese": "我十二点吃午饭。"},
            {"english": "I go home at four.", "chinese": "我四点回家。"},
            {"english": "I eat dinner at six.", "chinese": "我六点吃晚饭。"},
            {"english": "I go to bed at nine.", "chinese": "我九点睡觉。"},
            {"english": "When do you get up?", "chinese": "你什么时候起床？"},
            
            # 星期 (使用下册 Unit 6 词汇)
            {"english": "Today is Monday.", "chinese": "今天是星期一。"},
            {"english": "Today is Sunday.", "chinese": "今天是星期天。"},
            {"english": "I go to school on Monday.", "chinese": "我星期一上学。"},
            {"english": "I play football on Saturday.", "chinese": "我星期六踢足球。"},
        ]
    },
    "三年级": {
        "words": [
            # Unit 1 - 上册
            {"english": "nice", "chinese": "令人愉快的；友好的"},
            {"english": "hand", "chinese": "手"},
            {"english": "arm", "chinese": "胳膊"},
            {"english": "share", "chinese": "分享"},
            {"english": "smile", "chinese": "微笑；笑"},
            {"english": "listen", "chinese": "听；倾听"},
            {"english": "help", "chinese": "帮助"},
            {"english": "say", "chinese": "说；讲"},
            {"english": "goodbye", "chinese": "再见"},
            {"english": "toy", "chinese": "玩具"},
            {"english": "good", "chinese": "好的"},
            {"english": "me", "chinese": "我"},
            {"english": "family", "chinese": "家；家庭"},
            {"english": "cousin", "chinese": "堂(表)兄弟；堂(表)姐妹"},
            {"english": "baby", "chinese": "婴儿"},
            {"english": "uncle", "chinese": "伯父；叔父；舅父；姑父；姨父"},
            {"english": "aunt", "chinese": "伯母；婶母；舅母；姑母；姨母"},
            {"english": "some", "chinese": "一些"},
            {"english": "small", "chinese": "小的"},
            
            # Unit 2 - 上册
            {"english": "mum", "chinese": "(口语)妈妈"},
            {"english": "dad", "chinese": "(口语)爸爸；爹爹"},
            {"english": "grandma", "chinese": "奶奶；姥姥"},
            {"english": "grandpa", "chinese": "爷爷；姥爷"},
            
            # Unit 3 - 上册
            {"english": "pet", "chinese": "宠物"},
            {"english": "rabbit", "chinese": "兔"},
            {"english": "fox", "chinese": "狐狸"},
            {"english": "Miss", "chinese": "(学生对女教师的称呼)老师；女士"},
            {"english": "panda", "chinese": "大熊猫"},
            {"english": "cute", "chinese": "可爱的"},
            {"english": "elephant", "chinese": "大象"},
            {"english": "lion", "chinese": "狮；狮子"},
            {"english": "animal", "chinese": "动物"},
            {"english": "fast", "chinese": "快的"},
            
            # Unit 4 - 上册
            {"english": "farm", "chinese": "农场"},
            {"english": "air", "chinese": "空气"},
            {"english": "grape", "chinese": "葡萄"},
            {"english": "garden", "chinese": "花园"},
            {"english": "plant", "chinese": "种植；植物"},
            {"english": "sun", "chinese": "阳光；太阳"},
            {"english": "give", "chinese": "给"},
            {"english": "us", "chinese": "我们"},
            {"english": "them", "chinese": "它们；他们；她们"},
            
            # Unit 5 - 上册
            {"english": "make", "chinese": "使出现；做"},
            {"english": "purple", "chinese": "紫色；紫色的"},
            {"english": "brown", "chinese": "棕色；棕色的"},
            {"english": "duck", "chinese": "鸭"},
            {"english": "sea", "chinese": "海；海洋"},
            {"english": "pink", "chinese": "粉色；粉色的"},
            {"english": "draw", "chinese": "画"},
            {"english": "white", "chinese": "白色；白色的"},
            
            # Unit 6 - 上册
            {"english": "year", "chinese": "年纪；年"},
            {"english": "o'clock", "chinese": "(表示整点)……点钟"},
            {"english": "cut", "chinese": "切块"},
            {"english": "eat", "chinese": "吃"},
            {"english": "cake", "chinese": "蛋糕"},
            
            # Unit 1 - 下册
            {"english": "from", "chinese": "(表示来源)来自，从……来"},
            {"english": "about", "chinese": "大约；去左"},
            {"english": "student", "chinese": "学生"},
            {"english": "after", "chinese": "在……后面"},
            {"english": "neighbour", "chinese": "邻居"},
            {"english": "Mr", "chinese": "(用于男子的姓氏或姓名前)先生"},
            {"english": "English", "chinese": "英语的；英语"},
            {"english": "very", "chinese": "很；非常；十分"},
            {"english": "UK", "chinese": "英国"},
            {"english": "China", "chinese": "中国"},
            {"english": "Canada", "chinese": "加拿大"},
            {"english": "USA", "chinese": "美国"},
            
            # Unit 2 - 下册
            {"english": "has", "chinese": "(have的第三人称单数形式)具有(某种外表、特性或特征)"},
            {"english": "long", "chinese": "(长度或距离)长的"},
            {"english": "body", "chinese": "身体"},
            {"english": "leg", "chinese": "腿"},
            {"english": "right", "chinese": "(意见或判断)准确，确切，恰当"},
            {"english": "fat", "chinese": "肥的；肥胖的"},
            {"english": "slow", "chinese": "缓慢的；慢的"},
            {"english": "love", "chinese": "喜爱；爱"},
            {"english": "tail", "chinese": "尾；尾巴"},
            {"english": "gift", "chinese": "礼物"},
            {"english": "picture", "chinese": "图画；绘画"},
            {"english": "sing", "chinese": "唱(歌)；演唱"},
            {"english": "dance", "chinese": "跳舞"},
            {"english": "all", "chinese": "所有；全部"},
            {"english": "so", "chinese": "(表示大小或数量)这么，那么"},
            
            # Unit 3 - 下册
            {"english": "eraser", "chinese": "橡皮"},
            {"english": "find", "chinese": "找到；找回"},
            {"english": "pen", "chinese": "钢笔"},
            {"english": "bag", "chinese": "包；袋"},
            {"english": "paper", "chinese": "纸"},
            {"english": "these", "chinese": "这些"},
            {"english": "see", "chinese": "看见"},
            {"english": "hear", "chinese": "听见；听到"},
            {"english": "learn", "chinese": "学；学习"},
            {"english": "class", "chinese": "课；班级"},
            {"english": "computer", "chinese": "计算机；电脑"},
            {"english": "talk", "chinese": "(用某种语言)讲；说；说话"},
            {"english": "song", "chinese": "歌；歌曲"},
            {"english": "much", "chinese": "许多；大量"},
            
            # Unit 4 - 下册
            {"english": "breakfast", "chinese": "早餐；早饭"},
            {"english": "bread", "chinese": "面包"},
            {"english": "noodle", "chinese": "(常用复数)面条"},
            {"english": "meat", "chinese": "肉"},
            {"english": "healthy", "chinese": "健康的"},
            {"english": "soup", "chinese": "汤"},
            {"english": "fruit", "chinese": "水果"},
            
            # Unit 5 - 下册
            {"english": "keep", "chinese": "保有；留着"},
            {"english": "home", "chinese": "家；住所"},
            {"english": "cap", "chinese": "帽子"},
            {"english": "map", "chinese": "地图"},
            {"english": "put", "chinese": "放；安置"},
            
            # Unit 6 - 下册
            {"english": "sixteen", "chinese": "十六"},
            {"english": "seventeen", "chinese": "十七"},
            {"english": "eighteen", "chinese": "十八"},
            {"english": "nineteen", "chinese": "十九"},
        ],
        "sentences": [
            # 自我介绍和问候 (使用 Unit 1 词汇)
            {"english": "What is your name?", "chinese": "你叫什么名字？"},
            {"english": "My name is Tom.", "chinese": "我的名字是汤姆。"},
            {"english": "Nice to meet you.", "chinese": "很高兴认识你。"},
            {"english": "This is my friend.", "chinese": "这是我的朋友。"},
            {"english": "Goodbye!", "chinese": "再见！"},
            {"english": "I can share my toys.", "chinese": "我可以分享我的玩具。"},
            {"english": "Can you help me?", "chinese": "你能帮助我吗？"},
            {"english": "I have a big family.", "chinese": "我有一个大家庭。"},
            {"english": "This is my mother and father.", "chinese": "这是我的妈妈和爸爸。"},
            {"english": "I have a baby brother.", "chinese": "我有一个小弟弟。"},
            
            # 家庭成员 (使用 Unit 2 词汇)
            {"english": "I love my mum and dad.", "chinese": "我爱我的妈妈和爸爸。"},
            {"english": "My grandma is very nice.", "chinese": "我的奶奶/姥姥很好。"},
            {"english": "My grandpa is old.", "chinese": "我的爷爷/姥爷很老了。"},
            
            # 动物 (使用 Unit 3 词汇)
            {"english": "I like dogs.", "chinese": "我喜欢狗。"},
            {"english": "I have a pet cat.", "chinese": "我有一只宠物猫。"},
            {"english": "Let's go to the zoo.", "chinese": "让我们去动物园吧。"},
            {"english": "The panda is cute.", "chinese": "熊猫很可爱。"},
            {"english": "The tiger is fast.", "chinese": "老虎很快。"},
            {"english": "The elephant is big.", "chinese": "大象很大。"},
            {"english": "I can see a monkey.", "chinese": "我能看见一只猴子。"},
            {"english": "The giraffe is tall.", "chinese": "长颈鹿很高。"},
            
            # 水果和植物 (使用 Unit 4 词汇)
            {"english": "I like apples.", "chinese": "我喜欢苹果。"},
            {"english": "I have a banana.", "chinese": "我有一根香蕉。"},
            {"english": "The orange is on the tree.", "chinese": "橙子在树上。"},
            {"english": "I go to school every day.", "chinese": "我每天上学。"},
            {"english": "We have a garden.", "chinese": "我们有一个花园。"},
            {"english": "I water the flowers.", "chinese": "我给花浇水。"},
            {"english": "The sun gives us light.", "chinese": "太阳给我们光。"},
            {"english": "I can plant a tree.", "chinese": "我可以种树。"},
            
            # 颜色 (使用 Unit 5 词汇)
            {"english": "What colour is it?", "chinese": "它是什么颜色？"},
            {"english": "It is red.", "chinese": "它是红色的。"},
            {"english": "I like blue.", "chinese": "我喜欢蓝色。"},
            {"english": "The grass is green.", "chinese": "草是绿色的。"},
            {"english": "I can draw a bear.", "chinese": "我可以画一只熊。"},
            {"english": "The duck is yellow.", "chinese": "鸭子是黄色的。"},
            {"english": "The sea is blue.", "chinese": "大海是蓝色的。"},
            
            # 年龄和时间 (使用 Unit 6 词汇)
            {"english": "How old are you?", "chinese": "你多大了？"},
            {"english": "I am five years old.", "chinese": "我五岁了。"},
            {"english": "What time is it?", "chinese": "现在几点了？"},
            {"english": "It is three o'clock.", "chinese": "现在三点钟。"},
            {"english": "I can cut the cake.", "chinese": "我可以切蛋糕。"},
            {"english": "Let's eat the cake.", "chinese": "让我们吃蛋糕吧。"},
            
            # 国家和人物 (使用下册 Unit 1 词汇)
            {"english": "Where are you from?", "chinese": "你来自哪里？"},
            {"english": "I am from China.", "chinese": "我来自中国。"},
            {"english": "He is from the UK.", "chinese": "他来自英国。"},
            {"english": "She is from Canada.", "chinese": "她来自加拿大。"},
            {"english": "Who is he?", "chinese": "他是谁？"},
            {"english": "He is my teacher.", "chinese": "他是我的老师。"},
            {"english": "She is a student.", "chinese": "她是一名学生。"},
            {"english": "He is my neighbour.", "chinese": "他是我的邻居。"},
            {"english": "He is very good.", "chinese": "他非常好。"},
            
            # 外貌描述 (使用下册 Unit 2 词汇)
            {"english": "He has a long tail.", "chinese": "它有一条长尾巴。"},
            {"english": "She has short hair.", "chinese": "她有短头发。"},
            {"english": "The dog has a fat body.", "chinese": "那只狗有一个胖身体。"},
            {"english": "I love my gift.", "chinese": "我喜欢我的礼物。"},
            {"english": "I can sing a song.", "chinese": "我会唱歌。"},
            {"english": "She can dance.", "chinese": "她会跳舞。"},
            {"english": "Look at her face.", "chinese": "看她的脸。"},
            
            # 学习用品 (使用下册 Unit 3 词汇)
            {"english": "I have a pen.", "chinese": "我有一支钢笔。"},
            {"english": "I can find my pencil.", "chinese": "我能找到我的铅笔。"},
            {"english": "Where is my ruler?", "chinese": "我的尺子在哪里？"},
            {"english": "I have a book and a bag.", "chinese": "我有一本书和一个书包。"},
            {"english": "These are my books.", "chinese": "这些是我的书。"},
            {"english": "I can see the eraser.", "chinese": "我能看见橡皮。"},
            {"english": "We learn English in class.", "chinese": "我们在课堂上学英语。"},
            {"english": "I can hear the song.", "chinese": "我能听到这首歌。"},
            
            # 食物 (使用下册 Unit 4 词汇)
            {"english": "It is time for breakfast.", "chinese": "该吃早饭了。"},
            {"english": "I like bread and milk.", "chinese": "我喜欢面包和牛奶。"},
            {"english": "I have an egg.", "chinese": "我有一个鸡蛋。"},
            {"english": "I like rice and meat.", "chinese": "我喜欢米饭和肉。"},
            {"english": "I eat vegetables every day.", "chinese": "我每天吃蔬菜。"},
            {"english": "Fruit is healthy.", "chinese": "水果是健康的。"},
            {"english": "I want some juice.", "chinese": "我想要一些果汁。"},
            
            # 位置和玩具 (使用下册 Unit 5 词汇)
            {"english": "Where is my ball?", "chinese": "我的球在哪里？"},
            {"english": "The doll is on the box.", "chinese": "玩偶在盒子上。"},
            {"english": "The car is under the bed.", "chinese": "汽车在床下。"},
            {"english": "Put the book in the bag.", "chinese": "把书放进书包里。"},
            {"english": "I am at home.", "chinese": "我在家。"},
            {"english": "The boat is on the water.", "chinese": "船在水上。"},
            {"english": "I can keep my toys.", "chinese": "我可以保管我的玩具。"},
            
            # 数字 (使用下册 Unit 6 词汇)
            {"english": "I have eleven pencils.", "chinese": "我有十一支铅笔。"},
            {"english": "She has twelve books.", "chinese": "她有十二本书。"},
            {"english": "I can count to twenty.", "chinese": "我能数到二十。"},
        ]
    },
    "四年级": {
        "words": [
            # Unit 1 - 上册
            {"english": "PE", "chinese": "体育（课）"},
            {"english": "job", "chinese": "工作；职业"},
            {"english": "doctor", "chinese": "医生"},
            {"english": "farmer", "chinese": "农场主；农民"},
            {"english": "nurse", "chinese": "护士"},
            {"english": "office worker", "chinese": "公司职员"},
            {"english": "factory worker", "chinese": "工厂工人"},
            {"english": "busy", "chinese": "忙碌的"},
            {"english": "tired", "chinese": "疲倦的"},
            {"english": "chore", "chinese": "家庭杂务"},
            {"english": "cook", "chinese": "烹饪；煮"},
            {"english": "clean", "chinese": "打扫；干净的"},
            {"english": "room", "chinese": "房间"},
            {"english": "look after", "chinese": "照顾"},
            {"english": "sweep", "chinese": "扫"},
            {"english": "floor", "chinese": "地板；地面"},
            {"english": "together", "chinese": "在一起；共同"},
            {"english": "people", "chinese": "人；人们"},
            {"english": "child", "chinese": "儿童；小孩"},
            {"english": "children", "chinese": "儿童(child的复数)"},
            
            # Unit 2 - 上册
            {"english": "strong", "chinese": "强壮的"},
            {"english": "hair", "chinese": "头发"},
            {"english": "also", "chinese": "也"},
            {"english": "kind", "chinese": "友好的"},
            {"english": "quiet", "chinese": "文静的"},
            {"english": "best", "chinese": "最好的"},
            {"english": "read", "chinese": "阅读"},
            {"english": "Chinese", "chinese": "中文；中国人；中国的"},
            {"english": "play", "chinese": "玩耍"},
            {"english": "game", "chinese": "游戏"},
            {"english": "football", "chinese": "足球运动"},
            {"english": "basketball", "chinese": "篮球运动"},
            {"english": "always", "chinese": "总是"},
            
            # Unit 3 - 上册
            {"english": "afternoon", "chinese": "下午"},
            {"english": "playground", "chinese": "游乐场；操场"},
            {"english": "over", "chinese": "在……的远端（或对面）"},
            {"english": "shop", "chinese": "商店"},
            {"english": "toilet", "chinese": "厕所；卫生间"},
            {"english": "bus stop", "chinese": "公共汽车站"},
            {"english": "library", "chinese": "图书馆"},
            {"english": "sport", "chinese": "体育运动"},
            {"english": "walk", "chinese": "散步；行走"},
            {"english": "community", "chinese": "社区"},
            {"english": "place", "chinese": "地方；场所"},
            {"english": "photo", "chinese": "照片"},
            {"english": "story", "chinese": "故事"},
            {"english": "buy", "chinese": "购买"},
            
            # Unit 4 - 上册
            {"english": "firefighter", "chinese": "消防队员"},
            {"english": "why", "chinese": "为什么"},
            {"english": "driver", "chinese": "司机"},
            {"english": "cleaner", "chinese": "清洁工"},
            {"english": "cook", "chinese": "厨师"},
            {"english": "delivery worker", "chinese": "快递员"},
            {"english": "police officer", "chinese": "警察；警员"},
            {"english": "a lot", "chinese": "大量；许多"},
            {"english": "now", "chinese": "现在"},
            {"english": "make the bed", "chinese": "铺床"},
            {"english": "tell", "chinese": "讲述；告诉"},
            {"english": "everyone", "chinese": "每人"},
            {"english": "Ms", "chinese": "（用于女子的姓氏或姓名前，不指明婚否）女士"},
            
            # Unit 5 - 上册
            {"english": "speak", "chinese": "说话；发音"},
            {"english": "bad", "chinese": "令人不快的；坏的"},
            {"english": "tomorrow", "chinese": "在明天"},
            {"english": "rain", "chinese": "下雨；雨"},
            {"english": "closed", "chinese": "关闭的"},
            {"english": "film", "chinese": "电影"},
            {"english": "idea", "chinese": "想法；主意"},
            {"english": "fly", "chinese": "操纵（飞行器等）；飞"},
            {"english": "kite", "chinese": "风筝"},
            {"english": "snowman", "chinese": "雪人"},
            {"english": "fun", "chinese": "享乐；乐趣"},
            {"english": "their", "chinese": "他们的；她们的；它们的"},
            {"english": "Sydney", "chinese": "悉尼"},
            
            # Unit 6 - 上册
            {"english": "whose", "chinese": "谁的"},
            {"english": "sweater", "chinese": "毛衣"},
            {"english": "sock", "chinese": "短袜"},
            {"english": "mine", "chinese": "我的"},
            {"english": "wear", "chinese": "穿；戴"},
            {"english": "coat", "chinese": "大衣；外套"},
            {"english": "which", "chinese": "哪一个；哪一些"},
            {"english": "snow", "chinese": "下雪；雪"},
            {"english": "get together", "chinese": "聚会"},
            {"english": "fall", "chinese": "落下"},
            {"english": "leaf", "chinese": "叶"},
            {"english": "leaves", "chinese": "叶（leaf的复数）"},
            {"english": "glove", "chinese": "手套"},
            {"english": "then", "chinese": "然后；那时"},
            
            # Unit 1 - 下册
            {"english": "sorry", "chinese": "对不起"},
            {"english": "hurry up", "chinese": "快点；赶快"},
            {"english": "late", "chinese": "迟到；迟发生"},
            {"english": "class", "chinese": "课；课程；班；班级"},
            {"english": "ready", "chinese": "准备好"},
            {"english": "rule", "chinese": "规则；规章"},
            {"english": "classroom", "chinese": "教室"},
            {"english": "turn off", "chinese": "关掉"},
            {"english": "light", "chinese": "灯；光"},
            {"english": "blackboard", "chinese": "黑板"},
            {"english": "desk", "chinese": "书桌；办公桌"},
            {"english": "chair", "chinese": "椅子"},
            {"english": "tidy", "chinese": "整洁的；整齐的；使整洁；整理"},
            {"english": "music", "chinese": "音乐"},
            {"english": "door", "chinese": "门"},
            {"english": "window", "chinese": "窗"},
            {"english": "fan", "chinese": "风扇"},
            {"english": "when", "chinese": "当……时；什么时候"},
            {"english": "understand", "chinese": "懂；理解"},
            {"english": "wall", "chinese": "墙；壁"},
            {"english": "newspaper", "chinese": "报纸"},
            {"english": "hand out", "chinese": "分发"},
            {"english": "workbook", "chinese": "练习册；作业本"},
            
            # Unit 2 - 下册
            {"english": "watch", "chinese": "看"},
            {"english": "TV", "chinese": "电视"},
            {"english": "homework", "chinese": "家庭作业"},
            {"english": "first", "chinese": "首先；首次；第一"},
            {"english": "wet", "chinese": "湿的；未干的"},
            {"english": "run", "chinese": "跑；奔跑"},
            {"english": "living room", "chinese": "客厅；起居室"},
            {"english": "safe", "chinese": "安全的"},
            {"english": "word", "chinese": "言语；单词；字"},
            {"english": "wash", "chinese": "洗"},
            {"english": "helpful", "chinese": "有帮助的；有用的"},
            {"english": "loud", "chinese": "说话太大声的；吵闹的"},
            {"english": "sleep", "chinese": "睡觉"},
            {"english": "bedroom", "chinese": "卧室"},
            {"english": "kitchen", "chinese": "厨房"},
            {"english": "study", "chinese": "书房"},
            {"english": "bathroom", "chinese": "浴室；洗手间"},
            {"english": "think", "chinese": "想；思考"},
            
            # Unit 3 - 下册
            {"english": "work", "chinese": "（花费时间和精力）做（某事）；工作"},
            {"english": "hard", "chinese": "努力地；费力地"},
            {"english": "follow", "chinese": "遵循，听从（忠告、指示等）"},
            {"english": "feel", "chinese": "觉得；感到"},
            {"english": "over", "chinese": "结束（的）"},
            {"english": "kid", "chinese": "小孩"},
            {"english": "dinner", "chinese": "（中午或晚上吃的）正餐"},
            {"english": "art", "chinese": "美术；艺术"},
            {"english": "lunch", "chinese": "午餐"},
            {"english": "maths", "chinese": "数学"},
            {"english": "get up", "chinese": "起床"},
            {"english": "go to school", "chinese": "上学"},
            {"english": "go home", "chinese": "回家"},
            {"english": "go to bed", "chinese": "上床睡觉"},
            {"english": "want", "chinese": "想要"},
            {"english": "clock", "chinese": "时钟"},
            {"english": "just", "chinese": "只是；仅仅；正要"},
            {"english": "minute", "chinese": "分钟"},
            
            # Unit 4 - 下册
            {"english": "trousers", "chinese": "裤子"},
            {"english": "pair", "chinese": "（由连在一起的相似两部分构成的）一条，一副"},
            {"english": "clothes", "chinese": "衣服；服装"},
            {"english": "those", "chinese": "（指较远的人或事物）那些"},
            {"english": "shorts", "chinese": "短裤"},
            {"english": "jacket", "chinese": "夹克衫；短上衣"},
            {"english": "skirt", "chinese": "裙子"},
            {"english": "dear", "chinese": "亲爱的"},
            {"english": "expensive", "chinese": "昂贵的；价格高的"},
            {"english": "take", "chinese": "买下"},
            {"english": "cheap", "chinese": "便宜的"},
            {"english": "shoe", "chinese": "鞋"},
            {"english": "beautiful", "chinese": "美丽的"},
            {"english": "hat", "chinese": "帽子"},
            {"english": "sunglasses", "chinese": "太阳镜；墨镜"},
            {"english": "free", "chinese": "免费的"},
            {"english": "large", "chinese": "（服装、食物、日用品等）大型号的"},
            {"english": "size", "chinese": "尺码；号"},
            {"english": "list", "chinese": "清单；目录"},
            {"english": "try on", "chinese": "试穿"},
            {"english": "any", "chinese": "任何的；任一的"},
            
            # Unit 5 - 下册
            {"english": "cow", "chinese": "奶牛"},
            {"english": "horse", "chinese": "马"},
            {"english": "sheep", "chinese": "羊；绵羊"},
            {"english": "pig", "chinese": "猪"},
            {"english": "chicken", "chinese": "鸡；鸡肉"},
            {"english": "tomato", "chinese": "西红柿"},
            {"english": "bee", "chinese": "蜜蜂"},
            {"english": "mouse", "chinese": "（复数mice）老鼠"},
            {"english": "carrot", "chinese": "胡萝卜"},
            {"english": "potato", "chinese": "土豆"},
            {"english": "green bean", "chinese": "四季豆"},
            {"english": "can", "chinese": "（罐装饮料或食品的）罐"},
            {"english": "delicious", "chinese": "美味的"},
            {"english": "waste", "chinese": "浪费；滥用"},
            {"english": "food", "chinese": "食物"},
            {"english": "clear the table", "chinese": "收拾餐桌"},
            {"english": "set the table", "chinese": "摆餐桌"},
            {"english": "bowl", "chinese": "碗"},
            {"english": "spoon", "chinese": "勺；匙"},
            {"english": "supermarket", "chinese": "超市"},
            {"english": "herself", "chinese": "（用作第三人称单数女性的反身代词）她自己"},
            {"english": "pack", "chinese": "包装"},
            {"english": "milk", "chinese": "牛奶；挤奶"},
            {"english": "knife", "chinese": "刀"},
            {"english": "fork", "chinese": "叉子"},
            {"english": "chopstick", "chinese": "筷子"},
            {"english": "salad", "chinese": "色拉"},
            
            # Unit 6 - 下册
            {"english": "feed", "chinese": "（人）给（动物）食物；喂养"},
            {"english": "pass", "chinese": "递；传递"},
            {"english": "pick", "chinese": "采；摘"},
            {"english": "week", "chinese": "周；星期；周，礼拜"},
        ],
        "sentences": [
            # Unit 1 - 上册句子
            {"english": "What's your mother's job?", "chinese": "你妈妈做什么工作？"},
            {"english": "She's a doctor.", "chinese": "她是医生。"},
            {"english": "Mum and Dad are busy and tired.", "chinese": "爸爸妈妈又忙又累。"},
            {"english": "What can we do for them?", "chinese": "我们能为他们做些什么？"},
            {"english": "We can do some chores.", "chinese": "我们可以做一些家务活。"},
            
            # Unit 2 - 上册句子
            {"english": "What's your friend's name?", "chinese": "你的朋友叫什么名字？"},
            {"english": "His name is Zhang Peng.", "chinese": "他叫张鹏。"},
            {"english": "He's tall and strong.", "chinese": "他又高又壮。"},
            {"english": "He's also kind.", "chinese": "他也很友善。"},
            {"english": "He often helps me.", "chinese": "他经常帮助我。"},
            {"english": "Who's your best friend?", "chinese": "谁是你最好的朋友？"},
            {"english": "Chen Jie. She's funny.", "chinese": "陈杰。她很有趣。"},
            {"english": "She often makes me smile.", "chinese": "她经常让我开心。"},
            
            # Unit 3 - 上册句子
            {"english": "There is a playground.", "chinese": "那里有个游乐场。"},
            {"english": "We often play there.", "chinese": "我们经常在那里玩儿。"},
            {"english": "There is a taijiquan club.", "chinese": "这里有一个太极拳俱乐部。"},
            {"english": "There are many people.", "chinese": "这里有好多人。"},
            {"english": "There is a gym too.", "chinese": "这里还有一个体育馆。"},
            {"english": "Great! Let's do some sports.", "chinese": "太棒了！我们一起做运动吧。"},
            {"english": "My favourite place is the museum.", "chinese": "我最喜欢的地方是博物馆。"},
            
            # Unit 4 - 上册句子
            {"english": "Our neighbour is a firefighter.", "chinese": "我们的邻居是消防员。"},
            {"english": "He often helps people.", "chinese": "他经常帮助别人。"},
            {"english": "He's a school bus driver.", "chinese": "他是校车司机。"},
            {"english": "He takes us to school every day.", "chinese": "他每天送我们去学校。"},
            {"english": "That's an important job too!", "chinese": "那个工作也很重要！"},
            {"english": "Chen Jie is making the bed.", "chinese": "陈杰正在铺床。"},
            
            # Unit 5 - 上册句子
            {"english": "Hello! Mark speaking.", "chinese": "你好！我是马克。"},
            {"english": "Hi, Mark! This is John.", "chinese": "嗨，马克！我是约翰。"},
            {"english": "What's the weather like in Sydney?", "chinese": "悉尼的天气怎么样？"},
            {"english": "Well, it's sunny today.", "chinese": "嗯，今天是晴天。"},
            {"english": "It's only two degrees in Beijing.", "chinese": "北京只有两度。"},
            {"english": "It's raining now.", "chinese": "现在下雨了。"},
            {"english": "We can't play basketball in the park.", "chinese": "我们不能在公园打篮球了。"},
            {"english": "It's OK. We can go to the library.", "chinese": "没关系。我们可以去图书馆。"},
            {"english": "It's hot and sunny here.", "chinese": "这里很热，是个大晴天。"},
            {"english": "Their children swim in the pool.", "chinese": "他们的孩子在泳池里游泳。"},
            
            # Unit 6 - 上册句子
            {"english": "Whose sweater is this, Mum?", "chinese": "这是谁的毛衣，妈妈？"},
            {"english": "It's your dad's.", "chinese": "是你爸爸的。"},
            {"english": "Can I wear this new shirt today?", "chinese": "我今天可以穿这件新衬衫吗？"},
            {"english": "Yes, but wear a coat too.", "chinese": "可以，但是再穿一件外套吧。"},
            {"english": "It's cold and windy outside.", "chinese": "外面有风，很冷。"},
            {"english": "Which season do you like?", "chinese": "你喜欢哪个季节？"},
            {"english": "Winter. It snows a lot.", "chinese": "冬天。冬天经常下雪。"},
            {"english": "I like winter too.", "chinese": "我也喜欢冬天。"},
            {"english": "There are many festivals.", "chinese": "（在冬天）有很多节日。"},
            {"english": "It's full of life.", "chinese": "（春天）充满生机。"},
            {"english": "And enjoy mooncakes.", "chinese": "还品尝月饼。"},
            {"english": "Then spring comes again.", "chinese": "接着春天又来了。"},
            
            # Unit 1 - 下册句子
            {"english": "Hurry up! Don't be late for class!", "chinese": "快点！上课别迟到！"},
            {"english": "I'm ready. Let's go!", "chinese": "我准备好了。我们走吧！"},
            {"english": "Who's on duty today?", "chinese": "今天谁值日？"},
            {"english": "I can put back the desks and chairs.", "chinese": "我可以把桌椅放回原位。"},
            {"english": "Excuse me?", "chinese": "对不起，请再说一次可以吗？"},
            {"english": "It's 5 o'clock.", "chinese": "现在五点了。"},
            {"english": "Time to go home, kids.", "chinese": "孩子们，该回家了。"},
            {"english": "It's time for dinner.", "chinese": "该吃晚饭了。"},
            {"english": "It's time to get up.", "chinese": "该起床了。"},
            {"english": "Have a nice day!", "chinese": "祝你一天愉快！"},
            
            # Unit 2 - 下册句子
            {"english": "Mum, can I watch TV?", "chinese": "妈妈，我能看电视吗？"},
            {"english": "No. You have to do your homework first.", "chinese": "不行。你得先做作业。"},
            {"english": "Shh. Don't be so loud!", "chinese": "嘘。别这么大声！"},
            {"english": "Be careful, Jack. Don't touch hot things.", "chinese": "杰克，要小心。别碰烫的东西。"},
            
            # Unit 3 - 下册句子
            {"english": "What time is it?", "chinese": "几点了？"},
            {"english": "It's 5 o'clock.", "chinese": "现在五点了。"},
            {"english": "Time to go home, kids.", "chinese": "孩子们，该回家了。"},
            {"english": "It's time for dinner.", "chinese": "该吃晚饭了。"},
            {"english": "It's time to get up.", "chinese": "该起床了。"},
            {"english": "Have a nice day!", "chinese": "祝你一天愉快！"},
            
            # Unit 4 - 下册句子
            {"english": "Can I buy a new pair?", "chinese": "我能买条新的（裤子）吗？"},
            {"english": "Sure. Let's go to the clothes shop.", "chinese": "当然。我们去服装店吧。"},
            {"english": "You already have too many shorts. Let's buy trousers.", "chinese": "你已经有很多短裤了。我们买长裤吧。"},
            {"english": "Can I help you?", "chinese": "要帮忙吗？"},
            {"english": "Yes. I like this pink dress.", "chinese": "嗯。我喜欢这件粉色的长裙。"},
            {"english": "Let's take it.", "chinese": "我们买下它吧。"},
            
            # Unit 5 - 下册句子
            {"english": "What animals do you have on the farm?", "chinese": "你的农场上都养了哪些动物？"},
            {"english": "I have a lot of animals.", "chinese": "我养了很多动物。"},
            {"english": "What are these?", "chinese": "这些是什么？"},
            {"english": "They're tomatoes.", "chinese": "这些是西红柿。"},
            {"english": "How fresh!", "chinese": "真新鲜啊！"},
            {"english": "Can you please pass me the vegetables?", "chinese": "能否请你把蔬菜递给我？"},
            {"english": "Mike, Amy, would you like a knife and fork?", "chinese": "迈克、埃米，你们需要餐刀和餐叉吗？"},
            {"english": "No, thank you. Mr Wang. I can use chopsticks.", "chinese": "不用，谢谢您，王先生。我会用筷子。"},
            {"english": "Don't waste food, please.", "chinese": "请不要浪费食物。"},
            
            # Unit 6 - 下册句子
            {"english": "Let's feed the chickens.", "chinese": "我们喂鸡吧。"},
        ]
    }
}


def get_all_grades():
    """获取所有年级列表"""
    return list(WORD_BANK.keys())


def get_words_by_grade(grade: str):
    """获取指定年级的单词"""
    if grade in WORD_BANK:
        return WORD_BANK[grade]["words"]
    return []


def get_sentences_by_grade(grade: str):
    """获取指定年级的句子"""
    if grade in WORD_BANK:
        return WORD_BANK[grade]["sentences"]
    return []


def get_all_items_by_grade(grade: str):
    """获取指定年级的所有单词和句子"""
    words = [{"type": "word", **w} for w in get_words_by_grade(grade)]
    sentences = [{"type": "sentence", **s} for s in get_sentences_by_grade(grade)]
    return words + sentences


def get_items_by_grades(grades: list):
    """获取多个年级的所有单词和句子"""
    all_items = []
    for grade in grades:
        all_items.extend(get_all_items_by_grade(grade))
    return all_items
