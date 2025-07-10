from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.api.deps import get_current_admin_user, get_db
from app.crud import category
from app.models.user import User
from app.schemas.product import Category, CategoryCreate, CategoryUpdate

router = APIRouter()


@router.get("/", response_model=List[Category])
def read_categories(
    db: Session = Depends(get_db),
    parent_id: Optional[int] = Query(None, description="父分类ID"),
    active_only: bool = Query(True, description="只显示激活的分类"),
) -> Any:
    """获取分类列表"""
    if active_only:
        categories = category.get_active(db)
        if parent_id is not None:
            categories = [cat for cat in categories if cat.parent_id == parent_id]
    else:
        categories = category.get_by_parent(db, parent_id=parent_id)
    return categories


@router.post("/", response_model=Category)
def create_category(
    *,
    db: Session = Depends(get_db),
    category_in: CategoryCreate,
    current_user: User = Depends(get_current_admin_user),
) -> Any:
    """创建分类（管理员权限）"""
    category_obj = category.create(db, obj_in=category_in)
    return category_obj


@router.get("/{category_id}", response_model=Category)
def read_category(
    category_id: int,
    db: Session = Depends(get_db),
) -> Any:
    """获取分类详情"""
    category_obj = category.get(db, id=category_id)
    if not category_obj:
        raise HTTPException(status_code=404, detail="分类不存在")
    return category_obj


@router.put("/{category_id}", response_model=Category)
def update_category(
    *,
    db: Session = Depends(get_db),
    category_id: int,
    category_in: CategoryUpdate,
    current_user: User = Depends(get_current_admin_user),
) -> Any:
    """更新分类（管理员权限）"""
    category_obj = category.get(db, id=category_id)
    if not category_obj:
        raise HTTPException(status_code=404, detail="分类不存在")
    category_obj = category.update(db, db_obj=category_obj, obj_in=category_in)
    return category_obj


@router.delete("/{category_id}", response_model=Category)
def delete_category(
    *,
    db: Session = Depends(get_db),
    category_id: int,
    current_user: User = Depends(get_current_admin_user),
) -> Any:
    """删除分类（管理员权限）"""
    category_obj = category.remove(db, id=category_id)
    if not category_obj:
        raise HTTPException(status_code=404, detail="分类不存在")
    return category_obj
