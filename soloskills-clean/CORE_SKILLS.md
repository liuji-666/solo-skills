# SoloSkills 核心技能详解

## 📖 技能总览

SoloSkills的核心理念是：**技能不是工具，而是能力**。

每个技能都代表了AI协作中的一种核心能力，这些能力可以根据场景灵活组合。

---

## 🧠 核心技能体系

### 第一层：感知类技能

#### 1. ContextWeaver（上下文编织）

**定位**：感知的基础，所有协作的起点。

**核心能力**：

```python
class ContextWeaver:
    """多维度上下文编织"""
    
    # 维护的上下文维度
    dimensions = {
        "project": {
            "description": "项目整体状态",
            "sources": ["git", "file_system", "config"],
            "refresh_rate": "实时"
        },
        "task": {
            "description": "当前任务状态",
            "sources": ["conversation", "progress_log"],
            "refresh_rate": "按需"
        },
        "conversation": {
            "description": "对话历史轨迹",
            "sources": ["chat_history"],
            "refresh_rate": "持续"
        },
        "code": {
            "description": "相关代码片段",
            "sources": ["file_read", "buffer"],
            "refresh_rate": "按需"
        },
        "decision": {
            "description": "决策记录",
            "sources": ["conversation", "explicit_record"],
            "refresh_rate": "决策时"
        },
        "user": {
            "description": "用户偏好和习惯",
            "sources": ["history", "explicit_preference"],
            "refresh_rate": "持续学习"
        }
    }
```

**工作原理**：

```
用户输入 → 触发编织 → 多源感知 → 上下文融合 → 智能查询
              ↓
         自动维护 ← 持续更新 ← 变化检测
```

**典型应用场景**：

```
场景1：恢复中断的工作

Solo：让我重建上下文...
→ 读取上次会话记录（task维度）
→ 检查项目文件变化（project维度）
→ 查看最近的代码更改（code维度）
→ 重建当前思维状态

恢复完成！
上次你在：auth/login.ts 第58行
中断原因：实现JWT验证
当前状态：需要完成密码比对逻辑

准备好继续了吗？
```

```
场景2：理解复杂需求

Solo：让我先理解一下你的需求上下文...
→ 查看相关模块代码（code维度）
→ 检查是否有类似实现（decision维度）
→ 了解项目架构约定（project维度）
→ 评估用户技术水平（user维度）

综合分析：
• 这个功能涉及3个模块
• 其中auth模块已有完整的测试覆盖
• 项目偏好使用TypeScript装饰器
• 用户偏好简洁直接的实现

我有个方案，你要听听吗？
```

**与其他技能的配合**：

```python
# ContextWeaver + IntentDecoding
context = context_weaver.get_context()
intent = intent_decoding.decode(context)

# ContextWeaver + RhythmAwareness
context = context_weaver.get_context()
rhythm = rhythm_awareness.detect(context)

# ContextWeaver + KnowledgeKnitting
context = context_weaver.get_context()
knowledge.recall(context)
```

---

#### 2. RhythmAwareness（节奏感知）

**定位**：理解用户的工作状态，动态调整协作方式。

**核心能力**：

```python
class RhythmAwareness:
    """用户工作节奏检测"""
    
    # 节奏模式识别
    patterns = {
        "deep_focus": {
            "signals": [
                "typing_speed",      # 快速持续输入
                "focus_duration",    # 长时间无闲聊
                "error_tolerance",   # 低错误容忍
                "break_pattern"      # 短暂休息
            ],
            "特征": "高效工作区",
            "solo_mode": True,     # 启用静默模式
            "干预策略": "minimal"   # 最小干预
        },
        "exploration": {
            "signals": [
                "question_frequency",  # 频繁提问
                "file_browsing",       # 广泛浏览
                "code_reading",        # 阅读多于编写
                "search_usage"         # 大量搜索
            ],
            "特征": "学习和探索",
            "solo_mode": False,
            "干预策略": "teaching"    # 教学模式
        },
        "stuck": {
            "signals": [
                "pause_duration",      # 长时间停顿
                "revert_pattern",      # 反复撤销
                "frustration_indicators", # 挫败信号
                "help_seeking"         # 主动求助
            ],
            "特征": "遇到障碍",
            "solo_mode": False,
            "干预策略": "proactive"   # 主动帮助
        },
        "testing": {
            "signals": [
                "test_running",       # 频繁运行测试
                "assertion_adding",   # 添加断言
                "coverage_checking"   # 检查覆盖率
            ],
            "特征": "质量验证",
            "solo_mode": True,
            "干预策略": "supportive"  # 支持模式
        },
        "debugging": {
            "signals": [
                "error_reading",      # 阅读错误信息
                "stack_trace",        # 分析堆栈
                "breakpoint_adding",   # 添加断点
                "step_execution"       # 单步执行
            ],
            "特征": "问题排查",
            "solo_mode": False,
            "干预策略": "collaborative" # 协作模式
        }
    }
```

