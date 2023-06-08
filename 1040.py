N1,N2,N3,N4 = input().split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
media = (N1*2+N2*3+N3*4+N4*1)/10
print("Media: %.1f" % media)
if (media >= 7.0):
    print("Aluno aprovado.")
elif (media < 5.0):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota = float(input())
    media = (media + nota)/2
    print("Nota do exame: %.1f" % nota)
    if (media >= 5.0):
        print("Aluno aprovado.")
        print("Media final: %.1f" % media)
    else:
        print("Aluno reprovado.")
