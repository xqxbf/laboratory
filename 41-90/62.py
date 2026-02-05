#判断字符串是否回文

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

str = input("请输入一个字符串：")
#测试is_palindrome函数
print(is_palindrome(str))  # 输出: True