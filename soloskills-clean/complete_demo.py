#!/usr/bin/env python3
"""
SoloSkills - 完整演示
展示所有核心功能的完整示例
"""

import sys
from pathlib import Path

# 添加src到路径
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from soloskills import SoloSkills
from soloskills.core import ScenarioType


def main():
    """完整演示"""
    print("=" * 70)
    print("SoloSkills 完整演示 - Trae Solo 原生技能系统")
    print("=" * 70)
    print()
    
    # 1. 初始化
    print("1️⃣ 初始化 SoloSkills...")
    soloskills = SoloSkills()
    print(f"   ✓ 版本: {soloskills.config.get('version')}")
    print(f"   ✓ 用户: {soloskills.config['user']['name']}")
    print()
    
    # 2. 场景检测演示
    print("2️⃣ 场景检测演示...")
    test_inputs = [
        ("开始一个新任务吧", ScenarioType.IGNITE),
        ("代码出问题了", ScenarioType.DEBUG),
        ("有没有更好的方案？", ScenarioType.SPARK),
        ("准备冲刺交付", ScenarioType.SPRINT),
        ("今天先到这里", ScenarioType.WRAP)
    ]
    
    for user_input, expected in test_inputs:
        detected = soloskills.detect_scenario(user_input)
        status = "✓" if detected == expected else "✗"
        print(f"   {status} '{user_input}' → {detected.value}")
    print()
    
    # 3. 交互演示
    print("3️⃣ 交互演示...")
    print()
    
    conversations = [
        {
            "user": "开始一个新任务吧",
            "context": {"path": "/project/login", "type": "web"}
        },
        {
            "user": "代码报错了，登录失败",
            "context": None
        },
        {
            "user": "有没有更好的认证方案？",
            "context": None
        }
    ]
    
    for conv in conversations:
        print(f"👤 用户: {conv['user']}")
        
        result = soloskills.interact(
            conv['user'],
            conv.get('context')
        )
        
        print(f"🤖 SoloSkills:")
        print(f"   场景: {result['scenario']}")
        print(f"   {result['message']}")
        
        if 'steps' in result:
            print("   执行步骤:")
            for step in result['steps']:
                print(f"     {step['step']}. {step['name']}")
        
        print()
    
    # 4. 知识图谱演示
    print("4️⃣ 知识图谱演示...")
    
    # 添加一些知识
    soloskills.knowledge_graph.add(
        content="用户登录使用JWT认证，Token有效期7天",
        node_type="technical_decision"
    )
    soloskills.knowledge_graph.add(
        content="密码使用bcrypt加密，强度要求12",
        node_type="security_config"
    )
    
    # 查询
    results = soloskills.knowledge_graph.query("登录")
    print(f"   ✓ 添加了2个知识节点")
    print(f"   ✓ 查询'登录'找到 {len(results)} 个相关知识")
    
    # 保存
    soloskills.knowledge_graph.save()
    print(f"   ✓ 知识图谱已保存")
    print()
    
    # 5. 状态保存演示
    print("5️⃣ 状态保存演示...")
    
    # 模拟一些上下文
    soloskills.context.task_progress = 0.65
    soloskills.context.decisions.append({
        "type": "auth_method",
        "decision": "使用JWT"
    })
    
    # 保存
    soloskills.save_state()
    print(f"   ✓ 上下文已保存")
    
    # 加载
    soloskills.load_state()
    print(f"   ✓ 上下文已加载")
    print(f"   ✓ 任务进度: {soloskills.context.task_progress:.0%}")
    print(f"   ✓ 决策数量: {len(soloskills.context.decisions)}")
    print()
    
    # 6. 节奏感知演示
    print("6️⃣ 节奏感知演示...")
    
    rhythm1 = soloskills.understand_intent("代码出问题了").category
    print(f"   当前场景: {rhythm1.value}")
    
    print()
    print("=" * 70)
    print("✅ 演示完成！")
    print("=" * 70)
    print()
    print("核心功能展示：")
    print("  ✓ 场景自动检测")
    print("  ✓ 智能意图理解")
    print("  ✓ 多维上下文管理")
    print("  ✓ 知识图谱编织")
    print("  ✓ 状态持久化")
    print("  ✓ 节奏感知")
    print()
    print("下一步：")
    print("  • 使用 CLI: python -m soloskills.cli")
    print("  • 集成到Trae Solo")
    print("  • 自定义场景和技能")
    print()


if __name__ == '__main__':
    main()
