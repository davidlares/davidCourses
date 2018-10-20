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

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Course], safe=True) # should be extending Model -> that comes from peewee
    DATABASE.close()
