# Equal-Size Spectral Clustering
This is a modification of the spectral clustering code that builds clusters balanced 
in the number of points. This can be particularly useful for grouping schools into hubs of a given size from their geographical coordinates. The algorithm extends trivially to other applications such as children grouping based on n-dimensional characteristics.
A detailed explanation of this algorithm can be found 
[see also this Medium blog post for similar cases](https://medium.com/p/cce65c6f9ba3/edit).

## Prerequisities
You should install Python 3.9. There is a Pipfile to install the required libraries. Also seems to work fine in Python 3.8.3 (and packages from condo)

## Toy datasets
In the folder `datasets` we have provided you with a toy dataset
With the coordinates of London schools and another one with the coordinates of Amsterdam restaurants. Specifications of the input dataset
are explained in the blog post. 

## Examples
* example1.py: From a set of hyperparameters, you obtain clusters with sizes roughly equal to N / `nclusters`  
* example2.py: From a range of cluster sizes, you obtain the clusters hyperparameters to run the clustering code. 
