from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .user import User


class PostBase(BaseModel):
    """文章基础模型"""

    title: str
    content: Optional[str] = None
    is_published: bool = False


class PostCreate(PostBase):
    """创建文章模型"""

    pass


class PostUpdate(PostBase):
    """更新文章模型"""

    title: Optional[str] = None
    is_published: Optional[bool] = None


class Post(PostBase):
    """文章响应模型"""

    id: int
    author_id: int
    author: Optional[User] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
