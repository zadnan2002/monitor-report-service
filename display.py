import streamlit as st
import time
import pandas as pd
import altair as alt
from collections import deque
import sys
import os

# Adjust path to allow imports from sibling directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_stream_simulation.data_stream import data_stream
from anomaly_detection.detector import detect_anomaly  # Import detect_anomaly correctly

# Function to detect Mean Deviation anomalies (gradual deviation from mean)
def detect_mean_deviation_anomaly(data_point, window, threshold=5.0):
    mean = sum(window) / len(window)
    if abs(data_point - mean) > threshold:
        return True
    return False

# Real-time data stream dashboard using Streamlit with meaningful anomaly types
def streamlit_dashboard():
    # Set up the page configuration for the Streamlit dashboard
    st.set_page_config(page_title="Real-Time Anomaly Detection Dashboard", layout="wide")

    # Title and subtitle for the dashboard
    st.title("Real-Time Anomaly Detection Dashboard")
    st.subheader("Streaming Data with Different Types of Anomalies Highlighted in Real-Time")

    # Initialize Streamlit session state for data persistence between re-runs
    if 'data_points' not in st.session_state:
        st.session_state.data_points = deque(maxlen=200)  # Keep only the most recent 200 data points
        st.session_state.anomalies = deque(maxlen=200)  # Keep only the most recent 200 anomalies
        st.session_state.alert_log = []  # Log of detected anomalies for on-screen display

    # Rolling window to keep track of recent data
    window = deque(maxlen=50)

    # Initialize the data stream
    stream = data_stream()

    # Placeholders for the chart and alert log
    chart_placeholder = st.empty()
    log_placeholder = st.empty()  # Use an empty placeholder for the alert log

    # Stream the data and detect anomalies
    for i in range(500):
        # Get the next data point from the stream
        data_point = next(stream)
        window.append(data_point)

        # Append the real data point with its type to the rolling data storage
        st.session_state.data_points.append({"index": i, "value": float(data_point), "type": "Real Data"})

        # Check if the rolling window is full to start anomaly detection
        if len(window) == window.maxlen:
            new_anomaly_detected = False
            # Detect anomalies using different methods
            if detect_anomaly(data_point, window):
                anomaly = {"index": i, "value": float(data_point), "type": "Sudden Spike Anomaly"}
                st.session_state.anomalies.append(anomaly)
                # Add the anomaly to the on-screen log
                st.session_state.alert_log.append({
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "index": i,
                    "value": data_point,
                    "anomaly_type": "Sudden Spike Anomaly"
                })
                new_anomaly_detected = True
            elif detect_mean_deviation_anomaly(data_point, window):
                anomaly = {"index": i, "value": float(data_point), "type": "Mean Deviation Anomaly"}
                st.session_state.anomalies.append(anomaly)
                # Add the anomaly to the on-screen log
                st.session_state.alert_log.append({
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "index": i,
                    "value": data_point,
                    "anomaly_type": "Mean Deviation Anomaly"
                })
                new_anomaly_detected = True
            else:
                st.session_state.anomalies.append(None)

            # Update the alert log only if a new anomaly was detected
            if new_anomaly_detected:
                # Create a DataFrame for the log and use st.dataframe() for better responsiveness
                df_alert_log = pd.DataFrame(st.session_state.alert_log)
                log_placeholder.dataframe(df_alert_log, height=300)

        # Prepare the DataFrame for visualization, using rolling data
        df = pd.DataFrame(list(st.session_state.data_points))

        # Filter out None values from anomalies and prepare data for different types of anomalies
        anomalies_filtered = [a for a in st.session_state.anomalies if a is not None]
        df_anomalies = pd.DataFrame(anomalies_filtered)

        # Ensure the data types are explicitly set for Altair
        df = df.astype({'index': 'int', 'value': 'float'})
        if not df_anomalies.empty:
            df_anomalies = df_anomalies.astype({'index': 'int', 'value': 'float'})

        # Create the base chart for the real data stream
        base = alt.Chart(df).mark_line(color='blue').encode(
            x=alt.X('index:Q', title='Time Step'),
            y=alt.Y('value:Q', title='Value')
        ).properties(
            width=800,
            height=400
        )

        # Add anomaly points with different colors for different types
        if not df_anomalies.empty:
            sudden_spike_points = alt.Chart(df_anomalies[df_anomalies['type'] == 'Sudden Spike Anomaly']).mark_circle(color='red', size=60).encode(
                x='index:Q',
                y='value:Q',
                tooltip=['index', 'value', 'type']
            )
            mean_deviation_points = alt.Chart(df_anomalies[df_anomalies['type'] == 'Mean Deviation Anomaly']).mark_point(color='orange', size=60, shape='triangle').encode(
                x='index:Q',
                y='value:Q',
                tooltip=['index', 'value', 'type']
            )
            combined_chart = base + sudden_spike_points + mean_deviation_points
        else:
            combined_chart = base

        # Display the chart in Streamlit - update the same chart every 5 iterations to improve responsiveness
        if i % 5 == 0:
            chart_placeholder.altair_chart(combined_chart, use_container_width=True)

        # Introduce a short delay to simulate real-time streaming
        time.sleep(0.1)

# Run the Streamlit dashboard
if __name__ == "__main__":
    streamlit_dashboard()
