quantidade = 0
soma = 0
media  = 0
valor = float(input('Digite um valor: '))

while valor > 0.0:
    soma = soma + valor
    quantidade = quantidade + 1
    # Entrada de valores
    valor = float(input('Digite um valor: '))

#caso digite uma valor negativo o laço encerra
media = soma / quantidade
print("\n Total da Soma: {}".format(soma))
print("\n Quantidade de valores digitados: {}".format(quantidade))
print("\n Média dos valores: {}".format(media))
