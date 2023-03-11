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
desc:'The split for anomalous data'
type:float 
default:0.08
```

