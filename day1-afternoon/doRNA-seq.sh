#!/bin/bash


GENOME=~/qbb2018-answers/genomes/BDGP6
ANNOTATION=~/qbb2018-answers/genomes/BDGP6.Ensembl.81.gtf

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  mkdir $SAMPLE
  cd $SAMPLE
  cp ~/qbb2018-answers/rawdata/$SAMPLE.fastq $SAMPLE.fastq
  fastqc $SAMPLE.fastq
  hisat2 -p 4 -x $GENOME -U $SAMPLE.fastq -S $SAMPLE.sam 
  samtools view -b $SAMPLE.sam > $SAMPLE.bam
  samtools sort -o $SAMPLE_sorted.bam $SAMPLE.bam
  samtools index $SAMPLE_sorted.bam 
  stringtie $SAMPLE_sorted.bam -p 4 -e -G $ANNOTATION -o $SAMPLE.gft -B
  cd ..
done
