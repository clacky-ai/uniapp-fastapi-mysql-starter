from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user, get_db
from app.crud import post
from app.models.user import User
from app.schemas.post import Post, PostCreate, PostUpdate

router = APIRouter()


@router.get("/", response_model=List[Post])
def read_posts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
):
    """获取文章列表"""
    posts = post.get_multi(db, skip=skip, limit=limit)
    return posts


@router.get("/published", response_model=List[Post])
def read_published_posts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
):
    """获取已发布的文章列表"""
    posts = post.get_published(db, skip=skip, limit=limit)
    return posts


@router.get("/my", response_model=List[Post])
def read_my_posts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
    skip: int = 0,
    limit: int = 100,
):
    """获取当前用户的文章列表"""
    posts = post.get_by_author(db, author_id=current_user.id, skip=skip, limit=limit)
    return posts


@router.post("/", response_model=Post)
def create_post(
    *,
    db: Session = Depends(get_db),
    post_in: PostCreate,
    current_user: User = Depends(get_current_active_user),
):
    """创建文章"""
    post_obj = post.create_with_author(db, obj_in=post_in, author_id=current_user.id)
    return post_obj


@router.get("/{post_id}", response_model=Post)
def read_post(
    *,
    db: Session = Depends(get_db),
    post_id: int,
):
    """根据ID获取文章"""
    post_obj = post.get(db=db, id=post_id)
    if not post_obj:
        raise HTTPException(status_code=404, detail="文章不存在")
    return post_obj


@router.put("/{post_id}", response_model=Post)
def update_post(
    *,
    db: Session = Depends(get_db),
    post_id: int,
    post_in: PostUpdate,
    current_user: User = Depends(get_current_active_user),
):
    """更新文章"""
    post_obj = post.get(db=db, id=post_id)
    if not post_obj:
        raise HTTPException(status_code=404, detail="文章不存在")
    if post_obj.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="没有权限修改此文章")
    post_obj = post.update(db=db, db_obj=post_obj, obj_in=post_in)
    return post_obj


@router.delete("/{post_id}")
def delete_post(
    *,
    db: Session = Depends(get_db),
    post_id: int,
    current_user: User = Depends(get_current_active_user),
):
    """删除文章"""
    post_obj = post.get(db=db, id=post_id)
    if not post_obj:
        raise HTTPException(status_code=404, detail="文章不存在")
    if post_obj.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="没有权限删除此文章")
    post.remove(db=db, id=post_id)
    return {"message": "文章删除成功"}
