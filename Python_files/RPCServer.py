from xmlrpc.server import SimpleXMLRPCServer

def temp_str(temp_value):

    if (temp_value > 0 and temp_value <= 10):
        return 'Cold'
    elif (temp_value > 11 and temp_value < 20):
        return 'Warm'

server = SimpleXMLRPCServer(("localhost", 5002))
server.register_function(temp_str, 'tempCall')
server.serve_forever()