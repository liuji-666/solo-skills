# 贡献指南

感谢您对 SoloSkills 的兴趣！我们欢迎各种形式的贡献。

## 🤝 如何贡献

### 报告问题

如果您发现bug或有功能建议，请：

1. 搜索现有的 [issues](https://github.com/yourusername/soloskills/issues) 确保没有重复
2. 创建一个新的 issue
3. 使用问题模板（如果适用）
4. 提供详细信息：
   - 清晰的标题和描述
   - 复现步骤
   - 预期行为 vs 实际行为
   - 环境信息（Python版本、操作系统等）

### 提交代码

#### 开发流程

1. **Fork** 项目
2. **Clone** 你的 fork：
   ```bash
   git clone https://github.com/YOUR_USERNAME/soloskills.git
   cd soloskills
   ```
3. **创建分支**：
   ```bash
   git checkout -b feature/amazing-feature
   # 或
   git checkout -b fix/annoying-bug
   ```
4. **设置开发环境**：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
5. **开发**：实现你的功能或修复
6. **测试**：确保通过所有测试
7. **提交**：使用清晰的消息格式
8. **Push**：推送到你的 fork
9. **PR**：创建 Pull Request

#### 提交消息格式

我们遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

类型：
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档变更
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建/工具相关

示例：
```
feat(scenarios): add new spark scenario for ideation

Add the Spark scenario to help users when they need creative
inspiration or want to explore alternative approaches.

Closes #123
```

### 代码规范

#### Python 代码

- 遵循 [PEP 8](https://pep8.org/)
- 使用类型提示
- 编写 docstring
- 每个文件开头顶部添加：

```python
#!/usr/bin/env python3
"""
模块名称 - 简短描述

详细描述（如果需要）。
"""
```

#### 文档

- 使用清晰的标题和描述
- 提供代码示例
- 更新相关文档

#### 测试

- 为新功能添加测试
- 确保所有测试通过
- 保持测试覆盖率高

```python
import pytest
from soloskills import SoloSkills

def test_basic_interaction():
    """测试基本交互功能"""
    solo = SoloSkills()
    result = solo.interact("开始一个新任务")
    
    assert result is not None
    assert 'scenario' in result
    assert result['scenario'] == 'ignite'
```

## 📋 开发任务

### 标签说明

- `good first issue`: 适合新手
- `help wanted`: 需要帮助
- `bug`: Bug 修复
- `enhancement`: 功能增强
- `documentation`: 文档改进
- `question`: 问题/讨论

### 优先任务

我们会在 issue 中标记优先级：

- `P0`: 立即处理
- `P1`: 高优先级
- `P2`: 正常优先级
- `P3`: 低优先级

## 🧪 测试

### 运行测试

```bash
# 运行所有测试
pytest tests/

# 运行特定测试
pytest tests/test_core.py

# 带覆盖率
pytest --cov=soloskills tests/

# 带详细输出
pytest -v tests/
```

### 测试覆盖

我们使用 [pytest-cov](https://pytest-cov.readthedocs.io/)：

```bash
pytest --cov=soloskills --cov-report=html tests/
# 查看 htmlcov/index.html
```

## 📝 文档

### 更新文档

如果您的更改影响用户：

- 更新 README.md
- 添加/更新使用示例
- 在 CHANGELOG.md 中记录

### 文档格式

使用 Markdown，支持：

- 代码块（带语言标注）
- 表格
- 列表
- 链接

## 🔍 代码审查

### PR 要求

在创建 PR 之前：

- [ ] 代码遵循项目规范
- [ ] 添加了测试（如适用）
- [ ] 所有测试通过
- [ ] 文档已更新
- [ ] 提交消息清晰

### 审查流程

1. 自动化检查必须通过
2. 至少1人审查
3. 所有讨论解决
4. 维护者批准合并

## 📜 许可证

通过贡献代码，您同意将您的作品以 [MIT License](./LICENSE) 发布。

## 🙏 感谢

每个贡献都很重要！感谢您的时间。

---

**问题？** 欢迎在 [GitHub Discussions](https://github.com/yourusername/soloskills/discussions) 中提问。
