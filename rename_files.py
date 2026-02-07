import os
import re

# 定义要处理的文件夹路径
base_dir = r"c:\Users\ASUS\Desktop\shiy实验室"
folder_paths = [
    os.path.join(base_dir, "1-40"),
    os.path.join(base_dir, "41-90"),
    os.path.join(base_dir, "91-130")
]

# Windows文件名不允许的字符
invalid_chars = '<>:"/\\|?*'

# 清理文件名中的无效字符
def clean_filename(filename):
    for char in invalid_chars:
        filename = filename.replace(char, '')
    # 移除多余的空格
    filename = ' '.join(filename.split())
    return filename

# 处理每个文件夹
for folder_path in folder_paths:
    if not os.path.exists(folder_path):
        print(f"文件夹不存在: {folder_path}")
        continue
    
    print(f"处理文件夹: {folder_path}")
    
    # 遍历文件夹中的文件
    for filename in os.listdir(folder_path):
        # 只处理.py文件（包括.PY等大小写变体）
        if not filename.lower().endswith('.py'):
            continue
        
        # 跳过__pycache__文件夹和其他非Python文件
        if filename == "__pycache__":
            continue
        
        file_path = os.path.join(folder_path, filename)
        if not os.path.isfile(file_path):
            continue
        
        try:
            # 读取文件第一行
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                first_line = f.readline().strip()
            
            # 提取#后面的内容
            if first_line.startswith('#'):
                description = first_line[1:].strip()
            else:
                description = ""
            
            # 提取序号部分（文件名中最后一个.之前的数字部分）
            name_part = filename.rsplit('.', 1)[0]
            # 提取数字部分
            number_match = re.match(r'^[_\s]*([0-9]+)', name_part)
            if number_match:
                number = number_match.group(1)
            else:
                number = name_part
            
            # 构造新文件名
            if description:
                new_name = f"{number} {description}.py"
            else:
                new_name = filename
            
            # 清理文件名
            new_name = clean_filename(new_name)
            
            # 确保文件名长度合理
            if len(new_name) > 255:
                # 截断描述部分
                max_desc_length = 255 - len(number) - 5  # 5 = 空格 + .py
                if max_desc_length > 0:
                    truncated_desc = description[:max_desc_length]
                    new_name = f"{number} {truncated_desc}.py"
                    new_name = clean_filename(new_name)
                else:
                    new_name = f"{number}.py"
            
            new_file_path = os.path.join(folder_path, new_name)
            
            # 避免文件名冲突
            counter = 1
            while os.path.exists(new_file_path) and new_file_path != file_path:
                if description:
                    new_name = f"{number} {description} ({counter}).py"
                else:
                    new_name = f"{number} ({counter}).py"
                new_name = clean_filename(new_name)
                new_file_path = os.path.join(folder_path, new_name)
                counter += 1
            
            # 执行重命名
            if new_file_path != file_path:
                os.rename(file_path, new_file_path)
                print(f"重命名: {filename} -> {new_name}")
            else:
                print(f"跳过: {filename} (无需修改)")
                
        except Exception as e:
            print(f"处理文件失败 {filename}: {str(e)}")

print("\n重命名操作完成！")
