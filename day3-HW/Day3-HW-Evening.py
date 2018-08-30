#!/usr/bin/env python3

#Find matching k-mers between a single query sequence and a database of targets.#
#Copy your data to the same folder as this program and run with: ./Day3-HW-Evening.py <target.fa> <query.fa> <k> (e.g. ./Day3-HW-Evening.py subset.fa droYak2_seq.fa 11)#

import sys
import fasta

#Input#
target = fasta.FASTAReader( open(sys.argv[1]) )
query = fasta.FASTAReader( open(sys.argv[2]) )
k = ( int(sys.argv[3]) )
kmers = {}
#c = 0

#Make Query into dic#
for ident, sequence in query:
    for i in range(0, len(sequence) - k):
        #print(len(sequence))
        kmer = sequence[i:i+k]
        kmers[kmer] = i

#Look for match in the dic#
for tident, tsequence in target:
    #print(kmer, ident, sequence)
    for t in range(0, len(tsequence) - k):
        tkmer = tsequence[t:t+k]
        #print(kmer, tkmer)
        if tkmer in kmers:
            #print("test")
            print(tident, t, kmers[kmer], kmer)
            #c = c+1

            #else:
                #print("test")
            #print(ident)
       
#for name in kmers:
    #print (name, kmers[name])
#print(c)