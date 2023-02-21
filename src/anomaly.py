import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

def preproc(fp):
    
    res = []
    with open(fp, 'r') as file:
        for i in file.readlines():
            res.append(i.strip("\n").split(";"))
    df = pd.DataFrame(res)
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    return df
    

def isolationForest_anomaly(data):    
    # Train Isolation Forest Model
    model = IsolationForest(contamination=0.1)
    model.fit(data)
    
    # Predict anomalies
    anomaly_scores = model.decision_function(data)
    anomalies = np.where(anomaly_scores < 0, 1, 0)
    
    return anomalies