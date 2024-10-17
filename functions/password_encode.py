from hashlib import sha256
def encode(password):
    return sha256(b'{password}').hexdigest()