# SoloSkills 场景系统详解

## 📋 场景总览

场景是SoloSkills的核心组织单位，每个场景都是一个完整的工作模式，包含：

- **触发条件**：什么时候激活
- **目标**：要达成什么
- **技能组合**：使用哪些核心技能
- **交互模式**：采用什么沟通方式
- **退出条件**：什么时候结束

---

## 🔥 场景1：热启动 (Ignite)

### 触发时机

```
用户说：
- "开始工作"
- "准备开工"
- "继续上次"
- "切换任务"
- 或者长时间未活动后重新对话
```

### 场景目标

1. **恢复上下文**：快速回到上次的思维状态
2. **明确目标**：确定本次要完成什么
3. **评估状态**：检查项目当前状态
4. **规划行动**：制定接下来的步骤

### 技能组合

```
ContextWeaver → StateEvaluator → GoalClarifier → ActionPlanner
```

#### ContextWeaver（上下文编织）

**职责**：重建上次的工作上下文

**工作流程**：
```
1. 查询上次会话的最后状态
2. 读取项目关键文件的变化
3. 重建当前代码库的思维模型
4. 识别中断点和待完成项
```

**交互示例**：

```
Solo：让我看看上次的情况...
→ 上次你在实现用户登录功能
→ 完成了：注册表单、数据模型
→ 待完成：登录验证逻辑
→ 当前文件：auth/login.ts

准备好了吗？我们继续？
```

#### StateEvaluator（状态评估）

**职责**：评估项目当前状态

**检查清单**：
```
□ Git状态 - 有未提交的更改吗？
□ 测试状态 - 所有测试通过吗？
□ 构建状态 - 项目能正常启动吗？
□ 依赖状态 - 所有依赖安装了吗？
```

**输出格式**：

```yaml
project_state:
  git:
    status: "clean"
    last_commit: "2小时前"
  tests:
    passed: 45
    failed: 0
    coverage: 78%
  build:
    status: "success"
    last_build: "1小时前"
  dependencies:
    outdated: 3
    vulnerable: 0
```

#### GoalClarifier（目标明确）

**职责**：确认本次具体目标

**交互模式**：

```
Solo：我看到你有几个待完成的任务：
  1. 完成登录验证逻辑
  2. 修复导航栏样式问题
  3. 添加单元测试

今天想专注哪个？
或者你有其他想法？
```

#### ActionPlanner（行动规划）

**职责**：制定具体的行动计划

**输出示例**：

```
📋 行动计划：完成登录验证

步骤1：实现验证逻辑 (30分钟)
  → 添加密码哈希
  → 实现JWT生成
  → 添加错误处理

步骤2：编写测试 (20分钟)
  → 测试登录成功
  → 测试密码错误
  → 测试用户不存在

步骤3：集成测试 (15分钟)
  → 测试API端点
  → 测试前端集成

预计总时间：65分钟

开始吗？
```

### 交互模式

**Level 1-2（助手+伙伴）**

- Solo采用友好、鼓励的语气
- 多用"我们"而非"你"
- 定期确认理解是否正确
- 保持简洁，避免信息过载

### 退出条件

```
用户说：
- "开始" / "好的" / "开始吧"
- "换个目标"
- "先到这里"

或者完成所有计划步骤
```

---

## 💡 场景2：灵感触发 (Spark)

### 触发时机

```
用户说：
- "有没有更好的方案"
- "我想探索一下"
- "换个思路"
- "头脑风暴"
- "有什么创意"
- 或者检测到用户长时间卡在同一点
```

### 场景目标

1. **打破思维定式**：从不同角度看待问题
2. **探索可能性**：发现潜在的解决方案
3. **连接知识点**：将不相关的想法联系起来
4. **快速验证**：用最小成本验证想法的可行性

### 技能组合

```
ProblemReformulator → IdeaGenerator → ConstraintRelaxer → PrototypeSketcher
```

#### ProblemReformulator（问题重构）

**职责**：用不同的方式描述问题

**技术**：

