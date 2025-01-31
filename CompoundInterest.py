# Calculate compound interest
P = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate (in %): ")) / 100
T = float(input("Enter time (in years): "))
CI = P * (1 + R) ** T
print(f"Compound Interest = {CI:.2f}")
