#统计英文句子中的单词数

def count_words(sentence: str) -> int:
    """
    统计给定英文句子中的单词数量。
    以空白字符（空格、制表符、换行等）作为分隔符。
    """
    words = sentence.strip().split()
    return len(words)

s = input("请输入英文句子：")
print("单词数：", count_words(s))
