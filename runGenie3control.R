
library(GENIE3)
# library(igraph)

control_d <- read.table("C://Users//sapta//Documents//GitHub//DipjyotiARG//assets//GSE126584//control_d.tsv",
                        header=TRUE,
                        sep="\t",
                        row.names = 1)

expr <- data.matrix(control_d)

set.seed(123) # For reproducibility of results

control_net <- GENIE3::GENIE3(expr, K = 3, nTrees = 2, nCores = 2, verbose = FALSE)

control_edges <- GENIE3::getLinkList(control_net)

control_edges_top <- control_edges[which(control_edges$weight > 0), ]

## igraph is not producing good figs
# cnet <- igraph::graph_from_adjacency_matrix(control_net)
# layout <- igraph::layout_nicely(cnet)
# igraph::plot.igraph(cnet, layout = layout, labels = NA)

write.csv(control_edges_top,
          file = "C://Users//sapta//Documents//GitHub//DipjyotiARG//assets//GSE126584//control_sif.tsv",
          quote = FALSE,
          row.names = FALSE)

gene_labels <- rownames(expr)
gdf <- data.frame(gene_labels, gene_labels)
write.csv(gdf,
          file = "C://Users//sapta//Documents//GitHub//DipjyotiARG//assets//GSE126584//gene_labels.tsv",
          quote = FALSE,
          row.names = FALSE)
