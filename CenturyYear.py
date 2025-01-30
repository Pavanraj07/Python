# Check if a year is a century year
year = int(input("Enter a year: "))

if year % 100 == 0:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")
