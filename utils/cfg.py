class Config:
    pass


class DevConfig(Config):
    SECRET = ''
    host = '34.66.70.1'
    JWT_SECRET = 'jwtsecretrusmwrkk'
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
