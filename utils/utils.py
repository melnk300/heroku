import random
from utils.cfg import CONFIG
import bcrypt
import vk

token = CONFIG.VK_TOCKEN


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()


def check_password(password, hash):
    return bcrypt.checkpw(password.encode(), hash.encode())


def send_message(user_id, text):
    session = vk.Session()
    api = vk.API(session, v='5.110')
    api.messages.send(access_token=token, user_id=str(user_id), message=text,
                      random_id=random.getrandbits(64))