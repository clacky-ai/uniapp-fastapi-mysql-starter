from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.api.deps import get_current_admin_user, get_db
from app.crud import product
from app.models.user import User
from app.schemas.product import Product, ProductCreate, ProductUpdate

router = APIRouter()


@router.get("/", response_model=List[Product])
def read_products(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    category_id: Optional[int] = Query(None, description="分类ID"),
    search: Optional[str] = Query(None, description="搜索关键词"),
    active_only: bool = Query(True, description="只显示激活的商品"),
) -> Any:
    """获取商品列表"""
    if search:
        products = product.search_by_name(db, name=search, skip=skip, limit=limit)
    elif category_id:
        products = product.get_by_category(db, category_id=category_id, skip=skip, limit=limit)
    elif active_only:
        products = product.get_active(db, skip=skip, limit=limit)
    else:
        products = product.get_multi(db, skip=skip, limit=limit)
    return products


@router.post("/", response_model=Product)
def create_product(
    *,
    db: Session = Depends(get_db),
    product_in: ProductCreate,
    current_user: User = Depends(get_current_admin_user),
) -> Any:
    """创建商品（管理员权限）"""
    product_obj = product.create(db, obj_in=product_in)
    return product_obj


@router.get("/{product_id}", response_model=Product)
def read_product(
    product_id: int,
    db: Session = Depends(get_db),
) -> Any:
    """获取商品详情"""
    product_obj = product.get(db, id=product_id)
    if not product_obj:
        raise HTTPException(status_code=404, detail="商品不存在")
    return product_obj


@router.put("/{product_id}", response_model=Product)
def update_product(
    *,
    db: Session = Depends(get_db),
    product_id: int,
    product_in: ProductUpdate,
    current_user: User = Depends(get_current_admin_user),
) -> Any:
    """更新商品（管理员权限）"""
    product_obj = product.get(db, id=product_id)
    if not product_obj:
        raise HTTPException(status_code=404, detail="商品不存在")
    product_obj = product.update(db, db_obj=product_obj, obj_in=product_in)
    return product_obj


@router.delete("/{product_id}", response_model=Product)
def delete_product(
    *,
    db: Session = Depends(get_db),
    product_id: int,
    current_user: User = Depends(get_current_admin_user),
) -> Any:
    """删除商品（管理员权限）"""
    product_obj = product.remove(db, id=product_id)
    if not product_obj:
        raise HTTPException(status_code=404, detail="商品不存在")
    return product_obj
