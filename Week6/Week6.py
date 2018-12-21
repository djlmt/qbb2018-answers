#!/usr/bin/env python3

"""
Usage: ./Week6.py Mus_musculus.GRCm38.94_features.bed Gained-CTCF.bed Lost-CTCF.bed 

Mus_muculus.GRCm38.94_features.bed ctcf_gained.bed ctcf_lost.bed 

Produce a two panel plot containing two bar plots. The right panel should plot the number of sites lost and gained between the two cell types. The left panel should plot the number of sites in each type of region (exon, intron…) for each cell type.
"""

#Import#
import sys
import numpy as np
import matplotlib.pyplot as plt


#Def#
Gained_count = 0
promoter_gained = 0
exon_gained = 0
intron_gained = 0
Lost_count = 0
promoter_lost = 0
exon_lost = 0
intron_lost = 0
Lost_count = 0
Fea = {}
Gain_list = []
Lost_list = []


#Data input#
for line in open(sys.argv[1]):
    fields = line.rstrip("\r\n").split("\t")
    startsite = int(fields[1])
    endsite = int(fields[2])
    for site in range(startsite, endsite):
        Fea[site] = fields[3]
#print(Fea)

for line in open(sys.argv[2]):
    fields = line.rstrip("\r\n").split("\t")
    startsite = int(fields[1])
    endsite = int(fields[2])
    Gained = []
    for site in range(startsite, endsite):
        if site in Fea:
            Value = Fea[site]
            if Value in Gained:
                T = 0
            else:
                Gained.append(Value)
    Gained_count += 1
    Gain_list.append(Gained)

for i in Gain_list:
    if len(i) != 0:
        for item in i:
            if item == "promoter":
                promoter_gained += 1
            elif item == "intron":
                intron_gained += 1
            elif item == "exon":
                exon_gained += 1
# print(promoter_gained, exon_gained, intron_gained)

for line in open(sys.argv[3]):
    fields = line.rstrip("\r\n").split("\t")
    startsite = int(fields[1])
    endsite = int(fields[2])
    Lost = []
    for site in range(startsite, endsite):
        if site in Fea:
            Value = Fea[site]
            if Value in Lost:
                T = 0
            else:
                Lost.append(Value)
    Lost_count += 1
    Lost_list.append(Lost)

for i in Lost_list:
    if len(i) != 0:
        for item in i:
            if item == "promoter":
                promoter_lost += 1
            elif item == "intron":
                intron_lost += 1
            elif item == "exon":
                exon_lost += 1
# print(promoter_lost, exon_lost, intron_lostd)


#Plot#
fig, axes = plt.subplots(nrows=1,ncols=2)
axes = axes.flatten()
fig.set_size_inches(20, 12)

axes[0].set_title("Number of CTCF sites in each type of region for each cell type")
axes[0].set_ylabel("CTCF binding sites number")

axes[0].bar(0, exon_gained, color="purple")
axes[0].bar(0, exon_lost, color="orange")
axes[0].bar(1, intron_gained, color="purple")
axes[0].bar(1, intron_lost, color="orange")
axes[0].bar(2, promoter_gained, color="purple", label="Gained CTCF sites in ER4")
axes[0].bar(2, promoter_lost, color="orange", label="Lost CTCF sites in ER4")

axes[0].set_xticks([0, 1, 2])
axes[0].set_xticklabels(["exon", "Intron", "Promoter"])
axes[0].legend()

axes[1].set_title("Number of sites lost and gained between the G1E and ER4 cells")
axes[1].set_ylabel("CTCF binding sites number")

axes[1].bar(0, Gained_count, color="purple", width=0.16, align="center", label="Gained CTCF sites in ER4")
axes[1].bar(0.3, Lost_count, color="orange", width=0.16, align="center", label="Lost CTCF sites in ER4")

axes[1].set_xticks([0, 0.3])
axes[1].set_xticklabels(["Gained", "Lost"])
axes[1].legend()

fig.savefig("Week6.png")
plt.close(fig)