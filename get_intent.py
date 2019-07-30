import io
import json
import sys

from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import threading

seed = 42
engine = SnipsNLUEngine(config=CONFIG_EN, random_state=seed)

server = None
clients = []

class SimpleWSServer(WebSocket):
    def handleConnected(self):
        clients.append(self)

    def handleClose(self):
        clients.remove(self)


def run_server():
    global server
    global stop_thread
    server = SimpleWebSocketServer('', 9000, SimpleWSServer,
                                   selectInterval=(1000.0 / 15) / 1000)
    server.serveforever()

def run_pred(raw_command):
    with io.open("datasets/dataset.json") as f:
        dataset = json.load(f)
    engine.fit(dataset)
    parsed = engine.parse(raw_command)
    return parsed

def get_command(parsed_response):

    intent_dict = parsed_response["intent"]
    slots = parsed_response["slots"]

    command = intent_dict["intentName"]
    command_probability = intent_dict["probability"]

    component = []
    position = []

    for slot in slots:
        position_name = 'default'
        if slot["entity"] == 'component':
            component_name = slot["rawValue"]
            component.append(component_name)
        elif slot["entity"] == 'position':
            position_name = slot["rawValue"]
            position.append(position_name)

    if len(position) != len(component):
        diff = abs(len(position) - len(component))
        for i in range(diff):
            position.append('default')

    return command, command_probability, component, position

if __name__ == '__main__':

    t = threading.Thread(target=run_server)
    t.start()

    while True:
        user_command = input('> ')

        if user_command == '/stop':
            break
        parsed_response = run_pred(user_command)
        print(parsed_response)
        command, command_probability, component, position = get_command(parsed_response)
        for client in clients:
            client.sendMessage(json.dumps({'command': command, 'probability': command_probability, 'component': component, 'position': position}))

        print('Command: {}\nProbablity: {}\nComponent: {} \nPosition: {}'.format(command, command_probability, component, position))
    sys.exit("Bye!")
