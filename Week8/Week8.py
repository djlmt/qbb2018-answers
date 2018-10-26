#!/usr/bin/env python3

"""
Using meme-chip perform motif finding in the strongest 100 peaks from the ER4 state.
Scan these motifs against the JASPAR_CORE_2016 database using tomtom to find matches to known motifs. Consider motif widths up to 20bp.
Produce a plot showing where motif matches occur in the input sequences.
The x-axis is the relative position in the sequences where the motif matches are found, and the y-axis is a representation of how often we see motifs at that position.
Usage: ./Week8.py /Users/cmdb/qbb2018-answers/Week8/ER4_peaks.narrowPeak.bed
"""

#sort -nk9 -r ER4_peaks.narrowPeak | head -n 100 >Too100_ER4
#bedtools getfasta -fi chr19.fa -bed Too100_ER4 > Top100_FA
#meme-chip -db /Users/cmdb/qbb2018-answers/Week8/motif_databases/JASPAR/JASPAR_CORE_2016_vertebrates.meme -meme-maxw 20 Top100_FA 
#bedtools intersect -a /Users/cmdb/qbb2018-answers/Week8/memechip_out/fimo_out_1/fimo.gff -b ER4_peaks.narrowPeak -wa -wb > ER4_peaks.narrowPeak.bed

#Import#
import sys
import matplotlib.pyplot as plt

#Input#
Bed = open(sys.argv[1])

#Def#
Percentage = []

#Grab value & calculate#
for count, line in enumerate(Bed):
    "Skip the header"
    if line.startswith("#"):
        continue
    else:
        fields = line.rstrip("\r\n").split("\t")
        #print(fields)
        sm = float(fields[3])
        em = float(fields[4])
        sp = float(fields[10])
        ep = float(fields[11])
    #print(sm,em,sp,ep)
        percentage = abs((sm-sp)/(ep-sp))
        #print(percentage)
        Percentage.append(percentage)
#print(Percentage)

#Plot#
fig, ax = plt.subplots() 
fig.set_size_inches(12, 9)
plt.hist(Percentage, bins=300, color="red")
ax.set_xlabel("Frequency")
ax.set_ylabel("Relative position")
fig.suptitle("Top 100 motifs - Week 8 ")
fig.savefig("Week8.png")
plt.tight_layout()
plt.close(fig)