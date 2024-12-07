import time

import psutil
from flask import Flask, Response, render_template

app = Flask(__name__)


# A generator function that streams events to the client
def generate_usage():
    while True:
        cpu = psutil.cpu_percent(interval=1)  # Get CPU usage percentage
        ram = psutil.virtual_memory().percent  # Get RAM usage percentage
        yield f'data: {{"cpu": {cpu}, "ram": {ram}}}\n\n'
        time.sleep(1)  # Push updates every second


# Route to serve the SSE stream
@app.route("/stream")
def stream():
    return Response(generate_usage(), content_type="text/event-stream")


# Route to serve the HTML page
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
