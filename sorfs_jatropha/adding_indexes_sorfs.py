#Opening fasta file
entry = open("entry.fa")
lines = entry.readlines()
entry.close()
entry2 = open("titulos_sorfs.txt")
titulos = entry2.readlines()
entry2.close()
contador = 1
resultado = []
for i in range(0, len(lines)):
	if lines[i][0] == ">":
		titulo = titulos[contador].split(" ")
		titulo = ">" + titulo[1][1:-2] + "\n"
		resultado.append(titulo)
		contador = contador + 1
	else:
		resultado.append(lines[i])
result = open('result.fa', 'w')
result.writelines(resultado)
result.close()
