from json import loads
def save_json(path):
    with open(path, 'r') as f:
        content = loads(f.read())
        f.close()
    return content