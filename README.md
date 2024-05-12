<p align="center">
  <img src="https://github.com/sylvestb/WLZ/assets/169618458/93812730-9cd7-4142-900c-90fe35e1a263" />
</p>


# Abstract

WLZ has seen its scope increase dramatically over the last few years and now has to deal with an increasingly large dataset of schools, CYP, delivery partners, corporate partners etc. Optimal usage of this rich dataset requires formal statistical analysis/data mining approaches. Machine-Learning algorithms such as equal-size spectral clustering and k-means clustering are easily applicable and promise exciting opportunities to WLZ.

# Equal-Size Spectral Clustering & Optimal clustering of schools into local hubs
This is a modification of the spectral clustering code that builds clusters balanced 
in the number of points. This can be particularly useful for grouping schools optimally into geographical hubs of a given size from their geographical coordinates.
A detailed explanation of this algorithm can be found in [there](https://towardsdatascience.com/spectral-clustering-aba2640c0d5b) and further details in [this blog post](https://medium.com/p/cce65c6f9ba3/edit).

## Code Prerequisities
You should install Python 3.9. There is a Pipfile to install the required libraries. Also seems to work fine in Python 3.8.3 (and packages from condo)

## The London Schools Dataset
In the folder `datasets` we have provided you with an example dataset: the coordinates of London schools sourced from [GLC data](https://data.london.gov.uk/dataset/london-schools-atlas). The set is very rich - for the purpose of this study, we only require the latitude/longitude of said schools.

## Examples: 
* example1.py: From a set of hyperparameters, you obtain clusters with sizes roughly equal to N / `nclusters`. In practice: we ask for the creation of a set number of hubs and find the optimal hub/groupings
* example2.py: From a range of cluster sizes, you obtain the clusters hyperparameters to run the clustering code. In practice: we ask to find the best school hubs of fixed size. The number of such hubs is thus obviously implied by the total number of schools.
Further explanations of a similar sort of problem are explained in the blog post referred to earlier.

## Outputs
Examples' outputs
* output1.html: shows example1 grouping all London schools into 6 geographical hubs
* output2.html: shows example2 building hubs of size 30-40 that cover the whole of London
Please download the whole html file and open it - github fails to display such large html's

![School Hubs](https://github.com/sylvestb/WLZ/assets/169618458/b859e5be-ad10-46b5-a34c-d2d3d8f88997)


# k-Means Clustering & Optimal CYP targeting
The algorithm and related algorithms such as plain [k-Means clustering](https://en.wikipedia.org/wiki/K-means_clustering) apply to a number of other useful applications, e.g. identifying cluster of students by relevant criteria such as geographical location as we just did for schools... or equally by interests/strenths/areas of opportunity (think scores in different fields as reported by questionaires or Skills-Builder-style benchmarks). This can be particularly relevant for the creation of target groups for events or newsletters. 

The fundamental idea is to see each CYP as represented by N coordinates (e.g. 1/ longitude 2/ latitude 3/ communication rating 4/ problem solving rating 5/ self-management rating 6/ collaboration rating 7/ assessed interest in field X 8/ assessed interest in field Y ... N/ assessed interest in **** ), much like we saw schools represented by 2 coordinates (1/ longitude 2/ latitude). This is commonly known as an N-dimensional space (as opposed to the 2-dimensional space of geographical coordinates).
It is then possible to identify the main characteristics of each cluster/CYP-group by looking at what is technically known as the "centroid" of each group.

As a matter of fact the analysis of schools clustering into geographical hubs could also be extended to higher dimensions using non-geographical data, which would help identify other logical school groupings based on their specific characteristics and target them better with the programmes WLZ offers.

Implementation of these techniques from the above example should be fairly straightforward.





