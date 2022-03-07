from flask import Flask, request
from time import perf_counter

# Service start time
t1 = perf_counter()

# Create Flask object
app = Flask(__name__)

last_request = None

@app.route("/status", methods=["GET"])
def status():
  """URL to get status info via browser"""
  uptime_minutes = (perf_counter() - t1) / 60
  return """"service online<br>
             uptime: {:0.2f} min<br>
             last request: {}""".format(uptime_minutes, last_request)

@app.route("/receiver", methods=["POST"])
def receiver():
  """URL to receive POST requests. Parse content from json to dict"""
  global last_request
  last_request = request.json
  return "OK"
