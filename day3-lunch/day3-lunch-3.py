#!/usr/bin/env python3

#Find the nearest protein coding and non-protein coding genes.#
#Copy your data to the same folder as this program and run with: ./day3-lunch-3.py < data.gtf (e.g. ./day3-lunch-3.py < BDGP6.Ensembl.81.gtf)#

import sys

n = 0
Gene_name = []
Gene_position = []
Gene_type = []
Gene_name_n = []
Gene_position_n = []
Gene_type_n = []

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
        #Check whether it is a 3R gene#
        if fields[0] == "3R" and fields[2] == "gene":
            #Get information#
            start = int(fields [3])
            end = int(fields[4])
            mutation = 21378950
            fieldsn = fields[8].rstrip("\r\n").split(";")
            #print(fields[8])
            gene_name_raw = fieldsn[2].rstrip("\r\n").split('"')
            #print(gene_name_raw)
            gene_name = gene_name_raw[1]
            gene_type_raw = fieldsn[4].rstrip("\r\n").split('"')
            gene_type = gene_type_raw[1]
            if "protein_coding" in gene_type:
                Gene_name.append(gene_name)
                Gene_type.append(gene_type)
                if start >  mutation:
                    Gene_position.append(start-mutation)
                elif end < mutation:
                    Gene_position.append(mutation-end)
                else:
                    Gene_position.append(mutation-mutation)
            else:
                Gene_name_n.append(gene_name)
                Gene_type_n.append(gene_type)
                if start >  mutation:
                    Gene_position_n.append(start-mutation)
                elif end < mutation:
                    Gene_position_n.append(mutation-end)
                else:
                    Gene_position_n.append(mutation-mutation)

#Look for the nearest gene#         
index = Gene_position.index(min(Gene_position))
print("The nearest protein coding gene is " + Gene_name[index] + ".")
index_n = Gene_position_n.index(min(Gene_position_n))
print("The nearest nopn-protein coding gene is " + Gene_name_n[index_n] + ".")