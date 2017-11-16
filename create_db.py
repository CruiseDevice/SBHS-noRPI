import MySQLdb

db = MySQLdb.connect(host='localhost',
    user='root',
    passwd='saturn',)

print db
c = db.cursor()
c.execute('create database if not exists sbhs_norpi3')
db.close()