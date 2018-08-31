#!/usr/bin/env python3

"""
Usage: ./Day4-HW-Evening-Time_Course-3.py <gene_name_1> <gene_name_2>... <samples.csv> <ctab_dir>
e.g. ./Day4-HW-Evening-Time_Course-3.py msl-2 d ~/qbb2018/samples.csv ~/data/results/stringtie
Plot mean abundance of a/multiple gene(s) that are indidated at the command line.
"""

#Import#
import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

#Gene name input#
GN = sys.argv[1:(len(sys.argv)-2)]

#Function#
def Timecourse(gender, C, gn):
    df = pd.read_csv(sys.argv[-2])
    soi = df.loc[:, "sex"] == gender
    df = df.loc[soi,:]
    fpkms = []
    mean_fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join( sys.argv[-1], sample, "t_data.ctab" )
        #print(filename)
        ctab_df = pd.read_table( filename, index_col="t_name" )
        roi = ctab_df.loc[:,"gene_name"] == gn
        fpkms.append(ctab_df.loc[roi,"FPKM"])
        mean_fpkms.append(np.mean(fpkms))
    return mean_fpkms
  

    
#Plot#
for gene in GN:
    fig, ax = plt.subplots() 
    fig.set_size_inches(12, 8)
    mfpkms_mean = Timecourse("male", "blue", gene)
    ax.plot(mfpkms_mean, color = "blue")     
    ffpkms_mean = Timecourse("female", "red", gene)
    ax.plot(ffpkms_mean, color = "red")
    plt.legend(["male", "female"], loc = "center left", bbox_to_anchor = (1,0.5))
    ax.set_xlabel("Developmental Stage")
    ax.set_ylabel("Mean Abundance")
    ax.set_xticklabels(labels=("9", "10", "11", "12", "13", "14A", "14B", "14C", "14D"))
    plt.xticks(rotation = 90)
    fig.suptitle(gene + " Abundance through Development")
    fig.savefig(gene + ".png")
    plt.tight_layout()
    plt.close(fig)