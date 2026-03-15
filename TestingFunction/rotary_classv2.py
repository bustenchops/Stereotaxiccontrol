#!/usr/bin/env python
#
# Raspberry Pi Rotary Encoder Class
# $Id: rotary_class.py,v 1.3 2021/04/20 12:23:04 bob Exp $
#
# Author : Bob Rathbone
# Site : http://www.bobrathbone.com
#
# This class uses standard rotary encoder with push switch
#
#

import RPi.GPIO as GPIO

import time
from testvariables import test_vary


class RotaryEncoder:

    CLOCKWISE=1
    ANTICLOCKWISE=2
    BUTTONDOWN=3
    BUTTONUP=4
    
    rotary_a = 0
    rotary_b = 0
    rotary_c = 0
    last_state = 0
    direction = 0

    Ccount = 0
    CCcount = 0

    # Initialise rotary encoder object
    def __init__(self, pinA, pinB, button, callbackdef):

        self.pinA = pinA
        self.pinB = pinB
        self.button = button
        self.sendtoSteppercontrol = callbackdef

        GPIO.setmode(GPIO.BCM)

        # The following lines enable the internal pull-up resistors
        # on version 2 (latest) boards
        GPIO.setwarnings(False)
        GPIO.setup(self.pinA, GPIO.IN) #pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pinB, GPIO.IN) # pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
        # Add event detection to the GPIO inputs
        GPIO.add_event_detect(self.pinA, GPIO.BOTH, callback=self.switch_event)
        GPIO.add_event_detect(self.pinB, GPIO.BOTH, callback=self.switch_event)
        GPIO.add_event_detect(self.button, GPIO.BOTH, callback=self.button_event, bouncetime=200)

        return

    def eventdelayconfirm(self):
        print('eventdelay calculation')
        self.comparetimer = time.time() * 1000
        self.testtime = self.comparetimer - test_vary.eventime
        if self.testtime >= test_vary.eventdelay:
            test_vary.eventime = self.comparetimer
            print('delay:', self.testtime)
            return True
        else:
            return False

    def counterotationdelay(self):
        print('counterotation calculation')
        self.comparerottimer = time.time() * 1000
        self.testtimerot = self.comparerottimer - test_vary.eventime
        if self.testtimerot >= test_vary.backwardrotdelay:
            test_vary.backwardrotdelay = self.comparerottimer
            print('delay:', self.testtimerot)
            return True
        else:
            return False


    # Call back routine called by switch events
    def switch_event(self,switch):
        # self.eventtime = time.time() * 1000
        # print ('event time:', self.eventtime)
        # print(f"event detected on {switch}")

        if GPIO.input(self.pinA):
            self.rotary_a = 1
        else:
            self.rotary_a = 0

        if GPIO.input(self.pinB):
            self.rotary_b = 1
        else:
            self.rotary_b = 0

        self.rotary_c = self.rotary_a ^ self.rotary_b
        new_state = self.rotary_a * 4 + self.rotary_b * 2 + self.rotary_c * 1
        delta = (new_state - self.last_state) % 4
        self.last_state = new_state
        self.event = 0

        if delta == 1:

            if self.direction == self.CLOCKWISE:
                if self.eventdelayconfirm():
                    self.event = self.direction
                # self.deltaonetime = time.time() * 1000
                # #self.difftime = self.deltaonetime - self.eventtime
                # print ('diff time:', self.difftime)
                # if self.difftime < 200:
                #     self.Ccount +=1
                #     print(self.Ccount)
                # else:
                #     self.Ccount = 0
                    print(self.direction, "  CLOCKWISE   ", self.CLOCKWISE)
            else:
                if self.counterotationdelay():
                    self.direction = self.CLOCKWISE
                # self.Ccount = 0
                    print(self.direction, "  changed to CLOCKWISE   ", self.CLOCKWISE)
        elif delta == 3:
    
            if self.direction == self.ANTICLOCKWISE:
                if self.eventdelayconfirm():
                    self.event = self.direction
                # self.deltathreetime = time.time() * 1000
                # self.defftime = self.deltathreetime - self.eventtime
                # print ('defftime:', self.defftime)
                # if self.defftime < 200:
                #     self.CCcount +=1
                #     print(self.CCcount)
                    print(self.direction, "  ANTICLOCKWISE   ", self.ANTICLOCKWISE)
            else:
                if self.counterotationdelay():
                    self.direction = self.ANTICLOCKWISE
                # self.CCcount = 0
                    print(self.direction, "  changed to ANTICLOCKWISE   ", self.ANTICLOCKWISE)
        #print("detected", event, )
        if self.event > 0:
            if self.event == 1:
                print('ACTION clockwise')
                self.sendtoSteppercontrol(self.event)
            if self.event == 2:
                print('ACTION counterclockwise')
                self.sendtoSteppercontrol(self.event)
            else:
                return

        #    self.callback(event)
            # print('do something count = ',self.count)
            #self.count += 1
        # print(event)

        return

# Push button up event
    def button_event(self, button):

        if GPIO.input(button):
            event = self.BUTTONUP
        else:
            event = self.BUTTONDOWN

        self.callback(event)
        print('button')
        return
 
# Get a switch state
def getSwitchState(self, switch):
    return GPIO.input(switch)

# End of RotaryEncoder class
