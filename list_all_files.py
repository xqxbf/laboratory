import os

# 定义要遍历的根目录
base_dir = r"c:\Users\ASUS\Desktop\shiy实验室"
# 定义输出文件路径
output_file = os.path.join(base_dir, "all_files_list.txt")

# 收集所有文件的函数
def collect_files(directory):
    file_list = []
    # 遍历目录及其子目录
    for root, dirs, files in os.walk(directory):
        # 排除不需要的目录
        dirs[:] = [d for d in dirs if d not in ['__pycache__', '.vscode']]
        
        # 处理每个文件
        for file in files:
            # 计算相对路径
            relative_path = os.path.relpath(os.path.join(root, file), base_dir)
            file_list.append(relative_path)
    return file_list

# 主函数
def main():
    print(f"开始遍历文件夹: {base_dir}")
    
    # 收集所有文件
    files = collect_files(base_dir)
    
    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for file_path in files:
            f.write(f"{file_path}\n")
    
    print(f"遍历完成！")
    print(f"共找到 {len(files)} 个文件")
    print(f"文件名已保存到: {output_file}")

if __name__ == "__main__":
    main()
