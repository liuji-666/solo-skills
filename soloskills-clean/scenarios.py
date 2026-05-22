#!/usr/bin/env python3
"""
SoloSkills - 场景实现
包含5大核心场景的完整实现
"""

from .core import Scenario, Context, ScenarioType
from typing import Dict, Any, List


class IgniteScenario(Scenario):
    """热启动场景"""
    
    def __init__(self):
        super().__init__("热启动", ScenarioType.IGNITE)
        self.description = "快速恢复上下文，开始新工作"
        self.skills = ["ContextWeaver", "StateEvaluator"]
        self.interaction_level = 2
    
    def detect_trigger(self, user_input: str) -> bool:
        """检测触发"""
        keywords = ["开始", "开工", "继续", "新任务", "恢复", "启动"]
        return any(kw in user_input for kw in keywords)
    
    def execute(self, context: Context, user_input: str) -> Dict[str, Any]:
        """执行热启动"""
        result = {
            "message": "🔥 好的，让我帮你准备开始工作！",
            "context_update": {
                "action": "resume_or_start"
            },
            "suggestions": [
                "继续上次的工作",
                "开始一个新任务",
                "查看项目状态"
            ],
            "steps": [
                {
                    "step": 1,
                    "name": "检查上下文",
                    "status": "in_progress",
                    "details": self._check_context(context)
                },
                {
                    "step": 2,
                    "name": "评估状态",
                    "status": "pending",
                    "details": "评估项目整体状态..."
                },
                {
                    "step": 3,
                    "name": "准备开始",
                    "status": "pending",
                    "details": "准备开始工作..."
                }
            ],
            "next_action": "ready_to_start"
        }
        
        return result
    
    def _check_context(self, context: Context) -> str:
        """检查上下文"""
        if context.task_progress > 0:
            return f"发现未完成的任务，进度 {context.task_progress:.0%}"
        return "这是一个新项目"


class DebugScenario(Scenario):
    """调试突破场景"""
    
    def __init__(self):
        super().__init__("调试突破", ScenarioType.DEBUG)
        self.description = "系统化诊断和修复问题"
        self.skills = ["ReproductionEngine", "HypothesisGenerator", "EvidenceCollector"]
        self.interaction_level = 3
    
    def detect_trigger(self, user_input: str) -> bool:
        """检测触发"""
        keywords = ["错误", "bug", "崩溃", "不工作", "出问题", "修复", "报错"]
        return any(kw in user_input for kw in keywords)
    
    def execute(self, context: Context, user_input: str) -> Dict[str, Any]:
        """执行调试"""
        result = {
            "message": "🔧 发现问题了，让我帮你诊断！",
            "context_update": {
                "action": "diagnose"
            },
            "suggestions": [
                "描述具体的错误信息",
                "分享相关的代码片段",
                "运行测试看看"
            ],
            "steps": [
                {
                    "step": 1,
                    "name": "问题复现",
                    "status": "in_progress",
                    "details": "建立反馈循环，复现问题..."
                },
                {
                    "step": 2,
                    "name": "假设验证",
                    "status": "pending",
                    "details": "提出可能的原因，逐一验证..."
                },
                {
                    "step": 3,
                    "name": "根因定位",
                    "status": "pending",
                    "details": "找到问题的真正原因..."
                },
                {
                    "step": 4,
                    "name": "修复实施",
                    "status": "pending",
                    "details": "实施最小化修复..."
                },
                {
                    "step": 5,
                    "name": "回归验证",
                    "status": "pending",
                    "details": "确保修复不引入新问题..."
                }
            ],
            "next_action": "waiting_for_error_details"
        }
        
        return result


