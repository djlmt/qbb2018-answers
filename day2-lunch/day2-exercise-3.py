#!/usr/bin/env python3

import sys

i = 0
b = 0
c = 0
#t = 0
#Input#
if len(sys.argv) > 1:
    #open from file#
    f = open( sys.argv[1] )
else:
    #read from the stain by using <#
    f = sys.stdin
   
for count, line in enumerate( f ):
    #Alignments#
    if line.startswith("SRR072893"):
        fields = line.rstrip("\r\n").split("\t")
        c = 0
        try:
            b = fields[19]
        except IndexError:
            c = 1
        if c == 0:
            if fields[19] == "NH:i:1":
                i = i+1                

print("There are " + str(i) + " alignments that map to exactly one location in the genome.")