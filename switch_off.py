import serial
import time
import sys
ser = serial.Serial('/dev/ttyUSB1')
        
def switchOff(args):
    try:
        # it takes some time to initiate the port, add a sleep of 2 seconds.
        time.sleep(2)  
        print ser.name
        print type(ser)
        print ser
        print args
        arg = str(args[1]).zfill(2)
        # a = arg.split(' ')
        # print 'a=',a[]
        # return arg
        ser.write(b'N'+arg)
        ser.close()
    except:
        print 'Error: Cannot connect to device ',args

if __name__ == '__main__':
    switchOff(sys.argv)