class SparkScenario(Scenario):
    """灵感触发场景"""
    
    def __init__(self):
        super().__init__("灵感触发", ScenarioType.SPARK)
        self.description = "打破思维定式，激发创意"
        self.skills = ["ProblemReformulator", "IdeaGenerator", "ConstraintRelaxer"]
        self.interaction_level = 2
    
    def detect_trigger(self, user_input: str) -> bool:
        """检测触发"""
        keywords = ["创意", "探索", "换个", "头脑风暴", "想法", "更好的方案"]
        return any(kw in user_input for kw in keywords)
    
    def execute(self, context: Context, user_input: str) -> Dict[str, Any]:
        """执行灵感触发"""
        result = {
            "message": "💡 想探索新想法？让我帮你打开思路！",
            "context_update": {
                "action": "explore"
            },
            "suggestions": [
                "换个角度思考",
                "参考类似的解决方案",
                "先实现最小可行版本"
            ],
            "techniques": [
                {
                    "name": "抽象化",
                    "description": "用更高层的语言描述问题",
                    "example": "从'登录功能' → '用户认证机制'"
                },
                {
                    "name": "类比迁移",
                    "description": "借用其他领域的解决方案",
                    "example": "参考银行的认证流程"
                },
                {
                    "name": "反向思考",
                    "description": "从结果倒退原因",
                    "example": "什么时候不需要这个功能？"
                }
            ],
            "next_action": "waiting_for_problem_description"
        }
        
        return result


class SprintScenario(Scenario):
    """交付冲刺场景"""
    
    def __init__(self):
        super().__init__("交付冲刺", ScenarioType.SPRINT)
        self.description = "高效完成，争取交付"
        self.skills = ["PrioritySorter", "IncrementalDeliver", "QuickTester"]
        self.interaction_level = 3
    
    def detect_trigger(self, user_input: str) -> bool:
        """检测触发"""
        keywords = ["冲刺", "交付", "快速", "完成", "deadline"]
        return any(kw in user_input for kw in keywords)
    
    def execute(self, context: Context, user_input: str) -> Dict[str, Any]:
        """执行交付冲刺"""
        result = {
            "message": "🚀 准备冲刺交付！让我们高效完成！",
            "context_update": {
                "action": "sprint"
            },
            "suggestions": [
                "列出待办事项",
                "从最简单的开始",
                "先完成核心功能"
            ],
            "focus_areas": [
                {
                    "area": "核心功能",
                    "priority": 1,
                    "description": "必须完成的功能"
                },
                {
                    "area": "基本测试",
                    "priority": 2,
                    "description": "确保基本可用"
                },
                {
                    "area": "必要文档",
                    "priority": 3,
                    "description": "最基本的说明"
                }
            ],
            "time_boxes": [
                {"task": "核心功能", "time": "50% 时间"},
                {"task": "测试验证", "time": "30% 时间"},
                {"task": "文档准备", "time": "20% 时间"}
            ],
            "next_action": "waiting_for_task_list"
        }
        
        return result


class WrapScenario(Scenario):
    """优雅收尾场景"""
    
    def __init__(self):
        super().__init__("优雅收尾", ScenarioType.WRAP)
        self.description = "总结进度，准备交接"
        self.skills = ["ProgressConfirmer", "StateRecorder", "LessonExtractor"]
        self.interaction_level = 1
    
    def detect_trigger(self, user_input: str) -> bool:
        """检测触发"""
        keywords = ["结束", "收尾", "到这里", "保存", "再见", "完成"]
        return any(kw in user_input for kw in keywords)
    
    def execute(self, context: Context, user_input: str) -> Dict[str, Any]:
        """执行优雅收尾"""
        result = {
            "message": "🌙 好的，我们来做个收尾。",
            "context_update": {
                "action": "wrap_up"
            },
            "suggestions": [
                "总结今天的工作",
                "保存当前进度",
                "规划下一步"
            ],
            "summary_template": {
                "completed": "已完成的工作",
                "in_progress": "进行中的工作",
                "next_steps": "下一步计划",
                "learned": "学到的经验"
            },
            "handoff_checklist": [
                {"item": "代码已提交", "status": "pending"},
                {"item": "测试已通过", "status": "pending"},
                {"item": "文档已更新", "status": "pending"},
                {"item": "进度已记录", "status": "pending"}
            ],
            "next_action": "generating_summary"
        }
        
        return result


# 导出所有场景
__all__ = [
    'IgniteScenario',
    'DebugScenario',
    'SparkScenario',
    'SprintScenario',
    'WrapScenario'
]
