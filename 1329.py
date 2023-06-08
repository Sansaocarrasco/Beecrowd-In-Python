while(1):
    N = int(input())
    if (N==0):
        break
    ma = 0
    jo = 0
    while(N>0):
        x = int(input())
        if (x == 0):
            ma = ma+1
        elif(x == 1):
            jo = jo+1
        N=N-1
    print("Mary won {} times and John won {} times".format(ma,jo))
