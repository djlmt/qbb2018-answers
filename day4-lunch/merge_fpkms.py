#!/usr/bin/env python3

"""
Usage: ./merge_fpkms.py <threshold> <ctab_file1> <ctab_file2> ... <ctab_filen>
Combine FPKM values from 2 or more ctab files and report transcripts when the total FPKM is greater than a specified threshold.
"""

import sys
import os
import pandas as pd

#def#
t = sys.argv[1]
fpkms = {}
fpkms_sum = {}

#get FPKM information#
for transcript in range(2,len(sys.argv)):
    transcript_name = sys.argv[transcript].split(os.sep)[-2]
    fpkm = pd.read_csv(sys.argv[transcript], sep="\t", index_col="t_name").loc[:,"FPKM"]
    fpkms[transcript_name] = fpkm

#dataframe# 
fpkms_df = pd.DataFrame(fpkms)

#Sum and compare#
fpkms_df["Sum"] = fpkms_df[list(fpkms_df)].sum(axis=1)
#print(type(fpkms_df["Sum"]))
Value = fpkms_df.loc[:,"Sum"] > float(t)
#print(fpkms_df)

#Output
fpkms_df.loc[Value,fpkms_df.columns != "Sum"].to_csv(sys.stdout, sep = "\t")

#print(fpkms_df)
