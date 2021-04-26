import bcrypt


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()


def check_password(password, hash):
    return bcrypt.checkpw(password.encode(), hash.encode())


class AbstractCommand:
    def __init__(self, keys):
        self.__keys = []
        self.description = ''

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, mas):
        for k in mas:
            self.__keys.append(k.lower())

    def work(self):
        pass


class RegistrationCommand(AbstractCommand):
    def __init__(self):
        self.__keys = ['!рег', '!регистрация']
