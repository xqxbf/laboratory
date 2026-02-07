# 使用argparse 处理命令行参数

import argparse
import os
import time

def file_info(path, output_file=None):
    """获取文件行数、字符数、修改时间等信息
    
    :param path: 文件路径
    :param output_file: 输出文件路径，为None时输出到控制台
    """
    if not os.path.isfile(path):
        result = f"错误：'{path}' 不是一个有效的文件"
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result + '\n')
        else:
            print(result)
        return

    # 行数
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = sum(1 for _ in f)

    # 字符数（含换行）
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        chars = sum(len(line) for line in f)

    # 修改时间
    mtime = os.path.getmtime(path)
    mtime_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))

    # 生成结果
    result = []
    result.append(f"文件: {path}")
    result.append(f"行数: {lines}")
    result.append(f"字符数: {chars}")
    result.append(f"修改时间: {mtime_str}")
    result_str = '\n'.join(result)

    # 输出结果
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result_str + '\n')
        print(f"处理完成，结果已保存到: {output_file}")
    else:
        print(result_str)

def main():
    parser = argparse.ArgumentParser(description='查看文件行数、字符数、修改时间等信息')
    parser.add_argument('-f', '--file', help='目标文件路径')
    parser.add_argument('-o', '--output', help='输出文件路径')
    args = parser.parse_args()

    # 如果没有提供参数，默认显示帮助信息
    if not args.file:
        parser.print_help()
        return
    
    file_info(args.file, args.output)

if __name__ == '__main__':
    main()