**动态调整示例**：

```python
class SoloModeController:
    """动态Solo模式控制器"""
    
    def get_response_style(self, rhythm):
        if rhythm == "deep_focus":
            return ResponseStyle(
                verbosity="minimal",
                format="concise",
                interruptions=False,
                suggestions="limited"
            )
        elif rhythm == "exploration":
            return ResponseStyle(
                verbosity="detailed",
                format="educational",
                interruptions=True,
                suggestions="abundant"
            )
        elif rhythm == "stuck":
            return ResponseStyle(
                verbosity="moderate",
                format="problem_solving",
                interruptions=True,
                suggestions="specific"
            )
```

**交互示例**：

```
场景：检测到用户陷入困境

Solo：[检测到可能的障碍信号]
→ 暂停了3分钟
→ 最近有2次代码撤销
→ 没有新的代码提交

[自动调整为支持模式]

Solo：我注意到你可能在某个地方卡住了。

想让我帮忙看看吗？
我有几个建议：
  1. 可以尝试添加一些console.log看看变量值
  2. 或者运行测试看看具体哪里失败
  3. 也可以描述一下你现在的思路，我们一起分析

你想怎么推进？
```

```
场景：检测到用户进入深度工作状态

Solo：[切换到静默模式]

[用户继续快速输入...]
[Solo保持安静，仅在必要时提供反馈]

[检测到用户放慢速度]

Solo：好的，你似乎在思考什么。需要讨论一下吗？
```

---

#### 3. IntentDecoding（意图解码）

**定位**：理解用户真实意图，不只是字面意思。

**核心能力**：

```python
class IntentDecoding:
    """多层次意图解码"""
    
    # 意图层次模型
    layers = {
        "surface": {
            "description": "字面意图",
            "examples": [
                "加个登录功能" → "实现登录"
            ]
        },
        "middle": {
            "description": "功能意图",
            "examples": [
                "加个登录功能" → "需要用户认证系统"
            ]
        },
        "deep": {
            "description": "业务意图",
            "examples": [
                "加个登录功能" → "保护用户数据和隐私"
            ]
        },
        "root": {
            "description": "根本需求",
            "examples": [
                "加个登录功能" → "让用户感到安全可控"
            ]
        }
    }
```

**解码策略**：

```python
class IntentDecoder:
    """多策略意图解码"""
    
    def decode(self, user_message, context):
        # 1. 表面意图识别
        surface = self.recognize_surface(user_message)
        
        # 2. 上下文补充
        contextualized = self.enrich_with_context(surface, context)
        
        # 3. 意图验证
        clarified = self.verify_intent(contextualized, user_message)
        
        # 4. 深层意图挖掘
        deep = self.extract_deep_intent(clarified, context)
        
        return Intent(
            surface=surface,
            contextualized=contextualized,
            clarified=clarified,
            deep=deep,
            confidence=self.calculate_confidence(surface, deep)
        )
```

**意图类型分类**：

```python
class IntentType(Enum):
    """意图类型"""
    
    # 信息获取
    QUERY = "query"           # 查询信息
    LEARN = "learn"           # 学习知识
    EXPLORE = "explore"       # 探索了解
    
    # 任务执行
    CREATE = "create"          # 创建新内容
    MODIFY = "modify"         # 修改现有
    DELETE = "delete"         # 删除内容
    REFACTOR = "refactor"     # 重构代码
    
    # 问题解决
    DEBUG = "debug"            # 调试问题
    FIX = "fix"               # 修复错误
    OPTIMIZE = "optimize"     # 优化性能
    
    # 协作沟通
    CLARIFY = "clarify"       # 澄清理解
    ALIGN = "align"           # 对齐期望
    COLLABORATE = "collaborate" # 协作讨论
    
    # 元操作
    PLAN = "plan"             # 制定计划
    REVIEW = "review"          # 审查代码
    DOCUMENT = "document"      # 编写文档
```

**交互示例**：

