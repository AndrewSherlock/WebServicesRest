from flask import Flask, request
import datetime
import urllib.request
import json
import pika
import Datastore
import threading
import hprose
import socket

from logging_functions import record_func_call, add_to_users_log
import xmlrpc.client

app = Flask(__name__)
if __name__ == "__main__":
    app.run()

# Used to call function to start listening ports on first request
@app.before_first_request
def start_listening_threads():
    record_func_call('start_listening_ports')
    rabbit_thread = threading.Thread(target=start_rabbit_run) # starts the thread that will handle the rabbit mq, stops freezing
    th = threading.Thread(target=start_hprose)# handles thread for hprose
    rabbit_thread.start()
    th.start()


def start_hprose():
    server = hprose.HttpServer(port=7500)
    server.addFunction(ip_ping, 'ping') # add ping function for hprose to call
    server.start()


def start_rabbit_run():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_consume(callback, queue='hello', no_ack=True)
    channel.start_consuming()


def ip_ping(callers_ip):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    string_to_return = 'Pong target IP :: ' + str(ip_address) # retrieves ip address and displays to the user
    return string_to_return


@app.route("/")
def hello():
    record_func_call('hello')
    return "Hello World!"


@app.route("/justweather")
def weather_func():
    record_func_call('weather_func')
    # Gets the information from API
    x = urllib.request.urlopen('http://kylegoslin1.pythonanywhere.com/')
    json_file = json.load(x)
    current_weather = json_file['forecast']
    return '{Current weather :"' + current_weather + '"}'


@app.route("/updates")
def read_from_file():
    record_func_call('updates')
    f = open('updates.txt', 'r')
    x = f.readlines()
    output = '{'

    for line in x:
        output = output + '"line":' + '"' + line + '",'

    f.close()
    output = output[: -1] + '}'
    return output

buffer = []
jsonStr = ''


def callback(ch, method, properties, body):
    global buffer,jsonStr
    buffer.append(body)
    jsonStr = '{ "messages" : [ '

    # gets values in buffer and formats to json string
    for message in buffer:
        jsonStr = jsonStr + '"' + str(message) + '",'

    jsonStr = jsonStr[:-1] + ']}'



@app.route("/read")
def read_rabbit():
    record_func_call('read')
    global buffer,jsonStr
    return jsonStr


@app.route("/insert")
def record_user_log():
    student_no = request.args.get('student_no')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    record_func_call('record_user_log')

    # if parameters are missing, show error on page
    if student_no == None or first_name == None or last_name == None:
        return 'Missing data fields'

    # else add to log file and data store
    add_to_users_log(student_no, first_name, last_name)
    Datastore.add_user_to_db(first_name, last_name, student_no)

    return 'Info added to file'


@app.route('/ping', methods=['GET', 'POST'])
def ping():
    record_func_call('ping')
    return 'pong ' + str(datetime.datetime.utcnow())


@app.route('/callClient')
def temp_call():
    record_func_call('temp_call')
    temp = int(request.args.get('temp'))
    with xmlrpc.client.ServerProxy("http://127.0.0.1:5002/") as proxy:
        return str(proxy.tempCall(temp))


@app.route('/retrieve')
def retrieve():
    record_func_call('retrieve')
    return Datastore.retrieve_user_from_db()



#kylegoslin1.pythonanywhere.com
#python -m flask run
#SET FLASK_APP=main.py