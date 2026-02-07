# 验证用户输入的完整性

def validate_user_input(user_input: dict) -> bool:
    """
    验证用户输入的完整性
    返回 True 表示所有必填字段均已提供且非空，否则返回 False
    """
    required_fields = ["username", "email", "password"]
    for field in required_fields:
        if field not in user_input or not user_input[field].strip():
            return False
    return True

# 调用函数进行示例
example_input = {
    "username": "alice",
    "email": "alice@example.com",
    "password": "123456"
}

if validate_user_input(example_input):
    print("输入完整")
else:
    print("输入不完整")
