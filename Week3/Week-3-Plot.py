#!/usr/bin/env python3

"""
Usage: ./Week-3-Plot.py snpEff_calls.vcf

Input the data from the vcf file to plot the read depth distribution across each called variant
"""

#Import#
import sys
import numpy as np
import matplotlib.pyplot as plt

#Def#
DP_X_Value = []
DPV = []
QRV = []
AFV = []
Tick = []
header_count = 0
absoult_count = 0

#Input & data processing#
for count, line in enumerate(open(sys.argv[1])):
    "Skip the header"
    if line.startswith("#"):
        header_count = header_count +1
        continue
    "Grab the colum that contains the DP infromation"
    field = line.rstrip("\r\n").split("\t")
    "Grab the DP value"
    Values = field[7].split(";")
    #print(Values)
    #print(Values[27])
    DP_Value = Values[7].split("=")
    #print(DP_Value[0], DP_Value[1])
    DPV.append(DP_Value[1])
    QR_Value = Values[27].split("=")
    #print(QR_Value)
    QRV.append(QR_Value[1])
    AF_Value = Values[3].split("=")
    AFV.append(AF_Value[1])
    #print(AF_Value)
    absoult_count = count - header_count + 1
    DP_X_Value.append(absoult_count)
    #if absoult_count%100 == 0:
        #Tick.append(absoult_count)
#print(len(DP_X_Value), len(DP_Value))
#print(DP_X_Value)
#print(DPV)
#print(QRV)
#print(AFV)

snpEff = [42.162, 10.092, 4.368, 0.093, 0.0, 0.001, 0.011, 43.272]
Tags = ["Downstream", "Exon", "Intergenic", "Intron", "SS_Acceptor", "SS_Donor", "Splice Site", "Upstream"]

#Plot#
fig, axes = plt.subplots(nrows=2,ncols=2)
axes = axes.flatten()
fig.set_size_inches(20, 16)

axes[0].set_title("Read depth distribution across each called variant")
axes[0].hist(DPV, bins=96, color="purple")
#ax.scatter(DP_X_Value, DPV, alpha=0.16, s=2.68, color="blue")
#ax.scatter(DP_X_Value, QRV, alpha=0.16, s=2.68, color="red")
#ax.scatter(DP_X_Value, AFV, alpha=0.16, s=2.68, color="purple")
#plt.legend(["Read depth", "Genotype quality", "Allele frequency"], loc = "center left", bbox_to_anchor = (1,0.5))
#ax.set_yscale('log')
#x.set_xlim(0,60000)
#ax.set_ylim(0, 100000)
#plt.xticks(Tick)
axes[0].set_yscale("log")
axes[0].set_xlabel("Variants")
axes[0].set_ylabel("Read depth_log")

axes[1].set_title("Genotype quality distribution")
axes[1].hist(QRV, bins=156, color="blue")
#plt.bar(DP_X_Value, DPV, align='center')
#ax.scatter(DP_X_Value, DPV, alpha=0.16, s=2.68, color="blue")
#ax.scatter(DP_X_Value, QRV, alpha=0.16, s=2.68, color="red")
#ax.scatter(DP_X_Value, AFV, alpha=0.16, s=2.68, color="purple")
#plt.legend(["Read depth", "Genotype quality", "Allele frequency"], loc = "center left", bbox_to_anchor = (1,0.5))
#ax.set_yscale('log')
#x.set_xlim(0,60000)
#ax.set_ylim(0, 100000)
#plt.xticks(Tick)
#axes[1].set_yscale("log")
axes[1].set_xlabel("Variants")
axes[1].set_ylabel("Gene quality")


axes[2].set_title("Allele frequency spectrum")
axes[2].hist(AFV, bins=86, color="red")
#plt.hist(DPV, bins=1600, color="purple")
#plt.bar(DP_X_Value, DPV, align='center')
#ax.scatter(DP_X_Value, DPV, alpha=0.16, s=2.68, color="blue")
#ax.scatter(DP_X_Value, QRV, alpha=0.16, s=2.68, color="red")
#plt.legend(["Read depth", "Genotype quality", "Allele frequency"], loc = "center left", bbox_to_anchor = (1,0.5))
#ax.set_yscale('log')
#x.set_xlim(0,60000)
#ax.set_ylim(0, 100000)
#plt.xticks(Tick)
axes[2].set_xlabel("Variants")
axes[2].set_ylabel("Allele frequency")

axes[3].set_title("Predicted effects of each variant")
axes[3].bar(Tags, snpEff, color="pink")
axes[3].set_xticklabels(Tags, rotation=45)
axes[3].set_xlabel("Variant type")
axes[3].set_ylabel("Percentage")

plt.tight_layout()
fig.savefig("Multi-panel-plot_Week-3_HW.png")
plt.close(fig)