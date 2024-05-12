# Abstract

WLZ has seen its scope increase dramatically over the last few years and now has to deal with an increasingly large dataset of schools, CYP, delivery partners, corporate partners etc. Optimal usage of this rich dataset requires formal statistical analysis/data mining approaches. Machine-Learning algorithms such as equal-size spectral clustering and k-means clustering offer promising and exciting opportunities to WLZ.

# Equal-Size Spectral Clustering
This is a modification of the spectral clustering code that builds clusters balanced 
in the number of points. This can be particularly useful for grouping schools optimally into geographical hubs of a given size from their geographical coordinates.
A detailed explanation of this algorithm can be found in [there](https://towardsdatascience.com/spectral-clustering-aba2640c0d5b) and further details in [this blog post](https://medium.com/p/cce65c6f9ba3/edit).

## Prerequisities
You should install Python 3.9. There is a Pipfile to install the required libraries. Also seems to work fine in Python 3.8.3 (and packages from condo)

## Toy datasets
In the folder `datasets` we have provided you with a toy dataset
With the coordinates of London schools sourced from [GLC data](https://data.london.gov.uk/dataset/london-schools-atlas). Specifications of the input dataset
are explained in the blog post. 

## Examples
* example1.py: From a set of hyperparameters, you obtain clusters with sizes roughly equal to N / `nclusters`. In practice: we ask for the creation of a set number of hubs and find the optimal hub/groupings
* example2.py: From a range of cluster sizes, you obtain the clusters hyperparameters to run the clustering code. In practice: we ask to find the best school hubs of fixed size. The number of such hubs is thus obviously implied by the total number of schools.

## Outputs
Examples' outputs
* output1.html: shows example1 grouping all London schools into 6 geographical hubs
* output2.html: shows example2 building hubs of size 20-30 that cover the whole of London
Please download the whole html file and open it - github fails to display such large html's

# k-Means Clustering: Further applications
The algorithm and related algorithms such as plain [k-Means clustering](https://en.wikipedia.org/wiki/K-means_clustering) apply to a number of other useful applications, e.g. identifying cluster of students by relevant criteria such as geographical location as we just did for schools, or equally by interests/strenths/areas of opportunity (think scores in different fields as reported by questionaires or skillsBuilder-style criteria). This can be particularly relevant for the creation of target groups for events or newsletters. Implementation of these techniques from the above example should be fairly straightforward.
