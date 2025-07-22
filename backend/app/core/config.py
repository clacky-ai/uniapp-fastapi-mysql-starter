from typing import Optional

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """应用配置"""

    # 应用信息
    APP_NAME: str = Field(default="Mini Program Scaffold API", description="应用名称")
    APP_VERSION: str = Field(default="1.0.0", description="应用版本")
    DEBUG: bool = Field(default=True, description="调试模式")

    # 数据库配置
    DB_HOST: str = Field(default="127.0.0.1", description="数据库主机")
    DB_PORT: int = Field(default=3306, description="数据库端口")
    DB_USER: str = Field(default="root", description="数据库用户名")
    DB_PASSWORD: str = Field(description="数据库密码")
    DB_NAME: str = Field(default="blog_demo", description="数据库名称")

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        """构建数据库连接URL"""
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # JWT配置
    SECRET_KEY: str = Field(default="your-secret-key-change-this-in-production", description="JWT密钥")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=11520, description="访问令牌过期时间（分钟）")

    def validate_secret_key(self) -> None:
        """验证密钥是否为默认值"""
        if self.SECRET_KEY == "your-secret-key-change-this-in-production" and not self.DEBUG:
            raise ValueError("请在生产环境中更改SECRET_KEY")

    # CORS配置
    ALLOWED_HOSTS: list = ["*"]
    CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:8080",
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8080",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "*",
    ]

    # Redis配置（可选）
    REDIS_URL: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.validate_secret_key()


settings = Settings()
