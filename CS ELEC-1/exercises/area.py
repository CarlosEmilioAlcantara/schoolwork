shapes = ["square", "rectangle", "circle"]
units = ["cm", "m", "km", "mm"]

while True:
    print("AREA PROGRAM")
    print("######################################")
    print("Choose which shape to compute the area:")

    for shape in enumerate(shapes):
        print(shape)
    print("--------------------------------------")

    while True:
        shape_num = int(input("Enter the number of the shape: "))

        if shape_num < 0 or shape_num > 2:
            print("Invalid number. Please select a number from 0 to 2.")
        else:
            shape_chosen = shapes[shape_num]
            break

    for unit in enumerate(units):
        print(unit)
    print("--------------------------------------")

    while True:
        unit_num = int(input("Enter the number of the unit: "))

        if unit_num < 0 or unit_num > 3:
            print("Invalid number. Please select a number from 0 to 3.")
        else:
            unit_chosen = units[unit_num]
            break

    match shape_chosen:
        case "square":
            side = float(input("Enter the length of the sides: "))
            area = side ** 2
        case "rectangle":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length * width
        case "circle":
            radius = float(input("Enter the radius of the circle: "))
            area = 3.14159265359 * (radius ** 2)

    print("The area of the " + shape_chosen + " is " + str(area) + unit_chosen)

    confirmation = input("Stop computing[Y]?: ")
    if confirmation == "Y":
        break