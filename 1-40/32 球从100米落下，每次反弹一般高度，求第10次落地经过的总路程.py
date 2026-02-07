#球从100米落下，每次反弹一般高度，求第10次落地经过的总路程
height = 100
sum = 100

for _ in range(1, 10):
    height /= 2
    sum += height 

print(f"第10次落地经过的总路程是：{sum}米")
