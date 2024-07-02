# Create a program that gets the difference of two squares
# Use the math module
import math;

class Difference:
    def __init__(self):
        self.firstNum = 0
        self.secondNum = 0
        self.equation = ""
        self.answer = ""

        print("Difference of two squares calculator")
        print("########################################")

    def getDifference(self):
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

def main():
    squareDiffCalc = Difference()
    squareDiffCalc.getDifference()

if __name__ == "__main__":
    main()