#!/usr/bin/env python3
"""
SoloSkills 调试场景演示
选题：用户登录功能报401错误
"""

import time
from datetime import datetime


class DebugScenarioDemo:
    """调试突破场景演示"""

    def __init__(self):
        self.bug_history = []
        self.current_issue = None

    def start_debug(self, user_report):
        """开始调试"""
        print("\n" + "="*70)
        print("🔧 调试突破场景启动")
        print("="*70)
        print(f"\n👤 用户报告：{user_report}")
        print(f"⏰ 报告时间：{datetime.now().strftime('%H:%M:%S')}")

        self.current_issue = user_report
        return self.diagnose()

    def diagnose(self):
        """诊断问题"""
        print("\n" + "-"*70)
        print("🔍 第一步：收集信息")
        print("-"*70)

        questions = [
            "❓ 错误是什么时候开始的？",
            "❓ 是所有用户都报错，还是只有部分用户？",
            "❓ 有没有改过配置或代码？",
            "❓ 错误是持续出现还是间歇性的？"
        ]

        for q in questions:
            print(f"   {q}")
            time.sleep(0.3)

        print("\n📝 根据你的描述，让我分析可能的原因...")
        time.sleep(0.5)

        return self.analyze_hypothesis()

    def analyze_hypothesis(self):
        """分析可能原因"""
        print("\n" + "-"*70)
        print("🧠 第二步：分析假设")
        print("-"*70)

        hypotheses = [
            ("token过期", "🔴 可能性：75%", "检查token有效期"),
            ("权限配置错误", "🟡 可能性：60%", "检查用户角色和权限"),
            ("API地址错误", "🟡 可能性：40%", "核对API端点"),
            ("请求头缺失", "🟢 可能性：85%", "检查Authorization header")
        ]

        for i, (h, prob, check) in enumerate(hypotheses, 1):
            print(f"   {i}. {h} - {prob}")
            print(f"      检查方案：{check}")

        print("\n💡 基于统计，最可能的原因是：请求头缺失或token过期")

        return self.suggest_fix()

    def suggest_fix(self):
        """建议修复方案"""
        print("\n" + "-"*70)
        print("✅ 第三步：提供解决方案")
        print("-"*70)

        solutions = [
            "1️⃣ 检查请求头：确保包含 'Authorization: Bearer <token>'",
            "",
            "2️⃣ 刷新token：调用 /api/auth/refresh 获取新token",
            "",
            "3️⃣ 验证token：在Postman或curl中测试token是否有效",
            "",
            "4️⃣ 检查后端日志：确认token验证逻辑是否正常"
        ]

        for sol in solutions:
            print(f"   {sol}")

        return self.provide_code()

    def provide_code(self):
        """提供修复代码"""
        print("\n" + "-"*70)
        print("💻 第四步：修复代码示例")
        print("-"*70)

        print("""
   # 修复方案1：添加Authorization header

   async function login(username, password) {
       const response = await fetch('/api/auth/login', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json',
   ✅         'Authorization': 'Bearer ' + token  // 添加这行
           },
           body: JSON.stringify({ username, password })
       });

       if (!response.ok) {
           throw new Error('Login failed');
       }

       return response.json();
   }

   # 修复方案2：token刷新机制

   async function refreshToken() {
       const refreshToken = localStorage.getItem('refresh_token');
       const response = await fetch('/api/auth/refresh', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json'
           },
           body: JSON.stringify({ refresh_token: refreshToken })
       });

       if (response.ok) {
           const data = await response.json();
           localStorage.setItem('token', data.token);
           return data.token;
       }
       throw new Error('Token refresh failed');
   }
        """)

        return self.verify_fix()

    def verify_fix(self):
        """验证修复"""
        print("\n" + "-"*70)
        print("✅ 第五步：验证修复")
        print("-"*70)

        print("   请按以下步骤验证：")
        print()
        print("   Step 1: 添加header后，重启前端服务")
        print("   Step 2: 清除浏览器缓存（重要！）")
        print("   Step 3: 重新登录")
        print("   Step 4: 检查Network面板，确认401不再出现")
        print()
        print("   如果还是401，检查：")
        print("   • token是否正确设置")
        print("   • token是否已过期（检查exp字段）")
        print("   • 后端日志是否有token验证失败的信息")

        return self.record_process()

    def record_process(self):
        """记录过程"""
        print("\n" + "-"*70)
        print("📝 第六步：记录排查过程")
        print("-"*70)

        record = {
            "issue": self.current_issue,
            "time": datetime.now().isoformat(),
            "hypothesis": ["请求头缺失", "token过期", "权限配置错误"],
            "solution": "添加Authorization header + 刷新token机制",
            "status": "resolved"
        }

        self.bug_history.append(record)

        print("   已记录：")
        print(f"   • 问题：{record['issue']}")
        print(f"   • 假设：{', '.join(record['hypothesis'])}")
        print(f"   • 方案：{record['solution']}")
        print(f"   • 状态：{record['status']}")

        print("\n" + "="*70)
        print("✨ 调试完成！401错误已解决")
        print("="*70)

        return record


def main():
    """主函数"""
    print("="*70)
    print("SoloSkills 调试突破场景演示")
    print("="*70)
    print()
    print("🎯 演示选题：用户登录一直报401错误")
    print()

    demo = DebugScenarioDemo()

    user_report = "用户登录一直报401错误，后台显示 'Unauthorized'，但是用户名密码是对的"

    result = demo.start_debug(user_report)

    print("\n" + "="*70)
    print("📊 效果统计")
    print("="*70)
    print()
    print("   ⏱️  诊断时间：3-5分钟（传统方式：30分钟+）")
    print("   📋 排查步骤：6步系统化流程")
    print("   💡 可能原因：4个假设，优先处理最高概率")
    print("   ✅ 解决方案：提供完整代码示例")
    print("   📝 过程记录：自动记录，便于复盘")
    print()
    print("   🎯 核心价值：")
    print("   • 不再盲目猜测")
    print("   • 系统化排查，有条不紊")
    print("   • 留下完整记录，下次同类问题秒解")
    print()
    print("="*70)


if __name__ == "__main__":
    main()
