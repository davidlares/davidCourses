from flask import Flask
from flask import g # database on request
from flask import jsonify # geerating json responses
from flask import abort
from flask import request
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

@app.errorhandler(404)
def not_found(error):
    return jsonify(generate_response(404, error = 'Course not found'))

@app.errorhandler(400)
def bad_request(error):
    return jsonify(generate_response(404, error = 'Need parameters'))

@app.errorhandler(422)
def unprocessable_entity(error):
    return jsonify(generate_response(422, error = 'Unprocessable Entity'))


# all courses
@app.route('/api/v1/courses', methods=['GET'])
def get_courses():
    courses = Course.select() # select * from courses
    courses = [course.to_json() for course in courses]
    return jsonify(generate_response(data = courses))

# specific course
@app.route('/api/v1/course/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = try_course(course_id)
    return jsonify(generate_response(data = course.to_json())) # had to be serializable

def try_course(course_id):
    try:
        return Course.get(Course.id == course_id)
    except Course.DoesNotExist as e:
        abort(404)

# post courses
@app.route('/api/v1/courses', methods=['POST'])
def post_course():
    if not request.json:
        abort(400)
    # inserting and validating
    title = request.json.get('title','')
    description = request.json.get('description','')
    course = Course.new(title,description)
    if course is None:
        abort(422)
    return jsonify(generate_response(data = course.to_json()))

def generate_response(status = 200, data = None, error = None):
    return {'status': status, 'data': data, 'error': error}

if __name__ == "__main__":
    # running the model function
    initialize()
    app.run(port = PORT, debug = DEBUG)
