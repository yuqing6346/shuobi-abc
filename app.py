"""
英语单词听写工具
使用 KittenTTS 进行语音合成
支持词库选择、难度设置、答题判分和智能重点复习
"""

import gradio as gr
import numpy as np
import random
import json
import os
from datetime import datetime
from kittentts import KittenTTS
from word_bank import WORD_BANK, get_all_grades, get_items_by_grades
from game_state import game_state

# 设置 HuggingFace 镜像源
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# 初始化 TTS 模型
print("正在加载 TTS 模型，首次运行可能需要下载...")
print("使用 HuggingFace 镜像源: https://hf-mirror.com")
tts_model = KittenTTS("KittenML/kitten-tts-nano-0.8")
print("模型加载完成！")

# 可用的声音列表
VOICES = ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']

# 难度设置 - 句子占比
DIFFICULTY_LEVELS = {
    "轻松": {"sentence_ratio": 0.1, "description": "90%单词 + 10%句子"},
    "进阶": {"sentence_ratio": 0.3, "description": "70%单词 + 30%句子"},
    "挑战": {"sentence_ratio": 0.5, "description": "50%单词 + 50%句子"}
}

# 错误记录文件路径
ERROR_LOG_FILE = "error_records.json"
# 重点复习文件路径
REVIEW_FILE = "review_list.json"

# ============== 艾宾浩斯记忆曲线配置 ==============
# 复习时间间隔（天）：1天、2天、4天、7天、15天
EBBINGHAUS_INTERVALS = [1, 2, 4, 7, 15]
# 连续答对次数达标后移除
CORRECT_THRESHOLD = 2


