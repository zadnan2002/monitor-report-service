# Real-Time Anomaly Detection Dashboard

## Project Description

The Real-Time Anomaly Detection Dashboard is a Python-based tool that streams data in real-time, identifies anomalies, and visualizes them using an interactive dashboard built with **Streamlit**. This dashboard is intended for monitoring metrics such as financial transactions or system performance, with a focus on detecting unusual events or values. The dashboard continuously updates the live data stream, highlighting detected anomalies and maintaining an alert log to help users stay informed about unusual behavior as it happens.

The project simulates a real-time data stream with regular patterns, seasonal elements, and random noise. It employs multiple anomaly detection algorithms to classify data points into normal or anomalous categories, displaying the results in a user-friendly graphical format.

## Chosen Algorithm and Effectiveness

### Algorithm Selection

1. **Z-Score Based Detection**:
   - The Z-score-based detection method is used to identify **sudden spike anomalies** in the data stream. This approach calculates the **Z-score** for each data point based on a rolling window of previous values. If the Z-score exceeds a given threshold, the point is flagged as anomalous.
   - **Effectiveness**: This method is effective for identifying **sharp deviations** from normal values, such as spikes caused by sudden, unexpected events. It is computationally efficient and works well for real-time detection of outliers in normally distributed data.

2. **Rolling Mean Deviation**:
   - The Rolling Mean Deviation method calculates the **mean** value within a rolling window and flags data points that deviate significantly (by a specified threshold) from this mean as **Mean Deviation Anomalies**.
   - **Effectiveness**: This approach is particularly effective for detecting **gradual drift** or **systematic shifts** in the data, which might indicate emerging trends or operational issues. It complements Z-score-based detection by identifying anomalies that occur more gradually over time.

These two methods together help provide a comprehensive view of anomalies—**sudden outliers** and **gradual deviations**—offering a robust solution for real-time monitoring and alerting.

## Project Setup and Running Instructions

### Prerequisites

- **Python 3.x**
- **Pip** for package management

### Installation Steps

1. **Clone the Repository**
   
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/real-time-anomaly-dashboard.git
   cd real-time-anomaly-dashboard
   ```

2. **Install Required Dependencies**
   
   Use `pip` to install the required dependencies. Make sure you are in the project root directory:
   ```bash
   pip install -r requirements.txt
   ```
   
   The `requirements.txt` file includes the following packages:
   - `streamlit`
   - `numpy`
   - `pandas`
   - `scikit-learn`
   - `altair`

3. **Run the Streamlit Application**
   
   Launch the application with the following command:
   ```bash
   streamlit run display.py
   ```
   This will start a local server, and you can access the dashboard by navigating to `http://localhost:8501` in your web browser.

### Project Structure

- **`data_stream_simulation/`**: Contains code to simulate the real-time data stream.
- **`anomaly_detection/`**: Contains the algorithms for detecting anomalies.
- **`display.py`**: The main file to run the Streamlit dashboard.
- **`requirements.txt`**: Lists the dependencies required to run the project.

### Usage

- **Real-Time Data Streaming**: The dashboard continuously streams data points and displays them graphically.
- **Anomaly Detection**: Detected anomalies are highlighted on the graph, with distinct markers for sudden spikes (red circles) and mean deviations (orange triangles).
- **Alert Log**: The alert log, visible in the dashboard, updates in real-time to keep track of all detected anomalies, including their timestamp, type, and value.

### Notes

- The Z-score threshold and mean deviation threshold can be adjusted in the code to make the anomaly detection more or less sensitive, depending on the nature of the data being monitored.
- The dashboard can be customized further to accommodate different types of metrics or additional algorithms.

## Contact

If you have questions or would like to contribute, please reach out via [your email or GitHub profile](https://github.com/yourusername).

