N = int(input())
j = 0
while (N>0):
    i = input().split()
    i = int(i)
    j = i-1+j
    N = N-1
print("%d" % j)
