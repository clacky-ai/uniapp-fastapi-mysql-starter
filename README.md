# 电商管理系统

基于 FastAPI + MySQL + UniApp 构建的全栈电商管理系统脚手架。

## 🏗️ 项目架构

```
├── backend/              # FastAPI 后端
│   ├── app/
│   │   ├── api/         # API 路由
│   │   ├── core/        # 核心配置
│   │   ├── crud/        # 数据库操作
│   │   ├── db/          # 数据库连接
│   │   ├── models/      # 数据模型
│   │   └── schemas/     # Pydantic 模式
│   └── requirements.txt
├── frontend/            # UniApp 前端
│   ├── src/
│   │   ├── pages/      # 页面组件
│   │   ├── utils/      # 工具函数
│   │   └── static/     # 静态资源
│   └── package.json
├── database/           # 数据库脚本
├── scripts/           # 部署脚本
└── logs/             # 日志文件
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Node.js 16+
- MySQL 8.0+

### 1. 克隆项目

```bash
git clone <repository-url>
cd ecommerce-scaffold
```

### 2. 数据库配置

创建数据库：
```bash
mysql -h 127.0.0.1 -u root -p -e "CREATE DATABASE ecommerce_db;"
```

导入初始数据：
```bash
mysql -h 127.0.0.1 -u root -p ecommerce_db < database/init.sql
```

### 3. 后端配置

```bash
cd backend

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，设置数据库连接信息

# 启动后端服务
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. 前端配置

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev:h5
```

### 5. 一键启动（推荐）

```bash
# 启动所有服务
./scripts/start.sh

# 停止所有服务
./scripts/stop.sh
```

## 📱 功能特性

### 后端 (FastAPI)

- ✅ RESTful API 设计
- ✅ JWT 身份认证
- ✅ 数据库 ORM (SQLAlchemy)
- ✅ 数据验证 (Pydantic)
- ✅ API 文档自动生成
- ✅ 管理后台界面
- ✅ CORS 跨域支持
- ✅ 异步数据库操作

### 前端 (UniApp)

- ✅ Vue 3 + TypeScript
- ✅ 响应式设计
- ✅ 多端兼容 (H5/小程序/APP)
- ✅ 统一的 API 请求封装
- ✅ 组件化开发
- ✅ 路由导航

### 核心模块

1. **用户管理**
   - 用户注册/登录
   - 用户信息管理
   - 权限控制

2. **商品管理**
   - 商品 CRUD 操作
   - 商品分类管理
   - 商品搜索筛选

3. **订单管理**
   - 订单创建/查询
   - 订单状态管理
   - 订单统计

## 🔗 访问地址

启动服务后，可通过以下地址访问：

- **前端应用**: http://localhost:5173
- **后端API**: http://localhost:8000
- **API文档**: http://localhost:8000/docs
- **管理后台**: http://localhost:8000/admin

## 📁 核心文件说明

### 后端关键文件

- `backend/app/main.py` - FastAPI 应用入口
- `backend/app/core/config.py` - 应用配置
- `backend/app/db/database.py` - 数据库连接
- `backend/app/models/` - 数据模型定义
- `backend/app/api/v1/` - API 路由定义

### 前端关键文件

- `frontend/src/main.ts` - 应用入口
- `frontend/src/pages.json` - 页面配置
- `frontend/src/utils/request.ts` - API 请求封装
- `frontend/src/pages/` - 页面组件

## 🛠️ 开发指南

### 添加新的 API 接口

1. 在 `backend/app/models/` 中定义数据模型
2. 在 `backend/app/schemas/` 中定义 Pydantic 模式  
3. 在 `backend/app/crud/` 中实现数据库操作
4. 在 `backend/app/api/v1/endpoints/` 中添加路由
5. 在 `backend/app/api/v1/api.py` 中注册路由

### 添加新的前端页面

1. 在 `frontend/src/pages/` 中创建 Vue 组件
2. 在 `frontend/src/pages.json` 中配置路由
3. 在组件中使用 `api` 对象调用后端接口

### 数据库迁移

```bash
cd backend
# 生成迁移文件
alembic revision --autogenerate -m "描述"
# 执行迁移
alembic upgrade head
```

## 🧪 测试

### 后端测试

```bash
cd backend
pytest
```

### 前端测试

```bash
cd frontend
npm run test
```

## 📦 部署

### Docker 部署

```bash
# 构建镜像
docker-compose build

# 启动服务
docker-compose up -d
```

### 生产环境部署

1. 修改 `backend/.env` 中的生产配置
2. 构建前端生产版本：`npm run build:h5`
3. 使用 Nginx 代理前端静态文件
4. 使用 Gunicorn 运行 FastAPI 应用

## 🔧 配置说明

### 后端环境变量

```env
# 数据库配置
DATABASE_URL=mysql+pymysql://root:password@localhost/ecommerce_db

# JWT配置
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30

# 跨域配置
CORS_ORIGINS=["http://localhost:5173"]
```

### 前端配置

在 `frontend/src/utils/request.ts` 中修改 API 基础地址：

```typescript
const BASE_URL = 'http://your-api-domain.com'
```

## 🤝 贡献

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证

本项目基于 [MIT 许可证](LICENSE) 开源。

## 📞 支持

如有问题或建议，请提交 [Issue](../../issues) 或联系开发团队。

---

**Happy Coding! 🎉**