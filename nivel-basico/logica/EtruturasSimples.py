A = input("Informe um valor para a varável A: ")
B = input("Informe um valor para a varável B: ")

if (A > B):
    aux=A;
    A=B;
    B=aux;
print("O valor da variável A agora é : ", A)
print("O valor da variável B agora é : ", B)

idade = int (input ("Digite a idade da pessoa: "))
if idade > 18:
    print("Maior de idade")
else:
    print("Menor de idade")
