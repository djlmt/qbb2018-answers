#!/usr/bin/env python3

"""
Usage: ./Day4.sh <tab_file1> <tab_file2> ... <tab_file5> <t_data.ctab>
./Day5-lunch-4.py H3K9ac.tab H3K4me1.tab H3K4me3.tab H3K27me3.tab H3K27ac.tab /Users/cmdb/data/results/stringtie/SRR072893/t_data.ctab
Copy all data into the folder storing the .py file.
Perform ordinary linear regression for all of the four marks to determine how predictive each is of gene expression.
"""

#def#
import sys
import pandas as pd
import statsmodels.formula.api as sm

"""Import data needed to a dic"""
Dic = {}
for i in range(1, len(sys.argv)-1):
    modification = sys.argv[i].rstrip("\r\n").split(".")
    #print(modification[0])
    tab = pd.read_csv(sys.argv[i], sep="\t", index_col=0).iloc[:,-1]
    #print(tab)
    Dic[modification[0]] = tab
#print (Dic)
#Import ctab into Dic#
ctab_df = pd.read_table( sys.argv[-1], index_col="t_name" )
coi = ctab_df.loc[:,"FPKM"]
Dic["fpkm"] = coi

#DataFrame#
df = pd.DataFrame(Dic)
#df.to_csv(sys.stdout, sep="\t")

# OLS Model
mod = sm.ols(formula="fpkm ~ H3K4me1 + H3K4me3 + H3K9ac + H3K27ac + H3K27me3", data=df)
res = mod.fit()
print(res.summary())