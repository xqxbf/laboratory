#判断一个数是否为回文数
num = int(input("请输入一个整数："))

def is_palindrome_math(num) :
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    reversed_num = 0
    while num > reversed_num:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return num == reversed_num or num == reversed_num // 10

if is_palindrome_math(num):
    print(f"{num}是回文数")
else:
    print(f"{num}不是回文数")