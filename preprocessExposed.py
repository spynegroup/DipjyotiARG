# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 13:21:27 2025

@author: sapta
"""

import pandas as pd
import statistics as stats

exposed_files = ["assets/GSE126584/exposed_1_SRR8580017_gene_counts_by_locus_tag.txt", \
                 "assets/GSE126584/exposed_2_SRR8580018_gene_counts_by_locus_tag.txt", \
                 "assets/GSE126584/exposed_3_SRR8580019_gene_counts_by_locus_tag.txt"]

sample_labels = ["exposed1", "exposed2", "exposed3"]

exposed = pd.DataFrame()
for sid in range(3):
    expr = pd.read_csv(exposed_files[sid], low_memory = False, sep = "\t", header = None, names = ["gene", sample_labels[sid]], index_col = 0, nrows = 4280)
    if exposed.empty:
        exposed = expr
    else:
        exposed = pd.merge(exposed, expr, left_index = True, right_index = True, how='inner')
        

exposed = exposed.transpose()

gene_labels = exposed.columns

exposed_plus1 = exposed + 1

exposed_d = exposed_plus1.copy()

for gene in gene_labels:
    print(gene)
    vals = exposed_plus1.loc[:, gene]
    mval = stats.median(vals)
    doubled = 2 * mval
    halved = 0.5 * mval
    
    for ridx in exposed_d.index:
        # print(control_d.loc[ridx, gene])
        if exposed_plus1.loc[ridx, gene] >= doubled:
            exposed_d.loc[ridx, gene] = 3
        elif (exposed_plus1.loc[ridx, gene] < doubled) and (exposed_plus1.loc[ridx, gene] > halved):
            exposed_d.loc[ridx, gene] = 2 
        elif (exposed_plus1.loc[ridx, gene] <= halved):
            exposed_d.loc[ridx, gene] = 1

exposed_d = exposed_d.transpose()

exposed_d.to_csv('assets\GSE126584\exposed_d.tsv', index=True, header=True, sep='\t', encoding='utf-8')































