import MySQLdb
from environs import Env

env = Env()
env.read_env('.env')

db = MySQLdb.connect(user=env('USER'), password=env('PASSWORD'), database='beegeek')
cursor = db.cursor()
cursor.execute('SET FOREIGN_KEY_CHECKS=0')
cursor.execute('SHOW TABLES')
for table, *_ in cursor.fetchall():
    # cursor.execute(f'DROP TABLE IF EXISTS {table}')
    print(table)