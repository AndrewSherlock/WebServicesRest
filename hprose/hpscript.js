var hprose = require('hprose');
var client = hprose.Client.create('http://127.0.0.1:7500/');
var proxy = client.useService('http://127.0.0.1:7500/', 'ping');
proxy.ping('', function (result) {
    console.log(result);
});
//var result = client.ping('from javascript')
//console.log(result)
//var proxy = client.useService();
//var result = proxy.ping();
//console.log(result);
/*
function ping()
{
    //var ip = location.host;
    console.log('Called');
    return 'ping';
}

var server = new hprose.Server('http://127.0.0.1:7500/')
server.add(ping, 'ping');
server.start();

/*
var hprose = require("hprose");
var client = new hprose.HttpClient('http://127.0.0.1:5000/', 'ping');
var result = client.ping();
console.log(result)
/*
var proxy = client.useService('http://127.0.0.1:5000/', ['ping'])
proxy.ping(function(result){
    console.log(result);
});
/*
client.ready(function(proxy){
    proxy.ping('ping', function(result){
      console.log(result);
    });
});
/*
var proxy = client.useService(["ping", "GET"]);


proxy.ping("hello", function(result){
    console.log(result);
});
*/ 
