#!/usr/bin/env python3
"""
SoloSkills - Trae Solo 原生技能系统
完整可运行版本

核心功能：
1. 场景检测与自动切换
2. 多维上下文管理
3. 技能执行引擎
4. 知识编织系统
5. 节奏感知能力
"""

__version__ = "1.0.0"
__author__ = "SoloSkills Team"
__license__ = "MIT"

from .core import (
    SoloSkills,
    Scenario,
    Context,
    Intent,
    KnowledgeGraph,
    ScenarioType
)

from .scenarios import (
    IgniteScenario,
    DebugScenario,
    SparkScenario,
    SprintScenario,
    WrapScenario
)

from .skills import (
    ContextWeaver,
    RhythmAwareness,
    IntentDecoding,
    KnowledgeKnitting,
    AdaptiveExecutor,
    QualityGuardian,
)

__all__ = [
    # 核心
    "SoloSkills",
    "Scenario",
    "Context",
    "Intent",
    "KnowledgeGraph",
    "ScenarioType",
    
    # 场景
    "IgniteScenario",
    "DebugScenario",
    "SparkScenario",
    "SprintScenario",
    "WrapScenario",
    
    # 技能
    "ContextWeaver",
    "RhythmAwareness",
    "IntentDecoding",
    "KnowledgeKnitting",
    "AdaptiveExecutor",
    "QualityGuardian",
]
