#!/usr/bin/env python3
"""
SoloSkills - CLI工具
命令行界面
"""

import sys
import argparse
from pathlib import Path

# 添加src到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from soloskills import SoloSkills


def main():
    """CLI主入口"""
    parser = argparse.ArgumentParser(
        description="SoloSkills - Trae Solo 原生技能系统"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # init命令
    init_parser = subparsers.add_parser('init', help='初始化项目')
    init_parser.add_argument('--path', default='.', help='项目路径')
    
    # status命令
    status_parser = subparsers.add_parser('status', help='查看状态')
    
    # scenario命令
    scenario_parser = subparsers.add_parser('scenario', help='切换场景')
    scenario_parser.add_argument('type', choices=['ignite', 'debug', 'spark', 'sprint', 'wrap'],
                                 help='场景类型')
    
    # interact命令
    interact_parser = subparsers.add_parser('interact', help='交互')
    interact_parser.add_argument('message', help='用户消息')
    
    # context命令
    context_parser = subparsers.add_parser('context', help='上下文管理')
    context_parser.add_argument('action', choices=['show', 'rebuild', 'save', 'load'])
    
    # learn命令
    learn_parser = subparsers.add_parser('learn', help='学习')
    learn_parser.add_argument('--query', help='查询知识库')
    
    args = parser.parse_args()
    
    # 创建SoloSkills实例
    soloskills = SoloSkills()
    
    # 执行命令
    if args.command == 'init':
        init_project(args.path)
    elif args.command == 'status':
        show_status(soloskills)
    elif args.command == 'scenario':
        switch_scenario(soloskills, args.type)
    elif args.command == 'interact':
        interact(soloskills, args.message)
    elif args.command == 'context':
        manage_context(soloskills, args.action)
    elif args.command == 'learn':
        learn(soloskills, args.query)
    else:
        # 默认交互模式
        interactive_mode(soloskills)


def init_project(path: str):
    """初始化项目"""
    project_path = Path(path)
    soloskills_dir = project_path / '.soloskills'
    soloskills_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"✅ 已在 {project_path} 创建 SoloSkills 配置目录")


def show_status(soloskills: SoloSkills):
    """显示状态"""
    print("\n📊 SoloSkills 状态")
    print("=" * 50)
    print(f"当前场景: {soloskills.current_scenario.value if soloskills.current_scenario else '无'}")
    print(f"项目类型: {soloskills.context.project_type}")
    print(f"任务进度: {soloskills.context.task_progress:.0%}")
    print(f"会话历史: {len(soloskills.session_history)} 条")
    print(f"知识节点: {len(soloskills.knowledge_graph.nodes)} 个")
    print("=" * 50)


def switch_scenario(soloskills: SoloSkills, scenario_type: str):
    """切换场景"""
    from soloskills.core import ScenarioType
    
    scenario_map = {
        'ignite': ScenarioType.IGNITE,
        'debug': ScenarioType.DEBUG,
        'spark': ScenarioType.SPARK,
        'sprint': ScenarioType.SPRINT,
        'wrap': ScenarioType.WRAP
    }
    
    soloskills.current_scenario = scenario_map[scenario_type]
    
    scenario = soloskills.scenarios[soloskills.current_scenario]
    result = scenario.execute(soloskills.context, "")
    
    print(f"\n✅ 已切换到场景: {scenario.name}")
    print(f"\n{result['message']}")
    print("\n建议:")
    for suggestion in result.get('suggestions', []):
        print(f"  • {suggestion}")


def interact(soloskills: SoloSkills, message: str):
    """交互"""
    result = soloskills.interact(message)
    
    print(f"\n🎯 场景: {result['scenario']}")
    print(f"   意图: {result['intent']}")
    print(f"\n{result['message']}")
    
    if 'steps' in result:
        print("\n执行步骤:")
        for step in result['steps']:
            print(f"  {step['step']}. {step['name']} [{step['status']}]")
    
    if result.get('suggestions'):
        print("\n建议:")
        for suggestion in result['suggestions']:
            print(f"  • {suggestion}")


def manage_context(soloskills: SoloSkills, action: str):
    """管理上下文"""
    if action == 'show':
        print("\n📋 当前上下文")
        print("=" * 50)
        print(f"项目路径: {soloskills.context.project_path}")
        print(f"项目类型: {soloskills.context.project_type}")
        print(f"当前文件: {soloskills.context.current_files}")
        print(f"任务进度: {soloskills.context.task_progress:.0%}")
        print(f"决策记录: {len(soloskills.context.decisions)} 条")
        print("=" * 50)
        
    elif action == 'save':
        soloskills.save_state()
        print("✅ 上下文已保存")
        
    elif action == 'load':
        soloskills.load_state()
        print("✅ 上下文已加载")
        
    elif action == 'rebuild':
        # 重新构建上下文
        soloskills.context = soloskills.scenarios[0]._check_context(soloskills.context)
        print("✅ 上下文已重建")


def learn(soloskills: SoloSkills, query: str = None):
    """学习"""
    if query:
        results = soloskills.knowledge_graph.query(query)
        print(f"\n📚 查询结果: {len(results)} 个")
        for i, node in enumerate(results, 1):
            print(f"\n{i}. {node.content[:100]}...")
    else:
        print(f"\n📚 知识库统计")
        print("=" * 50)
        print(f"总节点数: {len(soloskills.knowledge_graph.nodes)}")
        print("=" * 50)


def interactive_mode(soloskills: SoloSkills):
    """交互模式"""
    print("\n🤖 SoloSkills 交互模式")
    print("输入消息开始交互，输入 'quit' 退出\n")
    
    while True:
        try:
            user_input = input("你: ").strip()
            
            if user_input.lower() in ['quit', 'exit', '退出']:
                print("\n👋 再见！")
                break
            
            if not user_input:
                continue
            
            result = soloskills.interact(user_input)
            
            print(f"\n🤖 SoloSkills:")
            print(f"   场景: {result['scenario']}")
            print(f"   {result['message']}")
            
            if result.get('suggestions'):
                print("\n💡 建议:")
                for suggestion in result['suggestions']:
                    print(f"   • {suggestion}")
            
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 再见！")
            break


if __name__ == '__main__':
    main()
