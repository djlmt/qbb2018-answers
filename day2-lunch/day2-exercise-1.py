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
    #Count number of alignments#
    if line.startswith("SRR072893"):
        i = i+1
    #else:
        #t = t+1

print("There are " + str(i) + " alignments.")