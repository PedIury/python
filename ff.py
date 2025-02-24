def nota():
    n=float(input("DIgite sua nota: "))	
    return n
def resultado(n1,n2):
    media=(n1+n2)/2
    print("nota 1: " ,n1)
    print("nota 2: " ,n2)
    print("Media:", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    elif media >= 4:
        print("Avaliaçao Final")
    else:
        print("Reprovado")

a = nota()
b = nota()
resultado(a,b)


    