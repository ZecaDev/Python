notaA = float(input("Digite a nota A: "))
notaB = float(input("Digite a nota B: "))

#calcular media
mediafinal = (notaA + notaB) / 2

#verificaçao
if mediafinal >= 7.0:
    print("A Média: %.1f - Aprovado " % mediafinal)
else:
    print("A Média: %.1f - Reprovado " % mediafinal)