for i in range (1,1000):
    s = 0
    j = 1
    while(j < i):
        if(i % j == 0):
              s = s + j
        j += 1
    if i == s:
       print(i)