import datetime


def record_func_call(func_call):
    file = open('calls.log', 'a') # opens func file and appends to file
    log_text = '[ function_call : ' + func_call + ' time_of_call : ' + str(datetime.datetime.utcnow()) + '] \n'
    file.write(log_text)
    file.close()


def add_to_users_log(student_no, first_name, last_name):
    file = open('users.log', 'a') # opens users file and adds user to file
    log_text = 'first_name : ' + first_name + ' second_name : ' + last_name + ' student_no ' + student_no + '\n'\
                'logged_time : ' + str(datetime.datetime.utcnow()) + '\n'

    file.write(log_text)
    file.close()