N = int(input())
while(N>0):
    h,d,g = input().split()
    h = int(h)
    d = int(d)
    g = int(g)
    if (h >= 200 and h <= 300):
        if (d >= 50):
            if (g>= 150):
                print("Sim")
            else :
                print("Nao")
        else :
            print("Nao")
    else :
        print("Nao")
    N=N-1

     
