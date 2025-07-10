from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.product import Category, Product
from app.schemas.product import CategoryCreate, CategoryUpdate, ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    """商品CRUD操作"""

    def get_by_category(
        self, db: Session, *, category_id: int, skip: int = 0, limit: int = 100
    ) -> List[Product]:
        """根据分类获取商品列表"""
        return (
            db.query(Product)
            .filter(Product.category_id == category_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_active(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Product]:
        """获取激活的商品列表"""
        return (
            db.query(Product)
            .filter(Product.is_active)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def search_by_name(
        self, db: Session, *, name: str, skip: int = 0, limit: int = 100
    ) -> List[Product]:
        """根据名称搜索商品"""
        return (
            db.query(Product)
            .filter(Product.name.contains(name))
            .offset(skip)
            .limit(limit)
            .all()
        )


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    """分类CRUD操作"""

    def get_by_parent(
        self, db: Session, *, parent_id: Optional[int] = None
    ) -> List[Category]:
        """根据父分类获取子分类"""
        return db.query(Category).filter(Category.parent_id == parent_id).all()

    def get_active(self, db: Session) -> List[Category]:
        """获取激活的分类列表"""
        return db.query(Category).filter(Category.is_active).all()


product = CRUDProduct(Product)
category = CRUDCategory(Category)
