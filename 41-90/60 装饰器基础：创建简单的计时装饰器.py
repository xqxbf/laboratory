#装饰器基础：创建简单的计时装饰器

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time} 秒")
        return result
    return wrapper

@timer_decorator
def slow_function(seconds):
    time.sleep(seconds)
    return f"函数执行了 {seconds} 秒"

slow_function(2)
