arquivo1 = open("orfs_jatropha_nolinebreak.fa")
fasta = arquivo1.readlines()
arquivo1.close()
result = []
for index1 in range(0, len(fasta)):
	linha = fasta[index1]
	if linha[0] == ">":
		if int(linha[3:9]) % 10 == 0:
			print(linha[3:9]) 
		temN = False
		palavra = fasta[index1+1]
		for letra in palavra:
			if letra == 'N' or letra == 'n':
				temN = True
				break
		if temN == False:
			result.append(linha)
			result.append(palavra)
arq_result = open('orfs_semN.fa', 'w')
arq_result.writelines(result)
arq_result.close()
