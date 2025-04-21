arquivo = open('texto.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Pratica')
arquivo.close()

#leitura do arquivo texto

leitura = open('texto.txt', 'r')
print(leitura.read())
leitura.close()