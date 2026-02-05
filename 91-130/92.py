# 多种方式读取文件内容

"""读取整个文件"""
with open('sample.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("整个文件内容：")
    print(content)

"""逐行读取"""
print("\n逐行读取：")
with open('sample.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

"""读取所有行到列表"""
with open('sample.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"\n共有{len(lines)}行")
