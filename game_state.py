"""
Minecraft 风格游戏化系统 - 游戏状态管理
探险家模式：低门槛 + 高频奖励 + 避免挫败感
新增：成就统计、积分体系、称号系统
"""

import json
import os
import random
from datetime import datetime, date
from typing import Dict, List, Optional

# 游戏存档文件路径
GAME_SAVE_FILE = "game_save.json"

# ============== 方块定义 ==============
BLOCKS = {
    # 基础方块（答对单词获得）
    "dirt": {"name": "泥土", "emoji": "🟫", "rarity": "common", "value": 1},
    "cobblestone": {"name": "圆石", "emoji": "⬜", "rarity": "common", "value": 1},
    "oak_wood": {"name": "橡木", "emoji": "🪵", "rarity": "common", "value": 1},
    "sand": {"name": "沙子", "emoji": "🟨", "rarity": "common", "value": 1},
    
    # 中级方块（答对句子获得）
    "iron_block": {"name": "铁块", "emoji": "🔲", "rarity": "uncommon", "value": 3},
    "gold_block": {"name": "金块", "emoji": "🟡", "rarity": "uncommon", "value": 5},
    "lapis_block": {"name": "青金石块", "emoji": "🔵", "rarity": "uncommon", "value": 3},
    
    # 稀有方块（连击获得）
    "diamond": {"name": "钻石", "emoji": "💎", "rarity": "rare", "value": 10},
    "emerald": {"name": "绿宝石", "emoji": "💚", "rarity": "rare", "value": 10},
    
    # 特殊方块（驯服怪物获得）
    "redstone": {"name": "红石", "emoji": "🔴", "rarity": "special", "value": 5},
    "obsidian": {"name": "黑曜石", "emoji": "⬛", "rarity": "special", "value": 8},
}

# ============== 怪物定义 ==============
MONSTERS = {
    "zombie": {"name": "僵尸", "emoji": "🧟", "description": "夜晚出没的不死生物"},
    "skeleton": {"name": "骷髅", "emoji": "💀", "description": "会射箭的骷髅弓箭手"},
    "creeper": {"name": "苦力怕", "emoji": "💚", "description": "会爆炸的绿色生物"},
    "spider": {"name": "蜘蛛", "emoji": "🕷️", "description": "八条腿的攀爬者"},
    "enderman": {"name": "末影人", "emoji": "👾", "description": "神秘的传送生物"},
    "slime": {"name": "史莱姆", "emoji": "🟢", "description": "弹跳的果冻怪"},
    "witch": {"name": "女巫", "emoji": "🧙‍♀️", "description": "会扔药水的巫师"},
    "phantom": {"name": "幻翼", "emoji": "🦇", "description": "夜空中的幽灵"},
}

# ============== 建筑定义 ==============
BUILDINGS = {
    "campfire": {"name": "营火", "emoji": "🔥", "blocks_needed": 5, "description": "冒险的起点"},
    "wooden_hut": {"name": "小木屋", "emoji": "🏠", "blocks_needed": 15, "description": "遮风挡雨的小窝"},
    "stone_house": {"name": "石头屋", "emoji": "🏡", "blocks_needed": 30, "description": "坚固的石头房子"},
    "farm": {"name": "农场", "emoji": "🌾", "blocks_needed": 50, "description": "自给自足的农庄"},
    "tower": {"name": "瞭望塔", "emoji": "🗼", "blocks_needed": 75, "description": "可以看到远方"},
    "castle": {"name": "城堡", "emoji": "🏰", "blocks_needed": 100, "description": "宏伟的城堡"},
    "diamond_palace": {"name": "钻石宫殿", "emoji": "💎", "blocks_needed": 150, "description": "闪闪发光的钻石宫"},
    "nether_portal": {"name": "下界传送门", "emoji": "🔮", "blocks_needed": 200, "description": "通往下界的神秘门"},
    "end_portal": {"name": "末地传送门", "emoji": "🌀", "blocks_needed": 300, "description": "通往末地的终极门"},
}

