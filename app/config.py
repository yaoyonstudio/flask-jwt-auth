DB_USER = 'root'
DB_PASSWORD = ''
DB_HOST = 'localhost'
DB_DB = 'flask-jwt-auth'

DEBUG = True
PORT = 3333
HOST = "192.168.1.141"
SECRET_KEY = "my blog"

JWT_AUTH_URL_RULE = '/login'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB
