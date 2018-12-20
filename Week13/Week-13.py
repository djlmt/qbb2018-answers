#!/usr/bin/env python

"""
Usage: ./Week-13.py GSM2418860_WT_CTCF_peaks.txt

Environment prep
conda create -n hifive python=2.7
conda activate hifive
conda install -y -c bioconda hifive

3D Genome-Week13
"""


#Import#
import sys
import hifive
import numpy as np


#Def#
Mid = []
Bin = []
Enriched = []


#Data input#
File = open(sys.argv[1])
for i, line in enumerate(File):
    fields = line.strip("\r\n").split("\t")
    if fields[0] == "chr17":
    	if int(fields[1]) >= 15000000:
    		if int(fields[2]) <= 17500000:
    			Value = (int(fields[1])/2)+(int(fields[2])/2)
    			Mid.append(Value)
#print Mid


#HiC#           
hic = hifive.HiC('hifive_output.hcp')

data = hic.cis_heatmap(chrom="chr17", start=15000000, stop=17500000, binsize=10000, datatype='fend', arraytype='full')
data[:, :, 1] *= np.sum(data[:, :, 0]) / np.sum(data[:, :, 1])
where = np.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = data[:, :, 0]


#Processing#
for m in Mid:
    Bin.append((m-15000000)/10000)
#print Bin
CTCF=np.unique(Bin)

#print(len(CTCF))

for i in range(len(CTCF)):
    for j in range(i,len(CTCF)):
        if float(data[CTCF[i],CTCF[j]]) > 1:
            Enriched.append((CTCF[i], CTCF[j], data[CTCF[i], CTCF[j]]))
#print Enriched

NEnriched = np.array(Enriched, dtype = np.dtype([('Bin1', int), ('Bin2', int), ('Score', float)]))
sort = np.argsort(NEnriched, order = ('Score', 'Bin1'))[::-1]
NEnriched = NEnriched[sort]

#Results#
print "Bin1\tBin2\tStart_Chr17\tEnd_Chr17\tEnrichment"
for Bin1, Bin2, Val in NEnriched:
	print Bin1, "\t", Bin2, "\t", (Bin1*10000)+15000000, "\t", (Bin2*10000)+15000000, "\t", Val 