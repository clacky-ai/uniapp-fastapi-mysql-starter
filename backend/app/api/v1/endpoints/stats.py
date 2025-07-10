from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.api.deps import get_db
from app.models.product import Product
from app.models.user import User
from app.models.order import Order

router = APIRouter()


@router.get("/dashboard")
def get_dashboard_stats(db: Session = Depends(get_db)) -> Any:
    """获取系统统计数据"""
    # 统计商品数量
    product_count = db.query(func.count(Product.id)).scalar() or 0
    
    # 统计用户数量
    user_count = db.query(func.count(User.id)).scalar() or 0
    
    # 统计订单数量
    order_count = db.query(func.count(Order.id)).scalar() or 0
    
    # 统计激活商品数量
    active_product_count = db.query(func.count(Product.id)).filter(Product.is_active == True).scalar() or 0
    
    return {
        "total_products": product_count,
        "active_products": active_product_count,
        "total_users": user_count,
        "total_orders": order_count,
        "system_status": "running",
        "message": "系统运行正常"
    }