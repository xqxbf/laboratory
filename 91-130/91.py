# 创建文件并写入内容

with open("sample.txt", 'w', encoding='utf-8') as f:
    f.write("这是第一行\n")
    f.write("这是第二行\n")
    f.write("这是第三行\n")

print("文件写入完成")

