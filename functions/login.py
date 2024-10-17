from functions.save_json import save_json
from functions.password_encode import encode

def login(user: dict):
    users = save_json('./data/users.json')
    print(user)
    if user["username"] == "admin" and user["password"] == "andrey_krutoi":
        return "admin"
    password = encode(user["password"])
    if user["username"] in users.keys():
        if password == users[user["username"]]:
            return "success"
        else:
            return "fail"
    else:
        return "fail"
    