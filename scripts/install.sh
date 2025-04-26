#!/bin/bash

# 安装脚本
echo "安装Cursor VIP工具..."

# 创建目录
mkdir -p ~/cursor-vip
cd ~/cursor-vip

# 下载主程序
curl -fsSL https://github.com/zhitrend/cursor-vip/raw/main/main.py -o cursor-vip.py

# 下载依赖文件
curl -fsSL https://github.com/zhitrend/cursor-vip/raw/main/requirements.txt -o requirements.txt

# 安装依赖
pip install -r requirements.txt

echo "安装完成！现在可以运行 python ~/cursor-vip/cursor-vip.py 启动程序"
