from typing import Any, List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.api.deps import get_current_active_user, get_current_admin_user, get_db
from app.crud import order
from app.models.user import User
from app.models.order import OrderStatus
from app.schemas.order import Order, OrderCreate, OrderUpdate

router = APIRouter()


@router.get("/", response_model=List[Order])
def read_orders(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    status: Optional[OrderStatus] = Query(None, description="订单状态"),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """获取订单列表"""
    if current_user.is_admin:
        # 管理员可以查看所有订单
        if status:
            orders = order.get_by_status(db, status=status, skip=skip, limit=limit)
        else:
            orders = order.get_multi(db, skip=skip, limit=limit)
    else:
        # 普通用户只能查看自己的订单
        orders = order.get_by_user(db, user_id=current_user.id, skip=skip, limit=limit)
        if status:
            orders = [o for o in orders if o.status == status]
    return orders


@router.post("/", response_model=Order)
def create_order(
    *,
    db: Session = Depends(get_db),
    order_in: OrderCreate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """创建订单"""
    order_obj = order.create_with_items(db, obj_in=order_in, user_id=current_user.id)
    return order_obj


@router.get("/{order_id}", response_model=Order)
def read_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """获取订单详情"""
    order_obj = order.get(db, id=order_id)
    if not order_obj:
        raise HTTPException(status_code=404, detail="订单不存在")
    
    # 检查权限：用户只能查看自己的订单或管理员可以查看所有订单
    if order_obj.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="权限不足")
    
    return order_obj


@router.put("/{order_id}", response_model=Order)
def update_order(
    *,
    db: Session = Depends(get_db),
    order_id: int,
    order_in: OrderUpdate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """更新订单"""
    order_obj = order.get(db, id=order_id)
    if not order_obj:
        raise HTTPException(status_code=404, detail="订单不存在")
    
    # 检查权限：用户只能更新自己的订单或管理员可以更新所有订单
    if order_obj.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="权限不足")
    
    order_obj = order.update(db, db_obj=order_obj, obj_in=order_in)
    return order_obj


@router.delete("/{order_id}", response_model=Order)
def delete_order(
    *,
    db: Session = Depends(get_db),
    order_id: int,
    current_user: User = Depends(get_current_admin_user),
) -> Any:
    """删除订单（管理员权限）"""
    order_obj = order.remove(db, id=order_id)
    if not order_obj:
        raise HTTPException(status_code=404, detail="订单不存在")
    return order_obj