X = int(input())
while(1):
    Y = int(input())
    if (Y>X):
        break
i = 0
j = 1
while(X<Y):
    X = X+i
    i = X+j
    j = j+1
print("%d" % j)
