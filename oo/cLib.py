# Counter

class Indicator: 
    def __init__(self, label0):
        self.iterationMax = 2 
        self.label = label0

    def plus(self):
        self.iterationMax = self.iterationMax + 1

    def minus(self):
        self.iterationMax = self.iterationMax - 1

    def show(self):
        print('Label: ', self.label)
        print('Iteraion: ', self.iterationMax)

word = Indicator("verb")
print(word)
word.show()
# iWord = input("num?")
word.plus()
print(word)
word.show()
print("--")
word.minus()
word.minus()
print(word)
word.show()
