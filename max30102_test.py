import spo2Sensor as ss

sensor = ss.Spo2Sensor()
while 1:
	print(sensor.getbuffer("Red"))