# 确保资源被正确释放
import contextlib

# 使用上下文管理器确保资源正确释放
@contextlib.contextmanager
def managed_resource():
    resource = open('example.txt', 'w')  # 假设打开一个文件资源
    try:
        yield resource
    finally:
        resource.close()  # 确保资源被释放

# 使用示例
with managed_resource() as res:
    res.write('Hello, world!')
# 离开 with 块时，资源会被自动关闭和释放
