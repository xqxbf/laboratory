# 词汇测试程序 从文件读取词汇

import random

def load_words(file_path):
    """从指定文件读取单词列表，每行一个单词"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("文件未找到，请确认路径正确。")
        return []

def quiz(words):
    """随机抽取单词进行拼写测试"""
    if not words:
        print("词库为空，无法开始测试。")
        return
    random.shuffle(words)
    score = 0
    for word in words:
        answer = input(f"请输入单词拼写（提示：{word[0]}...{word[-1]}）: ")
        if answer.strip().lower() == word.lower():
            print("正确！")
            score += 1
        else:
            print(f"错误！正确拼写：{word}")
    print(f"测试完成，得分：{score}/{len(words)}")

if __name__ == "__main__":
    file_path = input("请输入词汇文件路径：")
    word_list = load_words(file_path)
    if word_list:
        quiz(word_list)
