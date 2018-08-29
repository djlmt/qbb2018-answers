#!/usr/bin/env python3

#Count the amount of genes for each type of genes.#
#Copy your data to the same folder as this program and run with: ./day3-lunch-2.py < data.gtf (e.g. ./day3-lunch-2.py < BDGP6.Ensembl.81.gtf)#

import sys

n = 0
Dic = {}

#Input#
if len(sys.argv) > 1:
    #open from file#
    f = open( sys.argv[1] )
else:
    #read by using <#
    f = sys.stdin
    
#Read lines#
for count, line in enumerate( f ):
    if line.startswith("#!"):
        continue
    else:
        #Get the data line#
        fields = line.rstrip("\r\n").split("\t")
        #print(fields[8])
        #Check whether it is a gene#
        if fields[2] == "gene":
            #Get biotype information#
            fieldsn = fields[8].rstrip("\r\n").split(";")
            gene_type_raw = fieldsn[4].rstrip("\r\n").split('"')
            #print(gene_type_raw[1])
            gene_type = gene_type_raw[1]
            #Count and store information#
            if gene_type in Dic:
                Dic[gene_type] += 1
            else:
                Dic[gene_type] = 1

#Print results#
print("GeneType " + "Count")             
for gene_type, count in Dic.items():
    print(gene_type, count)