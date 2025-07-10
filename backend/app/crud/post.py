from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):
    """文章CRUD操作"""

    def get_by_author(self, db: Session, *, author_id: int, skip: int = 0, limit: int = 100) -> List[Post]:
        """根据作者获取文章列表"""
        return (
            db.query(Post)
            .filter(Post.author_id == author_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_published(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Post]:
        """获取已发布的文章列表"""
        return (
            db.query(Post)
            .filter(Post.is_published)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create_with_author(self, db: Session, *, obj_in: PostCreate, author_id: int) -> Post:
        """创建文章并指定作者"""
        db_obj = Post(
            title=obj_in.title,
            content=obj_in.content,
            is_published=obj_in.is_published,
            author_id=author_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


post = CRUDPost(Post)
