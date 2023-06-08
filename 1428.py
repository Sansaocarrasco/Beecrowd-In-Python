t = int(input())
while (t>0):
    n,m = input().split()
    n = int(n)
    m = int(m)
    n = n//3
    m = m//3
    prod = m*n
    print("%d" % prod)
    t = t-1

