import bcrypt


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()


def check_password(password, hash):
    return bcrypt.checkpw(password.encode(), hash.encode())