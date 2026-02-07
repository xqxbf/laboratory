# 创建自定义上下文管理器

import contextlib

class MyContext:
    """
    自定义上下文管理器
    用于在进入和退出上下文时执行特定操作
    """
    def __enter__(self):
        print("进入上下文")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出上下文")
        # 返回 False 表示异常继续抛出；True 则抑制异常
        return False

@contextlib.contextmanager
def my_context():
    """
    自定义上下文管理器的生成器函数
    用于在进入和退出上下文时执行特定操作
    """
    print("进入上下文")
    yield
    print("退出上下文")


# 使用示例
with MyContext():
    print("在上下文中执行")

with my_context():
    print("在上下文中执行")
