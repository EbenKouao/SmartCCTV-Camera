#!/usr/bin/python
import sys
import time
import RPi.GPIO as GPIO

def main(argv):
    start = argv[1]
    end = argv[2]
    delay = argv[3]
    loop = argv[4]

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(11, GPIO.OUT)

    servo1 = GPIO.PWM(11, 50)
    servo1.start(0)
    for i in range(0, int(loop)):
        for dc in range(int(start), int(end), 1):
            servo1.ChangeDutyCycle(2+(dc/18))
            time.sleep(float(delay))
            servo1.ChangeDutyCycle(0)
            time.sleep(0.3)
            print(dc)

    servo1.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print ("servo.py <start> <end> <delay> <loop>")
    else:
        main(sys.argv)
    
