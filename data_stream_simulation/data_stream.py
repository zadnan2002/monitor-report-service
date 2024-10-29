import numpy as np
import time

# Function to simulate a real-time data stream
def data_stream():
    time_step = 0
    while True:
        # Seasonal pattern - sine wave to simulate periodic change
        seasonal = np.sin(time_step / 20.0) * 10  

        # Trend - can simulate an increasing or decreasing pattern, for simplicity keeping it constant
        trend = 0.05 * time_step

        # Random noise - normally distributed
        noise = np.random.normal(0, 2)

        # Combine all components to create the data point
        data_point = seasonal + trend + noise

        # Introduce occasional anomalies
        anomaly = np.random.choice([0, np.random.normal(30, 5)], p=[0.98, 0.02])
        data_point += anomaly

        yield data_point
        time_step += 1

        # Simulate a real-time stream by adding a delay
        time.sleep(0.1)  # 0.1 seconds delay to simulate real-time data feed
