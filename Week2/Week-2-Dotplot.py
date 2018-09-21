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
sum = 0
i = 0
PlotX = []
PlotY = []

#Input & data processing#
Input = open(sys.argv[1])
for read in Input:
    fields = read.rstrip("\r\n").split("\t")
    #print(fields)
    if read.startswith("#score"):
        continue
    else:
        start = int(fields[4])
        end = int(fields[5])
        #print(start, end)
        sumn = sum+end-start
        PlotX.append((sum, sumn))
        sum = sumn
        PlotY.append((start, end))
#print(PlotX[0][1], PlotY[0][1])

#Plot
fig, ax = plt.subplots() 
fig.set_size_inches(20, 12)
for i in range(len(PlotX)):
    plt.plot([PlotX[i][0], PlotX[i][1]], [PlotY[i][0], PlotY[i][1]])
#ax.set_yscale('log')
#x.set_xlim(0,60000)
ax.set_ylim(0, 100000)
ax.set_xlabel("Assembled contigs")
ax.set_ylabel("Positions in reference")
fig.suptitle(sys.argv[2] + " alignments")
fig.savefig(sys.argv[2] + "_dotplot.png")
plt.tight_layout()
plt.close(fig)

