# 处理网络请求中的异常

import requests
import os
import logging

# 配置日志记录
if not os.path.exists("logs"):
    os.makedirs("logs")
    log_file = os.path.join("logs", "url_requests.log")
else:
    log_file = os.path.join("logs", "url_requests.log")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename=log_file)
logger = logging.getLogger("url_requests")


def url_requests(url, method="GET"):
    """
    发起 HTTP 请求
    :param url: 请求地址
    :param method: 请求方法，默认 GET
    :return: (success: bool, response: requests.Response or None, error: str or None)
    """
    try:
        resp = requests.request(method, url)
        resp.raise_for_status() # 如果状态码非 200 系列会抛出 HTTPError
        return True, resp, None
    except requests.Timeout:
        return False, None, "请求超时，请稍后重试"
    except requests.ConnectionError:
        return False, None, "网络连接失败，请检查网络设置"
    except requests.HTTPError as e:
        return False, None, f"HTTP错误：{e.response.status_code} {e.response.status}"


def __main__():
    url = input("请输入URL(记得带协议)：")
    method = input("请输入请求方法(GET/POST)：")
    method = method.upper()
    if method not in ["GET", "POST"]:
        logger.error(f"不支持的请求方法：{method}")
        return
    success, resp, err = url_requests(url, method)
    if success:
        logger.info(f"请求成功，状态码：{resp.status_code}")
        with open('response.html', 'w', encoding='utf-8') as f:
            f.write(resp.text)
        logger.info("响应内容已保存到 response.html")
    else:
        logger.error(f"请求失败：{err}")
    print("处理完成，请在logs目录下查看日志文件")

__main__()

