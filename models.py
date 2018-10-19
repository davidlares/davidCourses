import peewee import * #ORM
import datetime

# DB string connection
DATABASE = MySQLDatabase('PyRest',host="localhost", user="root", passwd="");

class Course(Model):
    class Meta:
        database = DATABASE

    title = CharField(unique=True, max_length=250)
    description = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
