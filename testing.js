var sys = require("sys") , my_http = require("http");
my_http.createServer(function(request,response){
    sys.put("I got kicked");
    response.writeHeader(200,{"Content-Type": "text/plain"});
    response.write("Hello world");
    response.end();
}).listen(8080);
sys.puts("Server Running on 8080");

my_http.createServer(function(request,response){}).listen(8080);
