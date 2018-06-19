import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(8, GPIO.OUT)
i = GPIO.input(PIR_PIN)
count = 0
seg = (4, 17, 27, 22, 23, 24, 25, 18)
# b a f g c d e h
digits = {
    '.': (0, 0, 0, 0, 0, 0, 0, 0),
    '0': (1, 1, 1, 0, 1, 1, 1, 0),
    '1': (1, 0, 0, 0, 1, 0, 0, 0),
    '2': (1, 1, 0, 1, 0, 1, 1, 0),
    '3': (1, 1, 0, 1, 1, 1, 0, 0),
    '4': (1, 0, 1, 1, 1, 0, 0, 0),
    '5': (0, 1, 1, 1, 1, 1, 0, 0),
    '6': (0, 1, 1, 1, 1, 1, 1, 0),
    '7': (1, 1, 1, 0, 1, 0, 0, 0),
    '8': (1, 1, 1, 1, 1, 1, 1, 0),
    '9': (1, 1, 1, 1, 1, 0, 0, 0)
}

for n in range(0, 8):
    GPIO.setup(seg[n], GPIO.OUT)

try:
               print ("Module Test CTRL+C to exit") 
               time.sleep(2)
               print ("Ready")
               while True :
                             if GPIO.input(PIR_PIN):
                                             print ("Motion Detected!", count)
                                             GPIO.output(8, 1)
                                             count += 1
                                             for n in range(0, 8):
                                                     GPIO.output(seg[n], digits[str( count  % 10 )][n])
                             elif i==0 :
                                 GPIO.output(8, 0)

                                 
               time.sleep(2)
except KeyboardInterrupt:
               print ("Quit")
               GPIO.cleanup()

