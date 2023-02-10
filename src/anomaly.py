import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

def preproc(data):
    df.iloc[0][0].split(";")
    df = pd.read_csv(data, names=columnnames)
    return df

def isolationForest_anomaly(data):    
    # Train Isolation Forest Model
    model = IsolationForest(contamination=0.1)
    model.fit(data)
    
    # Predict anomalies
    anomaly_scores = model.decision_function(data)
    anomalies = np.where(anomaly_scores < 0, 1, 0)
    
    return anomalies