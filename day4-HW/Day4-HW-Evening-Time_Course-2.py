#!/usr/bin/env python3

"""
Usage: /Day4-HW-Evening-Time_Course-2.py <gene_name> <samples.csv> <ctab_dir>
e.g. ./Day4-HW-Evening-Time_Course-2.py Sxl ~/qbb2018/samples.csv ~/data/results/stringtie
Plot mean abundance of the gene that is specified on the command line.
"""

#Import#
import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

#Def#
genename = sys.argv[1]

#Function#
def Timecourse(gender, C):
    df = pd.read_csv(sys.argv[2])
    soi = df.loc[:, "sex"] == gender
    df = df.loc[soi,:]

    fpkms = []
    mean_fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join( sys.argv[3], sample, "t_data.ctab" )
        #print(filename)
        ctab_df = pd.read_table( filename, index_col="t_name" )
        roi = ctab_df.loc[:,"gene_name"] == genename
        fpkms.append(ctab_df.loc[roi,"FPKM"])
        #Calculate the mean of each gene#
        mean_fpkms.append(np.mean(fpkms))
    return mean_fpkms
    
#Main#
fig, ax = plt.subplots() 
fig.set_size_inches(12, 8)
mfpkms_mean = Timecourse("male", "blue")
#print(mfpkms_mean)
ax.plot(mfpkms_mean, color = "blue")     
ffpkms_mean = Timecourse("female", "red")
#print(ffpkms_mean)
ax.plot(ffpkms_mean, color = "red")
plt.legend(["male", "female"], loc = "center left", bbox_to_anchor = (1,0.5))
ax.set_xlabel("Developmental Stage")
ax.set_ylabel("RNA Abundance")
ax.set_xticklabels(labels=("9", "10", "11", "12", "13", "14A", "14B", "14C", "14D"))
plt.xticks(rotation = 90)
fig.suptitle(genename + " Abundance through Development")
fig.savefig(genename + ".png")
plt.tight_layout()
plt.close(fig)