#!/usr/bin/env python3

"""
Usage: ./Day5-lunch-2.py /Users/cmdb/data/results/stringtie/SRR072893/t_data.ctab
Determine an approximation of the promoter region for each of the transcripts in SRR072893/t_data.ctab file.
"""

#Import#
import sys
import pandas as pd

#Read#
ctab_file = open( sys.argv[1] )

#Print header#
head = ["chr", "start", "end", "t_name"]
print("\t".join(head))

for i, line in enumerate( ctab_file ):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    bed_order = [fields[1], fields[2], fields[3], fields[5]]
    #print(bed_order)
    if bed_order[1] == "+":
        #print("+")
        bed_order[1] = str(int(bed_order[2])-500)
        #print(bed_order)
        if float(bed_order[1]) < 0:
            print("test")
            bed_order[1] = str(0)
    elif bed_order[1] == "-":
        bed_order[1] = (str(int(bed_order[2])+500))
    #print(bed_order[1], bed_order[2])
    if float(bed_order[1]) > float(bed_order[2]):
        t = bed_order[1]
        bed_order[1] = bed_order[2]
        bed_order[2] = t
    #print(bed_order)
    inf = "\t".join(bed_order)
    print(inf)

    
    #bed_order_c = []
    #print( bed_order[1] )
    #bed_order_c.append(bed_order[0])
    #bed_order_c.append(bed_order[2])
    #print( bed_order_c )
    #if bed_order[1] == "+":
        #print("+")
    #    bed_order_c.append(str(int(bed_order[2])+500))
    #elif bed_order[1] == "-":
    #    bed_order_c.append(str(int(bed_order[2])-500))
    #bed_order_c.append(bed_order[3])
    #print("\t".join(bed_order_c))
    #ctab [bed_order[0]] = "\t".join(bed_order_c)