# 处理异常并抛出新异常

import os


class FileManager:
    def __init__(self, base_path: str):
        self.base_path = base_path

    def create_file(self, filename: str, content: str = ""):
        """创建文件，若失败则抛出自定义异常"""
        try:
            full_path = os.path.join(self.base_path, filename)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except (OSError, IOError) as e:
            # 捕获底层异常并抛出自定义异常
            raise FileManageException(f"无法创建文件 {filename}") from e

    def delete_file(self, filename: str):
        """删除文件，若失败则抛出自定义异常"""
        try:
            full_path = os.path.join(self.base_path, filename)
            os.remove(full_path)
        except (OSError, IOError) as e:
            raise FileManageException(f"无法删除文件 {filename}") from e

    def read_file(self, filename: str) -> str:
        """读取文件，若失败则抛出自定义异常"""
        try:
            full_path = os.path.join(self.base_path, filename)
            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read()
        except (OSError, IOError) as e:
            raise FileManageException(f"无法读取文件 {filename}") from e

class FileManageException(Exception):
    """文件管理相关异常"""
    pass

fm = FileManager("/tmp")
fm.create_file("demo.txt", "hello")
print("文件已创建")
