#打印数字金字塔(如1，121， 12321， )
rows = int(input("请输入金字塔的行数："))

for i in range(1, rows+1):
    for j in range(rows-i):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end="")
    for j in range(i-1, 0, -1):
        print(j, end="")
    print()