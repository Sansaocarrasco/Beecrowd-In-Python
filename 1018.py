N = int(input())
if(0 < N and N < 1000000):
    print(N)
    n100 = N/100
    print("%d nota(s) de R$ 100,00" % n100)
    N = int(N%100)
    n50 = N/50
    print("%d nota(s) de R$ 50,00" % n50)
    N = int(N%50)
    n20 = N/20
    print("%d nota(s) de R$ 20,00" % n20)
    N = int(N%20)
    n10 = N/10
    print("%d nota(s) de R$ 10,00" % n10)
    N = int(N%10)
    n5 = N/5
    print("%d nota(s) de R$ 5,00" % n5)
    N = int(N%5)
    n2 = N/2
    print("%d nota(s) de R$ 2,00" % n2)
    N = int(N%2)
    n1 = N/1
    print("%d nota(s) de R$ 1,00" % n1)
