# CountNScream-
It will scream and count whenever people pass by it!


1)You will need these materials:

    1. 1 usable raspberry pi
    2. 1 PIR sensor
    3. 1 breadboard
    4. 1 buzzer
    5. 1 or 2 seven segment display (it depends on you)
    6. 2 10omega resister
    7. abundent jumper line
    
2)You will have to know which GPio you will plug-in
  (in this tutoral will use BCM)
   
    see pic1
    
3)Set up your PIR Sensor and make sure it can work

    1. Link Ground to the negitive line at breadboard
    2. Link Power to Positive line
    3. Link Output to any row and later on we will connect it with BCM 7 in case the jumper line isn't that long
    4. You can use PIR_test.py to test if PIR Sensor works
    
4)Set up your Buzzer and connect it with a resister and link it to BCM 8

5)Its time for the 7 segment display