```
场景：用户说"加个登录功能"

Solo：让我理解一下你的需求...

[意图解码分析]
表面意图：实现登录功能
功能意图：需要用户认证
深层意图：保护用户数据和控制访问
根本需求：让用户感到安全，同时方便管理

[生成澄清问题]

在开始之前，我想确认几个关键点：

1. 认证范围：
   → 只是登录/注册？
   → 还是需要完整的用户管理（角色、权限）？

2. 用户类型：
   → 普通注册用户？
   → 还是也需要管理员账户？

3. 安全要求：
   → 标准密码登录足够？
   → 还是需要社交登录、双因素等？

你有倾向的方案吗？或者我根据常见场景推荐一个？
```

---

### 第二层：认知类技能

#### 4. KnowledgeKnitting（知识编织）

**定位**：跨会话、跨项目积累和管理知识。

**核心能力**：

```python
class KnowledgeKnitting:
    """个人知识图谱编织"""
    
    def __init__(self):
        self.graph = KnowledgeGraph()
        self.pattern_extractor = PatternExtractor()
        self.relationship_builder = RelationshipBuilder()
    
    # 知识类型
    knowledge_types = {
        "pattern": {
            "description": "代码模式",
            "examples": [
                "单例模式", "工厂模式", "观察者模式"
            ],
            "storage": "patterns/"
        },
        "decision": {
            "description": "技术决策",
            "examples": [
                "选择React而非Vue",
                "使用PostgreSQL而非MongoDB"
            ],
            "storage": "decisions/"
        },
        "lesson": {
            "description": "经验教训",
            "examples": [
                "CORS配置导致登录失败",
                "大文件不要放Git"
            ],
            "storage": "lessons/"
        },
        "snippet": {
            "description": "代码片段",
            "examples": [
                "常用的工具函数",
                "配置模板"
            ],
            "storage": "snippets/"
        },
        "concept": {
            "description": "概念理解",
            "examples": [
                "JWT工作原理",
                "RESTful设计原则"
            ],
            "storage": "concepts/"
        }
    }
```

**知识提取流程**：

```python
class PatternExtractor:
    """从经验中提取模式"""
    
    def extract(self, experience):
        # 1. 识别重复元素
        repetitions = self.find_repetitions(experience)
        
        # 2. 抽象化
        abstraction = self.abstract(repetitions)
        
        # 3. 命名模式
        named_pattern = self.name(abstraction)
        
        # 4. 验证泛化性
        if self.validate(named_pattern):
            return named_pattern
        return None
    
    def find_repetitions(self, experience):
        """从经验中找重复"""
        # 分析代码变更历史
        # 识别常见的修改模式
        # 提取可复用的结构
        pass
    
    def abstract(self, repetitions):
        """抽象化"""
        # 保留核心结构
        # 移除具体细节
        # 简化表达
        pass
```

**知识关联构建**：

```python
class RelationshipBuilder:
    """构建知识关联"""
    
    relationship_types = {
        "depends_on": "依赖关系",
        "similar_to": "相似关系",
        "contradicts": "矛盾关系",
        "evolves_to": "演进关系",
        "solves": "解决关系"
    }
    
    def build(self, knowledge_item):
        relationships = []
        
        # 查找相似的知识
        similar = self.find_similar(knowledge_item)
        relationships.append(
            Relationship("similar_to", similar)
        )
        
        # 查找前置知识
        prerequisites = self.find_prerequisites(knowledge_item)
        relationships.append(
            Relationship("depends_on", prerequisites)
        )
        
        # 查找可解决的问题
        solves = self.find_problems_it_solves(knowledge_item)
        relationships.append(
            Relationship("solves", solves)
        )
        
        return relationships
```

**交互示例**：

```
场景：用户遇到新问题

Solo：让我查查知识库...

[知识检索]
找到相关记录：

📚 相关决策：
  • 之前选择了JWT作为认证方案
    → 关联：auth模块使用情况
    → 时间：3天前

📚 踩过的坑：
  • CORS配置导致登录失败
    → 教训：前后端分离要先处理CORS
    → 已解决

📚 相关模式：
  • 认证模块标准结构
    → 包含：注册、登录、登出、刷新
    → 可复用代码：https://...

[综合建议]
针对你当前的登录问题，我建议：

1. 先检查CORS配置（之前踩过的坑）
2. 参考认证模块标准结构
3. 复用已有的工具函数

需要我帮你具体实施吗？
```

---

#### 5. SolutionArchitect（方案架构）

**定位**：设计解决方案的整体架构。

**核心能力**：

