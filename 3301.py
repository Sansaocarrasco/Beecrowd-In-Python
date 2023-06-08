H,Z,L = input().split()
H = int(H)
Z = int(Z)
L = int(L)

if (H>L and H<Z):
    print("huguinho")
if (H<L and H>Z):
    print("huguinho")
if (L>H and L<Z):
    print("luisinho")
if (L<H and L>Z):
    print("luisinho")
if (Z>H and Z<L):
    print("zezinho")
if (Z<H and Z>L):
    print("zezinho")
