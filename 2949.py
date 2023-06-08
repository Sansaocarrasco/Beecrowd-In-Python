N = int(input())
X = 0
H = 0
E = 0
A = 0
M = 0
while(N>0):
    nome, esp = input().split()
    nome = str(nome)
    esp = (esp)
    if (esp == 'X'):
        X = X + 1
    if (esp == 'H'):
        H = H + 1
    if (esp == 'E'):
        E = E + 1
    if (esp == 'A'):
        A = A + 1
    if (esp == 'M'):
        M = M + 1
    N = N-1
print ("%d Hobbit(s)" %X)
print ("%d Humano(s)" %H)
print ("%d Elfo(s)" %E)
print ("%d Anao(s)" %A)
print ("%d Mago(s)" %M)
