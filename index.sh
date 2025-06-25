#!/bin/bash

# Step 1: 查找占用 7860 端口的进程
PORT=7860
PID=$(lsof -t -i:$PORT)

if [ ! -z "$PID" ]; then
    echo "发现占用端口 $PORT 的进程 (PID: $PID)，正在终止..."
    kill -9 $PID
    echo "进程 $PID 已被终止。"
else
    echo "端口 $PORT 没有被占用。"
fi

# Step 2: 使用 nohup 启动 python index.py
echo "使用 nohup 启动 python index.py..."
/home/deipss/anaconda3/bin/conda run -n py310 python index.py 2>&1
echo "脚本已启动"