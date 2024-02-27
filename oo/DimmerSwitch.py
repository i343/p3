# DimmerSwitch class
class DimmerSwitch():
    def __init__(self, labellocal):
        self.switchIsOn = False
        self.brightness = 0
        self.label = labellocal

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1
    
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Extra method for debugging
    def show(self):
        print('Label:', self.label)
        print('Switch is on?', self.switchIsOn)
        print('Brightness is:', self.brightness)

# Main code
oDimmer = DimmerSwitch("Dimmer0")
oDimmer.show()

# Turn switch on, and raise the level 5 times
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()

# Lower the level 2 times, and turn switch off
oDimmer.lowerLevel()
oDimmer.lowerLevel()
oDimmer.turnOff()
oDimmer.show()

# Turn switch on, and raise the level 3 times
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()

# Create first DimmerSwitch, turn it on, and raise the level twice
oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

# Create second DimmerSwitch, turn it on, and raise the level 3 times
oDimmer2 = DimmerSwitch('Dimmer2')
oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

# Create third DimmerSwitch, using the default settings

oDimmer3 = DimmerSwitch('Dimmer3')
# Ask each switch to show itself
oDimmer1.show()
oDimmer2.show()
oDimmer3.show()

