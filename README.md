# GZ event receiver
Receive GZ API push requests


## 1. Deploy python virtual environment
https://docs.python.org/3/library/venv.html

Create virtual environment
```
$ mkdir push_receiver
$ cd push_receiver
$ python3 -m venv virtual_environment
```

Activate virtual environment
```
$ . virtual_environment/bin/activate
```


## 2. Install flask
https://flask.palletsprojects.com/en/2.0.x/

```
$ pip install Flask
```


## 3. Deploy receiver script to virtual environment

One option:
```
$ nano push_receiver.py
```
See [push receiver script](./push_receiver.py) in this repository to see what it might look like.


## 4. Run Flask app

On localhost:
```
$ export FLASK_APP=push_receiver.py
$ flask run
* Running on http://127.0.0.1:5000/
```
Other OSs: https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/#run-the-application

Publicly:
```
$ flask run --host=0.0.0.0
```
This tells your OS to listen on all publicly available IPs
https://flask.palletsprojects.com/en/2.0.x/quickstart/?highlight=externally%20visible


## 5. Sample curl json request
```
$ curl -X POST http://127.0.0.1:5000/receiver -H "Content-Type: application/json" -H "Transfer-Encoding: chunked" -d '{"jsonrpc": "2.0", "method": "addEvents"}'
```
