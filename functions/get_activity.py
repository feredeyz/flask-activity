from functions.save_json import save_json

def get_activity():
    data = save_json('./data/users.json')
    activity = []
    for user in data.keys():
        activity.append(f'{user} зарегистрировался {data[user]["date"]}')
    
    return activity
    