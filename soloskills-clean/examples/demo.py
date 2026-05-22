#!/usr/bin/env python3
"""
SoloSkills - 演示程序
展示场景系统和核心技能的工作原理
"""

import time
from datetime import datetime


class SimpleContextWeaver:
    """简化的上下文编织技能"""
    
    def __init__(self):
        self.context = {}
        self.history = []
    
    def weave(self, user_input, project_state):
        """编织上下文"""
        return {
            "user_input": user_input,
            "project_state": project_state,
            "timestamp": datetime.now().isoformat(),
            "context_ready": True
        }


class SimpleRhythmAwareness:
    """简化的节奏感知"""
    
    def __init__(self):
        self.last_activity = time.time()
        self.typing_speed = 0
    
    def detect(self, user_input):
        """检测用户节奏"""
        current_time = time.time()
        gap = current_time - self.last_activity
        self.last_activity = current_time
        
        if gap < 10:
            return {"mode": "deep_focus", "suggestion": "保持高效"}
        elif gap < 60:
            return {"mode": "normal", "suggestion": "正常"}
        else:
            return {"mode": "paused", "suggestion": "继续？"}


class SimpleScenarioManager:
    """简化的场景管理器"""
    
    TRIGGERS = {
        "ignite": ["开始", "开工", "继续", "新任务"],
        "spark": ["创意", "探索", "换个", "头脑风暴"],
        "debug": ["错误", "Bug", "崩溃", "不工作"],
        "sprint": ["冲刺", "交付", "快速", "完成"],
        "wrap": ["结束", "收尾", "到这里"]
    }
    
    SCENARIOS = {
        "ignite": {
            "name": "热启动",
            "description": "恢复上下文，开始工作",
            "skills": ["ContextWeaver", "StateEvaluator"]
        },
        "debug": {
            "name": "调试突破",
            "description": "系统化诊断和修复问题",
            "skills": ["ReproductionEngine", "HypothesisGenerator"]
        },
        "spark": {
            "name": "灵感触发",
            "description": "打破思维定式，激发创意",
            "skills": ["ProblemReformulator", "IdeaGenerator"]
        },
        "sprint": {
            "name": "交付冲刺",
            "description": "高效完成，争取交付",
            "skills": ["PrioritySorter", "QuickTester"]
        },
        "wrap": {
            "name": "优雅收尾",
            "description": "总结进度，准备交接",
            "skills": ["ProgressConfirmer", "StateRecorder"]
        }
    }
    
    def detect_scenario(self, user_input):
        """检测场景"""
        user_input_lower = user_input.lower()
        for scenario, keywords in self.TRIGGERS.items():
            if any(kw in user_input_lower for kw in keywords):
                return scenario
        return "ignite"  # 默认场景
    
    def activate_scenario(self, scenario_id):
        """激活场景"""
        if scenario_id not in self.SCENARIOS:
            return None
        
        scenario = self.SCENARIOS[scenario_id]
        return {
            "scenario_id": scenario_id,
            "name": scenario["name"],
            "description": scenario["description"],
            "skills": scenario["skills"],
            "activated_at": datetime.now().isoformat()
        }


