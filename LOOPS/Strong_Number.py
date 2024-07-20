for i in range (1,50000):
    s = 0
    j = i
    while(j > 0):
        r = int(j % 10)
        f = 1
        for n in range(1,r+1):
              f = f * n
        s += f
        j = int(j/10)
    if(s == i):
        print(i)