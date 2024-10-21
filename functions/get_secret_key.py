import os
def get_secret_key():
    return os.urandom(30).hex()