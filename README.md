# DipjyotiARG

The control and exposed gene expression files of E. coli are saved inside the 'assets/GSE126584/' subfolder.

## Step 1: Preprocess the gene expression files
The preprocessing was done using 'preprocessControl.py' and 'preprocessExposed.py'.

## Step 2: Infer transcriptional regulatory networks
The transcriptional regulatory networks for control and exposed were inferred with 'runGenie3control.R' and 'runGenie3exposed.R', respectively.
For network inference, an R package named 'GENIE3' [1, 2] was used: https://bioconductor.org/packages/release/bioc/html/GENIE3.html .
[1] Huynh-Thu V, Irrthum A, Wehenkel L, Geurts P (2010). “Inferring regulatory networks from expression data using tree-based methods.” PLoS ONE, 5(9), e12776. doi:10.1371/journal.pone.0012776.
[2] Aibar S, Bravo Gonzalez-Blas C, Moerman T, Huynh-Thu V, Imrichova H, Hulselmans G, Rambow F, Marine J, Geurts P, Aerts J, van den Oord J, Kalender Atak Z, Wouters J, Aerts S (2017). “SCENIC: Single-Cell Regulatory Network Inference And Clustering.” Nature Methods, 14, 1083-1086. doi:10.1038/nmeth.4463.

## Step 3: Visualise the networks
For visualisation, a software called 'Cytoscape' was used: https://cytoscape.org/ .
Please download and install Cytoscape.
Then go to File -> Open Session -> select 'assets/GSE126584/vizNets.cys'.
It will open the control and exposed networks.