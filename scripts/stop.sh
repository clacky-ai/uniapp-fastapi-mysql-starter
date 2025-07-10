#!/bin/bash

# 停止整个项目的脚本

echo "正在停止电商管理系统..."

# 停止FastAPI后端
echo "停止后端服务..."
pkill -f "uvicorn app.main:app"
if [ $? -eq 0 ]; then
    echo "✅ 后端服务已停止"
else
    echo "⚠️  未找到运行中的后端服务"
fi

# 停止前端开发服务器
echo "停止前端服务..."
pkill -f "npm run dev:h5"
pkill -f "uni"
if [ $? -eq 0 ]; then
    echo "✅ 前端服务已停止"
else
    echo "⚠️  未找到运行中的前端服务"
fi

# 清理相关进程
pkill -f "vite"
pkill -f "node.*uni"

echo ""
echo "🛑 所有服务已停止"