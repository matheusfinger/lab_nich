library("Biostrings")
library("ORFik")
rm(genome, orfs, sorfs, sequences_orfs, sequences_sorfs)
# Criando uma variável de referềncia a um arquivo fasta (nesse caso, não estava indexado)
genome <- FaFile("genoma_jatropha.fna")
seqinfo(genome)
# Procurando por ORFs no arquivo Fasta em ambas as fitas e em todas as janelas de leitura que comecem com ATG
orfs <- findORFsFasta("genoma_jatropha.fna", startCodon = "ATG", minimumLength = 28)
#separando sORFs
sorfs <- orfs[lengths(orfs) <= 300]
# Extraindo as sequências das ORFs  
sequences_orfs <- getSeq(genome, orfs)
# Extraindo as sequências das sORFs
sequences_sorfs <- getSeq(genome, sorfs)
# Criando arquivo com o resultado
writeXStringSet(sequences_orfs, filepath = "orfs_jatropha.fa")
writeXStringSet(sequences_sorfs, filepath = "sorfs_jatropha.fa")