def load_error_records():
    """加载错误记录"""
    if os.path.exists(ERROR_LOG_FILE):
        try:
            with open(ERROR_LOG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_error_records(records):
    """保存错误记录"""
    with open(ERROR_LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def load_review_list():
    """加载重点复习列表"""
    if os.path.exists(REVIEW_FILE):
        try:
            with open(REVIEW_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_review_list(review_list):
    """保存重点复习列表"""
    with open(REVIEW_FILE, 'w', encoding='utf-8') as f:
        json.dump(review_list, f, ensure_ascii=False, indent=2)


def add_to_review_list(english_text, chinese_text, item_type):
    """
    添加到重点复习列表（艾宾浩斯记忆曲线）
    初始化复习计划和正确次数跟踪
    """
    review_list = load_review_list()
    current_time = datetime.now()
    
    if english_text not in review_list:
        # 新增到复习列表，设置第一次复习时间为1天后
        review_list[english_text] = {
            "chinese": chinese_text,
            "type": item_type,
            "added_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
            "review_count": 0,
            # 艾宾浩斯记忆曲线：记录当前复习阶段（0-4对应1,2,4,7,15天）
            "ebbinghaus_stage": 0,
            # 下次应该复习的时间
            "next_review_time": (current_time.replace(hour=0, minute=0, second=0, microsecond=0) + 
                                 __import__('datetime').timedelta(days=EBBINGHAUS_INTERVALS[0])).strftime("%Y-%m-%d %H:%M:%S"),
            # 连续答对次数
            "consecutive_correct": 0,
            # 复习历史记录
            "review_history": []
        }
        save_review_list(review_list)
    else:
        # 如果已存在但答错了，重置连续答对次数和复习阶段
        review_list[english_text]["consecutive_correct"] = 0
        review_list[english_text]["ebbinghaus_stage"] = 0
        review_list[english_text]["next_review_time"] = (current_time.replace(hour=0, minute=0, second=0, microsecond=0) + 
                                                          __import__('datetime').timedelta(days=EBBINGHAUS_INTERVALS[0])).strftime("%Y-%m-%d %H:%M:%S")
        save_review_list(review_list)


def update_review_progress(english_text):
    """
    更新复习进度（艾宾浩斯记忆曲线）
    答对后：
    1. 增加连续答对次数
    2. 如果达到2次，移除该词
    3. 否则，进入下一个复习阶段，设置下次复习时间
    """
    review_list = load_review_list()
    if english_text not in review_list:
        return {"removed": False, "message": "不在复习列表中"}
    
    item = review_list[english_text]
    item["consecutive_correct"] += 1
    current_time = datetime.now()
    
    # 记录本次复习
    item["review_history"].append({
        "time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
        "result": "correct",
        "stage": item["ebbinghaus_stage"]
    })
    
    # 检查是否达到移除标准
    if item["consecutive_correct"] >= CORRECT_THRESHOLD:
        # 连续答对2次，从复习列表移除
        del review_list[english_text]
        save_review_list(review_list)
        return {
            "removed": True,
            "message": f"🎉 已掌握！连续答对{CORRECT_THRESHOLD}次",
            "consecutive_correct": item["consecutive_correct"]
        }
    else:
        # 进入下一个复习阶段
        item["ebbinghaus_stage"] += 1
        
        # 如果还在艾宾浩斯间隔内，设置下次复习时间
        if item["ebbinghaus_stage"] < len(EBBINGHAUS_INTERVALS):
            next_interval = EBBINGHAUS_INTERVALS[item["ebbinghaus_stage"]]
            item["next_review_time"] = (current_time.replace(hour=0, minute=0, second=0, microsecond=0) + 
                                        __import__('datetime').timedelta(days=next_interval)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            # 已完成所有复习阶段，但未连续答对2次，保持最后阶段
            item["ebbinghaus_stage"] = len(EBBINGHAUS_INTERVALS) - 1
            next_interval = EBBINGHAUS_INTERVALS[-1]
            item["next_review_time"] = (current_time.replace(hour=0, minute=0, second=0, microsecond=0) + 
                                        __import__('datetime').timedelta(days=next_interval)).strftime("%Y-%m-%d %H:%M:%S")
        
        save_review_list(review_list)
        return {
            "removed": False,
            "message": f"✅ 答对 {item['consecutive_correct']}/{CORRECT_THRESHOLD} 次",
            "consecutive_correct": item["consecutive_correct"],
            "next_review_days": next_interval
        }


def remove_from_review_list(english_text):
    """从重点复习列表移除（直接删除，不推荐使用）"""
    review_list = load_review_list()
    if english_text in review_list:
        del review_list[english_text]
        save_review_list(review_list)


def get_error_count(english_text):
    """获取某个单词/句子的错误次数"""
    records = load_error_records()
    return records.get(english_text, {}).get("error_count", 0)


def get_review_statistics():
    """
    获取复习统计信息（艾宾浩斯记忆曲线）
    返回复习列表的统计数据
    """
    review_list = load_review_list()
    if not review_list:
        return {
            "total": 0,
            "due_count": 0,
            "stages": [0, 0, 0, 0, 0],
            "consecutive_stats": {},
            "items": []
        }
    
    due_items = get_due_review_items()
    due_count = len(due_items)
    
    # 统计各阶段的词汇数量
    stages = [0, 0, 0, 0, 0]
    consecutive_stats = {0: 0, 1: 0}  # 0次答对、1次答对
    
    all_items = []
    for english_text, item in review_list.items():
        stage = item.get("ebbinghaus_stage", 0)
        if stage < len(stages):
            stages[stage] += 1
        
        consecutive = item.get("consecutive_correct", 0)
        if consecutive in consecutive_stats:
            consecutive_stats[consecutive] += 1
        
        all_items.append({
            "english": english_text,
            "chinese": item["chinese"],
            "type": item["type"],
            "stage": stage,
            "consecutive": consecutive,
            "next_review": item.get("next_review_time", "未设置"),
            "added_time": item.get("added_time", "未知")
        })
    
    # 按阶段和连续答对次数排序
    all_items.sort(key=lambda x: (x["stage"], x["consecutive"]))
    
    return {
        "total": len(review_list),
        "due_count": due_count,
        "stages": stages,
        "consecutive_stats": consecutive_stats,
        "items": all_items
    }


def record_error(english_text, chinese_text, item_type):
    """记录一次错误"""
    records = load_error_records()
    if english_text not in records:
        records[english_text] = {
            "chinese": chinese_text,
            "type": item_type,
            "error_count": 0,
            "last_error": None
        }
    records[english_text]["error_count"] += 1
    records[english_text]["last_error"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_error_records(records)
    
    # 自动加入重点复习
    add_to_review_list(english_text, chinese_text, item_type)


def get_due_review_items():
    """
    获取到期需要复习的词汇（根据艾宾浩斯记忆曲线）
    返回已经到了复习时间的词汇列表
    """
    review_list = load_review_list()
    current_time = datetime.now()
    due_items = []
    
    for english_text, item in review_list.items():
        next_review_time = datetime.strptime(item.get("next_review_time", "2099-12-31 00:00:00"), "%Y-%m-%d %H:%M:%S")
        
        # 如果当前时间 >= 复习时间，表示到期了
        if current_time >= next_review_time:
            due_items.append({
                "english": english_text,
                "chinese": item["chinese"],
                "type": item["type"],
                "stage": item.get("ebbinghaus_stage", 0),
                "consecutive_correct": item.get("consecutive_correct", 0),
                "overdue_days": (current_time - next_review_time).days
            })
    
    # 按照逾期天数排序，逾期越久越优先
    due_items.sort(key=lambda x: x["overdue_days"], reverse=True)
    return due_items


def record_correct(english_text):
    """记录一次正确"""
    # 答对后更新复习进度（艾宾浩斯记忆曲线）
    review_result = update_review_progress(english_text)
    return review_result


def generate_speech(text: str, voice: str = "Luna", speed: float = 0.8):
    """生成语音 - 返回(采样率, 音频数组)元组供Gradio使用"""
    if not text.strip():
        return None
    audio = tts_model.generate(text.strip(), voice=voice, speed=speed)
    # Gradio Audio组件接受(sample_rate, numpy_array)元组
    return (24000, audio)


def select_items_for_quiz(grades: list, difficulty: str, count: int):
    """
    根据设置选择听写题目（艾宾浩斯智能复习）
    优先级：
    1. 到期需要复习的词汇（根据艾宾浩斯曲线）
    2. 其他重点复习词汇
    3. 正常词库（排除已掌握的词汇）
    """
    all_items = get_items_by_grades(grades)
    
    if not all_items:
        return []
    
    # 获取到期需要复习的词汇
    due_items = get_due_review_items()
    due_words_set = {item["english"] for item in due_items}
    
    # 加载重点复习列表
    review_list = load_review_list()
    
    # 分类题目
    due_review_items = []  # 到期需要复习的
    other_review_items = []  # 其他重点复习
    normal_items = []  # 正常词库
    
    for item in all_items:
        # 检查是否已掌握（如果第一次答对，则不再出现）
        is_sentence = item["type"] == "sentence"
        is_mastered = game_state.is_mastered(item["english"], is_sentence)
        
        # 如果已掌握且不在复习列表中，则跳过
        if is_mastered and item["english"] not in review_list and item["english"] not in due_words_set:
            continue
        
        if item["english"] in due_words_set:
            due_review_items.append(item)
        elif item["english"] in review_list:
            other_review_items.append(item)
        else:
            normal_items.append(item)
    
    # 分离单词和句子
    words = [item for item in normal_items if item["type"] == "word"]
    sentences = [item for item in normal_items if item["type"] == "sentence"]
    
    # 根据难度计算句子数量
    sentence_ratio = DIFFICULTY_LEVELS[difficulty]["sentence_ratio"]
    
    # ===== 新的选择策略 =====
    # 1. 优先选择到期复习的词汇（最多占50%）
    due_count = min(len(due_review_items), int(count * 0.5))
    
    # 2. 其他重点复习词汇（最多占30%）
    other_review_count = min(len(other_review_items), int(count * 0.3))
    
    # 3. 剩余的从正常词库选择
    normal_count = count - due_count - other_review_count
    
    sentence_count = int(normal_count * sentence_ratio)
    word_count = normal_count - sentence_count
    
    # 确保不超过可用数量
    sentence_count = min(sentence_count, len(sentences))
    word_count = min(word_count, len(words))
    
    # 如果某一类不够，用另一类补充
    if sentence_count < int(normal_count * sentence_ratio) and len(words) > word_count:
        word_count = min(normal_count - sentence_count, len(words))
    if word_count < normal_count - sentence_count and len(sentences) > sentence_count:
        sentence_count = min(normal_count - word_count, len(sentences))
    
    # 随机选择
    selected_words = random.sample(words, word_count) if words else []
    selected_sentences = random.sample(sentences, sentence_count) if sentences else []
    
    # 到期复习词汇按逾期天数排序，选择最需要复习的
    selected_due = due_review_items[:due_count] if due_review_items else []
    
    # 其他复习词汇随机选择
    selected_other_review = random.sample(other_review_items, other_review_count) if other_review_items else []
    
    # 合并：先放到期复习的（确保优先），然后打乱其他的
    other_items = selected_words + selected_sentences + selected_other_review
    random.shuffle(other_items)
    
    selected = selected_due + other_items
    
    return selected


# 全局状态
class QuizState:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.items = []
        self.current_index = 0
        self.answers = []
        self.results = []
        self.started = False
        self.finished = False
        self.current_error_count = 0
        self.show_answer_confirmed = False  # 是否已确认查看答案
        self.hint_used = False  # 是否使用了提示
    
    def current_item(self):
        if 0 <= self.current_index < len(self.items):
            return self.items[self.current_index]
        return None
    
    def reset_current_error(self):
        """重置当前题目的错误计数"""
        self.current_error_count = 0
        self.show_answer_confirmed = False
        self.hint_used = False
    
    def add_current_error(self):
        """增加当前题目的错误计数"""
        self.current_error_count += 1


quiz_state = QuizState()


def start_quiz(grades, difficulty, count, voice, speed):
    """开始听写"""
    if not grades:
        return (
            None, "⚠️ 请至少选择一个年级！", "", "",
            gr.update(visible=False), gr.update(visible=False),
            gr.update(visible=False), gr.update(visible=False),
            gr.update(visible=False), gr.update(visible=False),
            gr.update(visible=True), "",
            gr.update(visible=True), gr.update(value="📋 隐藏设置"),
            "", True,
        )
    
    quiz_state.reset()
    quiz_state.items = select_items_for_quiz(grades, difficulty, int(count))
    quiz_state.started = True
    
    if not quiz_state.items:
        return (
            None, "⚠️ 所选年级没有足够的单词/句子！", "", "",
            gr.update(visible=False), gr.update(visible=False),
            gr.update(visible=False), gr.update(visible=False),
            gr.update(visible=False), gr.update(visible=False),
            gr.update(visible=True), "",
            gr.update(visible=True), gr.update(value="📋 隐藏设置"),
            "", True,
        )
    
    # 生成第一题的音频
    current = quiz_state.current_item()
    audio_path = generate_speech(current["english"], voice, speed)
    item_type = "📝 单词" if current["type"] == "word" else "📄 句子"
    
    # 检查是否在重点复习列表
    review_list = load_review_list()
    is_review = current["english"] in review_list
    
    # 检查是否到期需要复习
    is_due = False
    review_stage_info = ""
    if is_review:
        due_items = get_due_review_items()
        due_words_set = {item["english"] for item in due_items}
        is_due = current["english"] in due_words_set
        
        # 显示复习阶段信息
        current_review_data = review_list.get(current["english"], {})
        stage = current_review_data.get("ebbinghaus_stage", 0)
        consecutive = current_review_data.get("consecutive_correct", 0)
        review_stage_info = f" [复习阶段{stage+1}, {consecutive}/{CORRECT_THRESHOLD}次]"
    
    review_hint = " 🔴 到期复习" + review_stage_info if is_due else (" 🟡 待复习" + review_stage_info if is_review else "")
    
    error_count = get_error_count(current["english"])
    error_info = f" (历史错误: {error_count}次)" if error_count > 0 else ""
    quiz_state.reset_current_error()
    
    return (
        audio_path,
        f"🎧 听写开始！请听音频写出 {item_type}{review_hint}{error_info}",
        "", "",
        gr.update(visible=True), gr.update(visible=True),
        gr.update(visible=True, value=""),
        gr.update(visible=True), gr.update(visible=False),
        gr.update(visible=False, value=""),
        gr.update(visible=False), f"📊 进度: {quiz_state.current_index + 1} / {len(quiz_state.items)}",
        gr.update(visible=False), gr.update(value="📋 显示设置"),
        "", False,
    )


def show_hint():
    """显示中文提示"""
    current = quiz_state.current_item()
    if current:
        quiz_state.hint_used = True
        return f"💡 **提示**: {current['chinese']}"
    return ""


def show_answer_with_confirmation():
    """显示答案（需要确认）"""
    current = quiz_state.current_item()
    if not current:
        return "", gr.update(visible=False)
    
    if not quiz_state.show_answer_confirmed:
        # 第一次点击，显示确认对话框
        quiz_state.show_answer_confirmed = True
        return (
            "⚠️ **确认要查看答案吗？**\n\n查看后此题将加入重点复习，以后会更频繁出现。\n\n请再次点击「公布答案」确认查看。",
            gr.update(visible=True)
        )
    else:
        # 第二次点击，显示答案并加入重点复习
        add_to_review_list(current["english"], current["chinese"], current["type"])
        return (
            f"📖 **正确答案**: {current['english']}\n\n✅ 已加入重点复习列表",
            gr.update(visible=True)
        )


def normalize_answer(text):
    """标准化答案文本"""
    import re
    text = text.strip().lower()
    text = re.sub(r'[.?!]+$', '', text).strip()
    
    contractions = {
        "i'm": "i am", "you're": "you are", "he's": "he is", "she's": "she is",
        "it's": "it is", "we're": "we are", "they're": "they are",
        "i've": "i have", "you've": "you have", "we've": "we have", "they've": "they have",
        "i'd": "i would", "you'd": "you would", "he'd": "he would", "she'd": "she would",
        "we'd": "we would", "they'd": "they would",
        "i'll": "i will", "you'll": "you will", "he'll": "he will", "she'll": "she will",
        "it'll": "it will", "we'll": "we will", "they'll": "they will",
        "isn't": "is not", "aren't": "are not", "wasn't": "was not", "weren't": "were not",
        "haven't": "have not", "hasn't": "has not", "hadn't": "had not",
        "won't": "will not", "wouldn't": "would not",
        "don't": "do not", "doesn't": "does not", "didn't": "did not",
        "can't": "cannot", "couldn't": "could not", "shouldn't": "should not",
        "let's": "let us", "that's": "that is", "what's": "what is",
        "who's": "who is", "where's": "where is", "how's": "how is",
    }
    return text, contractions


def compare_answers(correct, user_input):
    """智能比较答案"""
    import re
    correct_normalized, contractions = normalize_answer(correct)
    user_normalized, _ = normalize_answer(user_input)
    
    if correct_normalized == user_normalized:
        return True
    
    def expand_contractions(text, mapping):
        result = text
        for short, full in mapping.items():
            result = re.sub(r'\b' + re.escape(short) + r'\b', full, result)
        return result
    
    def contract_text(text, mapping):
        result = text
        for short, full in mapping.items():
            result = re.sub(r'\b' + re.escape(full) + r'\b', short, result)
        return result
    
    correct_expanded = expand_contractions(correct_normalized, contractions)
    user_expanded = expand_contractions(user_normalized, contractions)
    
    if correct_expanded == user_expanded:
        return True
    
    correct_contracted = contract_text(correct_normalized, contractions)
    user_contracted = contract_text(user_normalized, contractions)
    
    if correct_contracted == user_contracted:
        return True
    
    if correct_expanded == user_contracted or correct_contracted == user_expanded:
        return True
    
    return False


def submit_answer(answer, voice, speed):
    """提交答案"""
    current = quiz_state.current_item()
    if not current:
        return (
            None, "⚠️ 没有当前题目", "", "",
            gr.update(), gr.update(), gr.update(), gr.update(),
            gr.update(), gr.update(visible=False), gr.update(),
            "", gr.update(), gr.update(), "", gr.update(),
        )
    
    is_correct = compare_answers(current["english"], answer)
    item_type = "📝 单词" if current["type"] == "word" else "📄 句子"
    
    if is_correct:
        # 答对了！
        is_sentence = current["type"] == "sentence"
        no_hint = not quiz_state.hint_used
        
        # === 新增：更新连击 ===
        streak_result = game_state.update_streak(True)
        streak = streak_result["current_streak"]
        
        # === 新增：积分系统 ===
        base_score = 20 if is_sentence else 10
        score_result = game_state.add_score(
            base_score=base_score,
            streak=streak,
            no_hint=no_hint
        )
        
        # === 新增：词汇掌握统计 ===
        mastered_result = game_state.mark_as_mastered(
            english=current["english"],
            is_sentence=is_sentence,
            no_hint=no_hint
        )
        
        # === 新增：无提示连对统计 ===
        game_state.update_perfect_streak(is_correct=True, no_hint=no_hint)
        
        quiz_state.results.append({
            "item": current,
            "user_answer": answer,
            "is_correct": True,
            "error_count": quiz_state.current_error_count,
            "score_earned": score_result["score_added"],
            "mastered": mastered_result["newly_mastered"]
        })
        
        # 更新复习进度（艾宾浩斯记忆曲线）
        review_result = record_correct(current["english"])
        
        has_next = quiz_state.current_index < len(quiz_state.items) - 1
        
        if has_next:
            # 进入下一题
            quiz_state.current_index += 1
            quiz_state.reset_current_error()
            next_item = quiz_state.current_item()
            audio_path = generate_speech(next_item["english"], voice, speed)
            next_item_type = "📝 单词" if next_item["type"] == "word" else "📄 句子"
            
            # 检查是否在重点复习列表
            review_list = load_review_list()
            is_review = next_item["english"] in review_list
            
            # 检查是否到期需要复习
            is_due = False
            review_stage_info = ""
            if is_review:
                due_items = get_due_review_items()
                due_words_set = {item["english"] for item in due_items}
                is_due = next_item["english"] in due_words_set
                
                # 显示复习阶段信息
                next_item_review_data = review_list.get(next_item["english"], {})
                stage = next_item_review_data.get("ebbinghaus_stage", 0)
                consecutive = next_item_review_data.get("consecutive_correct", 0)
                review_stage_info = f" [复习阶段{stage+1}, {consecutive}/{CORRECT_THRESHOLD}次]"
            
            review_hint = " 🔴 到期复习" + review_stage_info if is_due else (" 🟡 待复习" + review_stage_info if is_review else "")
            
            history_error_count = get_error_count(next_item["english"])
            error_info = f" (历史错误: {history_error_count}次)" if history_error_count > 0 else ""
            
            # 生成反馈消息
            feedback = "✅ 正确！"
            if score_result["score_added"] > 0:
                feedback += f" +{score_result['score_added']}分"
                if streak >= 3:
                    feedback += f" 🔥{streak}连击！"
            if mastered_result["newly_mastered"]:
                feedback += " 📚已掌握！"
            
            # 添加复习进度反馈
            if review_result and review_result.get("message"):
                feedback += f" {review_result['message']}"
                if review_result.get("removed"):
                    feedback += " 已从复习列表移除！"
                elif review_result.get("next_review_days"):
                    feedback += f" 下次复习: {review_result['next_review_days']}天后"
            
            if score_result.get("title_up"):
                new_title = score_result["new_title"]
                feedback += f"\n\n🎊 称号晋升：{new_title['emoji']} {new_title['name']}！"
            
            return (
                audio_path,
                f"{feedback}\n\n🎧 请听音频写出 {next_item_type}{review_hint}{error_info}",
                "", "",
                gr.update(visible=True), gr.update(visible=True),
                gr.update(visible=True, value="", elem_classes=[]),
                gr.update(visible=True), gr.update(visible=False),
                gr.update(visible=False, value=""),
                gr.update(visible=False),
                f"📊 进度: {quiz_state.current_index + 1} / {len(quiz_state.items)}",
                gr.update(), gr.update(), "", gr.update(),
            )
        else:
            # 最后一题答对
            return show_summary_with_sidebar()
    else:
        # 答错了！
        quiz_state.add_current_error()
        record_error(current["english"], current["chinese"], current["type"])
        
        # === 新增：中断连击和连对 ===
        game_state.update_streak(False)
        game_state.update_perfect_streak(is_correct=False, no_hint=not quiz_state.hint_used)
        
        error_msg = f"❌ 错误！请重新输入 (本题已错 {quiz_state.current_error_count} 次)"
        
        # 重新生成音频，让用户可以继续听
        audio_path = generate_speech(current["english"], voice, speed)
        
        return (
            audio_path, error_msg, "", "",
            gr.update(visible=True), gr.update(visible=True),
            gr.update(visible=True, elem_classes=["shake-animation"]),
            gr.update(visible=True), gr.update(visible=False),
            gr.update(visible=False, value=""),
            gr.update(visible=False),
            f"📊 进度: {quiz_state.current_index + 1} / {len(quiz_state.items)}",
            gr.update(), gr.update(),
            f"🔴 本题错误: {quiz_state.current_error_count} 次",
            gr.update(),
        )


def show_summary():
    """显示听写总结"""
    total_count = len(quiz_state.results)
    correct_count = sum(1 for r in quiz_state.results if r["is_correct"])
    total_errors = sum(r.get("error_count", 0) for r in quiz_state.results)
    
    accuracy = (correct_count / total_count * 100) if total_count > 0 else 0
    
    # === 新增：完成一轮听写 ===
    session_result = game_state.complete_session()
    stats = game_state.get_stats()
    title_info = stats["title"]
    
    # 计算本次获得积分
    total_score_earned = sum(r.get("score_earned", 0) for r in quiz_state.results)
    
    summary = f"""
## 🎉 听写完成！

### 🏅 当前称号：{title_info['emoji']} {title_info['name']}
- **总积分**: {stats['score']} 分 (本次+{total_score_earned}分)
"""
    if title_info['next_title']:
        next_t = title_info['next_title']
        summary += f"- 距离 {next_t['emoji']} {next_t['name']}：还需 {next_t['score_needed']} 分\n"
    
    summary += f"""
### 📊 成绩统计
- **总题数**: {total_count} 题
- **正确数**: {correct_count} 题
- **正确率**: {accuracy:.1f}%
- **总错误次数**: {total_errors} 次
- **最高连击**: {stats['stats']['max_streak']} 连击

### 📚 学习进度
- **完成轮次**: {session_result['total_sessions']} 轮
- **达成天数**: {session_result['session_days']} 天
- **掌握单词**: {stats['mastered_words_count']} 个
- **掌握句子**: {stats['mastered_sentences_count']} 个

### 📝 详细记录
"""
    
    for i, result in enumerate(quiz_state.results, 1):
        item = result["item"]
        emoji = "✅" if result["is_correct"] else "❌"
        error_info = f" (错误{result['error_count']}次)" if result.get("error_count", 0) > 0 else ""
        summary += f"\n{i}. {emoji} {item['english']} - {item['chinese']}{error_info}"
    
    # 检查重点复习列表
    review_list = load_review_list()
    if review_list:
        summary += f"\n\n### 🔴 重点复习列表 ({len(review_list)}个)\n"
        for eng, data in list(review_list.items())[:5]:
            summary += f"\n- {eng} - {data['chinese']}"
        if len(review_list) > 5:
            summary += f"\n- ... 还有 {len(review_list) - 5} 个"
    
    quiz_state.finished = True
    
    return (
        None, summary, "", "",
        gr.update(visible=False), gr.update(visible=False),
        gr.update(visible=False), gr.update(visible=False),
        gr.update(visible=False),
        gr.update(visible=True, value=summary),
        gr.update(visible=True), "",
        gr.update(visible=False), gr.update(value="📋 显示设置"),
        "", False,
    )


def show_summary_with_sidebar():
    """显示总结并保持侧边栏状态"""
    result = show_summary()
    return result


def view_error_records():
    """查看错误记录和艾宾浩斯复习统计"""
    records = load_error_records()
    review_stats = get_review_statistics()
    
    if not records:
        return "暂无错误记录"
    
    sorted_records = sorted(
        records.items(),
        key=lambda x: x[1]["error_count"],
        reverse=True
    )
    
    output = f"## 📊 错误记录 (共 {len(records)} 个)\n\n"
    
    # ===== 艾宾浩斯复习统计 =====
    output += "---\n\n"
    output += f"### 🧠 艾宾浩斯记忆复习统计\n\n"
    output += f"**总复习词汇**: {review_stats['total']} 个  \n"
    output += f"**🔴 到期需复习**: {review_stats['due_count']} 个  \n"
    output += f"**复习原理**: 按照艾宾浩斯遗忘曲线，分别在 **1天、2天、4天、7天、15天** 后复习  \n"
    output += f"**掌握标准**: 连续答对 **{CORRECT_THRESHOLD}次** 后移除  \n\n"
    
    if review_stats['total'] > 0:
        output += "#### 📈 各阶段词汇分布\n\n"
        stage_names = ["第1阶段(1天)", "第2阶段(2天)", "第3阶段(4天)", "第4阶段(7天)", "第5阶段(15天)"]
        for i, count in enumerate(review_stats['stages']):
            if i < len(stage_names):
                output += f"- {stage_names[i]}: {count} 个\n"
        
        output += "\n#### 📊 答对进度统计\n\n"
        for consecutive, count in sorted(review_stats['consecutive_stats'].items()):
            output += f"- 连续答对 {consecutive}/{CORRECT_THRESHOLD} 次: {count} 个\n"
        
        output += "\n---\n\n"
    
    # ===== 到期复习列表（详细） =====
    output += f"### 🔴 到期需复习 ({review_stats['due_count']} 个)\n\n"
    
    due_shown = 0
    for item in review_stats['items']:
        if item['english'] in [due['english'] for due in get_due_review_items()]:
            item_type = "📝" if item["type"] == "word" else "📄"
            stage_name = ["1天", "2天", "4天", "7天", "15天"][min(item['stage'], 4)]
            output += f"- {item_type} **{item['english']}** - {item['chinese']} "
            output += f"[阶段{item['stage']+1}({stage_name}), 答对{item['consecutive']}/{CORRECT_THRESHOLD}次]\n"
            due_shown += 1
    
    if due_shown == 0:
        output += "*暂无到期需复习的词汇* ✨\n"
    
    # ===== 其他复习列表 =====
    output += f"\n### 🟡 待复习 ({review_stats['total'] - review_stats['due_count']} 个)\n\n"
    
    other_shown = 0
    for item in review_stats['items']:
        if item['english'] not in [due['english'] for due in get_due_review_items()]:
            item_type = "📝" if item["type"] == "word" else "📄"
            stage_name = ["1天", "2天", "4天", "7天", "15天"][min(item['stage'], 4)]
            output += f"- {item_type} **{item['english']}** - {item['chinese']} "
            output += f"[阶段{item['stage']+1}({stage_name}), 答对{item['consecutive']}/{CORRECT_THRESHOLD}次, 下次: {item['next_review']}]\n"
            other_shown += 1
    
    if other_shown == 0:
        output += "*暂无待复习的词汇* ✨\n"
    
    # ===== 其他错误记录（不在复习列表） =====
    output += f"\n### 📋 其他错误记录\n\n"
    
    review_list = load_review_list()
    other_errors_shown = 0
    for english, data in sorted_records:
        if english not in review_list:
            item_type = "📝" if data["type"] == "word" else "📄"
            output += f"- {item_type} **{english}** - {data['chinese']} "
            output += f"(错误 {data['error_count']} 次, 最后错误: {data.get('last_error', '未知')})\n"
            other_errors_shown += 1
    
    if other_errors_shown == 0:
        output += "*所有错误词汇都已加入复习计划* 🎉\n"
    
    return output


def clear_error_records():
    """清除所有记录"""
    save_error_records({})
    save_review_list({})
    return "✅ 已清除所有错误记录和重点复习列表"


# 自定义CSS
custom_css = """
/* 震动动画 */
@keyframes shake {
    0%, 100% { transform: translateX(0); }
    10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
    20%, 40%, 60%, 80% { transform: translateX(5px); }
}

.shake-animation {
    animation: shake 0.5s;
}

/* 结果卡片样式 */
.result-card {
    padding: 15px;
    border-radius: 8px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    margin: 10px 0;
}

/* 按钮悬停效果增强 */
button:hover {
    transform: translateY(-1px);
    transition: all 0.2s ease;
}

/* 输入框样式加强 */
#answer-input textarea {
    font-size: 1.3em !important;
    font-weight: 500 !important;
    padding: 20px !important;
    border: 3px solid #4CAF50 !important;
    border-radius: 10px !important;
    background-color: #f9fff9 !important;
    min-height: 80px !important;
}

#answer-input textarea:focus {
    border-color: #2196F3 !important;
    box-shadow: 0 0 10px rgba(33, 150, 243, 0.4) !important;
}

/* 公布答案按钮样式 - 灰色低调 */
#show-answer-btn {
    background-color: #9e9e9e !important;
    color: white !important;
    opacity: 0.6 !important;
    font-size: 0.9em !important;
}

#show-answer-btn:hover {
    opacity: 0.85 !important;
    background-color: #757575 !important;
}

/* 提示和答案显示区域 */
#hint-text, #answer-text {
    font-size: 1.1em;
    padding: 10px;
    border-left: 4px solid #2196F3;
    background-color: #e3f2fd;
    border-radius: 4px;
    margin: 10px 0;
}
"""

# 创建 Gradio 界面
with gr.Blocks(title="英语听写练习") as app:
    gr.Markdown("""
    # � 欢迎Timmy来到 英语冒险世界
    """)
    
    with gr.Tabs():
        # 听写练习标签
        with gr.TabItem("📝 听写练习"):
            with gr.Row():
                # 左侧：成就卡片 + 设置区域（可收起）
                with gr.Column(scale=3, visible=True) as sidebar:
                    # === 首页成就统计卡片 ===
                    stats = game_state.get_stats()
                    title_info = stats["title"]
                    
                    # 计算进度条
                    progress_percent = title_info.get('progress', 0)
                    next_title_info = title_info.get('next_title')
                    
                    # 构建进度条
                    if next_title_info:
                        filled_blocks = int(progress_percent / 10)  # 10个方块代表100%
                        empty_blocks = 10 - filled_blocks
                        progress_bar = "🟩" * filled_blocks + "⬜" * empty_blocks
                        next_info = f"**下一称号**: {next_title_info['emoji']} {next_title_info['name']} (还需 {next_title_info['score_needed']} 分)"
                    else:
                        progress_bar = "🟩" * 10
                        next_info = "**已达最高称号！** 🎉"
                    
                    gr.Markdown(f"""
### 🎖️ 当前成就

**称号**: {title_info['emoji']} {title_info['name']}  
**当前积分**: {stats['score']} 分

{next_info}  
{progress_bar} {int(progress_percent)}%

📅 **累计听写**: {stats['session_days']} 天  
📝 **单词掌握**: {stats['mastered_words_count']} 个  
📄 **句子掌握**: {stats['mastered_sentences_count']} 个

---

### ⚙️ 听写设置
""")
                    
                    grade_select = gr.CheckboxGroup(
                        choices=get_all_grades(),
                        value=get_all_grades(),
                        label="📚 选择词库（可多选）"
                    )
                    
                    # 动态显示词库统计
                    def update_wordbank_stats(selected_grades):
                        """更新词库统计信息"""
                        if not selected_grades:
                            return "⚠️ 请选择至少一个词库"
                        
                        all_items = get_items_by_grades(selected_grades)
                        word_count = sum(1 for item in all_items if item["type"] == "word")
                        sentence_count = sum(1 for item in all_items if item["type"] == "sentence")
                        total_count = len(all_items)
                        
                        stats_text = f"""
**📊 当前词库统计**  
📝 单词: **{word_count}** 个 | 📄 句子: **{sentence_count}** 个 | 📚 总计: **{total_count}** 个
"""
                        return stats_text
                    
                    # 显示初始统计
                    initial_stats = update_wordbank_stats(get_all_grades())
                    wordbank_stats = gr.Markdown(initial_stats)
                    
                    # 更新统计
                    grade_select.change(
                        update_wordbank_stats,
                        inputs=[grade_select],
                        outputs=[wordbank_stats]
                    )
                    
                    difficulty_select = gr.Radio(
                        choices=list(DIFFICULTY_LEVELS.keys()),
                        value="进阶",
                        label="📊 难度等级"
                    )
                    
                    difficulty_info = gr.Markdown("*70%单词 + 30%句子*")
                    
                    def update_difficulty_info(diff):
                        return f"*{DIFFICULTY_LEVELS[diff]['description']}*"
                    
                    difficulty_select.change(
                        update_difficulty_info,
                        inputs=[difficulty_select],
                        outputs=[difficulty_info]
                    )
                    
                    count_slider = gr.Slider(
                        minimum=5,
                        maximum=30,
                        value=10,
                        step=1,
                        label="📋 听写数量"
                    )
                    
                    gr.Markdown("### 🎤 语音设置")
                    
                    voice_select = gr.Dropdown(
                        choices=VOICES,
                        value="Rosie",
                        label="选择声音"
                    )
                    
                    speed_slider = gr.Slider(
                        minimum=0.5,
                        maximum=1.2,
                        value=1.0,
                        step=0.1,
                        label="语速 (慢 ← → 快)"
                    )
                    
                    start_btn = gr.Button("🚀 开始听写", variant="primary", size="lg")
                
                # 右侧：听写区域
                with gr.Column(scale=4):
                    with gr.Row():
                        toggle_sidebar_btn = gr.Button("📋 隐藏设置", visible=True, size="sm", scale=0, min_width=120)
                        gr.Markdown("### 🎧 听写区域")
                    
                    progress_text = gr.Markdown("")
                    status_text = gr.Markdown("点击「开始听写」按钮开始练习")
                    audio_player = gr.Audio(label="🔊 听音频", type="filepath", autoplay=True)
                    
                    # 提示和答案显示区域 - 放在输入框上方
                    hint_text = gr.Markdown("", elem_id="hint-text")
                    answer_text = gr.Markdown("", elem_id="answer-text")
                    error_count_display = gr.Markdown("")
                    
                    answer_input = gr.Textbox(
                        label="✏️ 输入你的答案",
                        placeholder="听完音频后在这里输入，按回车提交...",
                        visible=False,
                        lines=3,
                        elem_id="answer-input"
                    )
                    
                    with gr.Row():
                        submit_btn = gr.Button("✅ 提交答案", variant="primary", visible=False, scale=2)
                        hint_btn = gr.Button("💡 显示提示", variant="secondary", visible=False, scale=1)
                        show_answer_btn = gr.Button("📕 公布答案", visible=False, scale=1, elem_id="show-answer-btn")
                    
                    next_btn = gr.Button("下一题 ➡️", variant="secondary", visible=False)
                    result_display = gr.Markdown("", visible=False)
            
            sidebar_visible = gr.State(True)
            
            def toggle_sidebar(is_visible):
                new_state = not is_visible
                btn_text = "📋 显示设置" if not new_state else "📋 隐藏设置"
                return gr.update(visible=new_state), new_state, gr.update(value=btn_text)
            
            toggle_sidebar_btn.click(
                toggle_sidebar,
                inputs=[sidebar_visible],
                outputs=[sidebar, sidebar_visible, toggle_sidebar_btn]
            )
            
            outputs = [
                audio_player, status_text, hint_text, answer_text, hint_btn, 
                show_answer_btn, answer_input, submit_btn, next_btn, result_display,
                start_btn, progress_text, sidebar, toggle_sidebar_btn,
                error_count_display, sidebar_visible
            ]
            
            start_btn.click(
                start_quiz,
                inputs=[grade_select, difficulty_select, count_slider, voice_select, speed_slider],
                outputs=outputs
            )
            
            hint_btn.click(show_hint, outputs=[hint_text])
            show_answer_btn.click(show_answer_with_confirmation, outputs=[answer_text, show_answer_btn])
            
            submit_btn.click(
                submit_answer,
                inputs=[answer_input, voice_select, speed_slider],
                outputs=outputs
            )
            
            answer_input.submit(
                submit_answer,
                inputs=[answer_input, voice_select, speed_slider],
                outputs=outputs
            )
        
        # 错误记录标签
        with gr.TabItem("📋 错误记录 & 艾宾浩斯复习"):
            gr.Markdown("### 📊 查看错误记录和复习进度")
            gr.Markdown("🧠 **艾宾浩斯记忆曲线**：科学复习，隔一段时间自动复习错误词汇，连续答对2次即可掌握！")
            
            view_btn = gr.Button("🔍 查看记录", variant="primary")
            clear_btn = gr.Button("🗑️ 清除所有记录", variant="secondary")
            
            error_display = gr.Markdown("")
            
            view_btn.click(view_error_records, outputs=[error_display])
            clear_btn.click(clear_error_records, outputs=[error_display])
            
            gr.Markdown("---")
            gr.Markdown("### ⚠️ 数据重置")
            gr.Markdown("**注意**：此操作会清除所有数据，包括积分、称号、掌握的单词、错误记录等。旧数据会自动备份。")
            
            with gr.Row():
                reset_all_btn = gr.Button("🔄 重置所有数据（归零）", variant="stop")
            
            reset_result = gr.Markdown("")
            
            def reset_all_data_handler():
                """重置所有数据"""
                # 清除游戏状态
                result = game_state.reset_all_data()
                
                # 清除错误记录和复习列表
                save_error_records({})
                save_review_list({})
                
                return f"""
### ✅ 重置成功！

所有数据已清零：
- ✅ 积分和称号已重置
- ✅ 掌握的单词和句子已清空
- ✅ 错误记录和复习列表已清空
- ✅ 连击和统计数据已重置

🗂️ 旧数据已自动备份到项目文件夹

**刷新页面后生效** 🔄
"""
            
            reset_all_btn.click(reset_all_data_handler, outputs=[reset_result])
        
        # === 新增：成就统计标签 ===
        with gr.TabItem("📊 成就统计"):
            gr.Markdown("### 📈 Timmy英语听写 - 成就统计")
            gr.Markdown("*查看你的听写成就、积分、称号和掌握的词汇！*")
            
            stats_display = gr.Markdown(game_state.get_achievement_stats_display())
            refresh_stats_btn = gr.Button("🔄 刷新统计", variant="primary")
            
            refresh_stats_btn.click(
                lambda: game_state.get_achievement_stats_display(),
                outputs=[stats_display]
            )
    
    gr.Markdown("""
    ---
    
    ### 💡 快速指南
    
    **积分规则**：单词10分，句子20分（无提示答对才有积分）  
    **连击加分**：连击越多,奖励越高！🔥  
    **称号晋升**：每1000分晋升一级  
    
    **🧠 艾宾浩斯记忆复习**：  
    - 答错的词会自动加入复习计划  
    - 按科学记忆曲线在 1天、2天、4天、7天、15天 后复习  
    - 每次答对进入下一阶段，连续答对 **2次** 即可掌握！  
    - 系统会优先安排到期需要复习的词汇  
    
    ---
    *Powered by KittenTTS*
    """)


if __name__ == "__main__":
    app.launch(share=False, server_name="0.0.0.0", server_port=7860, css=custom_css)
