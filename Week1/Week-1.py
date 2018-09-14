#!/usr/bin/env python3

"""
Usage: ./Week-1.py transeq_results_output.fa Blast_results.fa 

Use BLAST to identify homologous sequences to your query of interest
Perform a “codon” alignment of these sequences by translating into amino acid sequences, performing multiple alignment, and translating the alignment back into nucleotide space.
For each site, determine the ratio of non-synonymous to synonymous changes and look for sites where this ratio is significantly different than expectation
Produce a plot showing the ratio at each position in the sequence, and highlight sites under significant positive selection in red.
"""

#Import#
import sys
import fasta
import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Input#
AA_Reader = fasta.FASTAReader( open(sys.argv[1]) )
DNA_Reader = fasta.FASTAReader( open(sys.argv[2]) )
#print(DNA_Reader)

#Def#
Dic = {}
Z = []
diff = []
Red = []
Blue = []
R_Position = []
B_Position = []
q = 0
sum = 0
sd_sum = 0

#Match DNA sequence with AA sequence#
for (dna_id, dna), (aa_id, aa) in zip(DNA_Reader, AA_Reader):
    c = 0
    DNA = []
    AA = []
    for i in range(len(aa)):
        #print(i)
        AA.append(aa[i])
        if aa[i] == "-":
            DNA.append("-")
            DNA.append("-")
            DNA.append("-")
        else:
            DNA += dna[c:c+3]
            c = c+3
    if q == 1:
        Dic[aa] = "".join(DNA)
    elif q == 0:
        aa_query = AA
        dna_query = DNA
        #print(len(aa_query), len(dna_query))
        N_Count=[0]*len(aa_query)
        S_Count=[0]*len(aa_query)
        q = 1
        #print("Query established.")
#print(DNA[0:10])
#print(Dic)

#Count dn $ ds#
for aa in Dic:
    #print(len(aa),len(Dic[aa]))
    for i in range(len(aa)):
        if aa[i] =="-":
            continue
        elif aa[i] != aa_query[i]:
            N_Count[i] = N_Count[i]+1
        elif Dic[aa][3*i] != dna_query[3*i] or Dic[aa][3*i+1] != dna_query[3*i+1] or Dic[aa][3*i+2] != dna_query[3*i+2]:
            S_Count[i] = S_Count[i]+1
#print(S_Count)
#print(N_Count)
#print(len(S_Count), len(N_Count))

#Z test#
for i in range(len(aa_query)):
    diff.append(N_Count[i]-S_Count[i])
    #diff = N_Count[i]-S_Count[i]
    #sum = sum + diff
n = len(aa_query)
#avg = sum/n
#for i in range(len(aa_query)):
    #diff = N_Count[i]-S_Count[i]
    #sd_diff = diff*diff
    #sd_sum = sd_sum+sd_diff
#SD = math.sqrt(sd_sum/(n-1))
SD = np.std(diff)
SE = SD/(math.sqrt(n))
#print(SE)
#print(len([0]), len([0,0,0]), len("0"), len("000"))
for i in range(len(aa_query)):
    #Z = (Dc - Dn) / SE, Dc is the difference between dN and dS, Dn is the null hypothesis which is 0 here, SE is the standard error.
    Z.append((diff[i]-0)/SE)
#print(Z)

#Seperate based on significance#
for i in range(len(aa_query)):
    N = N_Count[i]
    if S_Count[i] == 0:
        S = 1
    else:
        S = S_Count[i]
    #For Z test, 2.58 for 1% two-tail test#
    if Z[i] > 2.58:
        Red.append(np.log2(N/S))
        R_Position.append(i+1)
    else:
        Blue.append(np.log2(N/S))
        B_Position.append(i+1)
#print(Position, Red, Blue)  

#Plot
fig, ax = plt.subplots() 
fig.set_size_inches(20, 12)
#sns.barplot(x=Position, y=Red, color="r")
#sns.barplot(x=Position, y=Blue, color="b")
ax.scatter(R_Position, Red, alpha=0.28, s=6.68, color="red")
ax.scatter(B_Position, Blue, alpha=0.28, s=6.68, color="blue")
#ax.set_yscale('log')
ax.set_xlabel("Condon site")
ax.set_ylabel("log2(Non-synonymous changes / Synonymous changes)")
fig.suptitle("dN/dS")
plt.legend(["Significant", "Insignificant"], loc = "center left", bbox_to_anchor = (1,0.5))
fig.savefig("Sequence alignment and evolution.png")
plt.tight_layout()
plt.close(fig)

#print(N_Count, S_Count)

