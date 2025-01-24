# Convert a decimal number to binary
decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]
print(f"The binary representation of {decimal} is {binary}.")
