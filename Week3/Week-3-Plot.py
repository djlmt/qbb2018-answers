#!/usr/bin/env python3

"""
Usage: ./Week-3-Plot.py calls.vcf

Input the data from the vcf file to plot the read depth distribution across each called variant
"""

#Import#
import sys
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

#Plot#
fig, ax = plt.subplots() 
fig.set_size_inches(20, 12)
#plt.hist(DPV, bins=1600, color="purple")
#plt.bar(DP_X_Value, DPV, align='center')
ax.scatter(DP_X_Value, DPV, alpha=0.16, s=2.68, color="blue")
#ax.scatter(DP_X_Value, QRV, alpha=0.16, s=2.68, color="red")
#ax.scatter(DP_X_Value, AFV, alpha=0.16, s=2.68, color="purple")
#plt.legend(["Read depth", "Genotype quality", "Allele frequency"], loc = "center left", bbox_to_anchor = (1,0.5))
#ax.set_yscale('log')
#x.set_xlim(0,60000)
#ax.set_ylim(0, 100000)
#plt.xticks(Tick)
ax.set_xlabel("Positions")
ax.set_ylabel("Read depth")
fig.suptitle("Read depth distribution across each called variant")
fig.savefig("Read_depth.png")
plt.tight_layout()
plt.close(fig)

fig, ax = plt.subplots() 
fig.set_size_inches(20, 12)
#plt.hist(DPV, bins=1600, color="purple")
#plt.bar(DP_X_Value, DPV, align='center')
#ax.scatter(DP_X_Value, DPV, alpha=0.16, s=2.68, color="blue")
ax.scatter(DP_X_Value, QRV, alpha=0.16, s=2.68, color="red")
#ax.scatter(DP_X_Value, AFV, alpha=0.16, s=2.68, color="purple")
#plt.legend(["Read depth", "Genotype quality", "Allele frequency"], loc = "center left", bbox_to_anchor = (1,0.5))
#ax.set_yscale('log')
#x.set_xlim(0,60000)
#ax.set_ylim(0, 100000)
#plt.xticks(Tick)
ax.set_xlabel("Positions")
ax.set_ylabel("Genotype quality")
fig.suptitle("Genotype quality distribution")
fig.savefig("Genotype_quality.png")
plt.tight_layout()
plt.close(fig)

fig, ax = plt.subplots() 
fig.set_size_inches(20, 12)
#plt.hist(DPV, bins=1600, color="purple")
#plt.bar(DP_X_Value, DPV, align='center')
#ax.scatter(DP_X_Value, DPV, alpha=0.16, s=2.68, color="blue")
#ax.scatter(DP_X_Value, QRV, alpha=0.16, s=2.68, color="red")
ax.scatter(DP_X_Value, AFV, alpha=0.16, s=2.68, color="purple")
#plt.legend(["Read depth", "Genotype quality", "Allele frequency"], loc = "center left", bbox_to_anchor = (1,0.5))
#ax.set_yscale('log')
#x.set_xlim(0,60000)
#ax.set_ylim(0, 100000)
#plt.xticks(Tick)
ax.set_xlabel("Positions")
ax.set_ylabel("Allele frequency")
fig.suptitle("Allele frequency spectrum")
fig.savefig("Allele_frequency_spectrum.png")
plt.tight_layout()
plt.close(fig)