from functions.write_to_json import write_to_json
from functions.save_json import save_json
from uuid import uuid1

def write_messages(username, message):
    data = save_json('./data/msgs.json')
    data[str(uuid1())] = {"content": message, "user": username}
    write_to_json('./data/msgs.json', data)
    