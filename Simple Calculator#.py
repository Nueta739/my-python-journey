while (True):
    print()
    print("Python Calculator")
    print("====================")
    print()

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"You entered: {num1} {num2}")

    operator = input("Enter an operation (+, -, *, /, **): ")
    print(f"You chose: {operator}")
    print()

    if operator == "+":
        result = num1 + num2
        print(f"{num1} {operator} {num2} = {result}")

    elif operator == "-":
        result = num1 - num2
        print(f"{num1} {operator} {num2} = {result}")

    elif operator == "*":
        result = num1 * num2
        print(f"{num1} {operator} {num2} = {result}")

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} {operator} {num2} = {result}")
        else:
            print("Cannot divide by Zero!")

    elif operator == "**":
        result = num1 ** num2
        print(f"{num1} {operator} {num2} = {result}")

    else:
        print("Invalid Operator!")

    print()
    reset = input("Press 'C' to calculate again. Press any other key to exit! ")

    if reset not in ("C", "c"):
        print("GOODBYE!")
        print()
        break

    else:
        continue

