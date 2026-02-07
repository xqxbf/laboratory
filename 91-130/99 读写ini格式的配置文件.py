# 读写ini格式的配置文件

import os
import logging
import configparser


def read_ini(file_path, encoding='utf-8') -> configparser.ConfigParser:
    """
    读取 ini 配置文件
    :param file_path: ini 文件路径
    :param encoding: 文件编码，默认 utf-8
    :return: 成功返回 configparser.ConfigParser 对象；失败返回 None
    """
    if not os.path.isfile(file_path):
        logger.error(f"文件不存在：{file_path}")
        return None

    cfg = configparser.ConfigParser()
    try:
        cfg.read(file_path, encoding=encoding)
        return cfg
    except configparser.MissingSectionHeaderError:
        logger.error(f"缺少节标题，文件格式错误：{file_path}")
    except configparser.ParsingError as e:
        logger.error(f"解析 ini 文件失败：{file_path}\n详情：{e}")
    except Exception as e:
        logger.error(f"读取 ini 文件时发生未知错误：{file_path}\n详情：{e}")
    return None

import logging
logger = logging.getLogger("my_logger")

def write_ini(file_path, data, encoding='utf-8') -> bool:
    """
    写入 ini 配置文件
    :param file_path: 目标 ini 文件路径
    :param data: dict，格式如 {"section": {"key": "value"}}
    :param encoding: 文件编码，默认 utf-8
    :return: 成功返回 True；失败返回 False
    """
    cfg = configparser.ConfigParser()

    # 将外部传入的字典写入 ConfigParser
    for section, kv_map in data.items():
        cfg.add_section(section)
        for k, v in kv_map.items():
            cfg.set(section, k, str(v))

    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding=encoding) as f:
            cfg.write(f)
        return True
    except PermissionError:
        logger.error(f"没有权限写入文件：{file_path}")
    except Exception as e:
        logger.error(f"写入 ini 文件时发生未知错误：{file_path}\n详情：{e}")
    return False

import logging
logger = logging.getLogger("my_logger")

def main() -> None:
    """
    主程序示例：读取一个 ini 文件，修改后再写回
    """

    ini_file = input("请输入 ini 文件路径 (如果在当前目录下，直接输入文件名即可)：")

    # 读取
    cfg = read_ini(ini_file or "settings.ini")
    if cfg is None:
        logger.error("读取失败，程序结束。")
        return

    # 示例：修改或新增
    if not cfg.has_section("General"):
        cfg.add_section("General")
    cfg.set("General", "language", "zh-CN")

    # 将 ConfigParser 对象转回字典，便于调用写函数
    data_to_write = {s: dict(cfg.items(s)) for s in cfg.sections()}

    # 写回
    if write_ini(ini_file, data_to_write):
        logger.info("配置文件已成功更新。")
    else:
        logger.error("配置文件写入失败。")


if __name__ == "__main__":
    main()
