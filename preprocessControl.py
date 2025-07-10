# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 13:21:27 2025

@author: sapta
"""

import pandas as pd
import statistics as stats

control_files = ["assets/GSE126584/control_1_SRR8580014_gene_counts_by_locus_tag.txt", \
                 "assets/GSE126584/control_2_SRR8580015_gene_counts_by_locus_tag.txt", \
                 "assets/GSE126584/control_3_SRR8580016_gene_counts_by_locus_tag.txt"]

sample_labels = ["control1", "control2", "control3"]

control = pd.DataFrame()
for sid in range(3):
    expr = pd.read_csv(control_files[sid], low_memory = False, sep = "\t", header = None, names = ["gene", sample_labels[sid]], index_col = 0, nrows = 4280)
    if control.empty:
        control = expr
    else:
        control = pd.merge(control, expr, left_index = True, right_index = True, how='inner')
        

control = control.transpose()

gene_labels = control.columns

control_plus1 = control + 1

control_d = control_plus1.copy()

for gene in gene_labels:
    print(gene)
    vals = control_plus1.loc[:, gene]
    mval = stats.median(vals)
    doubled = 2 * mval
    halved = 0.5 * mval
    
    for ridx in control_d.index:
        # print(control_d.loc[ridx, gene])
        if control_plus1.loc[ridx, gene] >= doubled:
            control_d.loc[ridx, gene] = 3
        elif (control_plus1.loc[ridx, gene] < doubled) and (control_plus1.loc[ridx, gene] > halved):
            control_d.loc[ridx, gene] = 2 
        elif (control_plus1.loc[ridx, gene] <= halved):
            control_d.loc[ridx, gene] = 1

control_d = control_d.transpose()

control_d.to_csv('assets\GSE126584\control_d.tsv', index=True, header=True, sep='\t', encoding='utf-8')































