import time


# Function to simulate RAM usage
def ram_intensive_task():
    data = []
    while True:
        data.extend([1] * 10_000_000)  # Append 10 million integers to the list
        print(
            f"Allocated {len(data) * 4 / (1024 ** 3):.2f} GB of memory"
        )  # Approx memory usage in GB
        time.sleep(1)  # Allow some time before the next allocation


print("Simulating high RAM usage. Press Ctrl+C to stop.")
ram_intensive_task()