```python
class ProblemReformulator:
    """多角度问题重构"""
    
    techniques = {
        "抽象化": "用更高层的语言描述",
        "具象化": "用具体的例子说明",
        "反向思考": "从结果倒退原因",
        "类比迁移": "借用其他领域的解决方案",
        "约束挑战": "质疑问题的前提假设"
    }
    
    def reformulate(self, problem):
        # 生成5种不同的表述
        reformulations = []
        for technique in self.techniques:
            reformulated = self.apply(problem, technique)
            reformulations.append(reformulated)
        return reformulations
```

**交互示例**：

```
Solo：让我从几个不同的角度重新看看这个问题...

原问题：如何在登录页面实现"记住我"功能？

抽象角度：
  本质是"延长用户会话有效期"
  涉及"状态管理"和"安全问题"

反向思考：
  什么时候用户不希望被记住？
  如何让用户主动选择？

类比迁移：
  浏览器书签 vs 自动登录
  咖啡店的会员卡 vs 免密支付

你觉得哪个角度最有启发性？
```

#### IdeaGenerator（创意生成）

**职责**：快速产生大量想法

**生成策略**：

```python
class IdeaGenerator:
    """多策略创意生成"""
    
    def generate(self, context):
        ideas = []
        
        # 1. 经典模式
        ideas.extend(self.classic_patterns(context))
        
        # 2. 跨界借鉴
        ideas.extend(self.cross_domain(context))
        
        # 3. 反面思考
        ideas.extend(self.reverse_thinking(context))
        
        # 4. 组合创新
        ideas.extend(self.combinations(context))
        
        return self.prioritize(ideas)
```

**输出示例**：

```
Solo：我生成了一些想法，让我们看看：

🔥 高潜力（强烈推荐）：
  1. 社交登录 + 传统登录并存
     优点：覆盖所有用户，渐进迁移
     风险：实现复杂度高

  2. 渐进式增强登录
     优点：先实现基础，逐步添加高级功能
     风险：需要良好的架构设计

🌟 有趣的想法（值得探索）：
  3. 无密码登录（邮箱链接）
     优点：更安全，用户无需记忆密码
     风险：用户体验变化大

  4. 零知识证明登录
     优点：最高安全性
     风险：实现复杂，用户教育成本高

你想深入哪个方向？
```

#### ConstraintRelaxer（约束放松）

**职责**：暂时放下限制，激发创意

**工作方式**：

```
Solo：好的，现在让我们玩个游戏：
假设没有技术限制、没有时间压力、没有安全问题...

你想实现什么？
```

**然后逐步加回约束**：

```
Solo：好的，如果加上"2周内完成"的约束呢？
Solo：如果必须兼容旧浏览器呢？
Solo：如果团队只有你一个人呢？
```

#### PrototypeSketcher（原型速写）

**职责**：用最小代码验证想法

**输出示例**：

```python
# 方案A的最小可行原型
# 只需要30行代码验证核心思路

from auth import SocialLogin

def quick_auth_demo():
    # 1. 模拟社交登录
    provider = SocialLogin("github")
    
    # 2. 快速验证流程
    token = provider.authenticate(code="demo")
    
    # 3. 检查是否满足需求
    return token is not None

# 运行测试
# 如果通过，说明方案可行
```

### 交互模式

**Level 2-3（伙伴+专家）**

- Solo扮演创意伙伴的角色
- 鼓励大胆想象，不批评
- 用"如果...会怎样"激发思考
- 帮助连接分散的想法

### 退出条件

```
用户说：
- "我觉得方案X不错"
- "就用这个思路"
- "先试试这个"
- "可以了"

或者选定了明确方向
```

---

## 🔧 场景3：调试突破 (Debug)

### 触发时机

```
用户说：
- "出错了"
- "Bug"
- "不工作了"
- "报错了"
- "崩溃了"
- 或者检测到编译失败、测试失败
```

### 场景目标

1. **快速复现**：稳定地重现问题
2. **准确定位**：找到问题的真正原因
3. **有效修复**：用最小的改动解决问题
4. **防止回归**：确保问题不再出现

### 技能组合

```
ReproductionEngine → HypothesisGenerator → EvidenceCollector → FixImplementer → RegressionBuilder
```

