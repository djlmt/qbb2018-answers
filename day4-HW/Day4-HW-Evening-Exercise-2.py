#!/usr/bin/env python3

"""
Usage: ./Day4-HW-Evening-Exercise-2.py <t_name> <samples.csv> <ctab_dir>
e.g. ./Day4-HW-Evening-Exercise-2.py FBtr0331261 ~/qbb2018/samples.csv ~/data/results/stringtie
Plot a second series of FBtr0331261 abundance for both male and female samples. Style the plot similarly to Lott et al., 2011 PLoS Biology.
"""

#def#
import sys
import pandas as pd
import os
import matplotlib.pyplot as plt

#Function#
def Timecourse(gender, C):

    df = pd.read_csv(sys.argv[2])
    
    soi = df.loc[:, "sex"] == gender
    df = df.loc[soi,:]

    fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join( sys.argv[3], sample, "t_data.ctab" )
        #print(filename)
        ctab_df = pd.read_table( filename, index_col="t_name" )
        roi = ctab_df.loc[:,"gene_name"] == sys.argv[1]
        fpkms.append(ctab_df.loc[sys.argv[1],"FPKM"])
        #Plot#
    return fpkms
    
#Main#
fig, ax = plt.subplots() 
fig.set_size_inches(12, 8)
mfpkms = Timecourse("male", "blue")
ax.plot(mfpkms, color = "blue")     
ffpkms = Timecourse("female", "red")
ax.plot(ffpkms, color = "red")
plt.legend(["male", "female"], loc = "center left", bbox_to_anchor = (1,0.5))
ax.set_xlabel("Developmental Stage")
ax.set_ylabel("RNA Abundance")
ax.set_xticklabels(labels=("9", "10", "11", "12", "13", "14A", "14B", "14C", "14D"))
plt.xticks(rotation = 90)
fig.suptitle("FBtr0331261 RNA Abundance through Development")
fig.savefig("Timecourse.png")
plt.tight_layout()
plt.close(fig)