# ============== 成就定义 ==============
ACHIEVEMENTS = {
    "first_block": {"name": "第一块方块", "emoji": "🎉", "description": "收集到第一个方块", "condition": "blocks >= 1"},
    "monster_hunter": {"name": "怪物猎人", "emoji": "⚔️", "description": "驯服第一只怪物", "condition": "tamed >= 1"},
    "streak_3": {"name": "连击新手", "emoji": "🔥", "description": "连续答对3题", "condition": "max_streak >= 3"},
    "streak_5": {"name": "连击达人", "emoji": "🔥🔥", "description": "连续答对5题", "condition": "max_streak >= 5"},
    "streak_10": {"name": "连击大师", "emoji": "🔥🔥🔥", "description": "连续答对10题", "condition": "max_streak >= 10"},
    "builder": {"name": "建造者", "emoji": "🏗️", "description": "解锁第一个建筑", "condition": "buildings >= 1"},
    "architect": {"name": "建筑师", "emoji": "🏛️", "description": "解锁5个建筑", "condition": "buildings >= 5"},
    "diamond_finder": {"name": "钻石猎人", "emoji": "💎", "description": "收集到第一颗钻石", "condition": "diamonds >= 1"},
    "daily_3": {"name": "坚持三天", "emoji": "📅", "description": "连续登录3天", "condition": "login_streak >= 3"},
    "daily_7": {"name": "一周达人", "emoji": "🗓️", "description": "连续登录7天", "condition": "login_streak >= 7"},
    "collector_50": {"name": "收藏家", "emoji": "📦", "description": "收集50个方块", "condition": "total_blocks >= 50"},
    "collector_100": {"name": "大收藏家", "emoji": "🗃️", "description": "收集100个方块", "condition": "total_blocks >= 100"},
    "all_monsters": {"name": "怪物大师", "emoji": "👹", "description": "驯服所有种类怪物", "condition": "unique_monsters >= 8"},
    # 新增成就
    "first_session": {"name": "初次听写", "emoji": "📝", "description": "完成第一次听写", "condition": "sessions >= 1"},
    "master_10_words": {"name": "词汇新手", "emoji": "📖", "description": "掌握10个单词", "condition": "mastered_words >= 10"},
    "master_50_words": {"name": "词汇达人", "emoji": "📚", "description": "掌握50个单词", "condition": "mastered_words >= 50"},
    "master_100_words": {"name": "词汇大师", "emoji": "🎓", "description": "掌握100个单词", "condition": "mastered_words >= 100"},
    "score_1000": {"name": "千分之旅", "emoji": "🌟", "description": "获得1000积分", "condition": "score >= 1000"},
    "score_5000": {"name": "五千之路", "emoji": "⭐", "description": "获得5000积分", "condition": "score >= 5000"},
    "perfect_streak": {"name": "完美连击", "emoji": "💯", "description": "无提示连对20题", "condition": "perfect_streak >= 20"},
}

# ============== 每日惊喜 ==============
DAILY_REWARDS = [
    {"name": "幸运宝箱", "emoji": "🎁", "blocks": {"diamond": 1}},
    {"name": "木材大礼包", "emoji": "📦", "blocks": {"oak_wood": 5}},
    {"name": "矿石袋", "emoji": "💰", "blocks": {"iron_block": 2, "gold_block": 1}},
    {"name": "稀有宝石", "emoji": "💎", "blocks": {"emerald": 1}},
    {"name": "红石能量", "emoji": "🔴", "blocks": {"redstone": 3}},
]

# ============== Minecraft 称号系统 ==============
# 积分等级体系：初始500积分升级，之后每次升级增加200积分
# 1级→2级: 500, 2级→3级: 700, 3级→4级: 900, 以此类推
TITLES = [
    {"name": "新手冒险家", "emoji": "🌱", "min_score": 0},      # 1级起点
    {"name": "石器工匠", "emoji": "⛏️", "min_score": 500},      # 需要500积分
    {"name": "铁甲战士", "emoji": "⚔️", "min_score": 1200},     # 需要700积分(500+700)
    {"name": "金牌猎人", "emoji": "🏅", "min_score": 2100},     # 需要900积分(1200+900)
    {"name": "钻石骑士", "emoji": "💎", "min_score": 3100},     # 需要1000积分(2100+1000)
    {"name": "绿宝石商人", "emoji": "💚", "min_score": 4200},   # 需要1100积分(3100+1100)
    {"name": "红石工程师", "emoji": "🔴", "min_score": 5400},   # 需要1200积分(4200+1200)
    {"name": "下界探索者", "emoji": "🔥", "min_score": 6700},   # 需要1300积分(5400+1300)
    {"name": "末影龙骑士", "emoji": "🐉", "min_score": 8100},   # 需要1400积分(6700+1400)
    {"name": "创世神", "emoji": "👑", "min_score": 9600},       # 需要1500积分(8100+1500)
]


