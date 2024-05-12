"""
This script shows how to run the spectral equal size clustering.
From a set of hyperparameters, you get clusters with size roughly equal to N/ncluster
"""
import pandas as pd
import numpy as np
import logging
from source_code.spectral_equal_size_clustering import SpectralEqualSizeClustering
from source_code.visualisation import visualise_clusters
from source_code.distanceMatrixFromCoordinates import buildDistanceMatrixFromCoordinates



logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

# read the file with coordinates. This file is used only for visualization purposes
#coords = pd.read_csv("datasets/restaurants_in_amsterdam.csv")
coords = pd.read_csv("datasets/all_schools_xy_2016.csv")


# read the file of the symmetric distance matrix associated to the coords data frame
dist_tr =buildDistanceMatrixFromCoordinates("datasets/all_schools_xy_2016.csv")
print(type(dist_tr))

clustering = SpectralEqualSizeClustering(nclusters=6,
                                         nneighbors=int(dist_tr.shape[0] * 0.1),
                                         equity_fraction=1,
                                         seed=1234)

labels = clustering.fit(dist_tr)

coords["cluster"] = labels
logging.info(f"Points per cluster: \n {coords.cluster.value_counts()}")
clusters_figure = visualise_clusters(coords,
                                     longitude_colname="longitude",
                                     latitude_colname="latitude",
                                     label_col="cluster",
                                     zoom=11)
print("hello")

import plotly.io as pio
pio.renderers.default = "browser"
clusters_figure.show()
clusters_figure.write_html("outputs/output1.html")

