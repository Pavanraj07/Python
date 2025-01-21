# Input the number
num = int(input("Enter a number: "))

# Generate multiplication table
print(f"Multiplication Table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
