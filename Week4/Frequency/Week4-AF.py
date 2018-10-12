#!/usr/bin/env python3

"""
Usage: ./Week4-AF.py ../BYxRM_segs_saccer3.bam.simplified.vcf 
Visualize the Allele Frequency spectrum by plotting a histogram of allele frequencies.
"""

#Import#
import sys
import pandas as pd
import matplotlib.pyplot as plt

#Def#
AF = []
#Position = []

for count, line in enumerate(open(sys.argv[1])):
    "Skip the header"
    if line.startswith("#"):
        continue
    "Grab the colum that contains the DP infromation"
    field = line.rstrip("\r\n").split("\t")
    "Grab the DP value"
    #print(field[7], len(field))
    if "," in field[7].split("=")[1]:
        AF.append(float(field[7].split("=")[1].split(",")[0]))
        AF.append(float(field[7].split("=")[1].split(",")[1]))
    else:
        AF.append(float(field[7].split("=")[1]))
    #Position.append(count)
#print(AF)

#Plot#
fig, ax = plt.subplots() 
fig.set_size_inches(10, 8)
plt.hist(AF, bins=360, color="orange")
#ax.set_xlim(0,600)
#ax.set_ylim(0,600)
ax.set_xlabel("Frequency")
ax.set_ylabel("Allele counts")
#plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
fig.suptitle("Allele Frequency")
fig.savefig("Allele_frequency.png")
plt.tight_layout()
plt.close(fig)

