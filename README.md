# AnomalyDetection

A short project detailing different methods of detecting anomalies for cloud services. 

### Loading Data

To make the dataset, run the following below 

```
$ cd data
$ python datagen.py
```

There are also line arguments that can be passed when calling datagen:

```
--rows
desc: The number of rows to generate (default: 100)
type:int 
default:100, 

--freq 
desc: The frequency of the data in seconds
type:str 
default:'S'

--filename 
desc: The filename of the output CSV file (default: "synthetic_cloud_ops.csv")
type:str  
default:'synthetic_cloud_ops.csv'

--split 
desc: The split for anomalous data
type:float 
default:0.08
```

### Examining Results
Make sure to be in a conda environment, and have a notebook editor. Change directories to the notebook directory

```
$ cd notebooks
$ jupyter notebook
```

You can reproduce the results shown in the notebooks.


### Interpreting Results

1. Visually, we see that KMeans Clustering identified the anomalies the best, simply based on the clusters of data. 
2. Moreover, we examine that a normal  distribution is a viable heuristic method in determining anomalous events.
