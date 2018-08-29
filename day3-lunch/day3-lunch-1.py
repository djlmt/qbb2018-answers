#!/usr/bin/env python3

#Count the amount of protein coding genes.#
#Copy your data to the same folder as this program and run with: ./day3-lunch-1.py < data.gtf (e.g. ./day3-lunch-1.py < BDGP6.Ensembl.81.gtf)#

import sys

n = 0

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
            #print (fieldsn[4])
            #Check whether it is protein_coding#
            if "protein_coding" in fieldsn[4]:
                #print(fieldsn[4])
                n += 1

#Print results#             
print ("There are " + str(n) + " protein coding genes.")