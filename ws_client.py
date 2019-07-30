import websocket
import sys
try:
    import thread
except ImportError:
    import _thread as thread
import time
import json
from web_builder import add_component

def on_message(ws, sock_data):
    message = json.loads(sock_data)
    command = message["command"]
    probability = message["probability"]
    component = message["component"]
    position = message["position"]

    range_len = len(component)
    if command == "createComponent":
        for i in range(range_len):
            add_component(component[i], position[i])

def on_error(ws, error):
    print (error)

def on_close(ws):
    print ("### closed ###")
    time.sleep(2)
    sys.exit(0)

def on_open(ws):
    print('Open')

def initiate():
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:9000/",
        on_message = on_message,
        on_error = on_error,
        on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()

if __name__ == "__main__":
    initiate()
