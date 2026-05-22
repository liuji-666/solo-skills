# SoloSkills 使用教程

## 📖 基本使用

### Python API

#### 1. 初始化

```python
from soloskills import SoloSkills

# 创建实例
solo = SoloSkills()

# 或指定配置
solo = SoloSkills(config_path=".soloskills/config.yml")
```

#### 2. 对话交互

```python
# 基本对话
result = solo.interact("帮我开始一个新任务")

# 带项目上下文
result = solo.interact(
    "代码出问题了",
    project_context={
        "path": "/project/auth",
        "type": "web",
        "files": ["auth/login.ts", "auth/register.ts"]
    }
)

# 查看结果
print(result['scenario'])  # 场景类型
print(result['message'])   # SoloSkills 响应
print(result['suggestions'])  # 建议
```

#### 3. 场景切换

```python
# 检测当前场景
print(solo.current_scenario)

# 手动切换场景
from soloskills.core import ScenarioType
solo.current_scenario = ScenarioType.DEBUG
```

#### 4. 上下文管理

```python
# 查看当前上下文
print(solo.context.project_path)
print(solo.context.task_progress)
print(solo.context.conversation_history)

# 更新上下文
solo.context.task_progress = 0.75
solo.context.decisions.append({
    "type": "auth_method",
    "decision": "使用JWT"
})

# 保存状态
solo.save_state()

# 加载状态
solo.load_state()
```

#### 5. 知识图谱

```python
# 添加知识
node_id = solo.knowledge_graph.add(
    content="用户登录使用JWT认证",
    node_type="technical_decision",
    metadata={"date": "2024-01-01"}
)

# 查询知识
results = solo.knowledge_graph.query("登录")

# 遍历结果
for node in results:
    print(node.content)
    print(node.type)
    print(node.metadata)
```

### CLI 工具

#### 基本命令

```bash
# 初始化项目
soloskills init

# 查看状态
soloskills status

# 切换场景
soloskills scenario debug
```

#### 交互模式

```bash
# 进入交互模式
soloskills interact "帮我开始"

# 交互式对话
soloskills
# 然后输入你的消息
```

#### 上下文管理

```bash
# 查看上下文
soloskills context show

# 保存上下文
soloskills context save

# 加载上下文
soloskills context load

# 重建上下文
soloskills context rebuild
```

#### 知识管理

```bash
# 查询知识库
soloskills learn --query "登录"

# 查看统计
soloskills learn
```

## 🎯 场景使用

### 热启动场景

当您开始新工作或恢复中断时：

```python
# 使用场景
result = solo.interact("开始一个新任务")

# 响应示例
# {
#     'scenario': 'ignite',
#     'message': '🔥 好的，让我帮你准备开始工作！',
#     'steps': [
#         {'step': 1, 'name': '检查上下文', 'status': 'in_progress'},
#         {'step': 2, 'name': '评估状态', 'status': 'pending'},
#         {'step': 3, 'name': '准备开始', 'status': 'pending'}
#     ],
#     'suggestions': ['继续上次的工作', '开始一个新任务', '查看项目状态']
# }
```

### 调试突破场景

当您遇到Bug或错误时：

```python
# 使用场景
result = solo.interact("代码报错了")

# 响应示例
# {
#     'scenario': 'debug',
#     'message': '🔧 发现问题了，让我帮你诊断！',
#     'steps': [
#         {'step': 1, 'name': '问题复现', 'status': 'in_progress'},
#         {'step': 2, 'name': '假设验证', 'status': 'pending'},
#         {'step': 3, 'name': '根因定位', 'status': 'pending'},
#         {'step': 4, 'name': '修复实施', 'status': 'pending'},
#         {'step': 5, 'name': '回归验证', 'status': 'pending'}
#     ],
#     'suggestions': ['描述具体的错误信息', '分享相关的代码片段', '运行测试看看']
# }
```

### 灵感触发场景

当您需要创意或探索新方案时：

```python
# 使用场景
result = solo.interact("有没有更好的认证方案？")

# 响应示例
# {
#     'scenario': 'spark',
#     'message': '💡 想探索新想法？让我帮你打开思路！',
#     'techniques': [
#         {'name': '抽象化', 'description': '用更高层的语言描述问题'},
#         {'name': '类比迁移', 'description': '借用其他领域的解决方案'},
#         {'name': '反向思考', 'description': '从结果倒退原因'}
#     ],
#     'suggestions': ['换个角度思考', '参考类似的解决方案', '先实现最小可行版本']
# }
```

### 交付冲刺场景

当您需要快速交付时：

