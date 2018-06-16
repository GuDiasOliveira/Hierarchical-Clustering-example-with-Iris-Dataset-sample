# Hierarchical Clustering example with Iris Dataset sample

These scripts are run on **command line interface** and on **Linux** Operating system.

The ```iris.data``` dataset can be got from: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data.

## Required installations

1. **R**: https://www.r-project.org/
2. **Python**, with PIP and T-kinter: ```sudo apt-get install python python-pip python-tk```
3. **Matplotlib** Python library: ```python -m pip install matplotlib```

## Running the scripts

### Clustering data

Command:
```bash
Rscript clustering.r [tree-height]
```

Where ```[tree-height]``` is the number of the height in the hierarchical clustering tree where you want to cut (without the brackets).

Example:
```bash
Rscript clustering.r 3
```

It will write the file ```clusters.txt``` with each respective one-based cluster id.

### Checking accuracy

You can also get the accuracy of the clustering algorithm, based on the already classified data in ```iris.data``` file.

```bash
python accuracy.py
```

It reads from ```clusters.txt``` file and outputs the accuracy in percent.

### Clustering and then checking accuracy

You can run the clustering and then accuracy check at once:

```bash
Rscript clustering.r [tree-height] && python accuracy.py
```

It'll print the accuracy percentage. Replace ```[tree-height]``` with the tree height where you want to capture the clustered data.

### Reporting accuracies from 1 until a specific height

You can run a report of accuracies for each tree height value, with it's values in a sequence from 1 to a specific height cut.

```bash
./clust-acc.sh [max-tree-height]
```

Replace ```[max-tree-height]``` with the last tree height value.

Example, report clustering accuracy for height cuts from 1 (first) to the 7th clustering step:

```bash
./clust-acc.sh 7
```

### Viewing the accuracies report graphically

Pipe the report output to ```plot.py``` Python program.

```bash
./clust-acc.sh [max-tree-height] | python plot.py
```

For example, plot the accuracies report from the first to the 11th hirerarchical clustering step:

```bash
./clust-acc.sh 11 | python plot.py
```