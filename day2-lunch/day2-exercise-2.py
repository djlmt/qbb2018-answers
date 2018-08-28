#!/usr/bin/env python3

import sys

i = 0
b = 0
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
        b = 0
        for l in fields[5]:
            if l in ("I", "D", "N", "S", "H", "P", "=", "X"):
                b = 1
        for l in fields[5]:
            if l in ("M") and b == 0:
                i = i+1

print("There are " + str(i) + " alignments that match perfectly to the genome.")