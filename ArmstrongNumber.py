# Input a number
num = int(input("Enter a number: "))

# Calculate the sum of cubes of digits
sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))

# Check if Armstrong
if num == sum_of_cubes:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
