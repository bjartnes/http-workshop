import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/fail")
def generate_crash():
    for i in range(10):
        yield f"{i}, {i*i}\n"
        if i > 8:
            raise OverflowError()
    return generate_crash()

@app.route("/hang/<delay>")
def generate_hang(delay):
    for i in range(10):
        if i > 4:
            time.sleep(float(delay))
        yield f"{i}, {i*i}\n"
    return generate_hang(delay)
