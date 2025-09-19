# FastAPI 基础项目模板

这是一个基于 FastAPI 开发的后端接口模块，提供了一个完整的项目基础架构，可用于快速克隆搭建新项目，也适合用于学习 FastAPI 开发。

## 🚀 项目特性

- **FastAPI 框架**: 高性能的现代 Python Web 框架
- **Tortoise ORM**: 异步 ORM，支持 MySQL 数据库
- **Pydantic 数据验证**: 自动数据验证和序列化
- **模块化设计**: 清晰的项目结构，易于扩展
- **异常处理**: 统一的异常处理机制
- **自动化测试**: 完整的测试框架
- **完全容器化**: 本地开发和生产部署均在容器中运行，保证环境一致性
- **开发环境隔离**: 每个开发者拥有独立的容器化开发环境
- **代码热更新**: 本地代码映射到容器，修改即时生效
- **日志系统**: 基于 Loguru 的日志管理

## 📁 项目结构

```
baseproject/
├── app.py                 # 应用核心类和异常处理
├── index.py               # FastAPI 应用入口
├── main.py                # 测试运行入口
├── debug_build.sh         # 本地容器化开发启动脚本 ⭐
├── build-docker.sh        # Docker 镜像构建脚本
├── unittest.sh            # 完整测试套件脚本 ⭐
├── _delete_tables.py      # 数据库表重置脚本
├── config/
│   └── config.json        # 配置文件
├── lib/
│   └── singleton.py       # 单例模式装饰器
├── models/
│   ├── __init__.py        # 数据库初始化和分页
│   ├── models.py          # 数据模型定义
│   ├── fields.py          # 自定义字段类型
│   └── exceptions.py      # 模型异常类
├── router/
│   ├── autoload.py        # 路由自动加载
│   ├── base.py            # 基础路由装饰器和上下文
│   └── tag.py             # 标签相关 API
├── schema/
│   ├── base.py            # 基础数据模式
│   ├── config.py          # 配置数据模式
│   └── tag.py             # 标签数据模式
├── test/
│   ├── __init__.py        # 测试工具函数
│   └── test_tag.py        # 标签 API 测试
├── docker/
│   ├── Dockerfile         # Docker 镜像构建
│   └── requirements.txt   # Python 依赖
├── docker-compose.yaml    # Docker Compose 服务配置
└── conftest.py           # pytest 配置
```

## 🛠 技术栈

- **Python 3.9+**
- **FastAPI 0.85.0** - 现代高性能 Web 框架
- **Tortoise ORM 0.19.2** - 异步 ORM
- **Pydantic 1.10.2** - 数据验证
- **Uvicorn 0.18.3** - ASGI 服务器
- **MySQL 5.7** - 数据库
- **Loguru 0.6.0** - 日志系统
- **Pytest 7.1.3** - 测试框架

## 🚀 快速开始

### 🎯 核心理念：完全容器化开发

本项目采用完全容器化的开发模式，确保本地开发环境与生产环境的完全一致性：
- ✅ **环境一致性**: 本地开发和生产部署使用相同的容器环境
- ✅ **开发隔离**: 每个开发者拥有独立的容器化环境，互不干扰
- ✅ **代码同步**: 本地代码目录映射到容器，修改实时生效
- ✅ **服务集成**: 通过 Docker Compose 统一管理应用和依赖服务

### 1. 环境准备

确保您的系统已安装：
- **Docker** 和 **Docker Compose** (必须)
- Git (用于克隆项目)

> ⚠️ **注意**: 无需安装 Python 或其他依赖，一切都在容器中运行！

### 2. 克隆项目

```bash
git clone <repository-url>
cd baseproject
```

### 3. 启动容器化开发环境

使用项目提供的开发脚本：

```bash
# 首次运行（构建镜像 + 启动开发环境）
./debug_build.sh --build

# 后续运行（直接启动，无需重新构建）
./debug_build.sh
```

### 4. 开发环境详解

`debug_build.sh` 脚本会自动完成以下操作：

1. **构建应用镜像** (仅在使用 `--build` 参数时)
2. **启动依赖服务** (MySQL、phpMyAdmin 等)
3. **创建开发容器** 并进入交互式 bash
4. **映射本地代码** 到容器的 `/app` 目录
5. **配置网络** 让容器间可以互相访问

### 5. 在容器中运行应用

进入开发容器后，执行：

```bash
# 在容器中运行应用
python index.py
```

### 6. 访问服务

- **FastAPI 应用**: `http://localhost:8952`
- **API 文档 (Swagger)**: `http://localhost:8952/docs`
- **API 文档 (ReDoc)**: `http://localhost:8952/redoc`
- **phpMyAdmin**: `http://localhost:8927`

### 7. 开发工作流

