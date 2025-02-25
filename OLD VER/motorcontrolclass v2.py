import RPi.GPIO as GPIO

class StepperSetup:
    
    def _init_(self,enable,step,direction,limit):
        self.enable = enable
        self.step = step
        self.direction = direction
        self.limit = limit
        
        # setup GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.enable, GPIO.OUT, initial=1)
        GPIO.setup(self.step, GPIO.OUT, initial=0)
        GPIO.setup(self.direction, GPIO.OUT, initial=0)
        GPIO.setup(self.limit, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    def SteppGo(self,spindir,speed):
        
        for x in range (speed);
            if GPIO.input(self.limit):
                GPIO.output(self.enable,1)
                GPIO.output(self.direction,spindir)
                GPIO.output(self.step, 1)
                time.sleep(0.0001)
                GPIO.output(self.step, 0)
                time.sleep(0.0001)
            else:
                print("ERROR - limit reached")
        
        
    def ZeroStep(self,spindir,backoff):

        while GPIO.input(self.limit):
            SteppGo(spindir,1)
            
        if spindir == 0:
            revspin = 1
        else:
            revspin = 0
            
        for x in range(backoff):
            SteppGo(revspin,1)       
    
        
    def HomeTo(self,spindir,curStep,StepTo)
        self.curStep = curStep
        if self.curStep > StepTo:
            while self.curStep > StepTo:
                if GPIO.input(self.limit):
                    SteppGo(spindir,1)
                    self.curStep -= 1
                else:
                    print("ERROR - limit reached")
            
            return self.curStep
        
        else:
            while self.curStep < StepTo:
                if GPIO.input(self.limit):
                    SteppGo(spindir,1)
                    self.curStep += 1
            
            return self.curStep