from fastapi import FastAPI, Request
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.responses import RedirectResponse

from app.core.config import settings
from app.crud.user import user
from app.db.database import engine, get_db
from app.models.user import User


class AdminAuthBackend(AuthenticationBackend):
    """管理后台认证后端"""
    
    async def login(self, request: Request) -> bool:
        """登录验证"""
        # 从表单数据获取用户名和密码
        form = await request.form()
        username = form.get("username")
        password = form.get("password")
        
        if not username or not password:
            return False
            
        db = next(get_db())
        try:
            # 验证用户
            auth_user = user.authenticate(db, username=str(username), password=str(password))
            if auth_user and user.is_active(auth_user):
                # 将用户ID存储在session中
                request.session["user_id"] = auth_user.id
                request.session["username"] = auth_user.username
                return True
            return False
        except Exception as e:
            print(f"Login error: {e}")
            return False
        finally:
            db.close()
    
    async def logout(self, request: Request) -> bool:
        """登出"""
        request.session.clear()
        return True
    
    async def authenticate(self, request: Request) -> bool:
        """认证检查"""
        return "user_id" in request.session


class UserAdmin(ModelView, model=User):
    """用户管理"""

    column_list = [
        User.id,
        User.username,
        User.email,
        User.full_name,
        User.is_active,
        User.created_at,
    ]
    column_details_list = [
        User.id,
        User.username,
        User.email,
        User.full_name,
        User.is_active,
        User.created_at,
        User.updated_at,
    ]
    column_searchable_list = [User.username, User.email, User.full_name]
    column_sortable_list = [User.id, User.username, User.email, User.created_at]
    form_excluded_columns = [User.password_hash, User.created_at, User.updated_at]
    name = "用户"
    name_plural = "用户管理"
    icon = "fa-solid fa-users"


def setup_admin(app: FastAPI):
    """设置管理后台"""

    # 创建认证后端
    auth_backend = AdminAuthBackend(secret_key=settings.SECRET_KEY)
    
    # 创建 SQLAdmin 实例
    admin = Admin(
        app, 
        engine, 
        title="用户管理系统",
        authentication_backend=auth_backend
    )

    # 添加模型视图
    admin.add_view(UserAdmin)

    return admin