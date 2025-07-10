# 博客管理系统 Demo

这是一个简化版的博客管理系统，用于演示前后端联调和数据库操作。

## 项目结构

```
├── backend/          # FastAPI 后端服务
├── frontend/         # Vue3 + UniApp 前端应用
├── database/         # 数据库初始化脚本
├── logs/            # 日志文件
└── scripts/         # 启动脚本
```

## 功能特性

### 后端功能
- ✅ 用户管理（注册、登录、用户信息）
- ✅ 文章管理（CRUD操作、发布状态）
- ✅ JWT认证和权限控制
- ✅ 数据统计API
- ✅ 管理后台界面
- ✅ API文档自动生成

### 前端功能
- ✅ 响应式设计的首页
- ✅ 文章列表浏览
- ✅ 文章详情查看
- ✅ 实时数据统计展示
- ✅ 跨平台支持（H5、小程序）

### 数据库
- ✅ MySQL数据库
- ✅ 用户表和文章表
- ✅ 关联查询支持
- ✅ 示例数据自动生成

## 快速开始

### 1. 启动后端服务
```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 2. 启动前端应用
```bash
cd frontend
npm run dev:h5
```

### 3. 访问地址
- **前端应用**: http://localhost:5174/
- **API文档**: http://localhost:8000/docs
- **管理后台**: http://localhost:8000/admin/

## 测试账户

**预设管理员账户：**
- 用户名：`admin`
- 密码：`secret`

## API接口

### 统计信息
```
GET /api/v1/stats/dashboard
```

### 文章相关
```
GET /api/v1/posts/published  # 获取已发布文章
GET /api/v1/posts/{id}       # 获取文章详情
POST /api/v1/posts/          # 创建文章（需认证）
```

### 用户相关
```
POST /api/v1/auth/login      # 用户登录
POST /api/v1/users/          # 用户注册
GET /api/v1/users/me         # 获取当前用户信息
```

## 数据库结构

### 用户表 (users)
- id, username, email, password_hash, full_name, is_active, created_at, updated_at

### 文章表 (posts)
- id, title, content, author_id, is_published, created_at, updated_at

## 技术栈

**后端：**
- FastAPI + Python 3.12
- SQLAlchemy ORM
- MySQL数据库
- SQLAdmin管理后台
- JWT认证

**前端：**
- Vue 3 + TypeScript
- UniApp框架
- Vite构建工具
- 响应式UI设计

## 开发说明

这是一个从复杂电商系统简化而来的博客demo，专注于：
1. 展示基本的CRUD操作
2. 演示前后端API联调
3. 实现用户认证流程
4. 提供管理后台功能

适合作为学习参考或项目脚手架使用。