# 查找子串出现的所有位置

def find_all_occurrences(text: str, sub: str) -> list[int]:
    """
    查找子串 sub 在 text 中出现的所有位置（起始索引），
    返回一个升序的索引列表。如果子串不存在，返回空列表。
    """
    positions = []
    start = 0
    while True:
        idx = text.find(sub, start)
        if idx == -1:
            break
        positions.append(idx)
        start = idx + 1 
    return positions


# 示例用法
if __name__ == "__main__":
    s = "ababcababc"
    sub = "abc"
    print(*find_all_occurrences(s, sub), end=' ')
