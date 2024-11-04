#!/bin/bash
input_a=$1
input_b=$2
output_a=$3
output_combined=$4

(zcat $input_b | awk '{$4=""; print $0}'; zcat $input_a ) | tr ' ' '\t' > $output_combined

zless $output_combined | awk '{print $4}' > combined_length.txt

#Sorting of the file 
zless combined_length.txt | sort -n | uniq -c > Data_length.tsv

# Calculate the total from the second column and store it in a variable
total=$(zless Data_length.tsv | awk '{total += $1} END {print total}')

# Normalize the second column and print the original line along with the normalized value
zless Data_length.tsv | awk  -v total="$total" '{normalized = $1 / total; print $0, normalized}' > normalised_sorted.tsv 

#Pasting the Reference and bed file together
paste <(cut -d ' ' -f 1-2 reference.hist) <(cut -d ' ' -f 4 <(tr -s ' ' ' ' <  normalised_sorted.tsv ))  > file_normalised.tsv

#Finding Max difference point
awk '{print $0 ,$2-$3}' file_normalised.tsv | tr ' ' '\t' >  $output_a


