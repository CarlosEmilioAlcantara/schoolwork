# Create a program that:
# a. Gets the difference of two squares
# b. Gets the difference of points
# c. Computes for double angle formulas (sin, cos, tan)
# d. Compute for sample mean (grouped, ungrouped)
# Use the math module
# Use the cmath module
import math;
import cmath;

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

        print("MATHEMATICAL CALCULATOR")
        print("###############################")

    def getDifferenceOfSquares(self):
        print("Calculating for the difference of two squares")
        print("-------------------------------")

        while True:
            try:
                self.firstNum = input("Enter the first square: ")
                self.secondNum = input("Enter the second square: ")
                
                if self.firstNum.isnumeric() and self.secondNum.isnumeric():
                    self.firstNum = int(self.firstNum)
                    self.secondNum = int(self.secondNum)

                    self.equation = "(" + str(self.firstNum) + " - " + \
                                  str(self.secondNum) + ")"

                    self.answer = "(" + str(math.sqrt(self.firstNum)) + \
                                    " + " + str(math.sqrt(self.secondNum)) + \
                                    ")(" + str(math.sqrt(self.firstNum)) + \
                                    " - " + str(math.sqrt(self.secondNum)) + ")"

                    print("The equation:\n" + self.equation) 
                    print("The answer:\n" + self.answer) 

                    break
                else:
                    print("Wrong values!")
            except ValueError:
                print("Wrong entry!")

    def getDifferenceOfPoints(self):
        print("Calculating for the difference of points")
        print("-------------------------------")

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
    
    def getDoubleAngles(self):
        print("Calculating for the double angle formulas")
        print("-------------------------------")

        while True:
            try:
                self.firstNum = input("Enter the number: ")
                
                if self.firstNum.isnumeric():
                    self.firstNum = math.radians(int(self.firstNum))

                    sinEquation = "2 x sin(" + str(self.firstNum) + "°)cos(" + \
                                  str(self.firstNum) + "°)"
                    
                    self.answer = 2 * cmath.sin(self.firstNum) * \
                                  cmath.cos(self.firstNum)

                    print("The double sine equation: \n" + sinEquation)
                    print("The answer: " + str(self.answer) + "\n")

                    cosEquation = "1 - 2 x sin²(" + str(self.firstNum) + \
                                  "°)"
                    
                    self.answer = 1 - 2 * \
                                  cmath.sin(self.firstNum)**2

                    print("The double cosine equation: \n" + cosEquation)
                    print("The answer: " + str(self.answer) + "\n")

                    tanEquation = "2tan(" + str(self.firstNum) + \
                                  "°) / 1 - tan²(" + str(self.firstNum) + "°)"
                    
                    self.answer = 2 * \
                                  cmath.tan(self.firstNum) / \
                                  (1 - cmath.tan(self.firstNum)**2)

                    print("The double tangent equation: \n" + tanEquation)
                    print("The answer: " + str(self.answer) + "\n")

                    break
                else:
                    print("Wrong values!")
            except ValueError:
                print("Wrong entry!")

    def getUngroupedSampleMean(self):
        numbers = []
        summation = 0
        equation = ""

        print("Calculating for the ungrouped sample mean")
        print("-------------------------------")

        while True:
            try:
                number = float(input("Enter the number: "))
                numbers.append(number)

                confirmation = input("Continue inputting[Y]? ")

                if confirmation != "Y":
                    break
            except ValueError:
                print("Wrong entry!")

        for i in range(len(numbers)):
           summation += numbers[i] 

           equation += str(numbers[i]) + " + " 

        strippedOne = equation.rstrip()
        strippedTwo = strippedOne.rstrip("+")
        strippedThree = strippedTwo.rstrip()
        print("The equation for the ungrouped sample mean is:\n" + \
              "(" + strippedThree + ") / " + str(len(numbers)))

        sampleMeanUngrouped = summation/len(numbers)
        print("The answer is: " + str(sampleMeanUngrouped))

    def getGroupedSampleMean(self, data):
        frequency = 0
        midpointFrequency = 0

        print("Calculating for the grouped sample mean")
        print("-------------------------------")

        for interval, frequency in data:
            midpoint = (interval[0] + interval[1]) / 2
            midpointFrequency += midpoint * frequency
            frequency += frequency

        print("The dataset given: " + str(data))
        print("The grouped sample mean is: " + \
              str(midpointFrequency / frequency))

def main():
    calc = Difference()
    calc.getDifferenceOfSquares()
    calc.getDifferenceOfPoints()
    calc.getDoubleAngles()
    calc.getUngroupedSampleMean()

    data = [((4, 8), 2), ((10, 20), 4)]
    calc.getGroupedSampleMean(data)

if __name__ == "__main__":
    main()