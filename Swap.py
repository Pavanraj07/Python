# Swap two numbers
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

a, b = b, a
print(f"After swapping: a = {a}, b = {b}")
