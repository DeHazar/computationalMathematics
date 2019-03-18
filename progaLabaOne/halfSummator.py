from progaLabaOne.gate import *
class halfSum(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def getPinA(self):
        return super().getPinA()

    def getPinB(self):
        return super().getPinB()

    def setNextPin(self, source):
        super().setNextPin(source)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            sum = 0
        elif (a == 0 and b == 1) or (a == 1 and b == 0):
            sum = 1
        else:
            sum = 0

        if a == 1 and b == 1:
            carry = 1
        else:
            carry = 0

        return sum, carry