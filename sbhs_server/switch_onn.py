import sys
import serial
import time
ser = serial.Serial('/dev/ttyUSB0')
def switchOnn(args):    
    try:
        for i in range(1,17):
            # print 'args[1] ',args 
            time.sleep(1)
            arg = str(i).zfill(2)
            print arg
            ser.write(b'F'+arg)
        ser.close()
    except:
        print 'Error: Cannot connect to device ',args

if __name__ == '__main__':
    switchOnn(sys.argv)