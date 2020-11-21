#Receveing the fasta file with the sequences of the parts (introns, exons or others) of the transcripts
entry = open("entry.fa")
lines = entry.readlines()
entry.close()
#adding an index to the first sequence
lines[0] = lines[0].strip()
lines[0] = lines[0] + "_1\n"
#going through the var with the information of the fasta file
for i in range(0, len(lines)):
	#checking if it is a identification line
	if lines[i][0] == ">" and i != 0:
		#checking if the sequence belongs to the same transcript of the previous sequence or if it belong to a new one
		if lines[i][0:-1] == lines[i-2][0:-3]:
			##it will enter here if the sequence belongs to the same transcript
			#adding one to the previous index
			index = int(lines[i-2][len(lines[i-2])-2])+1
			#adding the new index to the sequence
			lines[i] = lines[i].strip()
			lines[i] = lines[i] + "_" + str(index) + "\n"
		else:
			##it will enter if the sequence belongs to a new transcript
			#adding the index to the sequence
			lines[i] = lines[i].strip()
			lines[i] = lines[i] + "_1\n"
#creating the result file
result = open('result.fa', 'w')
result.writelines(lines)
result.close()
