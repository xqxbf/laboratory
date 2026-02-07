#多种方法字符串反转

def reverse_string1(s):
    return s[::-1]

def reverse_string2(s):
    return ''.join(reversed(s))

str = input("请输入一个字符串：")
#测试reverse_string1函数
print(reverse_string1(str))  # 输出: "olleh"
#测试reverse_string2函数
print(reverse_string2(str))  # 输出: "olleh"
