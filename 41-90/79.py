from collections import Counter

def count_elements(lst):
    """
    统计列表中元素出现次数
    :param lst: 输入列表
    :return: 字典，键为元素，值为出现次数
    """
    return dict(Counter(lst))

# 示例用法
if __name__ == "__main__":
    list = []
    
    str = input("请输入：")
    list.extend(str.split())
    
    print(count_elements(list))
