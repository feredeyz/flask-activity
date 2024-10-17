from datetime import datetime

def get_datetime():
    curr = datetime.now()
    return f'{curr.year}-{curr.month}-{curr.day} {curr.hour}:{curr.day}'
    