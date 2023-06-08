H, E, A, O, W, X = input().split()
H = int(H)
E = int(E)
A = int(A)
O = int(O)
W = int(W)
X = int(X)
bem = (H+E+A+X)
mal = (O+W)
if (bem<mal):
    print("Sauron has returned.")
else :
    print("Middle-earth is safe.")
