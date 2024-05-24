
from flask import Flask

# Create a flask
app = Flask(__name__)

# Create an API end point
@app.route('/')
def say_hello():
    return "Hello World"

if __name__ == '__main__': 
     app.run(host='0.0.0.0', port=8000)