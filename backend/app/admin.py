from fastapi import FastAPI
from sqladmin import Admin, ModelView

from app.db.database import engine
from app.models.order import Order
from app.models.product import Product
from app.models.user import User


class UserAdmin(ModelView, model=User):
    """用户管理"""
    column_list = [User.id, User.username, User.email, User.full_name, User.is_active, User.is_admin, User.created_at]
    column_details_list = [User.id, User.username, User.email, User.full_name, User.is_active, User.is_admin, User.created_at, User.updated_at]
    column_searchable_list = [User.username, User.email, User.full_name]
    column_sortable_list = [User.id, User.username, User.email, User.created_at]
    form_excluded_columns = [User.password_hash, User.created_at, User.updated_at]
    name = "用户"
    name_plural = "用户管理"
    icon = "fa-solid fa-users"


class ProductAdmin(ModelView, model=Product):
    """商品管理"""
    column_list = [Product.id, Product.name, Product.price, Product.stock_quantity, Product.category_id, Product.is_active, Product.created_at]
    column_details_list = [Product.id, Product.name, Product.description, Product.price, Product.stock_quantity, Product.category_id, Product.image_url, Product.is_active, Product.created_at, Product.updated_at]
    column_searchable_list = [Product.name, Product.description]
    column_sortable_list = [Product.id, Product.name, Product.price, Product.stock_quantity, Product.created_at]
    form_excluded_columns = [Product.created_at, Product.updated_at]
    name = "商品"
    name_plural = "商品管理"
    icon = "fa-solid fa-box"


class OrderAdmin(ModelView, model=Order):
    """订单管理"""
    column_list = [Order.id, Order.user_id, Order.total_amount, Order.status, Order.created_at]
    column_details_list = [Order.id, Order.user_id, Order.total_amount, Order.status, Order.shipping_address, Order.created_at, Order.updated_at]
    column_searchable_list = [Order.status, Order.shipping_address]
    column_sortable_list = [Order.id, Order.total_amount, Order.created_at]
    form_excluded_columns = [Order.created_at, Order.updated_at]
    name = "订单"
    name_plural = "订单管理"
    icon = "fa-solid fa-shopping-cart"


def setup_admin(app: FastAPI):
    """设置管理后台"""

    # 创建 SQLAdmin 实例
    admin = Admin(app, engine, title="电商管理后台")

    # 添加模型视图
    admin.add_view(UserAdmin)
    admin.add_view(ProductAdmin)
    admin.add_view(OrderAdmin)

    return admin
