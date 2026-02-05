# 安装和使用pip安装的库

import os
import importlib
import time

try:
    import requests
except ImportError:
    print("requests 库未安装，正在安装...")
    time.sleep(1)
    os.system("pip install requests")
else:
    print(requests.__version__)
    print("尝试访问（https://cn.bing.com/）")
    time.sleep(1)
    response = requests.get("https://cn.bing.com/")
    print("\n状态码:", response.status_code)
    time.sleep(1)
    print("\n响应内容:", response.text)
