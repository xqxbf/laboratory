# 一个except处理多个异常

import traceback

try:
    # 一些可能会引发异常的代码
    result = 10 / 0
except (ZeroDivisionError, ValueError) as e:
    # 处理 ZeroDivisionError 和 ValueError 异常
    print(f"发生异常: {e}")
    traceback.print_exc()