```python
# 使用场景
result = solo.interact("准备冲刺交付")

# 响应示例
# {
#     'scenario': 'sprint',
#     'message': '🚀 准备冲刺交付！让我们高效完成！',
#     'focus_areas': [
#         {'area': '核心功能', 'priority': 1},
#         {'area': '基本测试', 'priority': 2},
#         {'area': '必要文档', 'priority': 3}
#     ],
#     'time_boxes': [
#         {'task': '核心功能', 'time': '50% 时间'},
#         {'task': '测试验证', 'time': '30% 时间'},
#         {'task': '文档准备', 'time': '20% 时间'}
#     ]
# }
```

### 优雅收尾场景

当您结束工作时：

```python
# 使用场景
result = solo.interact("今天先到这里")

# 响应示例
# {
#     'scenario': 'wrap',
#     'message': '🌙 好的，我们来做个收尾。',
#     'summary_template': {
#         'completed': '已完成的工作',
#         'in_progress': '进行中的工作',
#         'next_steps': '下一步计划',
#         'learned': '学到的经验'
#     },
#     'handoff_checklist': [
#         {'item': '代码已提交', 'status': 'pending'},
#         {'item': '测试已通过', 'status': 'pending'},
#         {'item': '文档已更新', 'status': 'pending'},
#         {'item': '进度已记录', 'status': 'pending'}
#     ]
# }
```

## ⚙️ 配置

### 默认配置

```yaml
version: "1.0.0"

user:
  name: "开发者"
  expertise: "intermediate"  # beginner | intermediate | expert

collaboration:
  help_level: "伙伴"  # 观察者 | 助手 | 伙伴 | 专家 | 导师
  communication_style: "balanced"  # concise | balanced | detailed

scenarios:
  enabled:
    - ignite
    - debug
    - spark
    - sprint
    - wrap
  default: "ignite"

context:
  auto_save: true
  save_interval: 300  # seconds
  max_history: 100
```

### 自定义配置

创建 `.soloskills/config.yml`：

```yaml
user:
  name: "张三"
  expertise: "expert"

collaboration:
  help_level: "专家"
  communication_style: "concise"

scenarios:
  default: "debug"
```

## 🧪 高级用法

### 自定义场景

```python
from soloskills.core import Scenario, ScenarioType

class MyScenario(Scenario):
    def __init__(self):
        super().__init__("我的场景", ScenarioType.IGNITE)
    
    def execute(self, context, user_input):
        return {
            "message": "执行自定义场景",
            "custom_data": {}
        }

# 注册场景
solo = SoloSkills()
solo.scenarios[ScenarioType.IGNITE] = MyScenario()
```

### 自定义技能

```python
from soloskills.skills import ContextWeaver

class MyContextWeaver(ContextWeaver):
    def weave(self, context, trigger=None):
        # 自定义逻辑
        result = super().weave(context, trigger)
        # 添加自定义处理
        result['custom_field'] = "custom_value"
        return result

# 使用
weaver = MyContextWeaver()
result = weaver.weave(solo.context)
```

### 事件钩子

```python
# 在交互前后执行自定义逻辑
def before_interact(solo, user_input):
    print(f"用户输入: {user_input}")

def after_interact(solo, result):
    print(f"响应场景: {result['scenario']}")

# 注册钩子
solo.before_interact = before_interact
solo.after_interact = after_interact
```

## 📊 示例代码

更多示例请参考：

- [基础演示](../examples/demo.py)
- [完整演示](../examples/complete_demo.py)

## 🎓 最佳实践

1. **定期保存状态**
   ```python
   solo.save_state()
   ```

2. **使用项目上下文**
   ```python
   solo.interact("开始", project_context={"path": "/project", "type": "web"})
   ```

3. **利用知识图谱**
   ```python
   solo.knowledge_graph.add("重要信息", "经验")
   ```

4. **根据场景调整期望**
   - 调试场景：详细诊断
   - 冲刺场景：快速交付
   - 收尾场景：完整记录

## ❓ 常见问题

### Q: 如何切换默认场景？

A: 在配置文件中设置：

```yaml
scenarios:
  default: "debug"
```

### Q: 如何禁用某个场景？

A: 在配置文件中：

```yaml
scenarios:
  enabled:
    - ignite
    - debug
    # - spark  # 注释掉即可禁用
    - sprint
    - wrap
```

### Q: 如何导出知识图谱？

A:

```python
solo.knowledge_graph.save()
# 保存到 .soloskills/knowledge.json
```

---

**需要帮助？** 查看 [GitHub Issues](https://github.com/yourusername/soloskills/issues)
