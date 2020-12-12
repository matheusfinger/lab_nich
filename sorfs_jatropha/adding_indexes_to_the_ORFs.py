#Receveing the fasta file with the sequences of the ORFs
entry = open("entry.fa")
lines = entry.readlines()
entry.close()
#adding an index to the first ORF
lines[0] = lines[0].strip()
lines[0] = lines[0] + "_1\n"
#going through the var with the information of the fasta file
for i in range(0, len(lines)):
	#checking if it is a identification line
	if lines[i][0] == ">" and i != 0:
		parts1 = lines[i-2].split("_")
		parts2 = parts1[0]
		parts3 = lines[i][0:-1]
		#checking if the ORF belongs to the same contig of the previous ORF or if it belong to a new one
		if parts2 == parts3:
			##it will enter here if the ORF belongs to the same contig
			#adding one to the previous index
			parts4 = parts1[1].strip()
			index = int(parts4)+1
			#adding the new index to the ORF
			lines[i] = lines[i].strip()
			lines[i] = lines[i] + "_" + str(index) + "\n"
		else:
			##it will enter if the ORF belongs to another contig
			#adding the index to the ORF
			lines[i] = lines[i].strip()
			lines[i] = lines[i] + "_1\n"
#creating the result file
result = open('result.fa', 'w')
result.writelines(lines)
result.close()
