def calculator():
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    operation = input("Enter an operator (+, -, *, /): ")

    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print(" Div by zero is not allowed.")
                return
        case _:
            print("Invalid operator!")
            return

    print(f"Result: {result}")

calculator()
