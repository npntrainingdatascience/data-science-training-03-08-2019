for i in range(1,10):
    for j in (2,i):
        if i%j==0:
            break
    else:
        print(i)
