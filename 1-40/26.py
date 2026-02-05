#公鸡5元，母鸡3元，小鸡1元3只，100元买100只鸡
for rooster in range(20):
    for hen in range(33):
        for child in range(100):
            if (rooster + hen + 3*child) == 100 :
                if (5*rooster + 3*hen + child) == 100 :
                    print(f"公鸡{rooster}只，母鸡{hen}只，小鸡{child*3}只")