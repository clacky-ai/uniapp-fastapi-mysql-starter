from fastapi import FastAPI
from sqladmin import Admin, ModelView

from app.db.database import engine
from app.models.post import Post
from app.models.user import User


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


class PostAdmin(ModelView, model=Post):
    """文章管理"""

    column_list = [Post.id, Post.title, Post.author_id, Post.is_published, Post.created_at]
    column_details_list = [
        Post.id,
        Post.title,
        Post.content,
        Post.author_id,
        Post.is_published,
        Post.created_at,
        Post.updated_at,
    ]
    column_searchable_list = [Post.title, Post.content]
    column_sortable_list = [Post.id, Post.title, Post.created_at]
    form_excluded_columns = [Post.created_at, Post.updated_at]
    name = "文章"
    name_plural = "文章管理"
    icon = "fa-solid fa-newspaper"


def setup_admin(app: FastAPI):
    """设置管理后台"""

    # 创建 SQLAdmin 实例
    admin = Admin(app, engine, title="博客管理系统")

    # 添加模型视图
    admin.add_view(UserAdmin)
    admin.add_view(PostAdmin)

    return admin
