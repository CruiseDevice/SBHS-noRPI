import os
# from time import time,sleep
from datetime import datetime
import time

import serial
# from threading import Timer

nowDate = datetime.now().date()
nowHour = datetime.now()
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sbhs_server.settings')

import django
django.setup()

from sbhs_server.tables.models import Booking, Account, Board

ser = serial.Serial('/dev/ttyUSB1')

def switch_on(b_id, booking_Date, nowhour,slot_id):
    if datetime.now().date() == booking_Date: #This must be booking date:
        tim_e = slot_id-2
        # print time
        # print type(time)
        # print nh
        # d = datetime.datetime.today() - timedelta(hours = 0 , minutes=5)
        # print d
        # convert time variable into time time:55
        nowHour = datetime.now()
        # print '{}:58'.format(time)
        tim_e = '{}:{}'.format(tim_e,nowHour.minute)
        tim_e = datetime.strptime(tim_e,'%H:%M').time()

        # create a newvariable with current hour:minute
        current_time = '{}:{}'.format(nowHour.hour,nowHour.minute)
        current_time = datetime.strptime(current_time,'%H:%M').time()

        # compare time with newvariable.
        # If both are equal, device should turn on
        # print 'inside switch_on', type(b_id)
        board = Board.objects.get(id=b_id)
        mid = board.mid
        mid = str(mid).zfill(2)   
        print mid 
        # if tim_e == current_time:
        time.sleep(0.2)
        ser.write(b'F'+mid)
        print ser
        board.power_status = 1
        board.save()
         
def switch_off(b_id):
    # print 'b_id in switch_off: ',b_id
    board = Board.objects.get(id=b_id)
    mid = str(b_id).zfill(2)   
    time.sleep(0.2)
    ser.write(b'N'+mid)
    # print ser
    board.power_status = 0
    board.save()

def check_future_slots():
    print nowDate    
    # b = Booking.objects.filter(booking_date=nowDate)
    # print b
    # print nowHour.hour
    print 'nowHour.hour+2',nowHour.hour + 2
    if nowHour.minute > 55:
        nowhour = nowHour.hour + 2
    else:
        nowhour = nowHour.hour + 1
    print 'nowhour ',nowhour
    # nowhour = str(nowHour)
    # nowHour = nowHour.now()+1
    get_slot_id = Booking.objects.filter(booking_date=nowDate,slot_id = nowhour).values('booking_date','slot_id','account_id') #this returns queryset
    # iterate over queryset to get slot_id and booking_date
    print 'get_slot_id',get_slot_id
    b_id_array = []
    for slot in get_slot_id:
        print slot['slot_id']
        print slot['booking_date'].date()
        print slot['account_id']
        slot_id = slot['slot_id']
        booking_Date = slot['booking_date'].date()
        id = slot['account_id']
        print slot_id
        print booking_Date
        print id
        get_board_id = Account.objects.get(id=id)
        print get_board_id
        b_id = get_board_id.board_id
        print b_id
        b_id = str(b_id).zfill(2)
        b_id_array.append(int(b_id))
        print b_id_array
   
    for b_id in b_id_array:
        print 'type of',type(b_id)
        switch_on(b_id,booking_Date,nowhour,slot_id)
    
    b_id_set = set(b_id_array)
    board_set = set(range(1,17))
    print 'board_set', board_set
    print 'intersection result:', board_set.difference(b_id_set)
    b_id_set_intersection = board_set.intersection(b_id_set)
    print b_id_set_intersection
    for b_id in board_set.difference(b_id_set):
        # print type(b_id)
        switch_off(b_id)
        # pass     
        
        











        # print booking_date['booking_date']
    # for dat_e in get_slot_id:
    #     print dat_e['booking_date'].date()

    # booking_Date = get_slot_id.booking_date.date()
    # slot_id = get_slot_id.slot_id
    # print slot_id
    # print get_slot_id.account_id
    # id = get_slot_id.account_id
    # get_user = Account.objects.get(id=id)
    # print get_user.board_id
    # print get_slot_id
    # b_id = get_user.board_id
    # print b_id
    # b_id = str(b_id).zfill(2)
    # switch_on(b_id, booking_Date, nowhour, slot_id)
    # ser.close()
    ser.close()    
        
check_future_slots()
    
