args <- commandArgs(trailingOnly=TRUE)

irisdata <- read.delim(file = 'iris.data', header = FALSE, sep = ',')
d <- dist(irisdata[-length(irisdata)], method = 'euclidian')
hc <- hclust(d, method = 'average')
plot(hc)
cl <- cutree(hc, k = args[1])
write(cl, file = 'clusters.txt', ncolumns = 1)