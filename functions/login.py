from functions.save_json import save_json
from functions.password_encode import encode

def login(user: dict):
    users = save_json('./data/users.json')
    print(user)
    password = encode(user["password"])
    if user["username"] in users.keys():
        if password == users[user["username"]]["password"]:
            return "success"
        else:
            return "fail"
    else:
        return "fail"
    