import time

#
## class to handle simple toggling of a boolean every "delay" number of seconds
#

class TimedToggle(object):
    # inti variables
    def __init__(self, delay):
        self.lastToggleTime = time.time()
        self.toggleDelay = delay
        self.toggleState = True
        self.toggleSinceLast = False
     
    #
    # get the current toggle state after first updating state if it's time to do so
    #   
    def getToggleStatus(self):
        elapsed = time.time() - self.lastToggleTime
        if elapsed > self.toggleDelay:
            self.toggleState = not self.toggleState
            self.lastToggleTime = time.time()
            self.toggleSinceLast = True
        return self.toggleState
 
    #
    # method so caller can check if state just changed (since last call to getToggleStatus)
    # if it did, reset self.toggleSinceLast back to False
    # return: value of self.toggleSinceLast
    #   
    def getToggleSinceLast(self):
        tmp = self.toggleSinceLast # save current state to return
        if self.toggleSinceLast == True: # change state if needed for next time
            self.toggleSinceLast = False
        return tmp # return value of self.toggleSinceLast before we changed it


