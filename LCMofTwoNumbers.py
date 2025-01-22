# Input two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Find LCM
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

lcm = (a * b) // gcd(a, b)

print(f"The LCM of {a} and {b} is {lcm}.")
