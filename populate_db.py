import MySQLdb
import os,sys
import datetime
from time import gmtime, strftime

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'sbhs_server.settings')


import django
django.setup()

from sbhs_server.tables.models import Board
from sbhs_server.credentials as credentials
from django.contrib.auth.hashers import make_password

db = MySQLdb.connect(host='credentials.DB_HOST',
    user='credentials.DB_USER',
    passwd='credentials.DB_PASS',
    db='credentials.DB_NAME')

print db
print 'database opened successfully'
# cursor = db.cursor()

## Datetime used when script runs
nowDate=datetime.datetime.now().date()
nowTime=str(datetime.datetime.now().time())
SplittedTime=nowTime.split(":")
NowdaTe=str(nowDate)
NowdaTe=NowdaTe.strip()   

print 'Nowdate ', NowdaTe
print 'SplittedTime ', SplittedTime
print 'nowTime ', nowTime[:8]

def create_board(number_of_board_and_users):
    cursor1 = db.cursor()
    for i in range(2,int(number_of_board_and_users)+1):
        mid = i
        print 'mid ',mid
        online = 1
        print 'online ',online
        created_at = datetime.datetime.now()
        print 'created_at ',created_at
        updated_at = datetime.datetime.now()
        print 'updated_at ',updated_at
        temp_offline = 0
        print 'temp_offline ',temp_offline
        power_status = 0
        ToInsert = [int(mid),int(online),created_at,updated_at,temp_offline,power_status]
        cursor1.execute("INSERT into tables_board(mid,online,created_at,updated_at,temp_offline,power_status) VALUES(%s,%s,%s,%s,%s,%s)",ToInsert)
        db.commit()
        cursor1.close()


def create_account(number_of_board_and_users):
    cursor2 = db.cursor()
    for i in range(1,int(number_of_board_and_users)+1):
        name = 'Super User '+str(i)
        print 'name ',name
        email= 'suser'+str(i)+'@gmail.com'
        print 'email ',email
        username='suser'+str(i)
        print 'username ',username
        password = 'suser'+str(i)+credentials.suserpasswd
        print 'password ',password
        pwd = make_password(password)
        print 'pwd ',pwd
        is_active = 1
        print 'is_active ',is_active
        is_admin = 0
        print 'is_admin ',is_admin
        # board = Board.objects.get(mid=i)
        # temp = i
        # if temp > 30:
        #     temp = 1
        board = i
        print 'board_id ',board
        created_at = datetime.datetime.now()
        print 'created_at ',created_at
        updated_at = datetime.datetime.now()
        print 'updated_at ',updated_at
        ToInsert = [pwd,name,username,email,is_active,is_admin,created_at,updated_at,board]
        cursor2.execute("INSERT into tables_account(password,name,username,email,is_active,is_admin,created_at,updated_at,board_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",ToInsert)
        db.commit()
        cursor2.close()

def create_slot(number_of_slot):
    cursor3 = db.cursor()
    for i in range(int(number_of_slot)):
        start_hour = i
        start_minute=0
        end_hour = i
        end_minute = 55
        create_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()
        ToInsert = [start_hour,start_minute, end_hour,end_minute,create_at,updated_at]
        cursor3.execute("INSERT into tables_slot(start_hour,start_minute,end_hour,end_minute,created_at,updated_at)VALUES(%s,%s,%s,%s,%s,%s)",ToInsert)
        db.commit()    
        cursor3.close()

number_of_board_and_users = raw_input('Enter Number of board and raw users you want.')
# number_of_slot = raw_input('Enter how many slots to create.')
create_slot(24) 
create_board(number_of_board_and_users)
create_account(number_of_board_and_users)
# cursor1.close()
# cursor2.close()
db.close()
print 'database closed successfully'