# Real-Time System Resource Monitor

## Project Overview

This is a simple Flask-based web application that demonstrates Server-Sent Events (SSE) for real-time monitoring of system CPU and RAM usage. The application provides a live dashboard that updates in real-time without requiring page refreshes.

- Server-Sent Events (SSE) for continuous data streaming
- Simple web dashboard to visualize system resources

<div align="center">
<img width="787" alt="Screenshot 2024-12-07 at 9 45 48 PM" src="https://github.com/user-attachments/assets/fd399146-7210-4c12-905f-3a40de8d4134">
</div>

## Prerequisites

- Python 3.8+
- Flask
- psutil

## Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required dependencies:

   ```bash
   pip install flask psutil
   ```

## Running the Application

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:3000`

### Simulating Resource Usage (Optional)

To test the monitoring dashboard with simulated high resource consumption:

1. In a separate terminal, run the CPU usage simulation:

   ```bash
   python increase_cpu_usage.py
   ```

2. In another terminal, run the RAM usage simulation:

   ```bash
   python increase_ram_usage.py
   ```

## How It Works

### Server-Sent Events (SSE)

The application uses Flask's `generate_usage()` function to create a continuous stream of system resource data. The client-side JavaScript listens to this stream and updates the dashboard in real-time.

### Resource Monitoring

- CPU Usage: Uses `psutil.cpu_percent()` to get the current CPU utilization
- RAM Usage: Uses `psutil.virtual_memory().percent` to get the current memory usage

## Customization

- Modify the update interval in `app.py` by changing the `time.sleep()` duration
- Adjust the number of threads in `increase_cpu_usage.py` to simulate different CPU loads
