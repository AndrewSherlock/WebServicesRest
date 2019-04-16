import ZODB, ZODB.FileStorage
import persistent
import transaction

def add_user_to_db(first_name, second_name, student_no):

    storage = ZODB.FileStorage.FileStorage('mydata.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    root.s1 = Student(first_name, second_name, student_no)
    transaction.commit()
    db.close()


def retrieve_user_from_db():

    storage = ZODB.FileStorage.FileStorage('mydata.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    transaction.commit()
    info = root.s1.first_name + ' ' + root.s1.second_name + ' ' + root.s1.student_no
    db.close()
    return  info


class Student(persistent.Persistent):
    def __init__(self, first_name, second_name, student_no):
        self.first_name = first_name
        self.second_name = second_name
        self.student_no = student_no

