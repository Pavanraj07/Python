# Find the sum of digits of a number
num = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(num))
print(f"The sum of digits of {num} is {digit_sum}.")