class SoloSkillsDemo:
    """SoloSkills演示"""
    
    def __init__(self):
        self.context_weaver = SimpleContextWeaver()
        self.rhythm_awareness = SimpleRhythmAwareness()
        self.scenario_manager = SimpleScenarioManager()
        self.current_scenario = None
    
    def interact(self, user_input):
        """交互入口"""
        # 1. 检测节奏
        rhythm = self.rhythm_awareness.detect(user_input)
        
        # 2. 检测场景
        detected_scenario = self.scenario_manager.detect_scenario(user_input)
        
        # 3. 如果场景变化，激活新场景
        if detected_scenario != self.current_scenario:
            scenario_info = self.scenario_manager.activate_scenario(detected_scenario)
            self.current_scenario = detected_scenario
            print(f"\n{'='*60}")
            print(f"🎯 场景切换：{scenario_info['name']}")
            print(f"   {scenario_info['description']}")
            print(f"   激活技能：{', '.join(scenario_info['skills'])}")
            print(f"{'='*60}\n")
        
        # 4. 根据场景生成响应
        response = self.generate_response(user_input, rhythm)
        return response
    
    def generate_response(self, user_input, rhythm):
        """根据场景生成响应"""
        if self.current_scenario == "ignite":
            return self.handle_ignite(user_input)
        elif self.current_scenario == "debug":
            return self.handle_debug(user_input)
        elif self.current_scenario == "spark":
            return self.handle_spark(user_input)
        elif self.current_scenario == "sprint":
            return self.handle_sprint(user_input)
        elif self.current_scenario == "wrap":
            return self.handle_wrap(user_input)
        else:
            return {"message": "我明白了，继续说..."}
    
    def handle_ignite(self, user_input):
        """处理热启动场景"""
        return {
            "message": "好的，让我帮你准备开始工作！\n\n" +
                      "1. 检查上次进度...\n" +
                      "2. 评估当前状态...\n" +
                      "3. 准备开始...",
            "suggestions": [
                "继续上次的工作",
                "开始一个新任务",
                "检查项目状态"
            ]
        }
    
    def handle_debug(self, user_input):
        """处理调试场景"""
        return {
            "message": "发现问题了，让我帮你诊断。\n\n" +
                      "1. 复现问题...\n" +
                      "2. 分析可能原因...\n" +
                      "3. 定位根因...",
            "suggestions": [
                "运行测试看看",
                "描述具体错误",
                "分享相关代码"
            ]
        }
    
    def handle_spark(self, user_input):
        """处理灵感触发场景"""
        return {
            "message": "想探索新想法？让我帮你打开思路！\n\n" +
                      "1. 从不同角度看问题...\n" +
                      "2. 生成多种可能...\n" +
                      "3. 快速验证...",
            "suggestions": [
                "有没有更好的方案？",
                "换个角度思考",
                "头脑风暴一下"
            ]
        }
    
    def handle_sprint(self, user_input):
        """处理交付冲刺场景"""
        return {
            "message": "准备冲刺交付！\n\n" +
                      "1. 确认核心功能...\n" +
                      "2. 排列优先级...\n" +
                      "3. 快速迭代...",
            "suggestions": [
                "列出待办事项",
                "开始核心功能",
                "准备交付文档"
            ]
        }
    
    def handle_wrap(self, user_input):
        """处理优雅收尾场景"""
        return {
            "message": "好的，我们来做个收尾。\n\n" +
                      "1. 确认完成进度...\n" +
                      "2. 记录当前状态...\n" +
                      "3. 规划下一步...",
            "suggestions": [
                "总结今天的工作",
                "保存当前进度",
                "准备交接文档"
            ]
        }


def main():
    """主函数"""
    print("="*60)
    print("SoloSkills 演示 - Trae Solo原生技能系统")
    print("="*60)
    
    demo = SoloSkillsDemo()
    
    # 模拟对话场景
    conversations = [
        ("开始一个新任务吧", "ignite"),
        ("代码出问题了", "debug"),
        ("有没有更好的方案？", "spark"),
        ("准备冲刺交付", "sprint"),
        ("今天先到这里", "wrap")
    ]
    
    for i, (user_input, expected) in enumerate(conversations, 1):
        print(f"\n[{i}] 用户：{user_input}")
        print(f"    预期场景：{expected}")
        
        response = demo.interact(user_input)
        print(f"    SoloSkills：{response['message'].split(chr(10))[0]}")
        
        time.sleep(0.5)
    
    print("\n" + "="*60)
    print("演示完成！")
    print("="*60)
    print("\nSoloSkills核心特性：")
    print("✓ 场景自动检测和切换")
    print("✓ 上下文感知编织")
    print("✓ 用户节奏检测")
    print("✓ 智能响应生成")
    print("\n这只是简化演示，完整版本包含：")
    print("- 5个完整场景系统")
    print("- 7个核心技能")
    print("- 知识图谱系统")
    print("- 多层次集成方案")


if __name__ == "__main__":
    main()
