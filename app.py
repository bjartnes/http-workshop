from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/failafterawhile")
def generate():
    for i in range(10):
        yield f"{i}, {i*i}\n"
        if i > 8:
            raise OverflowError()
    return generate()
