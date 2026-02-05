#定义计算圆面积的函数
def circle_area(radius):
    return 3.14 * radius ** 2

n = float(input("请输入圆的半径："))
print("圆的面积为", circle_area(n))