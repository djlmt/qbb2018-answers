#!/usr/bin/env python3

import sys

i = 0
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
    if line.startswith("SRR072893") and i < 10:
        i = i+1
        fields = line.rstrip("\r\n").split("\t")
        print(fields[2])
    if i >= 10:
        break