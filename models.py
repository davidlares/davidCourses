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

    # instance method
    def to_json(self):
        return {'id': self.id, 'title': self.title, 'description': self.description}

    # validating resources
    @classmethod
    def new(cls, title, description): # cls param is required
        try:
            return cls.create(title = title, description = description)
        except IntegrityError as e:
            print("IntegrityError bro")
            return None

# regular methods
def create_course():
    # dummy data method - GET method instead of POST
    title = 'Flask Course'
    description = 'Free Flask Course'
    if not Course.select().where(Course.title == title):
        Course.create(title = title, description = description)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Course], safe=True) # should be extending Model -> that comes from peewee
    create_course()
    DATABASE.close()
