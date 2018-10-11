#!/usr/bin/env python3

"""
Usage: ./Week4-Manhanttan.py plink.qassoc<start> plink.qassoc<end>
Use plink to perform quantitative association testing for all phenotypes. For each, produce a manhattan plot and highlight SNPs with p-values less than 10-5.
"""

#Import#
import sys
import numpy as np
import matplotlib.pyplot as plt

#Global def#
colors = ['orange', 'yellow', 'skyblue', 'sandybrown', 'grey']
highlights = ['red', 'green', 'steelblue', 'coral', 'black']

#Load files#
start = int(sys.argv[1])
end = int(sys.argv[2]) + 1

for n in range(start, end):
    file = 'plink.P'+str(n)+'.qassoc'
    print('Generating plot for '+file)
    
    #Reginal Def#
    Chrom = {}
    offset = 0
    tick_pos = []
    
    #Make dic#
    for count, line in enumerate(open('Manhattan/'+file)):
        "Skip the header"
        #print(line)
        if line.startswith(" CHR"):
            continue
        else:
            "Grab the colums of interest"
            field = line.rstrip("\r\n").split()
            if field[-1] != "NA":
                if field[0] in Chrom:
                    Chrom[field[0]].append(field[2])
                    Chrom[field[0]].append(field[-1])
                else:
                    Chrom[field[0]] = [field[2]]
                    Chrom[field[0]].append(field[-1])
        #print(Chrom)

    #Plot#
    fig, ax = plt.subplots(figsize=(12,9))
    for count, chrom in enumerate(Chrom):
        "Pull the data for a single chromsome"
        BP = []
        P = []
        #print(chrom)
        #print(Chrom[chrom])
        for i in range(len(Chrom[chrom])):
            #print(i)
            if i%2 == 0:
                BP.append(float(Chrom[chrom][i]))
            elif i%2 == 1:
                P.append(float(Chrom[chrom][i]))
            
        x = np.array(BP)
        y = np.array(-np.log10(P))
        #print(BP)
        #print(P)
        #print(x)
        #print(y)
        #break
    
        "Test significance"
        sig = (y > 5)
    
        plt.scatter(x[sig] + offset, y[sig], c=highlights[count%5], marker='.')
        plt.scatter(x[~sig] + offset, y[~sig], c=colors[count%5], marker='.')
    
        "Calcualte the offsets and the tick positions for the next chrosome's positions"
        maxx = max(x)
        tick_pos.append(offset + maxx/2)
        offset += maxx

    ax.set_xticks(tick_pos)
    ax.set_xticklabels(Chrom, rotation=90);
    "Cutoff line"
    ax.axhline(5, c='k', ls=':', label="Significance cutoff")
    ax.legend()
    ax.set_ylabel(r"$\log_{10}(P-value)$")
    ax.set_xlabel("Genomic Position")
    ax.set_title("Manhattan Plot\n"+file.split(".")[1]);
    fig.savefig("Manhattan_Plot_"+file.split(".")[1]+".png")
    plt.tight_layout()
    plt.close(fig)