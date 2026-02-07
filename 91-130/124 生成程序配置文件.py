# 生成程序配置文件

import json
import os

# 默认配置项
DEFAULT_CONFIG = {
    "debug": False,
    "host": "127.0.0.1",
    "port": 8080,
    "log_level": "INFO",
    "database": {
        "type": "sqlite",
        "path": "data.db"
    }
}

def generate_config_file(config_path="config.json"):
    """
    根据 DEFAULT_CONFIG 生成 JSON 配置文件
    :param config_path: 配置文件保存路径
    """
    # 确保目录存在
    os.makedirs(os.path.dirname(config_path) or ".", exist_ok=True)
    # 写入配置
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(DEFAULT_CONFIG, f, ensure_ascii=False, indent=4)
    print(f"配置文件已生成: {os.path.abspath(config_path)}")

try:
    if __name__ == "__main__":
        generate_config_file()
except Exception as e:
    print(f"生成配置文件时出错: {e}")
