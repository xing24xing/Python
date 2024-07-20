for i in range(1,100):
    c = 0
    j = 2
    while(j <= i/2):
       if i % j == 0:
          c = c + 1
       j = j + 1
    if c == 0:
         print(i)