```bash
# 1. 启动开发环境
./debug_build.sh

# 2. 在容器中运行应用
python index.py

# 3. 在另一个终端修改本地代码
# 代码修改会自动同步到容器中

# 4. 在容器中运行完整测试套件
./unittest.sh

# 或运行特定测试
pytest test/test_tag.py -v

# 5. 退出容器时，依赖服务会自动停止
exit
```

## 📝 API 接口

项目提供了完整的标签管理 API 作为示例：

### 标签管理 API

| 方法 | 路径 | 描述 |
|------|------|------|
| POST | `/tag/add` | 添加标签 |
| POST | `/tag/edit` | 修改标签 |
| POST | `/tag/remove` | 删除标签 |
| POST | `/tag/search` | 搜索标签 |

### 请求示例

**添加标签**
```bash
curl -X POST "http://localhost:8952/tag/add" \
     -H "Content-Type: application/json" \
     -H "x-forwarded-for-zl: 192.168.1.1" \
     -H "x-current-user-id: 1" \
     -H "x-current-username: admin" \
     -d '{"name": "Python"}'
```

**搜索标签**
```bash
curl -X POST "http://localhost:8952/tag/search" \
     -H "Content-Type: application/json" \
     -H "x-forwarded-for-zl: 192.168.1.1" \
     -H "x-current-user-id: 1" \
     -H "x-current-username: admin" \
     -d '{"page": 1, "page_size": 10, "keyword": ""}'
```

## 🧪 测试

### 容器化测试环境

所有测试都在容器环境中运行，确保测试环境的一致性：

```bash
# 1. 启动开发环境
./debug_build.sh

# 2. 在容器中运行完整测试套件（推荐）
./unittest.sh

# 或者分步执行：
# 2a. 重置数据库（删除所有表，让 ORM 重新创建）
python _delete_tables.py

# 2b. 运行所有测试用例
python main.py

# 3. 或使用 pytest 运行特定测试
pytest test/test_tag.py -v -s          # 运行单个测试文件
pytest test/test_tag.py::test_add_1 -v # 运行单个测试用例
pytest -k "add" -v                     # 运行包含 "add" 的测试
```

### 测试流程详解

#### `unittest.sh` 完整测试流程
1. **数据库重置** (`_delete_tables.py`):
   - 删除所有外键约束
   - 删除数据库中的所有表
   - 让 Tortoise ORM 根据模型定义重新创建表结构

2. **运行测试** (`main.py`):
   - 执行所有测试用例
   - 每个测试用例都有独立的数据环境

#### 为什么要重置数据库？
- 🔄 **表结构同步**: 开发过程中模型定义经常变更，重置确保表结构是最新的
- 🧹 **数据清理**: 确保测试数据不会相互影响
- ⚡ **开发效率**: 避免手动管理数据库迁移，提高开发效率
- ✅ **测试可靠性**: 每次测试都从干净的数据库状态开始

### 测试特性

- ✅ **异步测试**: 支持 FastAPI 异步特性
- ✅ **数据库重置**: 自动重置数据库结构和数据
- ✅ **API 测试**: 完整的 HTTP 客户端测试
- ✅ **隔离测试**: 每个测试用例数据独立
- ✅ **灵活运行**: 支持全量测试和单个测试用例运行

## 🐳 生产部署

### 构建生产镜像

```bash
# 构建生产镜像
./build-docker.sh

# 或指定镜像标签
./build-docker.sh -t myapp:v1.0.0
```

### 生产环境配置

1. **修改配置文件** - 将 `config/config.json` 中的配置改为生产环境配置
2. **构建镜像** - 使用 `build-docker.sh` 构建生产镜像
3. **部署运行** - 使用容器编排工具部署

### Docker Compose 部署示例

