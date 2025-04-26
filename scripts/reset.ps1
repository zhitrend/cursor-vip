# Windows重置Cursor机器ID脚本
Write-Host "正在重置Cursor机器ID..." -ForegroundColor Green

# 机器ID路径
$machineIdPath = "$env:APPDATA\Cursor\machineId"

# 备份原始ID
if (Test-Path $machineIdPath) {
    Copy-Item -Path $machineIdPath -Destination "$machineIdPath.bak" -Force
    Write-Host "已备份原始机器ID到 $machineIdPath.bak" -ForegroundColor Yellow
    
    # 删除机器ID文件
    Remove-Item -Path $machineIdPath -Force
    Write-Host "已删除机器ID文件，Cursor将在下次启动时生成新的ID" -ForegroundColor Green
} else {
    Write-Host "未找到机器ID文件，请确认Cursor已安装" -ForegroundColor Red
}

Write-Host "重置完成！请重启Cursor应用" -ForegroundColor Green
