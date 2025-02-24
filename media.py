def nota():
    av1 = float(input('nota da av1:'))
    av2 = float(input('nota da av2:'))
    media = (av1 + av2) / 2
    return media

media = nota()

resultado = "Aprovado" if media >= 7 else "avf" if media >= 4 else "Reprovado"
print(resultado)


