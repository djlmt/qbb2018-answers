#!/usr/bin/env python3

#Take as input the mapping file and a c_tab file from StringTie and find the corresponding translation from the mapping file.#
#Copy your data to the same folder as this program and run with: ./day2-HW-2.py mapping.txt StringTie.ctab optional_default_value (e.g. ./day2-HW-2.py fly.txt t_data.ctab NA)#

import sys
import numpy as np

Map = {}
i = 0
t = 0

#print(sys.argv[0], sys.argv[1], sys.argv[2])

#Check the input command#
if len(sys.argv) > 3:
    i = 1
    default = sys.argv[3]
    
#Create dictionary read by using <#
f = open(sys.argv[1])   
for count, line in enumerate( f ):
    if "DROME" in line: 
        fields = line.rstrip("\r\n").split()
        #Check whether the information is complete#
        if fields[-1].startswith("FBgn"):
            Map[fields[-1]] = fields[-2]

#print("test")

#Read from ctab file#
fn = open(sys.argv[2])
for countn, linen in enumerate( fn ):
    linen=linen.strip()
    if t > 0:
        fieldsn = linen.rstrip("\r\n").split()
        read = fieldsn[8]
        if read in Map:
            print(linen + "\t\t" + Map[read])
        elif i == 1:
            print(linen + "\t\t" + default)

    t += 1

#Count amount of reads#    
#print (i)