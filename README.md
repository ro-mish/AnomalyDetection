# AnomalyDetection

A short project detailing different methods of detecting anomalies for cloud services. 

#### To make the dataset, run the following below 

```
cd data
python datagen.py
```

There are also line arguments that can be passed when calling datagen:

```
--rows
type=int, default=100, help='The number of rows to generate (default: 100)')

--freq 
type=str, default='S', help='The frequency of the data (default: "S")')

--filename 
type=str, default='synthetic_cloud_ops.csv', help='The filename of the output CSV file (default: "synthetic_cloud_ops.csv")')

--split 
type=float, default=0.08, help='The split for anomalous data')
```

