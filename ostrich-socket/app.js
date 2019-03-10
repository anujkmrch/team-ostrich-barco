var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
	res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
	console.log('a user connected');
  	socket.on('disconnect', function(){
    	console.log('user disconnected');
  	});

  	socket.on("connectme",function(msg){
  		console.log(msg);
  	});

  // must be called by master to broadcast the
  socket.on('get_status', function(msg){
    socket.broadcast.emit('send_status');
  });

  socket.on('acknowledge', function(msg){
  	console.log(msg)
    // socket.broadcast.emit('send_status');
    //must run sql query to add the status in the database
  });

});	

http.listen(3000, function(){
  console.log('listening on *:3000');
});