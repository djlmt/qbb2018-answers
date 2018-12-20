#!/usr/bin/env python3

"""
Usage: ./Week10_clustering.py hema_data.txt

Cluster RNAseq data to generate dendrogram and gene expression heatmap graphs.
Use k-means clustering, and plot the results on the expression data for CFU and poly.
Identify genes which are differentially expressed between the two earliest stages in differentiation as compared to the two latest stages. Use a t-test to get the significance value for the difference in mean expression level.
"""

#Import#
import sys
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from scipy import stats


#Def#
Gene = []
Value = []
Gene_pv = []
most_up_gene = "N/A"
most_up_fold = 0
p = 0


#Input#
for count, line in enumerate(open(sys.argv[1])):
	"Skip the header"
	if line.startswith("gene"):
		continue
	else:
		field = line.rstrip("\r\n").split("\t")
		#print(field)
		gene = field[0]
		Gene.append(gene)
		Tem = []
		for value in field[1:]:
			Tem.append(float(value))
		Value.append(Tem)
        
		CFU = float(field[1])
		Poly = float(field[2])
		Unk = float(field[3])
		Mys = float(field[5])
		Avg1 = float((CFU+Mys)/2)
		Avg2 = float((Poly+Unk)/2)
		fold = float(Avg2/Avg1)
		ttest, pvalue = stats.ttest_ind([CFU, Mys], [Poly, Unk])
		if fold > 2 or fold < 0.5:
			if pvalue < 0.05:
				#print(type(most_up_fold))
				if fold > most_up_fold:
					most_up_gene = gene
					most_up_fold = fold
				Gene_pv.append([gene, pvalue])


#Plot#
X = np.array(Value)
Z = linkage(X, 'ward')
plt.figure(figsize=(60, 48))
plt.title('Differentiation sequence dendrogram')
dendrogram(Z, leaf_rotation=90., leaf_font_size=6)
plt.xlabel('Sample index')
plt.ylabel('Distance')
#plt.xticks(X, rotation = 90)
plt.savefig('Differentiation sequence dendrogram.png')
plt.close()


#Dataframe input#
data = pd.read_csv(open(sys.argv[1]), sep="\t", index_col='gene')
df = pd.DataFrame(data)


#Dataframe dendrogram plot#
fig, ax = plt.subplots(figsize=(12, 9))
ax.set_title("Dendrogram")
ax = sns.clustermap(df, metric="euclidean", standard_scale=1, method="ward", cmap="Blues")
ax.savefig("Clustered heatmap of gene expression.png")
plt.close(fig)


#KMeans cluster#
Kmeans = KMeans(n_clusters=4)
Kmeans.fit(df)
YKMeans = Kmeans.predict(df)
#print(Kmeans.fit(df))


#KMeans plot#
plt.figure(figsize=(8, 6))
plt.title("KMeans clustering")
plt.scatter(df["CFU"], df['poly'], s=5, c=YKMeans, cmap='magma')
plt.xlabel("CFU")
plt.ylabel("Poly")
plt.savefig("KMeans.png")
plt.close()


#Differential expression#
filea = open('Differential expression.txt','w')
for item in Gene_pv:
	if p == 0:
		filea.write("Gene\tPvalue\n")
	filea.write(str(Gene_pv[p][0]))
	filea.write("\t")
	filea.write(str(Gene_pv[p][1]))
	filea.write("\n")
	p = p+1
filea.close()


#Similar genes#
Upgene_clus = YKMeans[2]
Simigene = df.index[YKMeans == Upgene_clus]
#print(Upgene_clus, "Upgene_clus")
#print(Simigene, "Simigene")

fileb = open('Similar_gene.txt','w')
fileb.write(str(most_up_gene))
fileb.write(" is the most upregulated gene with ")
fileb.write(str(most_up_fold))
fileb.write(" fold change.\n")
for i in Simigene:
	fileb.write(str(i))
	fileb.write('\n')
fileb.close()


