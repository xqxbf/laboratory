# 综合的错误处理框架

import logging
import traceback
from functools import wraps
from typing import Callable, Any, Optional
import time

# 统一日志配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("ErrorHandler")


class BizException(Exception):
    """业务异常基类"""
    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg
        super().__init__(f"[{code}] {msg}")


class SysException(Exception):
    """系统异常基类"""
    pass


def safe_run(
    default: Any = None,
    *,
    swallow: bool = True,
    log_traceback: bool = True,
    reraise_biz: bool = False
) -> Callable:
    """
    通用安全执行装饰器
    :param default: 发生异常时的默认返回值
    :param swallow: 是否吞掉异常
    :param log_traceback: 是否记录完整堆栈
    :param reraise_biz: 业务异常是否继续抛出
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                return func(*args, **kwargs)
            except BizException as be:
                if log_traceback:
                    logger.warning(f"BizException in {func.__name__}: {be}")
                if reraise_biz:
                    raise
                return default
            except Exception as e:
                if log_traceback:
                    logger.error(f"Unexpected error in {func.__name__}: {e}\n{traceback.format_exc()}")
                if not swallow:
                    raise
                return default
        return wrapper
    return decorator


def retry(
    times: int = 3,
    delay: float = 0,
    exceptions: tuple = (Exception,)
) -> Callable:
    """
    重试装饰器
    :param times: 最大重试次数
    :param delay: 重试间隔秒数
    :param exceptions: 触发重试的异常类型
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exc: Optional[Exception] = None
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exc = e
                    if i < times - 1 and delay > 0:
                        time.sleep(delay)
            raise last_exc or RuntimeError("All retries failed")
        return wrapper
    return decorator


# 统一返回结构
def build_result(
    code: int = 0, 
    msg: str = "success", 
    data: Any = None
) -> dict:
    """
    构建统一返回结构
    :param code: 状态码，默认0表示成功
    :param msg: 状态描述，默认"success"
    :param data: 业务数据，默认None
    """
    return {"code": code, "msg": msg, "data": data}


def build_error_result(exc: Exception) -> dict:
    """
    构建错误返回结构
    :param exc: 捕获的异常对象
    """
    if isinstance(exc, BizException):
        return build_result(code=exc.code, msg=exc.msg)
    logger.exception("System error")
    return build_result(code=500, msg="Internal Server Error")


# 全局异常捕获中间件（示例）
class GlobalErrorMiddleware:
    """
    全局异常捕获中间件
    :param app: WSGI应用
    """
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        try:
            return self.app(environ, start_response)
        except Exception as e:
            response = build_error_result(e)
            # 这里可按需序列化并返回
            start_response("500 Internal Server Error", [("Content-Type", "application/json")])
            return [str(response).encode()]
