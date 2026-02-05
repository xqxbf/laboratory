# 创建并使用自定义模块

import _110 as my_module

# 示例1：使用 safe_run 装饰器
def risky_operation(a, b):
    """可能抛出异常的操作"""
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b

# 使用 safe_run 装饰器包装函数
safe_risky = my_module.safe_run(default={"code": 500, "msg": "操作失败"})(risky_operation)

# 调用包装后的函数
result1 = safe_risky(10, 2)  # 正常执行
result2 = safe_risky(10, 0)  # 发生异常，返回默认值

print("示例1结果:")
print(f"10/2 = {result1}")
print(f"10/0 = {result2}")

# 示例2：使用 build_result 函数
print("\n示例2结果:")
success_result = my_module.build_result(data={"name": "Alice", "age": 30})
error_result = my_module.build_result(code=400, msg="参数错误")

print(f"成功结果: {success_result}")
print(f"错误结果: {error_result}")

# 示例3：使用 BizException
print("\n示例3结果:")
try:
    raise my_module.BizException(code=403, msg="权限不足")
except my_module.BizException as e:
    print(f"捕获到业务异常: {e}")
    error_response = my_module.build_error_result(e)
    print(f"错误响应: {error_response}")