```python
class SolutionArchitect:
    """解决方案架构设计"""
    
    def design(self, problem, constraints):
        # 1. 问题分解
        components = self.decompose(problem)
        
        # 2. 方案探索
        options = self.explore_options(components)
        
        # 3. 方案评估
        evaluated = self.evaluate_options(options, constraints)
        
        # 4. 架构决策
        decision = self.make_decision(evaluated)
        
        # 5. 详细设计
        detailed = self.detail_design(decision)
        
        return Solution(
            overview=decision,
            components=detailed,
            risks=self.identify_risks(detailed),
            alternatives=self.document_alternatives(evaluated)
        )
```

**方案生成策略**：

```python
class OptionGenerator:
    """多方案生成"""
    
    generation_strategies = {
        "incremental": {
            "description": "增量方案",
            "approach": "在现有基础上逐步添加"
        },
        "big_bang": {
            "description": "整体方案",
            "approach": "一次性完整实现"
        },
        "prototype": {
            "description": "原型方案",
            "approach": "快速验证核心思路"
        },
        "hybrid": {
            "description": "混合方案",
            "approach": "核心用整体，其他用增量"
        }
    }
```

**交互示例**：

```
场景：用户需要实现支付功能

Solo：好的，让我为支付功能设计几个方案。

[问题分解]
支付功能包含：
  1. 支付入口和UI
  2. 订单创建和管理
  3. 支付网关集成
  4. 回调处理
  5. 退款处理

[方案设计]

方案A：快速上线方案（2天）
  ✓ 使用第三方支付SDK（Stripe/PayPal）
  ✓ 最小化开发，专注业务逻辑
  ✓ 支持主流支付方式
  ✗ 手续费较高
  ✗ 定制化受限

方案B：自建方案（2周）
  ✓ 完全可控，定制灵活
  ✓ 可对接多种支付渠道
  ✓ 长期成本低
  ✗ 开发周期长
  ✗ 需要处理PCI合规

方案C：混合方案（5天）
  ✓ 核心支付自建
  ✓ 复杂场景用第三方
  ✓ 平衡可控性和开发成本
  ⚠ 需要设计良好的抽象层

[推荐]
基于你提到的时间约束（5天），
我推荐方案C。

你觉得哪个方案更符合你的需求？
```

---

### 第三层：行动类技能

#### 6. AdaptiveExecutor（自适应执行器）

**定位**：智能执行任务，动态调整策略。

**核心能力**：

```python
class AdaptiveExecutor:
    """自适应任务执行"""
    
    def __init__(self):
        self.execution_engine = ExecutionEngine()
        self.progress_tracker = ProgressTracker()
        self.strategy_optimizer = StrategyOptimizer()
    
    async def execute(self, task):
        # 1. 分析任务
        plan = self.plan(task)
        
        # 2. 执行计划
        for step in plan.steps:
            result = await self.execute_step(step)
            
            # 3. 检查结果
            if self.needs_adjustment(result):
                # 4. 动态调整
                plan = self.adjust_plan(plan, result)
            
            # 5. 记录进度
            self.progress_tracker.update(step, result)
        
        # 6. 返回最终结果
        return self.compile_results(plan)
```

**执行策略选择**：

```python
class StrategySelector:
    """执行策略选择"""
    
    strategies = {
        "conservative": {
            "适用": "关键任务、高风险操作",
            "特点": "小步执行，每步验证"
        },
        "aggressive": {
            "适用": "探索性任务、低风险操作",
            "特点": "大步快跑，快速试错"
        },
        "collaborative": {
            "适用": "需要用户决策的任务",
            "特点": "定期暂停，确认方向"
        },
        "automated": {
            "适用": "重复性任务、低风险操作",
            "特点": "完全自动化，定期汇报"
        }
    }
    
    def select(self, task, user_preferences):
        # 基于任务特征和用户偏好选择策略
        pass
```

**交互示例**：

```
场景：实现用户注册功能

Solo：好的，我开始实现注册功能。

[执行计划]
步骤1：创建数据模型
  → 预计时间：5分钟
  → 风险：低
  
步骤2：实现API端点
  → 预计时间：10分钟
  → 风险：中（涉及验证逻辑）
  
步骤3：编写测试
  → 预计时间：8分钟
  → 风险：低

[开始执行]

✅ 步骤1完成
  → 创建了 User 模型
  → 添加了必要字段：email, password_hash, created_at

⏳ 步骤2进行中...
  → 需要确认：邮箱验证用同步还是异步？

用户：异步吧
[继续执行]

✅ 步骤2完成
  → 创建了 POST /api/users 端点
  → 实现了邮箱异步验证
  → 添加了错误处理

⏳ 步骤3进行中...
  → 正在编写测试用例

[进度更新]
完成度：66%
剩余时间：约8分钟
```

