# 创建一个简单的日志记录系统

import logging

import sys
import os
from datetime import datetime

def setup_logger(name="my_logger", log_level=logging.DEBUG, log_dir="logs"):
    """
    配置并返回日志记录器
    
    Args:
        name: 日志记录器名称
        log_level: 日志级别
        log_dir: 日志文件存储目录
    
    Returns:
        配置好的日志记录器对象
    """
    # 确保日志目录存在
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 创建日志记录器
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # 避免重复添加处理器
    if not logger.handlers:
        # 创建控制台处理器并设置级别为DEBUG
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        
        # 创建文件处理器并设置级别为INFO
        log_filename = os.path.join(log_dir, f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
        file_handler = logging.FileHandler(log_filename, encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        
        # 创建格式化器
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        # 将格式化器添加到处理器
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        
        # 将处理器添加到日志记录器
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    
    return logger

# 示例用法
if __name__ == "__main__":
    # 获取配置好的日志记录器
    logger = setup_logger()
    
    # 记录不同级别的日志
    logger.debug("这是一条调试信息")
    logger.info("这是一条普通信息")
    logger.warning("这是一条警告信息")
    logger.error("这是一条错误信息")
    logger.critical("这是一条严重错误信息")
    
    print("日志记录完成，请查看控制台输出和logs目录中的日志文件")
