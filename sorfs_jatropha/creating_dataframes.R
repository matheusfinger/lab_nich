library("Biostrings")
library("ORFik")
rm(list = ls())
# Criando uma variável de referềncia a um arquivo fasta (nesse caso, não estava indexado)
genome <- FaFile("genoma_jatropha.fa")
seqinfo(genome)
# Procurando por ORFs no arquivo Fasta em ambas as fitas e em todas as janelas de leitura que comecem com ATG
orfs <- findORFsFasta("genoma_jatropha.fa", startCodon = "ATG", minimumLength = 28)
#pegando os títulos gerados no script em python que eu fiz
titulos <- read.csv("titulo_orfs.txt", sep="\n", header = FALSE)
titulos <- as.character(titulos[,1])
#colocando o título relacionado às ORFs para poder depois separar os títulos das sORFS
orfs@elementMetadata@rownames <- titulos
#separando sORFs
sorfs <- orfs[lengths(orfs) <= 300]
# Criando arquivo com os nomes das sORFs que depois eu vou substituir no arquivo fasta
# pois o arquivo fasta das sequências das sORFs só tem o contig como título
write.table(sorfs@elementMetadata@rownames, file = "titulos_sorfs.txt")



#Criando data frames com os valores necessários para calcular a classficação das ORFS.

# As colunas são: a posição de começo, o tamanho e a fita (sense ou antisense)
# O nome das linhas são os títulos/IDs das sORFs.

fitas <- rep(orfs@strand@values, times = orfs@strand@lengths)
orfs_dat <- data.frame(start = orfs@ranges@start, width = orfs@ranges@width, strand = fitas)
titulos <- read.csv("titulo_orfs.txt", sep="\n", header = FALSE)
titulos <- as.character(titulos[,1])
rownames(orfs_dat) <- orfs@elementMetadata@rownames
write.csv(orfs_dat, "data_frame_orfs.csv")

fitas <- rep(sorfs@strand@values, times = sorfs@strand@lengths)
sorfs_dat <- data.frame(start = sorfs@ranges@start, width = sorfs@ranges@width, strand = fitas)
rownames(sorfs_dat) <- sorfs@elementMetadata@rownames
write.csv(sorfs_dat, "data_frame_sorfs.csv")
