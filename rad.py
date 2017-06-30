import psutil
import serial
rad = serial.Serial('/dev/ttyUSB0', 9600)
if rad.isOpen() == False:
    ser.open()
if rad.isOpen():
    rad.write('1,255\n')
    print 'Done'
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
