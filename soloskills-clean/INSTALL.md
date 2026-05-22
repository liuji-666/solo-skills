# SoloSkills 安装指南

## 📦 环境要求

- Python 3.8 或更高版本
- pip (Python 包管理器)

## 🚀 安装方式

### 方式1: pip 安装（推荐）

```bash
pip install soloskills
```

### 方式2: 源码安装（开发版）

```bash
# 克隆仓库
git clone https://github.com/yourusername/soloskills.git
cd soloskills

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 安装依赖
pip install -e .

# 或安装所有依赖
pip install -r requirements.txt
```

### 方式3: 直接使用

如果您不想安装，可以直接使用源码：

```bash
# 克隆仓库
git clone https://github.com/yourusername/soloskills.git
cd soloskills

# 直接运行
python -m src.soloskills.cli
```

## 📋 依赖项

### 必需依赖

```
- Python >= 3.8
- PyYAML >= 6.0
```

### 可选依赖

```
- pytest >= 7.0  # 测试
- pytest-cov >= 4.0  # 覆盖率
- black >= 23.0  # 代码格式化
- mypy >= 1.0  # 类型检查
```

## ✅ 验证安装

安装完成后，验证是否成功：

```bash
# 检查版本
soloskills --version

# 或
python -c "import soloskills; print(soloskills.__version__)"
```

## 🛠️ 开发环境设置

如果您想参与开发：

```bash
# 1. Fork 并克隆
git clone https://github.com/YOUR_USERNAME/soloskills.git
cd soloskills

# 2. 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 3. 安装开发依赖
pip install -e ".[dev]"

# 4. 安装pre-commit钩子
pip install pre-commit
pre-commit install

# 5. 运行测试
pytest tests/

# 6. 代码格式化
black src/

# 7. 类型检查
mypy src/
```

## 🐳 Docker 支持

使用 Docker：

```bash
# 构建镜像
docker build -t soloskills .

# 运行
docker run -it soloskills

# 进入shell
docker run -it soloskills /bin/bash
```

使用 docker-compose：

```bash
# 启动
docker-compose up

# 后台运行
docker-compose up -d

# 停止
docker-compose down
```

## 📦 requirements.txt

如果需要手动安装依赖：

```
PyYAML>=6.0
```

开发依赖：

```
-r requirements.txt
pytest>=7.0
pytest-cov>=4.0
black>=23.0
mypy>=1.0
pre-commit>=3.0
```

## 🔧 故障排除

### 问题：ImportError: No module named 'soloskills'

解决方案：

1. 确保已正确安装：
   ```bash
   pip install soloskills
   ```

2. 如果从源码运行，确保在项目根目录：
   ```bash
   cd /path/to/soloskills
   export PYTHONPATH="${PWD}/src:${PYTHONPATH}"
   ```

### 问题：Permission denied

在 Linux/Mac 上使用 `pip install` 时可能需要 sudo：

```bash
sudo pip install soloskills
```

或者使用 `--user` 安装到用户目录：

```bash
pip install --user soloskills
```

### 问题：Python 版本不兼容

SoloSkills 需要 Python 3.8+：

```bash
# 检查 Python 版本
python --version

# 如果需要，升级 Python
# Ubuntu:
sudo apt-get update
sudo apt-get install python3.8

# macOS:
brew install python@3.8
```

## 🎯 下一步

安装成功后，开始使用：

- [快速开始](../README.md#快速开始)
- [使用教程](./USAGE.md)
- [示例](../examples/)
