# Windows安装脚本
Write-Host "安装Cursor VIP工具..." -ForegroundColor Green

# 创建目录
$installDir = "$env:USERPROFILE\cursor-vip"
New-Item -ItemType Directory -Force -Path $installDir | Out-Null
Set-Location -Path $installDir

# 下载主程序
Invoke-WebRequest -Uri "https://github.com/zhitrend/cursor-vip/raw/main/main.py" -OutFile "$installDir\cursor-vip.py"

# 下载依赖文件
Invoke-WebRequest -Uri "https://github.com/zhitrend/cursor-vip/raw/main/requirements.txt" -OutFile "$installDir\requirements.txt"

# 安装依赖
pip install -r "$installDir\requirements.txt"

Write-Host "安装完成！现在可以运行 python $installDir\cursor-vip.py 启动程序" -ForegroundColor Green
