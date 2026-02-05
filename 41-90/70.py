# 验证字符串是否符合特定格式

str = input("请输入一个字符串（全小写）：")

str_format = str.strip().lower()

if str == str_format:
    print("字符串符合特定格式")
else:
    print("字符串不符合特定格式")

