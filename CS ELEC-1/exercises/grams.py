weights = ["MG", "KG", "P", "O", "C", "ALL"]
conversions = []

while True:
    print("GRAMS PROGRAM")
    print("######################################")
    print("Choose which unit of weight to convert to:")

    for weight in enumerate(weights):
        print(weight)
    print("--------------------------------------")

    while True:
        weight_num = int(input("Enter the number of the weight: "))

        if weight_num < 0 or weight_num > 5:
            print("Invalid number. Please select a number from 0 to 5.")
        else:
            weight_chosen = weights[weight_num]
            break

    while True:
        number = float(input("Enter the number you want to convert: "))

        if number < 0:
            print("Invalid number. Please input a proper number.")
        else:
            break

    for i in range(len(weights) - 1):
        if i == 0:
            weights[i] = number * 1000
        elif i == 1:
            weights[i] = number / 1000
        elif i == 2:
            weights[i] = number * 0.00220462
        elif i == 3:
            weights[i] = number * 0.035274
        elif i == 4:
            weights[i] = number * 5

        conversions.append(weights[i])
    
    # for we

    match weight_chosen:
        case "MG":
            print("The conversion of " + str(number) + " grams to milligram " +
                  " is " + str(conversions[0]))
        case "KG":
            print("The conversion of " + str(number) + " grams to kilogram " +
                  " is " + str(conversions[1]))
        case "P":
            print("The conversion of " + str(number) + " grams to pound " +
                  " is " + str(conversions[2]))
        case "O":
            print("The conversion of " + str(number) + " grams to ounce " +
                  " is " + str(conversions[3]))
        case "C":
            print("The conversion of " + str(number) + " grams to carat " +
                  " is " + str(conversions[4]))
        case "ALL":
            print("The conversion of gram to all the units are: ")
            for i in range(len(weights) - 1):
                print(weights[i] + ": " + str(conversions[i]))

    confirmation = input("Stop computing[Y]?: ")
    if confirmation == "Y":
        break