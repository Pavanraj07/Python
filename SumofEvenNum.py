# Sum of even numbers in a given range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

even_sum = sum(i for i in range(start, end + 1) if i % 2 == 0)
print(f"The sum of even numbers from {start} to {end} is {even_sum}.")
