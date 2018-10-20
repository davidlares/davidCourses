from flask import Flask

from models import DATABASE
from models import initialize
from models import Course

app = Flask(__name__)
PORT = 8000
DEBUG = True

@app.route('/api/v1/courses', methods=['GET'])
def get_courses():
    return "Hello, world"

if __name__ == "__main__":
    # running the model function
    initialize()
    app.run(port = PORT, debug = DEBUG)
