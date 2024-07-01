import datetime;

class :Area
    def __init__(self):
        self.numbers = []
        self.now = datetime.datetime.now()

        print("AREA CALCULATOR")
        print("########################")

    def giveNumbers(self):
        while True:
            try:
                number = float(input("Enter the length: "))
                self.numbers.append(number)

                confirmation = input("Do you want to get more areas?[Y] ")
                if confirmation != "Y":
                    break                
            except ValueError:
                print("Wrong value. Please enter a proper number!")

    def getArea(self):
        self.now.strftime("Calculated at: %B-%d-%Y ")
        print("------------------------")

class Square(Area):
    def __init__(self):
        super().__init__()
        print("Calculating for area of square")

    def getArea(self):
        Area.getArea(self)

        for number in self.numbers:
            area = lambda side: side ** 2
            print("Sides: " + str(number) + " Area: " + str(area(number)))

class Circle(Area):
    def __init__(self):
        super().__init__()
        print("Calculating for area of circle")

    def getArea(self):
        Area.getArea(self)

        for number in self.numbers:
            area = lambda radius: 3.14 * radius
            print("Radius: " + str(number) + " Area: " + str(area(number)))

def main():
    squareCalc = Square()
    squareCalc.giveNumbers()
    squareCalc.getArea()

    circleCalc = Circle()
    circleCalc.giveNumbers()
    circleCalc.getArea()

if __name__ == "__main__":
    main() 