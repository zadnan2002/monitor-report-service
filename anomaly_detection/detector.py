from collections import deque
import numpy as np

# Function to detect anomalies using a rolling Z-score approach
def detect_anomaly(data_point, window, threshold=2.5):
    # Calculate the mean and standard deviation of the rolling window
    mean = np.mean(window)
    std_dev = np.std(window)

    # Calculate Z-score
    if std_dev == 0:
        z_score = 0
    else:
        z_score = (data_point - mean) / std_dev

    # If Z-score exceeds the threshold, it's an anomaly
    return abs(z_score) > threshold

# Example usage with a data stream
if __name__ == "__main__":
    stream = data_stream()
    window = deque(maxlen=50)  # Create a rolling window with the last 50 data points
    
    for _ in range(100):  # Monitor the first 100 data points
        data_point = next(stream)
        window.append(data_point)
        
        # Wait until we have enough data points to fill the window
        if len(window) == window.maxlen:
            if detect_anomaly(data_point, window):
                print(f"Anomaly detected: {data_point:.2f}")
            else:
                print(f"Normal data point: {data_point:.2f}")
