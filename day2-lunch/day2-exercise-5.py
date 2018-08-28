#!/usr/bin/env python3

import sys

s = 0
t = 0
a = 0
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
        s = s+float(fields[4])
        t = t+1
             
a = s/t

print("The average MAPQ score is " + str(a) + ".")