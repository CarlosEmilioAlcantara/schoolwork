import datetime

class calcSquareArea:
    def __init__(self):
        self.numbers = []
        print("SQUARE AREA CALCULATOR")

        while True:
            number = input("Enter a number to get area: ")

            try:
                theArea = int(number)
                self.numbers.append(theArea)

                confirmation = input(
                    "Do you want to continue adding numbers[Y] ")
                
                if confirmation != "Y":
                    break
            except ValueError:
                print("Number is not an integer! Please enter a valid value.")


    def getArea(self):
        for number in self.numbers:
            area = lambda number: number ** 2
            print(area(number))


def main():
    area = calcSquareArea()
    area.getArea()

if __name__ == "__main__":
    main()