import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
#GPIO.add_event_detect(4, GPIO.BOTH)
#def my_callback():
#    GPIO.output(25, GPIO.input(4))
#GPIO.add_event_callback(4, my_callback)


def call(x):
    print "something happened:", x

#for i in range(0, 26):
for i in range(17, 18):
#    print i
    GPIO.setup(i, GPIO.IN)
#    #GPIO.add_event_detect(i, GPIO.BOTH)
#    GPIO.add_event_callback(i, call)


while True:
    print GPIO.input(17)
    time.sleep(1)