```bash
# 启动所有服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

当前 Docker Compose 包含的服务：
- **MySQL 5.7**: 数据库服务 (端口 3306)
- **phpMyAdmin**: 数据库管理界面 (端口 8927)

> 💡 **提示**: 生产环境建议移除 phpMyAdmin 服务，并使用外部数据库

## 🔧 核心功能

### 1. 统一异常处理

系统提供了统一的异常处理机制：

- **MyException**: 自定义业务异常
- **ModelException**: 模型层异常
- **422 错误处理**: 参数验证错误的中文化处理

### 2. 数据库模型

基于 Tortoise ORM 的数据模型：

- **BaseModel**: 基础模型类，包含 ID 和创建时间
- **TagModel**: 标签模型示例
- **自定义字段**: TimestampField, MyCharField 等

### 3. 数据验证

使用 Pydantic 进行数据验证：

- **RestfulModel**: 统一的 API 响应格式
- **分页支持**: 内置分页功能
- **类型安全**: 强类型数据验证

### 4. 路由管理

模块化的路由管理：

- **自动加载**: 路由自动注册机制
- **装饰器**: 统一的错误处理装饰器
- **上下文**: 请求上下文管理

### 5. 配置管理

灵活的配置系统：

- **JSON 配置**: 易于修改的配置文件
- **类型验证**: 配置项类型验证
- **单例模式**: 配置对象单例管理

## 🔄 容器化开发的优势

### 环境一致性保障
- **开发 = 测试 = 生产**: 所有环境使用相同的容器镜像
- **依赖锁定**: 容器内的 Python 版本、库版本完全一致
- **系统隔离**: 避免本地环境污染和冲突

### 团队协作优势
- **快速上手**: 新成员只需 `./debug_build.sh --build` 即可开始开发
- **环境独立**: 每个开发者的数据库、缓存等服务完全隔离
- **配置统一**: 通过 Docker Compose 统一管理服务配置

### 开发效率提升
- **热更新**: 代码修改实时同步到容器，无需重启
- **服务集成**: 数据库、缓存等服务一键启动
- **端口管理**: 自动分配端口，避免冲突

## 📈 扩展开发

### 添加新的依赖服务

在 `docker-compose.yaml` 中添加新服务：

```yaml
services:
  redis:
    image: redis:6.2-alpine
    ports:
      - "6379"
    networks:
      - dev_net
  
  minio:
    image: minio/minio
    ports:
      - "9000"
      - "9001"
    environment:
      - MINIO_ROOT_USER=minioadmin
      - MINIO_ROOT_PASSWORD=minioadmin
    command: server /data --console-address ":9001"
    networks:
      - dev_net
```

### 添加新的 API 模块

1. **创建模型** (`models/models.py`):
```python
class YourModel(BaseModel):
    name = MyCharField(100, null=False, description="名称")
    # 其他字段...

    class Meta:
        table = "your_table"
```

2. **创建数据模式** (`schema/your_module.py`):
```python
from pydantic import BaseModel, Field

class Add(BaseModel):
    name: str = Field("", title="名称")

class Edit(Add):
    id: int = Field(title="ID")
```

3. **创建路由** (`router/your_module.py`):
```python
from fastapi import APIRouter
from router.base import decorator
from schema import your_module

router = APIRouter()

@router.post("/your-module/add", tags=["your-module"])
@decorator
async def add(param: your_module.Add):
    # 实现逻辑
    return {"result": 1}
```

4. **注册路由** (`router/autoload.py`):
```python
from . import your_module

routers = [
    tag.router,
    your_module.router,  # 添加新路由
]
```

## 🔍 开发工具

### 代码规范

项目使用 Ruff 进行代码格式化和检查：

```bash
ruff check .
ruff format .
```

### 数据库管理

访问 phpMyAdmin: `http://localhost:8927`
- 用户名: root
- 密码: 123456

### 日志查看

日志配置在 `config/config.json` 中，支持：
- 日志级别设置
- 日志轮转
- 日志压缩
- 自定义日志路径

## 🆘 常见问题

### 容器化开发相关

**Q: 首次运行 `debug_build.sh --build` 很慢？**
A: 首次构建需要下载 Python 镜像和安装依赖，后续运行会很快。可以考虑使用国内镜像源。

**Q: 代码修改后没有生效？**
A: 确保代码是映射到容器的，检查容器内 `/app` 目录是否有最新代码。如果是 Python 缓存问题，可以删除 `__pycache__` 目录。

**Q: 端口被占用怎么办？**
A: 修改 `debug_build.sh` 中的 `port=8952` 为其他端口，或者停止占用端口的服务。

**Q: 容器无法连接数据库？**
A: 确保 `config/config.json` 中的 MySQL host 配置为 `mysql`（容器名），而不是 `localhost`。

### 开发配置相关

**Q: 如何修改数据库连接？**
A: 编辑 `config/config.json` 中的 `mysql` 配置项。注意容器环境中 host 应为服务名 `mysql`。

**Q: 如何添加新的数据表？**
A: 在 `models/models.py` 中定义新模型，系统会自动创建表结构。

**Q: 如何自定义异常处理？**
A: 继承 `MyException` 类或在 `index.py` 中添加新的异常处理器。

**Q: 如何进行性能优化？**
A: 可以调整 `config.json` 中的 `workers` 数量，使用数据库连接池等。

### 部署相关

**Q: 如何切换到生产环境？**
A: 修改 `config/config.json` 配置，构建生产镜像，使用容器编排工具部署。

**Q: 生产环境如何管理配置？**
A: 建议使用环境变量或配置管理系统，避免将敏感信息写入镜像。

---

**享受使用 FastAPI 进行开发！** 🎉