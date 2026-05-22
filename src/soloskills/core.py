#!/usr/bin/env python3
"""
SoloSkills - 核心引擎
完整可运行的核心系统实现
"""

import json
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum


class ScenarioType(Enum):
    """场景类型"""
    IGNITE = "ignite"        # 热启动
    DEBUG = "debug"          # 调试突破
    SPARK = "spark"          # 灵感触发
    SPRINT = "sprint"       # 交付冲刺
    WRAP = "wrap"           # 优雅收尾


@dataclass
class Context:
    """多维上下文"""
    project_path: str = ""
    project_type: str = "unknown"
    task_progress: float = 0.0
    conversation_history: List[Dict] = None
    current_files: List[str] = None
    decisions: List[Dict] = None
    user_preferences: Dict = None
    
    def __post_init__(self):
        if self.conversation_history is None:
            self.conversation_history = []
        if self.current_files is None:
            self.current_files = []
        if self.decisions is None:
            self.decisions = []
        if self.user_preferences is None:
            self.user_preferences = {}
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Context':
        """从字典创建"""
        return cls(**data)


@dataclass
class Intent:
    """用户意图"""
    surface: str
    category: ScenarioType
    confidence: float
    entities: Dict[str, Any]
    raw_input: str
    
    def __str__(self):
        return f"Intent({self.category.value}, confidence={self.confidence:.2f})"


@dataclass
class SkillResult:
    """技能执行结果"""
    skill_name: str
    success: bool
    output: Any
    suggestions: List[str]
    metadata: Dict
    
    def __str__(self):
        status = "✓" if self.success else "✗"
        return f"{status} {self.skill_name}"


class KnowledgeNode:
    """知识图谱节点"""
    
    def __init__(self, node_id: str, content: str, node_type: str):
        self.id = node_id
        self.content = content
        self.type = node_type
        self.connections: List[str] = []
        self.metadata: Dict = {}
        self.created_at = datetime.now()
        self.access_count = 0
    
    def connect_to(self, other_id: str):
        """连接到另一个节点"""
        if other_id not in self.connections:
            self.connections.append(other_id)
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "id": self.id,
            "content": self.content,
            "type": self.type,
            "connections": self.connections,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "access_count": self.access_count
        }


class KnowledgeGraph:
    """知识图谱"""
    
    def __init__(self, storage_path: Optional[str] = None):
        self.nodes: Dict[str, KnowledgeNode] = {}
        self.storage_path = storage_path or ".soloskills/knowledge.json"
    
    def add(self, content: str, node_type: str, metadata: Dict = None) -> str:
        """添加知识节点"""
        node_id = f"node_{len(self.nodes)}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        node = KnowledgeNode(node_id, content, node_type)
        if metadata:
            node.metadata = metadata
        self.nodes[node_id] = node
        self._auto_connect(node_id)
        return node_id
    
    def _auto_connect(self, node_id: str):
        """自动建立连接"""
        node = self.nodes[node_id]
        for other_id, other_node in self.nodes.items():
            if other_id != node_id:
                # 简单的相似度连接
                if self._similar(node.content, node.content):
                    node.connect_to(other_id)
                    other_node.connect_to(node_id)
    
    def _similar(self, text1: str, text2: str) -> bool:
        """判断是否相似（简化版）"""
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        intersection = words1 & words2
        return len(intersection) >= 2
    
    def query(self, query: str, limit: int = 5) -> List[KnowledgeNode]:
        """查询相关知识"""
        results = []
        query_lower = query.lower()
        
        for node in self.nodes.values():
            if query_lower in node.content.lower():
                node.access_count += 1
                results.append(node)
        
        return sorted(results, key=lambda n: n.access_count, reverse=True)[:limit]
    
    def save(self):
        """保存知识图谱"""
        Path(self.storage_path).parent.mkdir(parents=True, exist_ok=True)
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            data = {node_id: node.to_dict() for node_id, node in self.nodes.items()}
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load(self):
        """加载知识图谱"""
        if Path(self.storage_path).exists():
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for node_id, node_data in data.items():
                    node = KnowledgeNode(
                        node_data['id'],
                        node_data['content'],
                        node_data['type']
                    )
                    node.connections = node_data['connections']
                    node.metadata = node_data['metadata']
                    node.access_count = node_data['access_count']
                    self.nodes[node_id] = node


