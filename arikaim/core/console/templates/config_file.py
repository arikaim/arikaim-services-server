content = """# Arikaim services server config file

# app settings
settings = {
    'port': 5000,
    'host': '127.0.0.1'
}

# db settings
db = {
    'type': 'mysql',
    'host': '127.0.0.1',
    'username': 'user name',
    'password': 'password',
    'database': 'db name',
    'synchronize': True,
    'logging': False,
    'entities': []
}

# global middlewares
middleware = {
}
"""