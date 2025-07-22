from fastapi import APIRouter

from app.api.v1.endpoints import auth, stats, users

api_router = APIRouter()

# 包含各个模块的路由
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])

api_router.include_router(stats.router, prefix="/stats", tags=["statistics"])
