for i in range(100, 1000):
    total = 0
    tmp = i
    while tmp != 0:
        total += (tmp % 10) ** 3
        tmp //= 10
    if total == i:
        print(i)