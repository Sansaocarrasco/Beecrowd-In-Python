N = 1
i = 0
j = 0
k = 0
gre = 0
while (N==1):
    A, B = input().split()
    A = int(A)
    B = int(B)
    if (A>B):
        i=i+1
    elif (B>A):
        j=j+1
    else :
        k=k+1
    print("Novo grenal (1-sim 2-nao)");
    N = int(input())
    gre=gre+1
print("{} grenais".format(gre))
print("Inter:{}".format(i))
print("Gremio:{}".format(j))
print("Empates:{}".format(k))
if (i>j):
    print("Inter venceu mais")
elif (j>i):
    print("Gremio venceu mais")
else :
    print("Nao houve vencedor")
