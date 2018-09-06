#!/usr/bin/env python3

"""
Usage: ./Day5-lunch-6.sh <tab_file1> <tab_file2> ... <tab_file4> <t_data.ctab>
./Day5-lunch-6.py H3K9ac.tab H3K4me1.tab H3K4me3.tab H3K27me3.tab H3K27ac.tab /Users/cmdb/data/results/stringtie/SRR072893/t_data.ctab
Copy all data into the folder storing the .py file.
Transform gene expression into units of log(FPKM + 1). Refit linear model and plot residuals.
"""

#def#
import sys
import pandas as pd
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Import data needed to a dic#
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

#Transform into DataFrame#
df = pd.DataFrame(Dic)

#Log transformation#
df["log_fpkm"] = np.log(df["fpkm"]+1)
#df.to_csv(sys.stdout, sep="\t")

# OLS Model
mod = sm.ols(formula="log_fpkm ~ H3K4me1 + H3K4me3 + H3K9ac + H3K27ac + H3K27me3", data=df)
res = mod.fit()
print(res.summary())

#Plot the residuals#
fig, ax = plt.subplots() 
fig.set_size_inches(8, 5)
plt.hist(res.resid, bins=1600, color="orange")
plt.axis([-6, 8, 0, 350])
ax.set_xlabel("LogFPKMs Residuals")
ax.set_ylabel("Transcript counts")
fig.suptitle("Linear regression residuals evaluation")
fig.savefig("Log_LinearRegression_Residuals.png")
plt.tight_layout()
plt.close(fig)