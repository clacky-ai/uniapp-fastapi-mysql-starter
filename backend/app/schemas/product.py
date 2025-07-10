from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal


class CategoryBase(BaseModel):
    """分类基础模型"""
    name: str
    description: Optional[str] = None
    parent_id: Optional[int] = None
    sort_order: int = 0
    is_active: bool = True


class CategoryCreate(CategoryBase):
    """分类创建模型"""
    pass


class CategoryUpdate(BaseModel):
    """分类更新模型"""
    name: Optional[str] = None
    description: Optional[str] = None
    parent_id: Optional[int] = None
    sort_order: Optional[int] = None
    is_active: Optional[bool] = None


class Category(CategoryBase):
    """分类响应模型"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    """商品基础模型"""
    name: str
    description: Optional[str] = None
    price: Decimal
    stock_quantity: int = 0
    category_id: Optional[int] = None
    image_url: Optional[str] = None
    is_active: bool = True


class ProductCreate(ProductBase):
    """商品创建模型"""
    pass


class ProductUpdate(BaseModel):
    """商品更新模型"""
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    stock_quantity: Optional[int] = None
    category_id: Optional[int] = None
    image_url: Optional[str] = None
    is_active: Optional[bool] = None


class Product(ProductBase):
    """商品响应模型"""
    id: int
    category: Optional[Category] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True