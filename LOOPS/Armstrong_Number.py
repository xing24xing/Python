for i in range(1,10000):
    s = 0
    j = i
    while(j > 0):
        r = int(j % 10)
        s += r * r * r
        j = int(j / 10)
    if(i == s):
        print(i)