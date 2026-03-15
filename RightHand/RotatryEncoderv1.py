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
# Some modification to made by Kirk Mulatz - to adapt it for use in this scenario

import RPi.GPIO as GPIO

import time
from VariableList import var_list


class RotaryEncoder:
    CLOCKWISE = 1
    ANTICLOCKWISE = 2
    BUTTONDOWN = 3
    BUTTONUP = 4

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
        self.sendtoThreadedControl = callbackdef

        GPIO.setmode(GPIO.BCM)

        # The following lines enable the internal pull-up resistors
        # on version 2 (latest) boards
        GPIO.setwarnings(False)
        GPIO.setup(self.pinA, GPIO.IN) # pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pinB, GPIO.IN) # pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Add event detection to the GPIO inputs
        GPIO.add_event_detect(self.pinA, GPIO.BOTH, callback=self.switch_event)
        GPIO.add_event_detect(self.pinB, GPIO.BOTH, callback=self.switch_event)
        GPIO.add_event_detect(self.button, GPIO.BOTH, callback=self.button_event, bouncetime=200)

        return

    def stateanddelay(self, rotdata):
        print(var_list.eventime)
        print('state and delay calculation')
        self.comparetimer = time.time() * 1000
        if var_list.lastdirection == rotdata:
            print('test1')
            self.testtime = self.comparetimer - var_list.eventime
            if self.testtime >= var_list.eventdelay:
                print('test2')
                var_list.eventime = self.comparetimer
                print('delay:', self.testtime)
                return True
            else:
                print('event delay fail.....time:', self.testtime)
                return False
        elif var_list.lastdirection != rotdata:
            print('test3')
            self.testtime = self.comparetimer - var_list.eventime
            if self.testtime >= var_list.backwardrotdelay:
                print('test4')
                var_list.eventime = self.comparetimer
                print('delay:', self.testtime)
                return True
            else:
                print('event changerotation delay fail.....time:', self.testtime)
                return False


    # Call back routine called by switch events
    def switch_event(self, switch):
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
            if self.stateanddelay(delta):
                if self.direction == self.CLOCKWISE:
                    self.event = self.direction
                    print(self.direction, "  CLOCKWISE   ", self.CLOCKWISE)
                else:
                    print(self.direction, "  change to CLOCKWISE   ", self.CLOCKWISE)
                var_list.lastdirection = delta

        elif delta == 3:
            if self.stateanddelay(delta):
                if self.direction == self.ANTICLOCKWISE:
                    self.event = self.direction
                    print(self.direction, "  ANTICLOCKWISE   ", self.ANTICLOCKWISE)
                else:
                    self.direction = self.ANTICLOCKWISE
                    print(self.direction, "  changed to ANTICLOCKWISE   ", self.ANTICLOCKWISE)
                var_list.lastdirection = delta

            # print(self.direction, "  ANTICLOCKWISE   ", self.ANTICLOCKWISE)

        if self.event > 0:
            if self.event == 1:
                print('ACTION clockwise')
                self.sendtoThreadedControl(self.event)
            if self.event == 2:
                print('ACTION counterclockwise')
                self.sendtoThreadedControl(self.event)

        #    self.callback(event)
        # print('do something count = ',self.count)
        # self.count += 1
        # print(event)

        return

    # Push button up event
    def button_event(self, button):

        if GPIO.input(self.button):
            self.event = self.BUTTONUP
            print('release')
        else:
            self.event = self.BUTTONDOWN
            print('press')
            self.sendtoThreadedControl(self.event)
        # print('button pressed')
        # self.sendtoThreadedControl(self.event)

        return


# Get a switch state
def getSwitchState(self, switch):
    return GPIO.input(switch)

# End of RotaryEncoder class
