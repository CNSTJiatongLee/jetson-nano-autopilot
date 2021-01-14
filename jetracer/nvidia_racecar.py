from .racecar import Racecar
import traitlets
from adafruit_servokit import ServoKit
import threading

class NvidiaRacecar(Racecar):
    
    i2c_address = traitlets.Integer(default_value=0x40)
    steering_gain = traitlets.Float(default_value=-0.65)
    steering_offset = traitlets.Float(default_value=0)
    steering_channel = traitlets.Integer(default_value=0)
    throttle_gain = traitlets.Float(default_value=0.8)
    throttle_channel = traitlets.Integer(default_value=1)
    status = 0
    target = 0
    timer = None

    
    def __init__(self, *args, **kwargs):
        super(NvidiaRacecar, self).__init__(*args, **kwargs)
        self.kit = ServoKit(channels=16, address=self.i2c_address)
        self.kit._pca.frequency = 60
        self.steering_motor = self.kit.continuous_servo[self.steering_channel]
        self.throttle_motor = self.kit.continuous_servo[self.throttle_channel]
        self.steering_motor.throttle = 0
        self.throttle_motor.throttle = 0
    
    @traitlets.observe('steering')
    def _on_steering(self, change):
        self.steering_motor.throttle = change['new'] * self.steering_gain + self.steering_offset
    
    @traitlets.observe('throttle')
    def _on_throttle(self, change):
        global timer
        #self.throttle_motor.throttle = change['new'] * self.throttle_gain
        self.target = change['new'] * self.throttle_gain
        if((self.target < 0.1) and (self.target > -0.1)):
            self.status = self.target
            self.throttle_motor.throttle = self.status
        elif ((self.target < self.status) and (0 < self.status)):
            self.status = self.target
            self.throttle_motor.throttle = self.status
        else:
            self._soft_start()
        
    def _soft_start(self):
        global timer
        if(self.status <= self.target):
            self.status = self.status + 0.18
            if(self.status >= self.target):self.status=self.target
        else:
            self.status = self.status - 0.18
            if(self.status <= self.target):self.status=self.target
        self.throttle_motor.throttle = self.status
        if(self.status != self.target):
            timer = threading.Timer(1.2, self._soft_start)
            timer.start()
