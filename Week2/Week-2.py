#!/usr/bin/env python3

"""
Usage: ./Week-2.py ~/qbb2018-answers/Week2/Velveth/contigs.fa 

Compute the number of contigs, minimum/maximum/average contig length, and N50 of the assembled contigs. Data used here are Illumina 100bp paired-end reads.
"""

#Import#
import sys
import fasta

#Def
c = 0
max = 0
sum = 0
LN50 = []

#Input
Reader = fasta.FASTAReader( open(sys.argv[1]) )
#print(Reader)

#Count and calculate the min, max, and avg length and N50
for read in Reader:
    #print(read)
    length = len(read[1])
    LN50.append(length)
    if c == 0:
        min = length
    if length > max:
        max = length
    if length < min:
        min = length
    sum = sum+length
    #print(read[1], len(read[1]))
    c = c+1
avg = sum/c
LN50.sort()
#print(LN50)
if c%2 == 0:
    N50 = LN50[int(c/2)]
elif c%2 == 1:
    #print((c-1)/2)
    N50 = LN50[int((c-1)/2)]
    
#Print the results
print("There are " + str(c) + " contigs. The minimum contig length is " + str(min) + ". The maximum contig length is " + str(max) + ". The average contif length is " + str(avg) + ". The N50 is " + str(N50) + ".")