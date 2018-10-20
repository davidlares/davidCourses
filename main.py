from flask import Flask
from flask import g # database on request

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
    # print(courses)
    return "Already got the courses"

if __name__ == "__main__":
    # running the model function
    initialize()
    app.run(port = PORT, debug = DEBUG)
