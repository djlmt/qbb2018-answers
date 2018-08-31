#!/usr/bin/env python3

"""
Usage: ./Day4-HW-Evening-MA_Plot.py ~/data/results/stringtie/SRR072893/t_data.ctab ~/data/results/stringtie/SRR072896/t_data.ctab
Create an MA-plot for SRR072893 & SRR072896.
"""

#Import#
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Input#
df_1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
df_2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

#Calculate#
ratio = np.log2((df_1.loc[:,"FPKM"]+1)/(df_2.loc[:,"FPKM"]+1))
avg = np.log2((df_1.loc[:,"FPKM"]+1)*(df_2.loc[:,"FPKM"]+1))*0.5
#print(ratio)
#print(avg)

#Plot#
fig, ax = plt.subplots()
fig.suptitle("MA Plot of SRR072893 & SRR072896")
ax.set_xlabel("Avg_fpkm")
ax.set_ylabel("log2(fpkm(SRR072893)/fpkm(SRR072896))")
ax.scatter(avg, ratio, alpha=0.12, s=1.68, color="violet")
fig.savefig( "MA-Plot.png" )
plt.close(fig)