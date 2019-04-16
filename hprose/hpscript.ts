var hprose = require('hprose');
var client = hprose.Client.create('http://127.0.0.1:7500/');
var proxy = client.useService('http://127.0.0.1:7500/', 'ping')
proxy.ping('',function(result){
   console.log(result) 
});
