#!/bin/bash

# 重置Cursor机器ID脚本
echo "正在重置Cursor机器ID..."

# 检测操作系统类型
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    MACHINE_ID_PATH="$HOME/Library/Application Support/Cursor/machineId"
else
    # Linux
    MACHINE_ID_PATH="$HOME/.config/cursor/machineId"
fi

# 备份原始ID
if [ -f "$MACHINE_ID_PATH" ]; then
    cp "$MACHINE_ID_PATH" "${MACHINE_ID_PATH}.bak"
    echo "已备份原始机器ID到 ${MACHINE_ID_PATH}.bak"
    
    # 删除机器ID文件
    rm "$MACHINE_ID_PATH"
    echo "已删除机器ID文件，Cursor将在下次启动时生成新的ID"
else
    echo "未找到机器ID文件，请确认Cursor已安装"
fi

echo "重置完成！请重启Cursor应用"
