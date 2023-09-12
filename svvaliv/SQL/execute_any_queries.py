import MySQLdb
from environs import Env

env = Env()
env.read_env('.env')

db = MySQLdb.connect(user=env('USER'), password=env('PASSWORD'), database='beegeek')
cursor = db.cursor()