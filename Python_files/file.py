import urllib.request
import json

import xmlrpc.client

with xmlrpc.client.ServerProxy("http://127.0.0.1:5001/") as proxy:
    #print(proxy)
    print(str(proxy.tempCall(12)))

'''
x = urllib.request.urlopen('http://kylegoslin1.pythonanywhere.com/')
json_file = json.load(x)
print(json_file['forecast'])

f = open('updates.txt', 'r')
x = f.readlines()
count = 0

output = '{'

This for loop will run over the lines in the file and print them to the console.


for line in x:
    output = output + '"line":'+ '"' +  line + '",'

f.close()


output = output[: -1] + '}'
print(output)
'''