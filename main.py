from flask import Flask
app = Flask(__name__)
PORT = 8000
DEBUG = True

@app.route('/', methods=['GET'])
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(port = PORT, debug = DEBUG)
