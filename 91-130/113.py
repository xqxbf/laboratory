# 创建具有层次结构的包

# 顶层包
import os

# 定义包结构
package_structure = {
    "my_package": {
        "__init__.py": "# 顶层包初始化",
        "subpkg1": {
            "__init__.py": "# 子包1初始化",
            "module1.py": "# 子包1模块1",
            "module2.py": "# 子包1模块2"
        },
        "subpkg2": {
            "__init__.py": "# 子包2初始化",
            "subsubpkg": {
                "__init__.py": "# 子子包初始化",
                "module3.py": "# 子子包模块3"
            }
        }
    }
}

def create_package(base_path, structure):
    """递归创建包目录和文件"""
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_package(path, content)
        else:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content + '\n')

# 在当前目录创建包
create_package('.', package_structure)
