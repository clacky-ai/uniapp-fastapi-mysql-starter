#!/bin/bash

# 启动整个项目的脚本

echo "正在启动电商管理系统..."

# 检查MySQL连接
echo "检查MySQL连接..."
mysql -h 127.0.0.1 -u root -pFeNYotjr -e "SELECT 1;" > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "❌ MySQL连接失败，请检查数据库配置"
    exit 1
fi
echo "✅ MySQL连接正常"

# 启动后端
echo "启动FastAPI后端..."
cd backend
if [ ! -d "venv" ]; then
    echo "创建Python虚拟环境..."
    python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt > /dev/null 2>&1

# 后台启动FastAPI
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload > ../logs/backend.log 2>&1 &
BACKEND_PID=$!
echo "✅ 后端已启动 (PID: $BACKEND_PID)"

# 等待后端启动
sleep 5

# 检查后端是否启动成功
curl -s http://localhost:8000/docs > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ 后端API文档: http://localhost:8000/docs"
else
    echo "❌ 后端启动失败，请检查日志: logs/backend.log"
    exit 1
fi

# 启动前端
echo "启动UniApp前端..."
cd ../frontend

# 安装依赖（如果需要）
if [ ! -d "node_modules" ]; then
    echo "安装前端依赖..."
    npm install
fi

# 后台启动前端
nohup npm run dev:h5 > ../logs/frontend.log 2>&1 &
FRONTEND_PID=$!
echo "✅ 前端已启动 (PID: $FRONTEND_PID)"

# 等待前端启动
sleep 10

echo ""
echo "🎉 系统启动完成！"
echo ""
echo "📊 服务地址："
echo "   - 前端应用: http://localhost:5173"
echo "   - 后端API: http://localhost:8000"
echo "   - API文档: http://localhost:8000/docs"
echo "   - 管理后台: http://localhost:8000/admin"
echo ""
echo "📋 进程ID："
echo "   - 后端进程: $BACKEND_PID"
echo "   - 前端进程: $FRONTEND_PID"
echo ""
echo "🛑 停止服务: ./scripts/stop.sh"
echo "📝 查看日志: tail -f logs/backend.log 或 tail -f logs/frontend.log"