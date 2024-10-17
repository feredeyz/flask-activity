from functions.write_to_json import write_to_json
from functions.save_json import save_json
from functions.password_encode import encode
from functions.get_datetime import get_datetime

def register(user):
    users = save_json('./data/users.json')
    print(user["username"], user["password"])
    if user["password"] == '':
        return False
    elif user["username"] in users.keys():
        return False
    users[user["username"]] = {"password": encode(user["password"]), "date": get_datetime()}
    write_to_json('./data/users.json', users)
    
    return True