# OO_LightSwitch

class LightSwitch():
    def __init__(self) -> None:
        self.switchIsOn = True
        
    def turnOn(self) -> None:
        # turn the switch on
        self.switchIsOn = True

    def turnOff(self) -> None:
        # turn the switch off
        self.switchIsOn = False

    def show(self) -> None: # added for testing
        print(self.switchIsOn)

print("#1")
# Main code -1
oLightSwitch = LightSwitch() # create a LightSwitch object

# Calls to methods
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
oLightSwitch.turnOff()
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()

print("#2")
# Main code -2
oLightSwitch1 = LightSwitch()
oLightSwitch2 = LightSwitch()

object
# create a LightSwitch object
# create another LightSwitch
# Test code
oLightSwitch1.show()
oLightSwitch2.show()
oLightSwitch1.turnOn() # Turn switch 1 on

# Switch 2 should be off at start, but this makes it clearer
oLightSwitch2.turnOff()
oLightSwitch1.show()
oLightSwitch2.show()