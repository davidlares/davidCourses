from flask import Flask
from flask import g # database on request
from flask import jsonify # geerating json responses
from models import DATABASE
from models import initialize
from models import Course

app = Flask(__name__)
PORT = 8000
DEBUG = True

# open a DB connection
@app.before_request
def before_request():
    g.db = DATABASE
    g.db.connect()

# close the DB connection
@app.after_request
def after_request(request):
    g.db.close()
    return request

@app.route('/api/v1/courses', methods=['GET'])
def get_courses():
    courses = Course.select() # select * from courses
    courses = [ course.to_json() for course in courses]
    return jsonify(generate_response(data = courses))

def generate_response(status = 200, data = None, error = None):
    return {'status': status, 'data': data, 'error': error}

if __name__ == "__main__":
    # running the model function
    initialize()
    app.run(port = PORT, debug = DEBUG)
