# 批量重命名文件

import os

def batch_rename_files(directory, prefix='', suffix='', start_index=1, zero_padding=3, dry_run=True):
    """
    批量重命名指定目录下的所有文件。

    :param directory: 目标文件夹路径
    :param prefix: 新文件名前缀
    :param suffix: 新文件名后缀（不含扩展名）
    :param start_index: 起始编号
    :param zero_padding: 编号补零位数
    :param dry_run: 是否仅预览，不实际重命名
    :return: 包含 (旧文件名, 新文件名) 的列表
    """
    renamed_list = []
    files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

    for idx, filename in enumerate(files, start=start_index):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}{str(idx).zfill(zero_padding)}{suffix}{ext}"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        renamed_list.append((filename, new_name))

        if not dry_run:
            os.rename(old_path, new_path)

    return renamed_list


if __name__ == "__main__":
    # 示例用法
    target_dir = input("请输入要处理的文件夹路径：")
    prefix_input = input("请输入新文件名前缀（可留空）：")
    suffix_input = input("请输入新文件名后缀（可留空，不含扩展名）：")
    start = int(input("请输入起始编号（默认1）：") or "1")
    padding = int(input("请输入编号补零位数（默认3）：") or "3")
    dry = input("是否仅预览？（y/n，默认y）：").strip().lower() != 'n'

    results = batch_rename_files(target_dir, prefix_input, suffix_input, start, padding, dry)
    print("\n预览结果：" if dry else "\n重命名完成：")
    for old, new in results:
        print(f"{old}  ->  {new}")
