from fastapi import FastAPI
from fastapi_admin.app import app as admin_app
from fastapi_admin.enums import Method
from fastapi_admin.file_upload import FileUpload
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.resources import Action, Dropdown, Field, Link, Model
from fastapi_admin.widgets import displays, filters, inputs
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from app.models import User, Product, Category, Order, OrderItem


def create_admin():
    """创建管理后台"""
    # 配置登录提供者
    @admin_app.register
    class LoginProvider(UsernamePasswordProvider):
        async def login(
            self,
            username: str,
            password: str,
            remember_me: bool,
            request: Request,
        ) -> bool:
            # 这里实现登录逻辑，暂时使用简单的硬编码验证
            # 在实际项目中应该使用数据库验证
            if username == "admin" and password == "admin123":
                request.session.update({"user": username})
                return True
            return False

        async def is_authenticated(self, request: Request) -> bool:
            return request.session.get("user") is not None

        def get_admin_user(self, request: Request):
            user = request.session.get("user")
            if user:
                return user
            return None

        async def logout(self, request: Request):
            request.session.clear()

    # 用户管理
    @admin_app.register
    class UserResource(Model):
        label = "用户管理"
        model = User
        icon = "fas fa-users"
        page_pre_title = "用户管理"
        page_title = "用户列表"
        filters = [
            filters.Search(name="username", label="用户名", search_mode="contains"),
            filters.Search(name="email", label="邮箱", search_mode="contains"),
            filters.Boolean(name="is_active", label="是否激活"),
            filters.Boolean(name="is_admin", label="是否管理员"),
        ]
        fields = [
            "id",
            "username",
            "email",
            "full_name",
            Field(
                name="is_active",
                label="激活状态",
                display=displays.Boolean(),
                input_=inputs.Switch(),
            ),
            Field(
                name="is_admin",
                label="管理员",
                display=displays.Boolean(),
                input_=inputs.Switch(),
            ),
            "created_at",
            "updated_at",
        ]

    # 分类管理
    @admin_app.register
    class CategoryResource(Model):
        label = "分类管理"
        model = Category
        icon = "fas fa-tags"
        page_pre_title = "商品管理"
        page_title = "分类列表"
        filters = [
            filters.Search(name="name", label="分类名称", search_mode="contains"),
            filters.Boolean(name="is_active", label="是否激活"),
        ]
        fields = [
            "id",
            "name",
            "description",
            Field(
                name="parent_id",
                label="父分类",
                input_=inputs.ForeignKey(Category, "name"),
            ),
            "sort_order",
            Field(
                name="is_active",
                label="激活状态",
                display=displays.Boolean(),
                input_=inputs.Switch(),
            ),
            "created_at",
            "updated_at",
        ]

    # 商品管理
    @admin_app.register
    class ProductResource(Model):
        label = "商品管理"
        model = Product
        icon = "fas fa-boxes"
        page_pre_title = "商品管理"
        page_title = "商品列表"
        filters = [
            filters.Search(name="name", label="商品名称", search_mode="contains"),
            filters.ForeignKey(name="category_id", label="分类", model=Category),
            filters.Boolean(name="is_active", label="是否激活"),
        ]
        fields = [
            "id",
            "name",
            Field(
                name="description",
                label="描述",
                input_=inputs.TextArea(),
            ),
            Field(
                name="price",
                label="价格",
                input_=inputs.Number(step=0.01),
            ),
            Field(
                name="stock_quantity",
                label="库存数量",
                input_=inputs.Number(),
            ),
            Field(
                name="category_id",
                label="分类",
                input_=inputs.ForeignKey(Category, "name"),
            ),
            Field(
                name="image_url",
                label="图片链接",
                input_=inputs.URL(),
            ),
            Field(
                name="is_active",
                label="激活状态",
                display=displays.Boolean(),
                input_=inputs.Switch(),
            ),
            "created_at",
            "updated_at",
        ]

    # 订单管理
    @admin_app.register
    class OrderResource(Model):
        label = "订单管理"
        model = Order
        icon = "fas fa-shopping-cart"
        page_pre_title = "订单管理"
        page_title = "订单列表"
        filters = [
            filters.ForeignKey(name="user_id", label="用户", model=User),
            filters.Enum(name="status", label="订单状态", enum=Order.status.property.columns[0].type),
        ]
        fields = [
            "id",
            Field(
                name="user_id",
                label="用户",
                input_=inputs.ForeignKey(User, "username"),
            ),
            Field(
                name="total_amount",
                label="总金额",
                input_=inputs.Number(step=0.01),
            ),
            Field(
                name="status",
                label="订单状态",
                input_=inputs.Enum(Order.status.property.columns[0].type),
            ),
            Field(
                name="shipping_address",
                label="收货地址",
                input_=inputs.TextArea(),
            ),
            "created_at",
            "updated_at",
        ]

    return admin_app


def setup_admin(app: FastAPI):
    """配置管理后台"""
    # 创建管理后台
    admin = create_admin()
    
    # 挂载静态文件
    app.mount("/static", StaticFiles(directory="static"), name="static")
    
    # 挂载管理后台
    app.mount("/admin", admin)
    
    return app