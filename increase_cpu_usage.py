import threading


# Function to simulate CPU usage
def cpu_intensive_task():
    while True:
        [x**2 for x in range(10_000)]  # Perform a heavy computation in a loop


# Start multiple threads to increase CPU usage
for _ in range(4):  # Adjust the number of threads to control the CPU load
    thread = threading.Thread(target=cpu_intensive_task)
    thread.daemon = True  # Ensure threads stop when the script ends
    thread.start()

print("Simulating high CPU usage. Press Ctrl+C to stop.")
input()  # Keep the script running