#### ReproductionEngine（复现引擎）

**职责**：建立可靠的反馈循环

**优先级列表**：

```
1. 失败的测试用例
   → 最可靠，可自动化
   → 最佳选择

2. 明确的复现步骤
   → 用户能稳定复现
   → 次佳选择

3. 临时测试脚本
   → 需要创建额外代码
   → 第三选择

4. 日志分析
   → 被动信息
   → 最后手段

5. 二分查找
   → 穷举法
   → 万不得已
```

**交互示例**：

```
Solo：好的，让我们先复现这个问题。

我发现最近的更改涉及 auth 模块。
能否运行一下这个命令：

  npm test -- --grep "登录"

看看测试结果是什么？
或者你能描述下具体的错误现象吗？
```

#### HypothesisGenerator（假设生成器）

**职责**：系统地提出可能的原因

**输出格式**：

```yaml
hypotheses:
  - id: 1
    description: "密码验证逻辑错误"
    probability: 85%
    evidence: "测试用例4失败在密码检查"
    test: "检查login.ts第42行"
    
  - id: 2
    description: "JWT生成问题"
    probability: 30%
    evidence: "涉及token生成的测试都失败"
    test: "查看JWT配置"
    
  - id: 3
    description: "数据库连接池耗尽"
    probability: 10%
    evidence: "偶发性失败"
    test: "查看连接日志"
```

**交互方式**：

```
Solo：我提出了几个假设，按可能性排序：

1️⃣ 密码验证逻辑错误（85%）
   → 证据：测试精准失败在这个点
   → 验证方法：检查login.ts第42行

2️⃣ JWT配置问题（30%）
   → 证据：多个token相关测试失败
   → 验证方法：查看JWT初始化代码

3️⃣ 数据库连接问题（10%）
   → 证据：错误是偶发的
   → 验证方法：检查连接池配置

你想先验证哪个？
```

#### EvidenceCollector（证据收集器）

**职责**：系统地验证或否定假设

**工作流程**：

```python
class EvidenceCollector:
    async def collect(self, hypothesis):
        # 1. 设计最小验证实验
        experiment = self.design_experiment(hypothesis)
        
        # 2. 执行并观察结果
        result = await self.run(experiment)
        
        # 3. 记录证据
        evidence = self.record(result)
        
        # 4. 判断假设是否成立
        confirmed = self.evaluate(evidence, hypothesis)
        
        return {
            "hypothesis": hypothesis,
            "confirmed": confirmed,
            "evidence": evidence
        }
```

#### FixImplementer（修复实施器）

**职责**：实施最小化修复

**原则**：
```
1. 修复一个问题的改动应该尽量小
2. 改动越小，引入新问题的风险越低
3. 如果修复很复杂，说明需要重构
```

**输出示例**：