class GameState:
    """游戏状态管理器"""
    
    def __init__(self):
        self.data = self._load_or_create()
    
    def _load_or_create(self) -> Dict:
        """加载或创建游戏存档"""
        if os.path.exists(GAME_SAVE_FILE):
            try:
                with open(GAME_SAVE_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # 确保所有必要字段存在
                    return self._migrate_data(data)
            except:
                pass
        return self._create_new_save()
    
    def _create_new_save(self) -> Dict:
        """创建新存档"""
        return {
            "player_name": "探险家",
            "created_at": datetime.now().isoformat(),
            
            # 方块背包
            "blocks": {},
            "total_blocks": 0,
            
            # 怪物图鉴
            "monster_book": {},  # {monster_type: {"discovered": True, "tamed": False, "word": "xxx"}}
            "monsters_discovered": 0,
            "monsters_tamed": 0,
            
            # 建筑进度
            "buildings_unlocked": [],
            
            # 成就
            "achievements": [],
            
            # 统计数据
            "stats": {
                "total_correct": 0,
                "total_wrong": 0,
                "current_streak": 0,
                "max_streak": 0,
                "diamonds_collected": 0,
                "sessions_completed": 0,
            },
            
            # 登录记录
            "last_login": None,
            "login_streak": 0,
            "daily_reward_claimed": None,
            
            # 等级系统
            "level": 1,
            "exp": 0,
            
            # ========== 新增：成就统计系统 ==========
            # 积分系统
            "score": 0,
            "score_history": [],  # 积分历史记录
            
            # 听写轮次统计
            "total_sessions": 0,  # 总完成轮次
            "session_dates": [],  # 完成听写的日期列表
            
            # 词汇掌握统计
            "mastered_words": set(),  # 掌握的单词（无提示答对）
            "mastered_sentences": set(),  # 掌握的句子（无提示答对）
            
            # 连对统计
            "perfect_streak_count": 0,  # 无提示连对次数
            "max_perfect_streak": 0,  # 最大无提示连对
        }
    
    def _migrate_data(self, data: Dict) -> Dict:
        """迁移旧版本数据"""
        default = self._create_new_save()
        for key in default:
            if key not in data:
                data[key] = default[key]
        
        # 确保 mastered_words 和 mastered_sentences 是 set 类型
        if isinstance(data.get("mastered_words"), list):
            data["mastered_words"] = set(data["mastered_words"])
        elif not isinstance(data.get("mastered_words"), set):
            data["mastered_words"] = set()
        
        if isinstance(data.get("mastered_sentences"), list):
            data["mastered_sentences"] = set(data["mastered_sentences"])
        elif not isinstance(data.get("mastered_sentences"), set):
            data["mastered_sentences"] = set()
        
        return data
    
    def save(self):
        """保存游戏"""
        # 将 set 转换为 list 以便 JSON 序列化
        save_data = self.data.copy()
        save_data["mastered_words"] = list(self.data["mastered_words"])
        save_data["mastered_sentences"] = list(self.data["mastered_sentences"])
        
        with open(GAME_SAVE_FILE, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, ensure_ascii=False, indent=2)
    
    def reset_all_data(self):
        """重置所有游戏数据（包括积分、听写、掌握的词汇等）"""
        # 创建备份
        if os.path.exists(GAME_SAVE_FILE):
            backup_file = f"game_save_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            try:
                import shutil
                shutil.copy2(GAME_SAVE_FILE, backup_file)
            except:
                pass
        
        # 重置为新存档
        self.data = self._create_new_save()
        self.save()
        return {"success": True, "message": "所有数据已重置，旧数据已备份"}
    
    # ============== 方块系统 ==============
    
    def add_block(self, block_type: str, count: int = 1) -> Dict:
        """添加方块到背包"""
        if block_type not in BLOCKS:
            return {"success": False, "message": "未知方块类型"}
        
        if block_type not in self.data["blocks"]:
            self.data["blocks"][block_type] = 0
        
        self.data["blocks"][block_type] += count
        self.data["total_blocks"] += count
        
        block_info = BLOCKS[block_type]
        
        # 检查钻石成就
        if block_type == "diamond":
            self.data["stats"]["diamonds_collected"] += count
        
        self.save()
        self._check_achievements()
        
        return {
            "success": True,
            "block": block_info,
            "count": count,
            "total": self.data["blocks"][block_type]
        }
    
    def get_random_common_block(self) -> str:
        """获取随机普通方块"""
        common_blocks = [k for k, v in BLOCKS.items() if v["rarity"] == "common"]
        return random.choice(common_blocks)
    
    def get_random_uncommon_block(self) -> str:
        """获取随机中级方块"""
        uncommon_blocks = [k for k, v in BLOCKS.items() if v["rarity"] == "uncommon"]
        return random.choice(uncommon_blocks)
    
    def reward_for_correct_answer(self, is_sentence: bool, streak: int, no_hint: bool) -> List[Dict]:
        """根据答对情况给予奖励"""
        rewards = []
        
        # 基础奖励
        if is_sentence:
            block = self.get_random_uncommon_block()
            count = 1
        else:
            block = self.get_random_common_block()
            count = 1
        
        # 无提示奖励
        if no_hint:
            count *= 2
        
        # 连击奖励
        if streak >= 10:
            rewards.append(self.add_block("diamond", 1))
            rewards.append(self.add_block("emerald", 1))
        elif streak >= 5:
            rewards.append(self.add_block("diamond", 1))
        elif streak >= 3:
            rewards.append(self.add_block("gold_block", 1))
        
        # 基础方块奖励
        rewards.append(self.add_block(block, count))
        
        return rewards
    
    # ============== 怪物系统 ==============
    
    def discover_monster(self, english_word: str, chinese: str) -> Dict:
        """发现新怪物（答错时触发）"""
        # 根据单词hash选择怪物类型
        monster_types = list(MONSTERS.keys())
        monster_type = monster_types[hash(english_word) % len(monster_types)]
        
        monster_info = MONSTERS[monster_type]
        
        if english_word not in self.data["monster_book"]:
            self.data["monster_book"][english_word] = {
                "monster_type": monster_type,
                "chinese": chinese,
                "discovered": True,
                "tamed": False,
                "discover_time": datetime.now().isoformat(),
                "error_count": 1
            }
            self.data["monsters_discovered"] += 1
            is_new = True
        else:
            self.data["monster_book"][english_word]["error_count"] += 1
            is_new = False
        
        self.save()
        
        return {
            "monster_type": monster_type,
            "monster_info": monster_info,
            "is_new": is_new,
            "word": english_word,
            "chinese": chinese
        }
    
    def tame_monster(self, english_word: str) -> Optional[Dict]:
        """驯服怪物（之前答错的单词这次答对了）"""
        if english_word not in self.data["monster_book"]:
            return None
        
        monster_data = self.data["monster_book"][english_word]
        if monster_data["tamed"]:
            return None  # 已经驯服过了
        
        monster_data["tamed"] = True
        monster_data["tame_time"] = datetime.now().isoformat()
        self.data["monsters_tamed"] += 1
        
        # 驯服怪物获得特殊方块奖励
        self.add_block("redstone", 2)
        self.add_block("obsidian", 1)
        
        self.save()
        self._check_achievements()
        
        monster_info = MONSTERS[monster_data["monster_type"]]
        return {
            "success": True,
            "monster_type": monster_data["monster_type"],
            "monster_info": monster_info,
            "word": english_word
        }
    
    def get_untamed_monsters(self) -> List[Dict]:
        """获取未驯服的怪物列表"""
        untamed = []
        for word, data in self.data["monster_book"].items():
            if not data["tamed"]:
                monster_info = MONSTERS[data["monster_type"]]
                untamed.append({
                    "word": word,
                    "chinese": data["chinese"],
                    "monster_type": data["monster_type"],
                    "monster_info": monster_info,
                    "error_count": data["error_count"]
                })
        return sorted(untamed, key=lambda x: x["error_count"], reverse=True)
    
    def is_monster(self, english_word: str) -> bool:
        """检查某个单词是否是怪物（之前答错过）"""
        return english_word in self.data["monster_book"]
    
    # ============== 建筑系统 ==============
    
    def check_building_unlock(self) -> Optional[Dict]:
        """检查是否解锁新建筑"""
        total = self.data["total_blocks"]
        
        for building_id, building in BUILDINGS.items():
            if building_id not in self.data["buildings_unlocked"]:
                if total >= building["blocks_needed"]:
                    self.data["buildings_unlocked"].append(building_id)
                    self.save()
                    self._check_achievements()
                    return {
                        "building_id": building_id,
                        "building": building
                    }
        return None
    
    def get_building_progress(self) -> Dict:
        """获取建筑进度"""
        total = self.data["total_blocks"]
        unlocked = self.data["buildings_unlocked"]
        
        # 找到下一个要解锁的建筑
        next_building = None
        for building_id, building in BUILDINGS.items():
            if building_id not in unlocked:
                next_building = {
                    "building_id": building_id,
                    "building": building,
                    "progress": total / building["blocks_needed"] * 100,
                    "blocks_needed": building["blocks_needed"] - total
                }
                break
        
        return {
            "total_blocks": total,
            "unlocked": [(bid, BUILDINGS[bid]) for bid in unlocked],
            "next_building": next_building
        }
    
    # ============== 连击系统 ==============
    
    def update_streak(self, is_correct: bool) -> Dict:
        """更新连击"""
        if is_correct:
            self.data["stats"]["current_streak"] += 1
            self.data["stats"]["total_correct"] += 1
            if self.data["stats"]["current_streak"] > self.data["stats"]["max_streak"]:
                self.data["stats"]["max_streak"] = self.data["stats"]["current_streak"]
        else:
            self.data["stats"]["current_streak"] = 0
            self.data["stats"]["total_wrong"] += 1
        
        self.save()
        self._check_achievements()
        
        return {
            "current_streak": self.data["stats"]["current_streak"],
            "max_streak": self.data["stats"]["max_streak"]
        }
    
    # ============== 每日奖励 ==============
    
    def check_daily_login(self) -> Dict:
        """检查每日登录"""
        today = date.today().isoformat()
        last_login = self.data["last_login"]
        
        result = {
            "is_new_day": False,
            "login_streak": self.data["login_streak"],
            "daily_reward": None
        }
        
        if last_login != today:
            result["is_new_day"] = True
            
            # 检查是否连续登录
            if last_login:
                last_date = date.fromisoformat(last_login)
                today_date = date.today()
                diff = (today_date - last_date).days
                
                if diff == 1:
                    self.data["login_streak"] += 1
                elif diff > 1:
                    self.data["login_streak"] = 1
            else:
                self.data["login_streak"] = 1
            
            self.data["last_login"] = today
            result["login_streak"] = self.data["login_streak"]
            
            # 检查是否领取过今日奖励
            if self.data["daily_reward_claimed"] != today:
                reward = random.choice(DAILY_REWARDS)
                for block_type, count in reward["blocks"].items():
                    self.add_block(block_type, count)
                self.data["daily_reward_claimed"] = today
                result["daily_reward"] = reward
            
            self.save()
            self._check_achievements()
        
        return result
    
    # ============== 成就系统 ==============
    
    def _check_achievements(self):
        """检查并解锁成就"""
        new_achievements = []
        
        stats = self.data["stats"]
        
        for ach_id, ach in ACHIEVEMENTS.items():
            if ach_id in self.data["achievements"]:
                continue
            
            unlocked = False
            
            if ach_id == "first_block" and self.data["total_blocks"] >= 1:
                unlocked = True
            elif ach_id == "monster_hunter" and self.data["monsters_tamed"] >= 1:
                unlocked = True
            elif ach_id == "streak_3" and stats["max_streak"] >= 3:
                unlocked = True
            elif ach_id == "streak_5" and stats["max_streak"] >= 5:
                unlocked = True
            elif ach_id == "streak_10" and stats["max_streak"] >= 10:
                unlocked = True
            elif ach_id == "builder" and len(self.data["buildings_unlocked"]) >= 1:
                unlocked = True
            elif ach_id == "architect" and len(self.data["buildings_unlocked"]) >= 5:
                unlocked = True
            elif ach_id == "diamond_finder" and stats["diamonds_collected"] >= 1:
                unlocked = True
            elif ach_id == "daily_3" and self.data["login_streak"] >= 3:
                unlocked = True
            elif ach_id == "daily_7" and self.data["login_streak"] >= 7:
                unlocked = True
            elif ach_id == "collector_50" and self.data["total_blocks"] >= 50:
                unlocked = True
            elif ach_id == "collector_100" and self.data["total_blocks"] >= 100:
                unlocked = True
            elif ach_id == "all_monsters":
                unique_types = set(m["monster_type"] for m in self.data["monster_book"].values() if m["tamed"])
                if len(unique_types) >= len(MONSTERS):
                    unlocked = True
            # 新增成就检查
            elif ach_id == "first_session" and self.data["total_sessions"] >= 1:
                unlocked = True
            elif ach_id == "master_10_words" and len(self.data["mastered_words"]) >= 10:
                unlocked = True
            elif ach_id == "master_50_words" and len(self.data["mastered_words"]) >= 50:
                unlocked = True
            elif ach_id == "master_100_words" and len(self.data["mastered_words"]) >= 100:
                unlocked = True
            elif ach_id == "score_1000" and self.data["score"] >= 1000:
                unlocked = True
            elif ach_id == "score_5000" and self.data["score"] >= 5000:
                unlocked = True
            elif ach_id == "perfect_streak" and self.data["max_perfect_streak"] >= 20:
                unlocked = True
            
            if unlocked:
                self.data["achievements"].append(ach_id)
                new_achievements.append(ach)
        
        if new_achievements:
            self.save()
        
        return new_achievements
    
    def get_achievements(self) -> Dict:
        """获取成就列表"""
        unlocked = []
        locked = []
        
        for ach_id, ach in ACHIEVEMENTS.items():
            ach_data = {"id": ach_id, **ach}
            if ach_id in self.data["achievements"]:
                unlocked.append(ach_data)
            else:
                locked.append(ach_data)
        
        return {
            "unlocked": unlocked,
            "locked": locked,
            "total": len(ACHIEVEMENTS),
            "progress": len(unlocked) / len(ACHIEVEMENTS) * 100
        }
    
    # ============== 等级系统 ==============
    
    def add_exp(self, amount: int) -> Dict:
        """添加经验值"""
        self.data["exp"] += amount
        
        # 升级检查（每100经验升一级）
        exp_per_level = 100
        new_level = (self.data["exp"] // exp_per_level) + 1
        level_up = new_level > self.data["level"]
        
        if level_up:
            self.data["level"] = new_level
        
        self.save()
        
        return {
            "exp": self.data["exp"],
            "level": self.data["level"],
            "level_up": level_up,
            "exp_to_next": exp_per_level - (self.data["exp"] % exp_per_level)
        }
    
    # ============== 新增：积分和称号系统 ==============
    
    def add_score(self, base_score: int, streak: int = 0, no_hint: bool = True) -> Dict:
        """
        添加积分
        
        Args:
            base_score: 基础分数（单词10分，句子20分）
            streak: 当前连击数
            no_hint: 是否没有使用提示
        
        Returns:
            积分变化信息
        """
        old_score = self.data["score"]
        old_title = self.get_current_title()
        
        # 基础分数
        score_to_add = base_score
        
        # 无提示答对，分数不变
        # 使用提示答对，不加分
        if not no_hint:
            score_to_add = 0
        
        # 连击加分
        if no_hint and streak >= 3:
            if streak >= 10:
                bonus = base_score * 2  # 10连击：额外200%
            elif streak >= 7:
                bonus = base_score * 1.5  # 7连击：额外150%
            elif streak >= 5:
                bonus = base_score * 1  # 5连击：额外100%
            elif streak >= 3:
                bonus = base_score * 0.5  # 3连击：额外50%
            else:
                bonus = 0
            score_to_add += int(bonus)
        
        self.data["score"] += score_to_add
        
        # 记录积分历史
        self.data["score_history"].append({
            "timestamp": datetime.now().isoformat(),
            "score_added": score_to_add,
            "total_score": self.data["score"],
            "reason": f"streak_{streak}" if streak >= 3 else "base"
        })
        
        new_title = self.get_current_title()
        title_up = new_title["name"] != old_title["name"]
        
        self.save()
        self._check_achievements()
        
        return {
            "score_added": score_to_add,
            "total_score": self.data["score"],
            "old_title": old_title,
            "new_title": new_title,
            "title_up": title_up
        }
    
    def get_current_title(self) -> Dict:
        """获取当前称号"""
        score = self.data["score"]
        
        # 从高到低查找匹配的称号
        current_title = TITLES[0]  # 默认最低称号
        for title in TITLES:
            if score >= title["min_score"]:
                current_title = title
            else:
                break
        
        # 计算到下一称号的进度
        current_index = TITLES.index(current_title)
        if current_index < len(TITLES) - 1:
            next_title = TITLES[current_index + 1]
            progress = (score - current_title["min_score"]) / (next_title["min_score"] - current_title["min_score"]) * 100
            next_title_info = {
                "name": next_title["name"],
                "emoji": next_title["emoji"],
                "score_needed": next_title["min_score"] - score
            }
        else:
            progress = 100
            next_title_info = None
        
        return {
            "name": current_title["name"],
            "emoji": current_title["emoji"],
            "min_score": current_title["min_score"],
            "progress": min(progress, 100),
            "next_title": next_title_info
        }
    
    # ============== 新增：听写轮次统计 ==============
    
    def complete_session(self) -> Dict:
        """完成一轮听写"""
        today = date.today().isoformat()
        
        self.data["total_sessions"] += 1
        self.data["stats"]["sessions_completed"] += 1
        
        # 记录今天完成了听写
        if today not in self.data["session_dates"]:
            self.data["session_dates"].append(today)
        
        self.save()
        self._check_achievements()
        
        return {
            "total_sessions": self.data["total_sessions"],
            "session_days": len(self.data["session_dates"])
        }
    
    # ============== 新增：词汇掌握统计 ==============
    
    def is_mastered(self, english: str, is_sentence: bool) -> bool:
        """
        检查某个词汇是否已经掌握
        
        Args:
            english: 英文内容
            is_sentence: 是否是句子
        
        Returns:
            是否已掌握
        """
        if is_sentence:
            return english in self.data["mastered_sentences"]
        else:
            return english in self.data["mastered_words"]
    
    def mark_as_mastered(self, english: str, is_sentence: bool, no_hint: bool) -> Dict:
        """
        标记词汇为已掌握
        
        Args:
            english: 英文内容
            is_sentence: 是否是句子
            no_hint: 是否没有使用提示（只有无提示答对才算掌握）
        
        Returns:
            掌握情况
        """
        if not no_hint:
            return {
                "newly_mastered": False,
                "total_mastered_words": len(self.data["mastered_words"]),
                "total_mastered_sentences": len(self.data["mastered_sentences"])
            }
        
        is_new = False
        
        if is_sentence:
            if english not in self.data["mastered_sentences"]:
                self.data["mastered_sentences"].add(english)
                is_new = True
        else:
            if english not in self.data["mastered_words"]:
                self.data["mastered_words"].add(english)
                is_new = True
        
        if is_new:
            self.save()
            self._check_achievements()
        
        return {
            "newly_mastered": is_new,
            "total_mastered_words": len(self.data["mastered_words"]),
            "total_mastered_sentences": len(self.data["mastered_sentences"])
        }
    
    # ============== 新增：无提示连对统计 ==============
    
    def update_perfect_streak(self, is_correct: bool, no_hint: bool) -> Dict:
        """更新无提示连对记录"""
        if is_correct and no_hint:
            self.data["perfect_streak_count"] += 1
            if self.data["perfect_streak_count"] > self.data["max_perfect_streak"]:
                self.data["max_perfect_streak"] = self.data["perfect_streak_count"]
        else:
            self.data["perfect_streak_count"] = 0
        
        self.save()
        self._check_achievements()
        
        return {
            "current_perfect_streak": self.data["perfect_streak_count"],
            "max_perfect_streak": self.data["max_perfect_streak"]
        }
    
    # ============== 统计信息 ==============
    
    def get_stats(self) -> Dict:
        """获取完整统计信息"""
        return {
            "level": self.data["level"],
            "exp": self.data["exp"],
            "total_blocks": self.data["total_blocks"],
            "blocks": self.data["blocks"],
            "monsters_discovered": self.data["monsters_discovered"],
            "monsters_tamed": self.data["monsters_tamed"],
            "buildings_count": len(self.data["buildings_unlocked"]),
            "achievements_count": len(self.data["achievements"]),
            "login_streak": self.data["login_streak"],
            "stats": self.data["stats"],
            # 新增统计
            "score": self.data["score"],
            "title": self.get_current_title(),
            "total_sessions": self.data["total_sessions"],
            "session_days": len(self.data["session_dates"]),
            "mastered_words_count": len(self.data["mastered_words"]),
            "mastered_sentences_count": len(self.data["mastered_sentences"]),
            "perfect_streak": self.data["perfect_streak_count"],
            "max_perfect_streak": self.data["max_perfect_streak"],
        }
    
    def get_achievement_stats_display(self) -> str:
        """生成成就统计显示"""
        stats = self.get_stats()
        title = stats["title"]
        
        lines = []
        lines.append("## 📊 Timmy英语听写 - 成就统计\n")
        
        # 称号和积分
        lines.append(f"### {title['emoji']} 当前称号：{title['name']}\n")
        lines.append(f"**积分**: {stats['score']} 分\n")
        if title['next_title']:
            next_t = title['next_title']
            lines.append(f"距离 {next_t['emoji']} {next_t['name']}：还需 {next_t['score_needed']} 分\n")
        lines.append("\n---\n\n")
        
        # 听写轮次
        lines.append("### 📝 听写统计\n")
        lines.append(f"- 完成轮次：**{stats['total_sessions']}** 轮\n")
        lines.append(f"- 达成天数：**{stats['session_days']}** 天\n")
        lines.append(f"- 连续登录：**{stats['login_streak']}** 天\n")
        lines.append("\n")
        
        # 词汇掌握
        lines.append("### 📚 词汇掌握\n")
        lines.append(f"- 掌握单词：**{stats['mastered_words_count']}** 个\n")
        lines.append(f"- 掌握句子：**{stats['mastered_sentences_count']}** 个\n")
        total_mastered = stats['mastered_words_count'] + stats['mastered_sentences_count']
        lines.append(f"- 总计：**{total_mastered}** 个\n")
        lines.append("\n")
        
        # 连击记录
        lines.append("### 🔥 连击记录\n")
        lines.append(f"- 最高连击：**{stats['stats']['max_streak']}** 连击\n")
        lines.append(f"- 最高无提示连对：**{stats['max_perfect_streak']}** 连对\n")
        lines.append("\n")
        
        # 成就进度
        lines.append("### 🏆 成就进度\n")
        lines.append(f"- 已解锁成就：**{stats['achievements_count']}** / **{len(ACHIEVEMENTS)}**\n")
        
        return "".join(lines)
    
    def generate_inventory_display(self) -> str:
        """生成背包显示文本"""
        if not self.data["blocks"]:
            return "🎒 背包空空如也，开始冒险吧！"
        
        lines = ["## 🎒 我的背包\n"]
        
        # 按稀有度分组
        groups = {"rare": [], "special": [], "uncommon": [], "common": []}
        
        for block_type, count in self.data["blocks"].items():
            if block_type in BLOCKS:
                info = BLOCKS[block_type]
                groups[info["rarity"]].append((block_type, info, count))
        
        rarity_names = {
            "rare": "💎 稀有",
            "special": "⭐ 特殊",
            "uncommon": "🔷 中级",
            "common": "🔹 普通"
        }
        
        for rarity in ["rare", "special", "uncommon", "common"]:
            if groups[rarity]:
                lines.append(f"\n### {rarity_names[rarity]}\n")
                for _, info, count in groups[rarity]:
                    lines.append(f"{info['emoji']} {info['name']} × {count}\n")
        
        lines.append(f"\n---\n📦 **总计: {self.data['total_blocks']} 个方块**")
        
        return "".join(lines)


# 全局游戏状态实例
game_state = GameState()
