# encoding: utf-8
import sys

classes = [ ]

with open('iris.data') as irisfile:
	for line in irisfile:
		clss = line.split(',')[-1].strip()
		classes.append(clss)

clustersmap = { }
rightclasses = 0
with open('clusters.txt') as clustersfile:
	i = 0
	for line in clustersfile:
		clusterid = int(line.strip())
		if classes[i] in clustersmap:
			if clusterid == clustersmap[classes[i]]:
				rightclasses += 1
		elif clusterid in clustersmap.values():
			pass
		else:
			clustersmap[classes[i]] = clusterid
			rightclasses += 1
		i += 1

print '%.3f%%' % (float(rightclasses) / len(classes) * 100)
