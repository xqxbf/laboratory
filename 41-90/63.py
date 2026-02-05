#统计字符串中各字符出现次数

def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

str = input("请输入一个字符串：")

result = count_characters(str)
for char, cnt in result.items():
    print(f"{char}: {cnt}")
