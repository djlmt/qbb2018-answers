#!/usr/bin/env python3

"""
Usage: ./Week4-PCA.py plink.eigenvec
Visualize genetic relatedness between the strains by performing principal component analysis and plotting the first two components.
plink --pca 2 --allow-extra-chr --mind --allow-no-sex --vcf BYxRM_segs_saccer3.bam.simplified.vcf 
"""

#Import#
import sys
import pandas as pd
import matplotlib.pyplot as plt

#Dataframe#
df = pd.read_csv(sys.argv[1], names = ["Family_ID", "Sample_ID", "PC1", "PC2"], sep= " ")
pc1 = df.loc[:,"PC1"]
pc2 = df.loc[:,"PC2"]
#print(pc1,pc2)

#Plot#
fig, ax = plt.subplots() 
fig.set_size_inches(10, 8)
ax.scatter(pc1, pc2, alpha=0.86, s=8.68, color="purple")
#ax.set_yscale('log')
#x.set_xlim(0,60000)
#x.set_ylim(0,60000)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
fig.suptitle("Principal component analysis")
fig.savefig("Principal_component_analysis.png")
plt.tight_layout()
plt.close(fig)