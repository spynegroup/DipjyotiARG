
library(GENIE3)
# library(igraph)

exposed_d <- read.table("C://Users//sapta//Documents//GitHub//DipjyotiARG//assets//GSE126584//exposed_d.tsv",
                        header=TRUE,
                        sep="\t",
                        row.names = 1)

expr <- data.matrix(exposed_d)

set.seed(123) # For reproducibility of results

exposed_net <- GENIE3::GENIE3(expr, K = 3, nTrees = 2, nCores = 2, verbose = FALSE)

exposed_edges <- GENIE3::getLinkList(exposed_net)

exposed_edges_top <- exposed_edges[which(exposed_edges$weight > 0), ]

## igraph is not producing good figs
# cnet <- igraph::graph_from_adjacency_matrix(control_net)
# layout <- igraph::layout_nicely(cnet)
# igraph::plot.igraph(cnet, layout = layout, labels = NA)

write.csv(exposed_edges_top,
          file = "C://Users//sapta//Documents//GitHub//DipjyotiARG//assets//GSE126584//exposed_sif.tsv",
          quote = FALSE,
          row.names = FALSE)

# gene_labels <- rownames(expr)
# gdf <- data.frame(gene_labels, gene_labels)
# write.csv(gdf,
#           file = "C://Users//sapta//Documents//GitHub//DipjyotiARG//assets//GSE126584//gene_labels.tsv",
#           quote = FALSE,
#           row.names = FALSE)
