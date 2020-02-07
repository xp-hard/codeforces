import serial, time

serial_port = "/dev/ttyUSB0"
baund_rate = 9600
t1 = time.time()
counter = 0
f = open('output.txt', 'a')
linelist = []
ser = serial.Serial(serial_port, baund_rate)
while len(linelist) <= 100000:
    counter += 1
    line = ser.readline()
    line = line.decode('utf-8')
    linelist.append(line.strip())

print(*linelist, file=f, sep="")
f.close()
print(time.time() - t1)
