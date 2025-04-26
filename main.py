#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cursor VIP工具 - 重置机器ID和自动注册登录
"""

import os
import sys
import platform
import random
import string
import shutil
import time
import json
import requests
from colorama import init, Fore, Style

# 初始化colorama
init()

def print_banner():
    """打印程序横幅"""
    banner = f"""
    {Fore.CYAN}╔═══════════════════════════════════════════════╗
    ║ {Fore.YELLOW}Cursor VIP工具 {Fore.GREEN}v1.9.05{Fore.CYAN}                      ║
    ║ {Fore.WHITE}重置机器ID和自动注册登录{Fore.CYAN}                  ║
    ╚═══════════════════════════════════════════════╝{Style.RESET_ALL}
    """
    print(banner)

def get_machine_id_path():
    """获取机器ID文件路径"""
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.environ["APPDATA"], "Cursor", "machineId")
    elif system == "Darwin":  # macOS
        return os.path.join(os.path.expanduser("~"), "Library", "Application Support", "Cursor", "machineId")
    else:  # Linux
        return os.path.join(os.path.expanduser("~"), ".config", "cursor", "machineId")

def generate_random_id(length=32):
    """生成随机ID"""
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def reset_machine_id():
    """重置机器ID"""
    machine_id_path = get_machine_id_path()
    
    # 检查文件是否存在
    if not os.path.exists(machine_id_path):
        print(f"{Fore.RED}[错误] 未找到机器ID文件: {machine_id_path}{Style.RESET_ALL}")
        return False
    
    # 备份原始ID
    backup_path = f"{machine_id_path}.bak"
    try:
        shutil.copy2(machine_id_path, backup_path)
        print(f"{Fore.GREEN}[成功] 已备份原始机器ID到: {backup_path}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[错误] 备份机器ID失败: {str(e)}{Style.RESET_ALL}")
    
    # 生成新ID并写入文件
    new_id = generate_random_id()
    try:
        with open(machine_id_path, "w") as f:
            f.write(new_id)
        print(f"{Fore.GREEN}[成功] 已重置机器ID为: {new_id}{Style.RESET_ALL}")
        return True
    except Exception as e:
        print(f"{Fore.RED}[错误] 写入新机器ID失败: {str(e)}{Style.RESET_ALL}")
        return False

def main():
    """主函数"""
    print_banner()
    
    print(f"{Fore.YELLOW}[信息] 正在检测Cursor安装...{Style.RESET_ALL}")
    machine_id_path = get_machine_id_path()
    
    if os.path.exists(machine_id_path):
        print(f"{Fore.GREEN}[成功] 检测到Cursor安装，机器ID文件位于: {machine_id_path}{Style.RESET_ALL}")
        
        # 询问用户是否重置机器ID
        choice = input(f"{Fore.YELLOW}[询问] 是否重置机器ID? (y/n): {Style.RESET_ALL}").strip().lower()
        if choice == "y":
            if reset_machine_id():
                print(f"{Fore.GREEN}[成功] 机器ID重置完成，请重启Cursor应用{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[错误] 机器ID重置失败{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[信息] 已取消重置操作{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[错误] 未检测到Cursor安装，请先安装Cursor应用{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"
{Fore.YELLOW}[信息] 程序已被用户中断{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[错误] 程序发生异常: {str(e)}{Style.RESET_ALL}")
    
    # 等待用户按键退出
    input(f"
{Fore.CYAN}按任意键退出...{Style.RESET_ALL}")
