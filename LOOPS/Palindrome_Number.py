for i in range(1,100):
    s = 0
    j = i
    while (j > 0):
        r = int(j % 10)
        s = s * 10 + r;
        j = int(j / 10)
        # print(j)
    if i == s:
        print(i)
