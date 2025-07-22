from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

from app.admin import setup_admin
from app.api.v1.api import api_router
from app.core.config import settings

# 创建FastAPI应用实例
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    description="小程序开发脚手架后端API服务",
)

# 添加Session中间件（必须在admin设置之前）
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 设置管理后台
setup_admin(app)

# 包含API路由
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    """根路径重定向到admin后台"""
    return RedirectResponse(url="/admin", status_code=302)


@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy"}
