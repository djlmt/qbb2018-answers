#!/bin/bash


# Usage: Faster way for calculating the amount of  alignments

grep -v "^@" SRR072893.sam | grep -v 2110000 | cut -f 3 | sort | uniq -c | Head
