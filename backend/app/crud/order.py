from typing import List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.order import Order, OrderItem, OrderStatus
from app.schemas.order import OrderCreate, OrderUpdate, OrderItemCreate


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):
    """订单CRUD操作"""
    
    def get_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Order]:
        """根据用户获取订单列表"""
        return (
            db.query(Order)
            .filter(Order.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_by_status(
        self, db: Session, *, status: OrderStatus, skip: int = 0, limit: int = 100
    ) -> List[Order]:
        """根据状态获取订单列表"""
        return (
            db.query(Order)
            .filter(Order.status == status)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def create_with_items(
        self, db: Session, *, obj_in: OrderCreate, user_id: int
    ) -> Order:
        """创建包含商品的订单"""
        # 计算总金额
        total_amount = sum(item.price * item.quantity for item in obj_in.items)
        
        # 创建订单
        db_order = Order(
            user_id=user_id,
            total_amount=total_amount,
            shipping_address=obj_in.shipping_address,
        )
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        
        # 创建订单商品
        for item_data in obj_in.items:
            db_item = OrderItem(
                order_id=db_order.id,
                product_id=item_data.product_id,
                quantity=item_data.quantity,
                price=item_data.price,
            )
            db.add(db_item)
        
        db.commit()
        db.refresh(db_order)
        return db_order


class CRUDOrderItem(CRUDBase[OrderItem, OrderItemCreate, None]):
    """订单商品CRUD操作"""
    
    def get_by_order(self, db: Session, *, order_id: int) -> List[OrderItem]:
        """根据订单获取商品列表"""
        return db.query(OrderItem).filter(OrderItem.order_id == order_id).all()


order = CRUDOrder(Order)
order_item = CRUDOrderItem(OrderItem)