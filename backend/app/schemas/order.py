from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from decimal import Decimal
from app.models.order import OrderStatus
from .user import User
from .product import Product


class OrderItemBase(BaseModel):
    """订单商品基础模型"""
    product_id: int
    quantity: int
    price: Decimal


class OrderItemCreate(OrderItemBase):
    """订单商品创建模型"""
    pass


class OrderItem(OrderItemBase):
    """订单商品响应模型"""
    id: int
    order_id: int
    product: Optional[Product] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    """订单基础模型"""
    user_id: int
    total_amount: Decimal
    status: OrderStatus = OrderStatus.PENDING
    shipping_address: Optional[str] = None


class OrderCreate(BaseModel):
    """订单创建模型"""
    shipping_address: Optional[str] = None
    items: List[OrderItemCreate]


class OrderUpdate(BaseModel):
    """订单更新模型"""
    status: Optional[OrderStatus] = None
    shipping_address: Optional[str] = None


class Order(OrderBase):
    """订单响应模型"""
    id: int
    user: Optional[User] = None
    items: Optional[List[OrderItem]] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True