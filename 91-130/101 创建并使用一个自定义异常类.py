# 创建并使用一个自定义异常类

class NegativeDivisorError(Exception):
    """除数不能为负数"""
    def __init__(self, message="除数不能为负数"):
        """初始化自定义异常类"""
        self.message = message
        super().__init__(self.message)

def divide(a, b) -> float:
    """
    执行除法操作，若除数为负数则抛出自定义异常
    
    Args:
        a: 被除数
        b: 除数
    
    Returns:
        商
    
    Raises:
        NegativeDivisorError: 当除数为负数时抛出
    """
    if b < 0:
        raise NegativeDivisorError("除数不能为负数")
    return a / b

try:
    result = divide(10, -2)
except NegativeDivisorError as error:
    print("Error: ", error.message)
