# 备份指定目录的文件

import os
import time
import logging
import shutil
import sys


def backup_directory(directory_path, backup_path):
    """
    备份指定目录下的所有文件到备份目录
    :param directory_path: 待备份的目录路径
    :param backup_path: 备份目录路径
    """

    # 检查目录是否存在
    logging.debug(f"检查目录是否存在: {directory_path}")
    if not os.path.exists(directory_path):
        logging.error(f"目录 {directory_path} 不存在")
        return

    logging.debug(f"检查备份目录是否存在: {backup_path}")
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)
        logging.info(f"创建备份目录 {backup_path}")

    logging.debug(f"查看备份目录 {directory_path} 下的文件: {os.listdir(directory_path)}")
    # 查看指定目录下的文件列表（带序号）
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    logging.info(f"待备份目录 {directory_path} 中的文件列表：")
    for idx, file in enumerate(files, start=1):
        logging.info(f"{idx}. {file}")


    logging.debug(f"开始备份目录 {directory_path} 到 {backup_path}")
    # 遍历目录下所有文件
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            # 构建备份文件路径
            backup_item_path = os.path.join(backup_path, item)
            # 复制文件
            shutil.copy2(item_path, backup_item_path)
            logging.info(f"备份文件 {item} 到 {backup_item_path}")

if __name__ == "__main__":
    try:
        # 配置日志
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        
        directory_path = input("请输入待备份的目录路径: ")
        backup_path = input("请输入备份目录路径: ")
        backup_directory(directory_path, backup_path)
        print("备份完成")
    
    except KeyboardInterrupt:
        logging.info("备份操作被用户中断")
    except Exception as e:
        logging.error(f"备份过程中发生错误: {e}")
    finally:
        sys.exit(0)

