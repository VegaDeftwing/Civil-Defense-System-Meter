from __future__ import print_function
import psutil
import serial
import sys
import threading
import glob

def checkbtn(buttons):
    while 1:
        try:
            btnpress = buttons.read_until("\n")
            print(btnpress,end='')
            if btnpress == '2':
                print("Button 1 pressed")
        except:
            pass    



if sys.platform.startswith('win'):
    ports = ['COM%s' % (i + 1) for i in range(256)]
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    # this excludes your current terminal "/dev/tty"
    ports = glob.glob('/dev/tty[A-Za-z]*')
elif sys.platform.startswith('darwin'):
    ports = glob.glob('/dev/tty.*')
else:
    raise EnvironmentError('Unsupported platform')

result = []
names = []
for port in ports:
    try:
        s = serial.Serial(port, 9600, timeout=4)
        name = s.read_until("\n")
        print(name)
        if name == "RAD\r\n":
            print("RAD starting...")
            rad = s
        if name == "BUTTONS\r\n":
            print("BUTTONS starting...")
            s.close
            s = serial.Serial(port, 9600, timeout=1)
            buttons = s
        s.close()
        result.append(port)
        names.append(name)
    except (OSError, serial.SerialException):
        pass

print(result)
print(names)
if buttons.isOpen() == False:
    buttons.open()
if rad.isOpen() == False:
    rad.open()
if rad.isOpen():
    rad.write('1,255\n')
    print("Done")
bThread = threading.Thread(target=checkbtn,args=[buttons])
bThread.start()
while 1:
    cpu_percent = psutil.cpu_percent(interval=1) * 2.55
    cpu_formatted = "%d,%d\n" % (5,cpu_percent)

    ram_percent = psutil.virtual_memory()
    ram_percent =  ram_percent[2] * 2.55

    if ram_percent > 165:
        ram_formattedR = "%d,%d\n" % (1,ram_percent)
    else:
        ram_formattedR = "%d,%d\n" % (1,0)

    if ram_percent > 25 and ram_percent <  200:
        ram_formattedG = "%d,%d\n" % (2,ram_percent)
    else:
        ram_formattedG = "%d,%d\n" % (2,0)

    if ram_percent < 60:
        ram_formattedB = "%d,%d\n" % (3,ram_percent)
    else:
        ram_formattedB = "%d,%d\n" % (3,0)

    if ram_percent > 240 or cpu_percent > 240:
        yellow = "4,255"
    else:
        yellow = "4,0"

    if rad.isOpen():
        rad.write(cpu_formatted)
        rad.write(ram_formattedR)
        rad.write(ram_formattedG)
        rad.write(ram_formattedB)
        rad.write(yellow)
