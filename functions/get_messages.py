from functions.save_json import save_json
def get_messages():
    msgs = save_json('./data/msgs.json')
    return [f'{msg["user"]}: {msg["content"]}' for msg in msgs.values()]
    