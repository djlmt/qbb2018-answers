#!/usr/bin/env python3

#Map FlyBase gene IDs to UniProt IDs.#
#Copy your data to the same folder as this program and run with: ./day2-HW-1.py < mapping.txt (e.g. ./day2-HW-1.py < fly.txt)#

import sys
import numpy as np

Map = {}
i = 0

#Input#
if len(sys.argv) > 1:
    #open from file#
    f = open( sys.argv[1] )
else:
    #read by using <#
    f = sys.stdin
    
#Read lines#
for count, line in enumerate( f ):
    if "DROME" in line: 
        fields = line.rstrip("\r\n").split()
        #Check whether the information is complete#
        if fields[-1].startswith("FBgn"):
            Map[fields[-1]] = fields[-2]


#Print results#            
for Fly, Uni in Map.items(): 
    print(Fly + "\t\t" + Uni)
    i += 1

#Count amount of reads#    
#print (i)