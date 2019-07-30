var ws = new WebSocket('ws://localhost:9000');

ws.onopen = function() {
    console.log('open');
};

ws.onmessage = function(event) {
  var msg = JSON.parse(event.data);
  console.log(msg);
}
