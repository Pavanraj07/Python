def calculate_age(birth_year):
    current_year = 2025  # Update this to the current year as needed
    return current_year - birth_year

def main():
    birth_year = int(input("Enter your birth year: "))
    age = calculate_age(birth_year)
    
    print(f"You are {age} years old.")

if __name__ == "__main__":
    main()
