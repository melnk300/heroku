class Config:
    pass


class DevConfig(Config):
    SECRET = ''
    host = '34.66.70.1'
    JWT_SECRET = 'jwtsecretrusmwrkk'
    VK_SECRET = 'ZVqujr0gK3Vk8MuzjdiUYoEP8BVw5hzzC3HYkBY8'
    VK_TOCKEN = '2e0bdd87033cc895acaa9d86770a4db77f639492a5f6a493f8f8562892f791feb9a6e951b54908d2d35d1'
    PG = {
        'database': 'diary',
        'db_user': 'postgres',
        'password': 'Kat04102004',
        'host': '95.181.163.98',
        'port': 5432
    }


class TestConfig(Config):
    host = '34.66.70.1'
    PG = {
        'database': 'diary-test',
        'db_user': 'rusmwrkk',
        'password': 'Kat04102004',
        'host': '34.121.134.9',
        'port': 5432
    }


CONFIG = DevConfig()
