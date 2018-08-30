#!/usr/bin/env python3

"""
Usage: ./Day4-HW-Evening-Exercise-1.py <samples.csv> (e.g. ./Day4-HW-Evening-Exercise-1.py ~/qbb2018/samples.csv)
In this case, ctab files are stored in "~/data/results/stringtie/", sample_name, "t_data.ctab".
Create a single file all.csv that contains the FPKMs from all 16 samples in samples.csv.
"""


import sys
import os
import pandas as pd

fpkms = {}

#Sample input#
df =pd.read_csv(sys.argv[1])

for index, sample_name, sex, stage in df.itertuples():
    sample_info = sex + "_" +stage
    path = os.path.join("~/data/results/stringtie/", sample_name, "t_data.ctab")
    fpkm = pd.read_csv(path, sep="\t", index_col="t_name").loc[:,"FPKM"]
    fpkms[sample_info] = fpkm

#Output DataFrame#       
FPKM = pd.DataFrame(fpkms)
#print(FPKM)
FPKM.to_csv(sys.stdout, sep = ",")