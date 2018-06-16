# encoding: utf-8
import sys
import matplotlib.pyplot as plt

k = [ ]
acc = [ ]

sys.stdin.readline() # Discard header
for line in sys.stdin:
	inps = line.split()
	k.append(int(inps[0]))
	acc.append(float(inps[1][:-1]))

# Plotting
plt.xticks(k)
plt.xlabel('Tree height (k)')
plt.ylabel('Accuracy (%)')
plt.plot(k, acc)
plt.show()