---

#### 7. QualityGuardian（质量守护）

**定位**：保证交付质量，防止问题遗漏。

**核心能力**：

```python
class QualityGuardian:
    """质量守护"""
    
    quality_dimensions = {
        "correctness": {
            "description": "正确性",
            "checks": [
                "测试覆盖率",
                "边界条件处理",
                "错误处理"
            ]
        },
        "readability": {
            "description": "可读性",
            "checks": [
                "命名规范",
                "注释完整性",
                "代码结构"
            ]
        },
        "maintainability": {
            "description": "可维护性",
            "checks": [
                "耦合度",
                "内聚度",
                "依赖管理"
            ]
        },
        "performance": {
            "description": "性能",
            "checks": [
                "时间复杂度",
                "资源使用",
                "响应速度"
            ]
        }
    }
```

**智能检查示例**：

```python
class SmartChecker:
    """智能质量检查"""
    
    def check(self, code_changes):
        issues = []
        
        # 1. 测试覆盖检查
        test_coverage = self.check_test_coverage(code_changes)
        if test_coverage < 80%:
            issues.append(Issue(
                type="coverage",
                severity="warning",
                message="测试覆盖率低于80%"
            ))
        
        # 2. 安全检查
        security_issues = self.check_security(code_changes)
        issues.extend(security_issues)
        
        # 3. 性能检查
        performance_issues = self.check_performance(code_changes)
        issues.extend(performance_issues)
        
        # 4. 代码规范检查
        style_issues = self.check_style(code_changes)
        issues.extend(style_issues)
        
        return issues
```

**交互示例**：

```
场景：功能实现完成，进行质量检查

Solo：好的，功能基本完成了。
让我做一个质量检查...

[质量检查报告]

✅ 正确性
  • 测试覆盖率：85% ✓
  • 边界条件：已处理 ✓
  • 错误处理：完整 ✓

⚠️ 可读性
  • 注释覆盖率：60%
  → 建议：auth/login.ts 第45行添加注释

⚠️ 可维护性
  • auth模块耦合度：中等
  → 建议：提取验证逻辑为独立函数

✅ 性能
  • 响应时间：45ms ✓
  • 数据库查询：已优化 ✓

🔒 安全
  • 密码存储：使用bcrypt ✓
  • SQL注入：已防护 ✓
  • XSS：已防护 ✓

[总结]
质量评分：85/100

主要改进点：
1. 添加代码注释（5分钟）
2. 提取验证逻辑（10分钟）

要我帮你改进这两点吗？
```

---

## 🔗 技能组合模式

### 场景化组合

#### 紧急修复场景

```python
context_weaver + rhythm_awareness + intent_decoding + quality_guardian
```

**组合原因**：
- 紧急情况需要快速恢复上下文
- 需要感知用户的紧迫状态
- 需要准确理解问题所在
- 需要确保修复质量

#### 创意探索场景

```python
context_weaver + intent_decoding + knowledge_knitting + solution_architect
```

**组合原因**：
- 需要理解用户的创意需求
- 需要探索多种可能性
- 需要调用历史知识
- 需要设计整体方案

#### 深度开发场景

```python
context_weaver + rhythm_awareness + adaptive_executor + quality_guardian
```

**组合原因**：
- 需要持续维护上下文
- 需要感知工作节奏
- 需要智能执行任务
- 需要保证交付质量

---

## 📊 技能矩阵

| 技能 | 类型 | 核心功能 | 依赖 |
|------|------|----------|------|
| ContextWeaver | 感知 | 上下文编织 | 无 |
| RhythmAwareness | 感知 | 节奏感知 | ContextWeaver |
| IntentDecoding | 感知 | 意图解码 | ContextWeaver |
| KnowledgeKnitting | 认知 | 知识管理 | ContextWeaver |
| SolutionArchitect | 认知 | 方案设计 | IntentDecoding |
| AdaptiveExecutor | 行动 | 任务执行 | ContextWeaver, RhythmAwareness |
| QualityGuardian | 行动 | 质量把控 | ContextWeaver |

---

**核心技能构成了SoloSkills的智能基础，让AI真正成为用户的协作伙伴！** 🎯