```
Solo：找到问题了！login.ts第42行：

```typescript
// 错误代码
if (password === hash) {  // ❌ 应该是 hash 验证

// 修复后
if (await bcrypt.compare(password, hash)) {  // ✅
```

这个修改应该能解决问题。
要我现在应用吗？
```

#### RegressionBuilder（回归构建器）

**职责**：防止问题再次出现

**工作内容**：

```
1. 添加测试用例
   → 确保这个问题被测试覆盖

2. 添加断言
   → 在代码中加入防御性检查

3. 添加日志
   → 让未来调试更容易

4. 更新文档
   → 记录这个坑和解决方案
```

### 交互模式

**Level 2-3（伙伴+专家）**

- Solo采用系统化、冷静的语气
- 避免瞎猜，每一步都基于证据
- 让用户参与决策，不独断
- 完成后详细解释原因

### 退出条件

```
所有失败的测试通过
并且添加了回归测试
并且用户确认理解修复内容
```

---

## 🚀 场景4：交付冲刺 (Sprint)

### 触发时机

```
用户说：
- "准备交付"
- "冲刺一下"
- "快速完成"
- "时间不多了"
- 或者检测到接近deadline
```

### 场景目标

1. **最大化产出**：在有限时间内完成最多
2. **保证质量**：不因速度牺牲基本质量
3. **清晰交付**：让交接者快速理解
4. **减少压力**：让冲刺过程可控

### 技能组合

```
PrioritySorter → IncrementalDeliver → QuickTester → DocSimplifier → HandoffPreparer
```

#### PrioritySorter（优先级排序器）

**职责**：识别最重要、最有价值的工作

**排序算法**：

```python
def sort_by_value(items, deadline):
    scored_items = []
    
    for item in items:
        score = (
            item.business_value * 0.4 +    # 业务价值
            item.urgency * 0.3 +          # 紧急程度
            item.completion * 0.2 +        # 完成度（部分完成的优先）
            item.ease * 0.1               # 难易度（简单的优先）
        )
        scored_items.append((score, item))
    
    return sorted(scored_items, reverse=True)
```

**输出示例**：

```
Solo：根据剩余时间和任务评估，建议按这个顺序冲刺：

🎯 最高优先级：
  1. 完成登录功能的核心逻辑
     → 价值：解锁整个用户系统
     → 进度：80%
     → 剩余：15分钟

  2. 修复注册页面的验证提示
     → 价值：提升用户体验
     → 进度：50%
     → 剩余：10分钟

⏸️ 可以延后：
  3. 添加"忘记密码"功能
     → 可以用简单方案临时替代

📝 跳过本次：
  4. 登录页面的动画效果
     → 非核心功能

同意这个优先级吗？
```

#### IncrementalDeliver（增量交付器）

**职责**：将大功能拆分为可交付的小块

**输出示例**：

```
Solo：让我把登录功能拆成可交付的块：

版本1.0 - MVP（现在就能交付）
  ✅ 注册页面 + 数据保存
  ✅ 登录页面 + 简单验证
  ✅ 会话管理

版本1.1 - 增强（本周内）
  ⬜ 社交登录
  ⬜ 密码强度验证
  ⬜ 邮箱验证

版本2.0 - 完整（后续迭代）
  ⬜ 双重认证
  ⬜ SSO集成
  ⬜ 登录行为分析

现在就交付版本1.0可以吗？
```

#### QuickTester（快速测试）

**职责**：用最小测试保证基本质量

**测试金字塔**：

```
        ▲
       /E2E\        ← 只做核心流程
      /----\
     /集成  \      ← 只测模块边界
    /------\
   /  单元  \      ← 关键逻辑即可
  /----------\
  
不追求100%覆盖率
但确保核心路径不崩溃
```

#### DocSimplifier（文档简化）

**职责**：用最少的文字传递必要信息

**模板**：

```markdown
## 登录功能

### 这是什么
允许用户使用邮箱密码登录系统

### 如何使用
1. 访问 /login
2. 输入邮箱和密码
3. 点击登录

### 已知限制
- 不支持社交登录
- 会话有效期7天

### 测试方法
npm test -- auth
```

#### HandoffPreparer（交接准备）

**职责**：让接手的人快速上手

**输出示例**：

```
📋 交接文档

## 登录功能 - 开发完成

### 状态
✅ 功能完成
✅ 基本测试通过
⬜ 文档待完善

### 关键文件
- auth/login.ts - 主逻辑
- auth/register.ts - 注册
- auth/session.ts - 会话管理

### 待办
- [ ] 添加集成测试
- [ ] 编写API文档
- [ ] 性能优化

### 联系我
有疑问可以随时问！
```

### 交互模式

**Level 3-4（专家+导师）**

- Solo采用高效、直接的语气
- 避免过度讨论，快速决策
- 提供选择而非开放式问题
- 主动识别风险和遗漏

### 退出条件

```
核心功能交付完成
基本测试通过
交接文档准备好
```

---

## 🌙 场景5：优雅收尾 (Wrap)

### 触发时机

```
用户说：
- "今天到这里"
- "准备结束"
- "保存进度"
- "交接一下"
- 或者检测到长时间无活动
```

### 场景目标

1. **确认进度**：明确今天完成了什么
2. **保存状态**：为下次留下清晰的上下文
3. **总结经验**：提炼这次学到的教训
4. **规划未来**：明确下一步该做什么

### 技能组合

```
ProgressConfirmer → StateRecorder → LessonExtractor → NextStepsPlanner
```

#### ProgressConfirmer（进度确认）

**职责**：清晰总结本次工作成果

**输出示例**：

```
Solo：今天的收成不错！

✅ 完成了：
  • 登录功能核心逻辑
  • 注册页面UI
  • 数据模型设计

📝 进度：
  • 登录功能：80%
  • 注册功能：100%
  • 整体项目：35%

⏸️ 待继续：
  • 登录验证逻辑
  • 社交登录集成
```

#### StateRecorder（状态记录）

**职责**：保存完整的状态信息

**记录内容**：

```yaml
session_summary:
  date: "2024-05-22"
  duration: "2.5小时"
  
  completed:
    - name: "注册页面UI"
      files: ["auth/register.tsx", "auth/register.css"]
      tests: 3
      
  in_progress:
    - name: "登录功能"
      progress: "80%"
      last_file: "auth/login.ts"
      interruption_point: "正在实现JWT验证"
      
  decisions_made:
    - "使用JWT作为会话token"
    - "密码使用bcrypt加密"
    
  issues_encountered:
    - "CORS配置问题"
    - "已解决：添加了正确的headers"
```

#### LessonExtractor（经验提炼）

**职责**：从本次工作提取可复用的经验

**交互示例**：

```
Solo：这次开发过程中，有几个值得记录的点：

💡 技术收获：
  • JWT和Session的选择：JWT更适合API服务
  • 密码加密：bcrypt比MD5安全得多

⚠️ 踩过的坑：
  • CORS配置导致登录失败
  • 教训：前后端分离项目要优先处理CORS

🎯 可以复用的模式：
  • 统一的错误处理中间件
  • 表单验证的通用组件

要我把它们记录到项目知识库吗？
```

#### NextStepsPlanner（下一步规划）

**职责**：明确下次工作的起点

**输出示例**：

```
📋 下次开始时

1. 运行命令：
   npm run dev

2. 打开文件：
   auth/login.ts

3. 从这里继续：
   "实现JWT验证逻辑"
   (上次在第58行中断)

4. 今天的待办：
   □ 完成JWT验证
   □ 添加集成测试
   □ 修复导航栏问题
```

### 交互模式

**Level 1-2（助手+伙伴）**

- Solo采用温暖、鼓励的语气
- 强调进步和成果
- 提供清晰的交接信息
- 表达期待下次见面

### 退出条件

```
状态保存完成
用户确认"可以了"或"谢谢"
```

---

## 🎭 场景切换

### 自动检测

SoloSkills持续监控对话，自动检测场景切换：

```python
class ScenarioDetector:
    """场景自动检测"""
    
    triggers = {
        "Ignite": ["开始", "继续", "开工", "新任务"],
        "Spark": ["创意", "探索", "换个", "头脑风暴"],
        "Debug": ["错误", "Bug", "崩溃", "不工作"],
        "Sprint": ["冲刺", "交付", "快速", "时间"],
        "Wrap": ["结束", "收尾", "到这里", "再见"]
    }
    
    def detect(self, message):
        for scenario, keywords in self.triggers.items():
            if any(kw in message for kw in keywords):
                return scenario
        return None
```

### 主动询问

当检测到模糊信号时：

```
Solo：听起来你想做些不一样的事？
是想：
  1. 继续当前任务
  2. 探索新想法
  3. 还是遇到问题了？

告诉我，你想怎么推进？
```

---

## 🎯 场景选择指南

| 你想做什么 | 推荐场景 |
|-----------|----------|
| 开始新工作或恢复中断 | 热启动 (Ignite) |
| 需要创意或遇到瓶颈 | 灵感触发 (Spark) |
| 代码出错需要调试 | 调试突破 (Debug) |
| 接近deadline要冲刺 | 交付冲刺 (Sprint) |
| 结束工作或交接 | 优雅收尾 (Wrap) |

---

**场景系统让SoloSkills能够真正理解你的需求，提供恰到好处的帮助！** ✨
