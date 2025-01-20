# Print Fibonacci sequence up to n terms
steps = int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0
if steps <= 0:
    print("Please enter a positive integer.")
elif steps == 1:
    print(f"Fibonacci sequence up to {steps} term: {n1}")
else:
    print("Fibonacci sequence:")
    while count < steps:
        print(n1, end=" ")
        sum = n1 + n2
        n1 = n2
        n2 = sum
        count += 1
