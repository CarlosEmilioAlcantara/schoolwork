# Create a program that gets the difference of two points
# Use the math module
import math;

class Difference:
    def __init__(self):
        self.firstNum = 0
        self.secondNum = 0
        self.thirdNum = 0
        self.fourthNum = 0

        self.firstHalf = 0
        self.secondHalf = 0

        self.equation = ""
        self.answer = 0

        print("Difference of two points calculator")
        print("########################################")

    def getDifference(self):
        while True:
            try:
                self.firstNum = input("Enter the first point: ")
                self.secondNum = input("Enter the second point: ")
                self.thirdNum = input("Enter the third point: ")
                self.fourthNum = input("Enter the fourth point: ")
                
                if self.firstNum.isnumeric() and self.secondNum.isnumeric() and\
                   self.thirdNum.isnumeric() and self.fourthNum.isnumeric():
                    self.firstNum = int(self.firstNum)
                    self.secondNum = int(self.secondNum)
                    self.thirdNum = int(self.thirdNum)
                    self.fourthNum = int(self.fourthNum)

                    self.equation = "sqrt(" + str(self.firstNum) + " - " + \
                                    str(self.secondNum) + ")^2 + " + "(" + \
                                    str(self.thirdNum) + " + " + \
                                    str(self.fourthNum) + ")^2)"

                    self.firstNum = math.pow(self.firstNum, 2)
                    self.secondNum = math.pow(self.secondNum, 2)
                    self.thirdNum = math.pow(self.thirdNum, 2)
                    self.fourthNum = math.pow(self.fourthNum, 2)

                    self.firstHalf = self.firstNum - self.secondNum
                    self.secondHalf = self.thirdNum + self.fourthNum

                    self.answer = math.sqrt(self.firstHalf + self.secondHalf)

                    print("The equation: \n" + self.equation)
                    print("The answer: " + str(self.answer))

                    break
                else:
                    print("Wrong values!")
            except ValueError:
                print("Wrong entry!")

def main():
    pointsDiffCalc = Difference()
    pointsDiffCalc.getDifference()

if __name__ == "__main__":
    main()