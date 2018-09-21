#!/usr/bin/env python3

"""
Usage: ./Week-2-Dotplot.py <Lastz_sorted file> <file name> 
e.g. ./Week-2-Dotplot.py Lastz_sort short_reads_low

Use lastz to align the contigs to the reference and produce a dotplot.
The data need to be sorted by the end position ahead. Use the following command line: sort -k 5 -n Lastz > Lastz_sort.
"""

#Import#
import sys
import matplotlib.pyplot as plt

#Def#
DP_X_Value = []
DP_Y_Value = []
x = 1
#Input & data processing#
Input = open(sys.argv[1])
for read in Input:
    if read.startswith("#"):
        continue
    fields = read.rstrip("\r\n").split("\t")
    DP_List = fields[7].split(";")
    #print(DP)
    DP = DP_List[7]
    #print(DP)
    DP_Value = DP.split("=")
    #print(DP_Value[1])
    DP_Y_Value.append(DP_Value[1])
    DP_X_Value.append(x)
    x = x+1
#print(len(DP_X_Value), len(DP_Y_Value))
#print(DP_X_Value, DP_Y_Value)

#Plot
fig, ax = plt.subplots() 
fig.set_size_inches(20, 12)
ax.scatter(DP_X_Value, DP_Y_Value, alpha=0.18, s=1.68, color="blue")
#ax.set_yscale('log')
#x.set_xlim(0,60000)
#ax.set_ylim(0, 100000)
ax.set_xlabel("Assembled contigs")
ax.set_ylabel("Positions in reference")
fig.suptitle(" alignments")
fig.savefig("_dotplot.png")
plt.tight_layout()
plt.close(fig)