class Scenario:
    """场景基类"""
    
    def __init__(self, name: str, scenario_type: ScenarioType):
        self.name = name
        self.type = scenario_type
        self.description = ""
        self.skills: List[str] = []
        self.interaction_level = 2
    
    def detect_trigger(self, user_input: str) -> bool:
        """检测是否触发此场景"""
        return False
    
    def execute(self, context: Context, user_input: str) -> Dict[str, Any]:
        """执行场景"""
        return {
            "message": f"执行场景：{self.name}",
            "context_update": {},
            "suggestions": []
        }


class SoloSkills:
    """
    SoloSkills 主类
    完整可运行的AI协作系统
    """
    
    # 场景触发词
    TRIGGERS = {
        ScenarioType.IGNITE: ["开始", "开工", "继续", "新任务", "恢复", "启动", "准备"],
        ScenarioType.DEBUG: ["错误", "bug", "崩溃", "不工作", "出问题", "修复", "报错"],
        ScenarioType.SPARK: ["创意", "探索", "换个", "头脑风暴", "想法", "更好的方案"],
        ScenarioType.SPRINT: ["冲刺", "交付", "快速", "完成", "deadline"],
        ScenarioType.WRAP: ["结束", "收尾", "到这里", "保存", "再见", "完成"]
    }
    
    def __init__(self, config_path: Optional[str] = None):
        """初始化 SoloSkills"""
        self.config = self._load_config(config_path)
        self.context = Context()
        self.knowledge_graph = KnowledgeGraph()
        self.current_scenario: Optional[ScenarioType] = None
        self.session_history: List[Dict] = []
        self.user_preferences: Dict = self.config.get('user', {}).get('preferences', {})
        
        # 加载知识图谱
        self.knowledge_graph.load()
        
        # 初始化场景
        self.scenarios = self._init_scenarios()
    
    def _load_config(self, config_path: Optional[str]) -> Dict:
        """加载配置"""
        if config_path and Path(config_path).exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                if config_path.endswith('.json'):
                    return json.load(f)
                elif config_path.endswith(('.yaml', '.yml')):
                    return yaml.safe_load(f)
        
        # 默认配置
        return {
            "version": "1.0.0",
            "user": {
                "name": "开发者",
                "expertise": "intermediate"
            },
            "collaboration": {
                "help_level": "伙伴",
                "communication_style": "balanced"
            },
            "scenarios": {
                "enabled": ["ignite", "debug", "spark", "sprint", "wrap"],
                "default": "ignite"
            }
        }
    
    def _init_scenarios(self) -> Dict[ScenarioType, Scenario]:
        """初始化场景"""
        return {
            ScenarioType.IGNITE: IgniteScenario(),
            ScenarioType.DEBUG: DebugScenario(),
            ScenarioType.SPARK: SparkScenario(),
            ScenarioType.SPRINT: SprintScenario(),
            ScenarioType.WRAP: WrapScenario()
        }
    
    def detect_scenario(self, user_input: str) -> ScenarioType:
        """检测场景"""
        user_input_lower = user_input.lower()
        
        scores = {}
        for scenario_type, keywords in self.TRIGGERS.items():
            score = sum(1 for keyword in keywords if keyword in user_input_lower)
            scores[scenario_type] = score
        
        # 返回得分最高的场景
        if max(scores.values()) > 0:
            detected = max(scores.items(), key=lambda x: x[1])[0]
        else:
            # 默认场景
            detected = ScenarioType.IGNITE
        
        self.current_scenario = detected
        return detected
    
    def understand_intent(self, user_input: str) -> Intent:
        """理解用户意图"""
        # 检测场景
        scenario_type = self.detect_scenario(user_input)
        
        # 提取实体（简化版）
        entities = self._extract_entities(user_input)
        
        return Intent(
            surface=user_input,
            category=scenario_type,
            confidence=0.8,
            entities=entities,
            raw_input=user_input
        )
    
    def _extract_entities(self, text: str) -> Dict[str, Any]:
        """提取实体"""
        entities = {}
        
        # 提取引号内容
        import re
        quoted = re.findall(r'"([^"]*)"', text) + re.findall(r"'([^']*)'", text)
        if quoted:
            entities['references'] = quoted
        
        # 提取技术术语
        tech_terms = ['API', '数据库', '函数', '类', '模块', '测试', '部署']
        for term in tech_terms:
            if term in text:
                entities[term] = True
        
        return entities
    
    def execute_scenario(self, intent: Intent, context: Context) -> Dict[str, Any]:
        """执行场景"""
        scenario = self.scenarios.get(intent.category)
        if not scenario:
            return {
                "message": "未识别的场景",
                "suggestions": []
            }
        
        # 更新上下文
        self.context = context
        
        # 执行场景
        result = scenario.execute(self.context, intent.raw_input)
        
        # 记录到历史
        self.session_history.append({
            "timestamp": datetime.now().isoformat(),
            "intent": str(intent),
            "scenario": intent.category.value,
            "result": result
        })
        
        return result
    
    def interact(self, user_input: str, project_context: Optional[Dict] = None) -> Dict[str, Any]:
        """
        主要交互入口
        
        Args:
            user_input: 用户输入
            project_context: 项目上下文（可选）
            
        Returns:
            响应字典
        """
        # 1. 更新项目上下文
        if project_context:
            self.context.project_path = project_context.get('path', '')
            self.context.project_type = project_context.get('type', 'unknown')
            if 'files' in project_context:
                self.context.current_files = project_context['files']
        
        # 2. 理解意图
        intent = self.understand_intent(user_input)
        
        # 3. 记录对话
        self.context.conversation_history.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now().isoformat()
        })
        
        # 4. 执行场景
        result = self.execute_scenario(intent, self.context)
        
        # 5. 添加Solo响应
        result['scenario'] = intent.category.value
        result['intent'] = str(intent)
        
        # 6. 生成建议
        if not result.get('suggestions'):
            result['suggestions'] = self._generate_suggestions(intent)
        
        # 7. 保存知识（如果需要）
        if intent.category == ScenarioType.DEBUG:
            self._learn_from_debug(user_input, result)
        
        return result
    
    def _generate_suggestions(self, intent: Intent) -> List[str]:
        """生成建议"""
        suggestions = {
            ScenarioType.IGNITE: [
                "继续上次的工作",
                "开始一个新任务",
                "查看项目状态"
            ],
            ScenarioType.DEBUG: [
                "描述具体的错误信息",
                "分享相关的代码片段",
                "运行测试看看"
            ],
            ScenarioType.SPARK: [
                "换个角度思考",
                "参考类似的解决方案",
                "先实现最小可行版本"
            ],
            ScenarioType.SPRINT: [
                "列出待办事项",
                "从最简单的开始",
                "先完成核心功能"
            ],
            ScenarioType.WRAP: [
                "总结今天的工作",
                "保存当前进度",
                "规划下一步"
            ]
        }
        
        return suggestions.get(intent.category, [])
    
    def _learn_from_debug(self, user_input: str, result: Dict):
        """从调试中学习"""
        # 提取问题
        problem = user_input
        solution = result.get('message', '')
        
        # 添加到知识图谱
        node_id = self.knowledge_graph.add(
            content=f"问题：{problem}\n解决方案：{solution}",
            node_type="debug_experience",
            metadata={"scenario": "debug"}
        )
        
        # 自动保存
        self.knowledge_graph.save()
    
    def save_state(self, path: str = ".soloskills/session.json"):
        """保存状态"""
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        
        state = {
            "context": self.context.to_dict(),
            "session_history": self.session_history,
            "current_scenario": self.current_scenario.value if self.current_scenario else None,
            "user_preferences": self.user_preferences
        }
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
    
    def load_state(self, path: str = ".soloskills/session.json"):
        """加载状态"""
        if Path(path).exists():
            with open(path, 'r', encoding='utf-8') as f:
                state = json.load(f)
                
                self.context = Context.from_dict(state['context'])
                self.session_history = state.get('session_history', [])
                scenario_str = state.get('current_scenario')
                if scenario_str:
                    self.current_scenario = ScenarioType(scenario_str)
                self.user_preferences = state.get('user_preferences', {})


# 导入场景实现
from .scenarios import (
    IgniteScenario,
    DebugScenario,
    SparkScenario,
    SprintScenario,
    WrapScenario
)
