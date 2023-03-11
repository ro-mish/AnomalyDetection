import argparse
import pandas as pd
import numpy as np



# Define the command line arguments
parser = argparse.ArgumentParser(description='Generate synthetic cloud observability data and save it to a CSV file')
parser.add_argument('--rows', type=int, default=100, help='The number of rows to generate (default: 100)')
parser.add_argument('--freq', type=str, default='S', help='The frequency of the data (default: "S")')
parser.add_argument('--filename', type=str, default='synthetic_cloud_ops.csv', help='The filename of the output CSV file (default: "synthetic_cloud_ops.csv")')
parser.add_argument('--split', type=float, default=0.08, help='The split for anomalous data')

# Parse the command line arguments
args = parser.parse_args()

# Define the number of rows to generate
num_rows = args.rows
ANOMALY_SPLIT = args.split


# Define the start and end timestamps
start_time = pd.Timestamp('2022-01-01 00:00:00')
end_time = start_time + pd.Timedelta(seconds=num_rows-1)

# Define the list of metric names
metric_names = ['cpu_usage', 'memory_usage', 'network_throughput', 'error_rate']

# Define the list of dimensions for each metric
dimensions = [
    {'service': 'webserver', 'region': 'us-west-1'},
    {'service': 'database', 'region': 'us-west-1'},
    {'service': 'webserver', 'region': 'us-east-1'},
    {'service': 'worker', 'region': 'us-west-2'}
]

# Generate the timestamp column
timestamps = pd.date_range(start=start_time, end=end_time, freq=args.freq)

# Generate the metric_name and dimensions columns
metric_name = np.random.choice(metric_names, size=int(num_rows*(1-args.split)))
metric_name = np.append(metric_name, np.random.choice(metric_names, size=int(num_rows*(args.split))))

dimensions = np.random.choice(dimensions, size=num_rows)


# Generate the value column
regular_vals = np.random.uniform(low=10, high=50, size=int(num_rows*(1-ANOMALY_SPLIT)))
anom_vals = np.random.uniform(low=60, high=85, size=int(num_rows*(ANOMALY_SPLIT)))
values = np.append(regular_vals,anom_vals)
np.random.shuffle(values)

# Combine the columns into a pandas DataFrame
data = {
    'timestamp': timestamps,
    'metric_name': metric_name,
    'value': values,
    'dimensions': dimensions
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv(args.filename, index=False)

print(f'Successfully generated {num_rows} rows of synthetic cloud observability data and saved it to "{args.filename}"')
