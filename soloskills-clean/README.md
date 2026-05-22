# SoloSkills for Trae Solo

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="license">
  <img src="https://img.shields.io/badge/python-3.8+-yellow.svg" alt="python">
  <img src="https://img.shields.io/badge/platform-Trae's Solo-purple.svg" alt="platform">
</p>

<p align="center">
  <h2 align="center">🚀 重新定义AI与人类的协作方式</h2>
</p>

> **"不是又一个技能库，而是一套让AI真正懂你的协作协议"**

SoloSkills 是一个专为 Trae Solo 设计的原生技能系统，通过场景驱动、上下文感知和知识编织，让AI从"工具"进化为真正的"工作伙伴"。

---

## ✨ 核心特性

### 🎯 场景驱动设计

不是按功能分类，而是按**真实工作场景**组织：

| 🔥 热启动 | 💡 灵感触发 | 🔧 调试突破 | 🚀 交付冲刺 | 🌙 优雅收尾 |
|:--------:|:----------:|:-----------:|:-----------:|:-----------:|
| 快速开始 | 打破思维 | 系统诊断 | 高效交付 | 完美收尾 |

### 🧠 智能协作

- **上下文感知**: 自动维护项目、任务、对话多维度上下文
- **节奏感知**: 理解你的工作状态，动态调整交互方式
- **知识积累**: 跨会话学习，建立个人知识图谱
- **意图理解**: 不仅仅理解你说的，更理解你真正想要的

### 🚀 开箱即用

```python
from soloskills import SoloSkills

# 初始化
solo = SoloSkills()

# 直接对话，无需配置
result = solo.interact("帮我开始一个新任务")

# SoloSkills 自动：
# → 检测场景（热启动）
# → 加载上下文
# → 提供帮助
```

---

## 📦 快速开始

### 安装

```bash
# 方式1: pip安装
pip install soloskills

# 方式2: 直接使用源码
git clone https://github.com/yourusername/soloskills.git
cd soloskills
python -m src.soloskills.cli
```

### 使用

#### Python API

```python
from soloskills import SoloSkills

# 创建实例
solo = SoloSkills()

# 对话
result = solo.interact("代码出问题了")
print(result['message'])
print(result['suggestions'])
```

#### CLI工具

```bash
# 初始化项目
soloskills init

# 查看状态
soloskills status

# 切换场景
soloskills scenario debug

# 交互模式
soloskills interact "帮我开始"

# 上下文管理
soloskills context show
soloskills context save

# 知识查询
soloskills learn --query "登录"
```

#### Trae Solo 集成

直接在 Trae Solo 中使用自然语言：

```
"帮我开始一个新任务"      → 热启动场景
"代码出问题了"           → 调试突破场景
"有没有更好的方案？"      → 灵感触发场景
"准备冲刺交付"            → 交付冲刺场景
"今天先到这里"            → 优雅收尾场景
```

---

## 🎯 使用场景

### 场景1: 热启动 (Ignite)

**适用**: 开始新会话、恢复中断、切换任务

```
用户：继续上次的工作
SoloSkills：
  ✓ 检测场景：热启动
  ✓ 加载上次上下文
  ✓ 恢复任务进度
  → "好的，你上次在实现登录功能，完成度65%"
```

### 场景2: 调试突破 (Debug)

**适用**: Bug、错误、功能不工作

```
用户：代码报错了
SoloSkills：
  ✓ 检测场景：调试突破
  ✓ 激活诊断流程
  ✓ 提供系统化方法
  → "让我帮你诊断，请描述具体错误"
```

### 场景3: 灵感触发 (Spark)

**适用**: 需要创意、遇到瓶颈、想探索方案

```
用户：有没有更好的认证方案？
SoloSkills：
  ✓ 检测场景：灵感触发
  ✓ 激活创意生成
  ✓ 提供多角度思考
  → "让我从几个角度帮你分析..."
```

---

## 🏗️ 项目结构

```
soloskills/
├── src/
│   └── soloskills/
│       ├── __init__.py         # 包初始化
│       ├── core.py             # 核心引擎
│       ├── scenarios.py         # 场景实现
│       ├── skills.py           # 技能实现
│       └── cli.py              # CLI工具
├── examples/
│   ├── demo.py                # 基础演示
│   └── complete_demo.py       # 完整演示
├── docs/                       # 文档
│   ├── INSTALL.md             # 安装指南
│   ├── USAGE.md               # 使用教程
│   ├── SCENARIOS.md           # 场景详解
│   ├── CORE_SKILLS.md         # 技能详解
│   └── ANALYSIS.md            # 深度分析
├── README.md                   # 本文档
├── LICENSE                     # 许可证
└── CONTRIBUTING.md            # 贡献指南
```

---

## 📚 文档

- [📖 完整文档](./docs/)
- [🎯 场景系统详解](./docs/SCENARIOS.md)
- [🧠 核心技能详解](./docs/CORE_SKILLS.md)
- [🚀 安装指南](./docs/INSTALL.md)
- [💡 使用教程](./docs/USAGE.md)
- [🔍 深度分析](./docs/ANALYSIS.md)

---

## 🎓 与其他系统的区别

| 特性 | Matt Pocock Skills | SoloSkills |
|------|-------------------|------------|
| **组织方式** | 功能分类 | 场景分类 |
| **触发方式** | 手动调用 | 自动检测 |
| **上下文** | 每次重置 | 自动维护 |
| **学习能力** | ❌ | ✅ 知识图谱 |
| **节奏感知** | ❌ | ✅ 动态调整 |
| **集成方式** | 需要插件 | 原生集成 |

---

## 🤝 贡献

欢迎贡献代码！

1. **Fork** 项目
2. **Clone** 你的 fork: `git clone https://github.com/YOUR_USERNAME/soloskills.git`
3. **创建分支**: `git checkout -b feature/amazing-feature`
4. **开发**: 实现你的功能
5. **测试**: 确保通过所有测试
6. **提交**: `git commit -m "feat: add amazing feature"`
7. **Push**: `git push origin feature/amazing-feature`
8. **Pull Request**: 在 GitHub 创建 PR

详见 [CONTRIBUTING.md](./CONTRIBUTING.md)

---

## 📈 发展路线

- [x] v1.0: 核心框架和5大场景
- [ ] v1.1: Trae Solo 插件集成
- [ ] v1.2: 知识图谱增强
- [ ] v2.0: 团队协作功能
- [ ] v2.1: 多语言支持

详见 [ROADMAP.md](./ROADMAP.md)

---

## 📄 许可证

本项目采用 [MIT License](./LICENSE) 许可证。

---

## 🙏 致谢

- 灵感来源: [Matt Pocock Skills](https://github.com/mattpocock/skills)
- 设计参考: 各种AI协作系统和工程实践

---

## 💬 联系方式

- GitHub Issues: [报告问题](https://github.com/yourusername/soloskills/issues)
- 邮箱: your.email@example.com

---

<p align="center">
  <strong>让AI成为真正的伙伴，而不仅仅是工具</strong>
  <br>
  Made with ❤️ for Trae Solo
</p>
