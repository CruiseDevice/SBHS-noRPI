import sys
import serial
import time
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','sbhs_server.settings')

import django
django.setup()

from sbhs_server.tables.models import Board

ser = serial.Serial('/dev/ttyUSB1')
def switchOnn(args):    
    try:
        for i in range(1,17):
            b = Board.objects.get(id = i)
            # print 'args[1] ',args 
            time.sleep(0.2)
            arg = str(i).zfill(2)
            print arg
            ser.write(b'F'+arg)
            b.power_status = 1
            b.save()
        ser.close()
    except:
        print 'Error: Cannot connect to device ',args

if __name__ == '__main__':
    switchOnn(sys.argv)