from peewee import * #ORM
import datetime

# DB string connection
DATABASE = MySQLDatabase('PyRest',host="localhost", user="root", passwd="admin");

class Course(Model):
    class Meta:
        # database assignation
        database = DATABASE
        db_table = 'courses'

    title = CharField(unique=True, max_length=250)
    description = TextField()
    created_at = DateTimeField(default = datetime.datetime.now())

# dummy data method - GET method instead of POST
def create_course():
    title = 'Flask Course'
    description = 'Free Flask Course'
    if not Course.select().where(Course.title == title):
        Course.create(title = title, description = description)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Course], safe=True) # should be extending Model -> that comes from peewee
    create_course()
    DATABASE.close()
