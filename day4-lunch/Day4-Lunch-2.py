#!/usr/bin/env python3

"""
Usage: ./Day4.sh <threshold> <ctab_file1> <ctab_file2> ... <ctab_filen>
Plot the FPKM values of two samples
"""
#def#
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Input#
df_1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
df_2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")
fpkm1 = df_1.loc[:,"FPKM"]
fpkm2 = df_2.loc[:,"FPKM"]

#Corrcoef#
fpkm1_vs_fpkm2 = np.corrcoef(fpkm1, fpkm2)[0,1]
#print("Pearson's r: {0:0.4f}".format(fpkm1_vs_fpkm2))

#Plot#
fig, ax = plt.subplots()
fig.suptitle("Scatter")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("fpkm1")
ax.set_ylabel("fpkm2")
ax.scatter(fpkm1, fpkm2, alpha=0.18, s=1.68, color="blue")
plt.axis([.001, 10000, .001, 10000])
#np.polyfit("fpkm1", "fpkm2", 1)
#ax = plt.gca()
#fig = plt.gct()
fig.savefig( "Scatter.png" )
plt.close(fig)


