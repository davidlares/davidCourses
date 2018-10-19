from flask import Flask
app = Flask(__name__)
PORT = 8000
DEBUG = True

@app.route('/api/v1/courses', methods=['GET'])
def get_courses():
    pass

if __name__ == "__main__":
    app.run(port = PORT, debug = DEBUG)
