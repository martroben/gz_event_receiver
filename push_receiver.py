from flask import Flask, request
from time import perf_counter

# Service start time
t1 = perf_counter()

# Create Flask object
app = Flask(__name__)

last_request = None
headers = None

@app.route("/status", methods=["GET"])
def status():
  """URL to get status info via browser"""
  
  uptime_minutes = (perf_counter() - t1) / 60
  return """service online<br>
            uptime: {:0.2f} min<br>
            last request: {}<br>
            headers: {}""".format(uptime_minutes, last_request, headers)


@app.route("/receiver", methods=["POST"])
def receiver():
  """POST request receiver URL. Parse json content as dict"""
  
  global last_request
  last_request = request.json

  global headers
  headers = request.headers
  return "OK"
