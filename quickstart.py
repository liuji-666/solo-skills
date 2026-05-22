#!/usr/bin/env python3
"""
SoloSkills 快速启动脚本
一键体验5大场景
"""

import sys
import time


def print_header():
    """打印标题"""
    print("="*70)
    print("🎯 SoloSkills - 快速体验")
    print("="*70)
    print()


def print_scenarios():
    """打印场景列表"""
    scenarios = [
        ("1", "🔥 热启动", "开始新任务或恢复中断", "ignite"),
        ("2", "💡 灵感触发", "需要创意或打破瓶颈", "spark"),
        ("3", "🔧 调试突破", "Bug、错误、问题排查", "debug"),
        ("4", "🚀 交付冲刺", "快速完成、紧急任务", "sprint"),
        ("5", "🌙 优雅收尾", "结束工作、整理进度", "wrap"),
    ]

    print("📚 可用场景：")
    print()
    for num, emoji, desc, id in scenarios:
        print(f"  [{num}] {emoji} {desc}")
    print()
    print("[Q] 退出")
    print()


def run_scenario(scenario_id):
    """运行场景演示"""
    print()

    scenarios = {
        "1": ("🔥 热启动场景", [
            "检测到场景：热启动",
            "加载上次上下文...",
            "✓ 任务：用户登录功能开发",
            "✓ 进度：完成注册流程（100%）",
            "✓ 当前：第三方登录对接（65%）",
            "",
            "💡 建议：继续第三方登录开发，或先测试已完成的注册功能"
        ]),
        "2": ("💡 灵感触发场景", [
            "检测到场景：灵感触发",
            "分析问题：用户认证方案...",
            "",
            "🔍 当前方案：JWT Token",
            "",
            "💭 从不同角度思考：",
            "  • 安全性：Token泄露风险如何降低？",
            "  • 性能：每次请求都验证Token，压力大吗？",
            "  • 用户体验：Session和Token各有什么优势？",
            "",
            "✨ 建议探索：OAuth2.0 vs JWT vs Session"
        ]),
        "3": ("🔧 调试突破场景", [
            "检测到场景：调试突破",
            "启动诊断流程...",
            "",
            "❓ 请描述问题（模拟）：",
            "  用户报告：登录一直报401错误",
            "",
            "🔍 系统化排查：",
            "  1. 检查请求头 ✓",
            "  2. 验证Token ✓",
            "  3. 查看权限配置 ✓",
            "  4. 检查后端日志 ✓",
            "",
            "💡 最可能原因：Authorization header缺失",
            "✅ 解决方案：添加 'Authorization: Bearer <token>'"
        ]),
        "4": ("🚀 交付冲刺场景", [
            "检测到场景：交付冲刺",
            "激活高效模式...",
            "",
            "🎯 目标：明天上午12点前交付",
            "",
            "📋 优先级排序：",
            "  P0: 用户登录功能（必须完成）",
            "  P1: 注册流程测试（影响交付）",
            "  P2: UI细节优化（可以延期）",
            "",
            "⚡ 冲刺策略：",
            "  • 跳过边界情况",
            "  • 使用TODO代替详细注释",
            "  • 优先完成核心流程"
        ]),
        "5": ("🌙 优雅收尾场景", [
            "检测到场景：优雅收尾",
            "整理工作进度...",
            "",
            "📊 今日完成：",
            "  ✓ 用户注册功能",
            "  ✓ 邮箱验证流程",
            "  ◐ 第三方登录（进行中）",
            "",
            "📝 决策记录：",
            "  • 选择JWT方案（简洁、可扩展）",
            "  • 第三方登录暂支持微信",
            "",
            "🎯 明日计划：",
            "  1. 完成微信登录对接",
            "  2. 测试登录完整流程",
            "  3. 准备部署文档",
            "",
            "💾 状态已保存，下次可直接继续"
        ])
    }

    if scenario_id in scenarios:
        title, lines = scenarios[scenario_id]
        print(f"🎯 {title}")
        print("-" * 70)
        for line in lines:
            print(f"  {line}")
        print()
    else:
        print("❌ 无效的场景编号")
        print()


def main():
    """主函数"""
    print_header()
    print_scenarios()

    while True:
        try:
            choice = input("请选择场景 [1-5/Q]: ").strip()

            if choice.upper() == 'Q':
                print("\n👋 再见！期待下次使用 SoloSkills")
                print("="*70)
                break

            if choice in ['1', '2', '3', '4', '5']:
                run_scenario(choice)
                time.sleep(0.5)
                print("-" * 70)
                print()
            else:
                print("❌ 无效选择，请输入 1-5 或 Q\n")

        except KeyboardInterrupt:
            print("\n\n👋 已退出")
            break
        except EOFError:
            break


if __name__ == "__main__":
    main()
