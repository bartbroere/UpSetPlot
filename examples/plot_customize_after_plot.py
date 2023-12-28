"""
=======================
Customizing axis labels
=======================

This example illustrates how the return value of the plot method can be used
to customize aspects of the plot, such as axis labels.
"""

from matplotlib import pyplot as plt

from upsetplot import generate_counts, plot

example = generate_counts()
print(example)

##########################################################################

plot_result = plot(example)
plot_result["intersections"].set_ylabel("Subset size")
plot_result["totals"].set_ylabel("Category size")
plot_result["matrix"].set_xlabel("Subsets between categories")
plt.show()
