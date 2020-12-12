#Opening fasta file
entry = open("entry.fa")
lines = entry.readlines()
entry.close()
#creating variable where the full file without the line break will be stored
new = []
#creating variable that stores the sequences without the line break
string = ""
print(len(lines))
#going through the variable with the entry file by index
for i in range(0, len(lines)):
	#verifying if it is an identifier
	if lines[i][0] == ">":
		#adding the previous sequence before the identifier (which will be complete and without line breaks)
		new.append(string)
		#adding the line with the identifier
		new.append(lines[i])
	#verifying if it is the first line after the identifier
	elif lines[i-1][0] == ">":
		#adding the first line of the sequence in the variable string 
		string = lines[i]
	#it will enter here if it is the continuation of a sequence after the line break
	else:
		#removing the line break in the end of the variable string
		string = string.strip()
		#adding the continuation of the sequence in the variable string
		string = string + lines[i]
		#verificando se é o final do arquivo
#adding the last sequence
new.append(string)
#making a new file with the result
result = open('result.fa', 'w')
result.writelines(new)
result.close()
