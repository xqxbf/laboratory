# 统计文本中单词出现的频率

import sys

text = input("请输入文本：")
if text == "exit" :
    sys.exit(0)
    
text_list = text.split()
word_count = {}
for word in text_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"{word}: {count}", end='    ')
