# A simple calculator program
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /,%): ")

if operation == "+":
    print(f"The result is {n1 + n2}.")
elif operation == "-":
    print(f"The result is {n1 - n2}.")
elif operation == "*":
    print(f"The result is {n1 * n2}.")
elif operation == "/":
    if n2 != 0:
        print(f"The result is {n1 / n2}.")
    else:
        print("Error: Division by zero!")
elif operation == "%":
    print(f"The result is {n1 % n2}.")
else:
    print("Invalid operation.")
