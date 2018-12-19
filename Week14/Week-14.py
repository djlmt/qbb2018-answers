#!/usr/bin/env python3

"""
Usage: ./Week-14.py

Environment prep
conda create -n scanpy2 scanpy numpy matplotlib python=3.6
conda activate scanpy2

Step 1: Filtering
Filtering tools are largely under the sc.pp module. I would suggest using the Zheng et al. 2017 filtering approach. Produce a PCA plot before and after filtering (see the sc.api.tl module to actually perform the PCA and sc.api.pl for plotting).

Step 2: Clustering
Use louvain clustering to identify clusters in the data. Produce t-SNE and UMAP plots showing the clustering produced.

Step 3: Distinguishing genes
Identify and plot gene that distinguish each cluster. Use both the t-test and logistic regression appraoches

Step 4: Cell types
Using your knowledge identify some marker genes that should distinguish different brain cell types.
You can color UMAP and t-SNE plots by any gene of your choice, helpful in visualizing which clusters are enriched for which genes
You can also produce dotplots and clustermaps that allow you to see how a specific set of genes are associated with your clusters. Also, stacked violin plots, etc…
"""

#Import#
import sys
import matplotlib
matplotlib.use("Agg")
import scanpy.api as sc
sc.settings.autoshow = False

#Data input#
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

#PCA#
sc.tl.pca(adata)
sc.pl.pca(adata, save = "Nonfiltered.png")

#Filtering#
filtered_data = sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=True)
filtered_PCA = sc.tl.pca(filtered_data)
sc.pl.pca(filtered_data, save = "Filtered.png")

#Clustering#
sc.pp.neighbors(filtered_data, n_neighbors=15, n_pcs=None, use_rep=None, knn=True, random_state=0, method="umap", metric="euclidean", metric_kwds={}, copy=False)
sc.tl.louvain(filtered_data, resolution=None, random_state=0, restrict_to=None, key_added=None, adjacency=None, flavor="vtraag", directed=True, use_weights=False, partition_type=None, partition_kwargs=None, copy=False)
sc.tl.umap(filtered_data)
sc.pl.umap(filtered_data, save = "Umap.png")
sc.tl.tsne(filtered_data)
sc.pl.tsne(filtered_data, save = "Tsne.png")

#Distinguishing genes using the t-test and logistic regression appraoches#
sc.tl.rank_genes_groups(filtered_data, groupby = "louvain", method = "t-test")
sc.pl.rank_genes_groups(filtered_data, save = "ttest.png")
sc.tl.rank_genes_groups(filtered_data, groupby = "louvain", method = "logreg")
sc.pl.rank_genes_groups(filtered_data, save = "logisticreg.png")

#Identifying cell types#
sc.tl.tsne(filtered_data)
sc.pl.tsne(filtered_data, color = ["louvain", "Dbi"], save = "Marker_gene_1.png")
sc.pl.tsne(filtered_data, color = ["louvain", "Ctsb"], save = "Marker_gene_2.png")
sc.pl.tsne(filtered_data, color = ["louvain", "Ctss"], save = "Marker_gene_3.png")
sc.pl.tsne(filtered_data, color = ["louvain", "Apoe"], save = "Marker_gene_4.png")
sc.pl.tsne(filtered_data, color = ["louvain", "Tubb3"], save = "Marker_gene_5.png")
sc.pl.tsne(filtered_data, color = ["louvain", "Stmn2"], save = "Marker_gene_6.png")
sc.pl.tsne(filtered_data, color = ["louvain", "Tcf4"], save = "Marker_gene_7.png")
sc.pl.tsne(filtered_data, color = ["louvain", "Ubb"], save = "Marker_gene_8.png")
sc.pl.tsne(filtered_data, color = ["louvain", "Nrxn3"], save = "Marker_gene_9.png")

#sc.pl.rank_genes_group_dotplot(filtered_adata, groupby = "louvain", use_raw = None, log = False, num_categories = 7, color_map = "Reds", figsize = None, dendrogram = False, var_group_positions = None, var_group_labels = None, var_group_rotation = None, show = None, save = "dotplot.png")