from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.post import Post
from app.models.user import User

router = APIRouter()


@router.get("/dashboard")
def get_dashboard_stats(db: Session = Depends(get_db)) -> Any:
    """获取系统统计数据"""
    # 统计用户数量
    user_count = db.query(func.count(User.id)).scalar() or 0

    # 统计激活用户数量
    active_user_count = db.query(func.count(User.id)).filter(User.is_active).scalar() or 0

    # 统计文章数量
    post_count = db.query(func.count(Post.id)).scalar() or 0

    # 统计已发布文章数量
    published_post_count = db.query(func.count(Post.id)).filter(Post.is_published).scalar() or 0

    return {
        "total_users": user_count,
        "active_users": active_user_count,
        "total_posts": post_count,
        "published_posts": published_post_count,
        "system_status": "running",
        "message": "系统运行正常"
    }
