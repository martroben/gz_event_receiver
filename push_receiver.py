from flask import Flask, request
from time import perf_counter

# Service start time
t1 = perf_counter()

# Create Flask object
app = Flask(__name__)

body = None
headers = None

@app.route("/receiver", methods=["POST"])
def receiver():
  """accept POST requests by /receiver URL"""
  
  global body
  body = request.json
  
  global headers
  headers = request.headers
  return "OK"

@app.route("/status", methods=["GET"])
def status():
  """get status and last request by /status URL in browser"""
  
  uptime_minutes = (perf_counter() - t1) / 60
  return """service online<br>
            uptime: {:0.2f} min<br><br>
            last request:<br>
            headers: {}<br>
            body: {}""".format(uptime_minutes, headers, body)
