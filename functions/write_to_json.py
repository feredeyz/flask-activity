from json import dumps
def write_to_json(path, content):
    with open(path, 'w') as f:
        f.write(dumps(content))
        f.close()