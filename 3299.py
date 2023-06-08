N = int(input())
X = N
es = 0
while(X > 1):
    Y = X%10
    X = X//10
    if (Y == 3):
        if(X%10 == 1):
            print("%d es de Mala Suerte" %N)
            es = 1
            break
if (not (es)):
    print("%d NO es de Mala Suerte" %N)
